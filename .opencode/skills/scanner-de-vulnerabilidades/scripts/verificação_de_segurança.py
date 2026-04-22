#!/usr/bin/env python3
"""
Habilidade: scanner-de-vulnerabilidades
Script: varredura_seguranca.py
Propósito: Validar a aplicação dos princípios de segurança (OWASP) no projeto
Uso: python varredura_seguranca.py <caminho_do_projeto> [--scan-type all|deps|secrets|patterns|config]
Saída: JSON com as descobertas da validação

Este script verifica:
1. Dependências - Segurança da cadeia de suprimentos (OWASP A03)
2. Segredos - Ausência de credenciais expostas no código (OWASP A04)
3. Padrões de Código - Identificação de padrões perigosos (OWASP A05)
4. Configuração - Validação de definições de segurança (OWASP A02)
"""
import subprocess
import json
import os
import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# Corrige a codificação do console Windows para saída Unicode
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    pass  # Versão do Python < 3.7


# ============================================================================
#  CONFIGURAÇÃO
# ============================================================================

PADROES_SEGREDOS = [
    # Chaves de API e Tokens
    (r'api[_-]?key\s*[=:]\s*["\'][^"\']{10,}["\']', "Chave de API", "high"),
    (r'token\s*[=:]\s*["\'][^"\']{10,}["\']', "Token", "high"),
    (r'bearer\s+[a-zA-Z0-9\-_.]+', "Token Bearer", "critical"),
    
    # Credenciais de Nuvem (Cloud)
    (r'AKIA[0-9A-Z]{16}', "Chave de Acesso AWS", "critical"),
    (r'aws[_-]?secret[_-]?access[_-]?key\s*[=:]\s*["\'][^"\']+["\']', "Segredo AWS", "critical"),
    (r'AZURE[_-]?[A-Z_]+\s*[=:]\s*["\'][^"\']+["\']', "Credencial Azure", "critical"),
    (r'GOOGLE[_-]?[A-Z_]+\s*[=:]\s*["\'][^"\']+["\']', "Credencial GCP", "critical"),
    
    # Banco de Dados e Conexões
    (r'password\s*[=:]\s*["\'][^"\']{4,}["\']', "Senha", "high"),
    (r'(mongodb|postgres|mysql|redis):\/\/[^\s"\']+', "String de Conexão de Banco de Dados", "critical"),
    
    # Chaves Privadas
    (r'-----BEGIN\s+(RSA|PRIVATE|EC)\s+KEY-----', "Chave Privada", "critical"),
    (r'ssh-rsa\s+[A-Za-z0-9+/]+', "Chave SSH", "critical"),
    
    # JWT
    (r'eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+', "Token JWT", "high"),
]

PADROES_PERIGOSOS = [
    # Riscos de Injeção
    (r'eval\s*\(', "Uso de eval()", "critical", "Risco de Injeção de Código"),
    (r'exec\s*\(', "Uso de exec()", "critical", "Risco de Injeção de Código"),
    (r'new\s+Function\s*\(', "Construtor Function", "high", "Risco de Injeção de Código"),
    (r'child_process\.exec\s*\(', "child_process.exec", "high", "Risco de Injeção de Comando"),
    (r'subprocess\.call\s*\([^)]*shell\s*=\s*True', "subprocess com shell=True", "high", "Risco de Injeção de Comando"),
    
    # Riscos de XSS
    (r'dangerouslySetInnerHTML', "dangerouslySetInnerHTML", "high", "Risco de XSS"),
    (r'\.innerHTML\s*=', "Atribuição de innerHTML", "medium", "Risco de XSS"),
    (r'document\.write\s*\(', "document.write", "medium", "Risco de XSS"),
    
    # Indicadores de Injeção de SQL
    (r'["\'][^"\']*\+\s*[a-zA-Z_]+\s*\+\s*["\'].*(?:SELECT|INSERT|UPDATE|DELETE)', "Concatenação de String SQL", "critical", "Risco de Injeção de SQL"),
    (r'f"[^"]*(?:SELECT|INSERT|UPDATE|DELETE)[^"]*\{', "f-string SQL", "critical", "Risco de Injeção de SQL"),
    
    # Configurações Inseguras
    (r'verify\s*=\s*False', "Verificação SSL Desativada", "high", "Risco de MITM (Intercepção)"),
    (r'--insecure', "Flag Insegura", "medium", "Segurança desabilitada"),
    (r'disable[_-]?ssl', "SSL Desativado", "high", "Risco de MITM (Intercepção)"),
    
    # Desserialização insegura
    (r'pickle\.loads?\s*\(', "Uso de pickle", "high", "Risco de Desserialização"),
    (r'yaml\.load\s*\([^)]*\)(?!\s*,\s*Loader)', "Carga YAML insegura", "high", "Risco de Desserialização"),
]

DIRETORIOS_IGNORADOS = {'node_modules', '.git', 'dist', 'build', '__pycache__', '.venv', 'venv', '.next'}
EXTENSOES_CODIGO = {'.js', '.ts', '.jsx', '.tsx', '.py', '.go', '.java', '.rb', '.php'}
EXTENSOES_CONFIG = {'.json', '.yaml', '.yml', '.toml', '.env', '.env.local', '.env.development'}


# ============================================================================
#  FUNÇÕES DE VARREDURA
# ============================================================================

def scan_dependencies(project_path: str) -> Dict[str, Any]:
    """
    Valida a segurança da cadeia de suprimentos (OWASP A03).
    Verifica: npm audit, presença de lock files, integridade.
    """
    resultados = {"ferramenta": "scanner_dependencias", "descobertas": [], "status": "[OK] Seguro"}
    
    # Verificação de arquivos de bloqueio (lock files)
    arquivos_lock = {
        "npm": ["package-lock.json", "npm-shrinkwrap.json"],
        "yarn": ["yarn.lock"],
        "pnpm": ["pnpm-lock.yaml"],
        "pip": ["requirements.txt", "Pipfile.lock", "poetry.lock"],
    }
    
    for gerenciador, arquivos in arquivos_lock.items():
        arquivo_pkg = "package.json" if gerenciador in ["npm", "yarn", "pnpm"] else "setup.py"
        caminho_pkg = Path(project_path) / arquivo_pkg
        
        if caminho_pkg.exists() or (gerenciador == "pip" and (Path(project_path) / "requirements.txt").exists()):
            tem_lock = any((Path(project_path) / f).exists() for f in arquivos)
            if not tem_lock:
                resultados["descobertas"].append({
                    "tipo": "Arquivo Lock Ausente",
                    "severidade": "high",
                    "mensagem": f"{gerenciador}: Nenhum arquivo lock encontrado. Integridade da cadeia de suprimentos em risco."
                })
    
    # Executa npm audit se aplicável
    if (Path(project_path) / "package.json").exists():
        try:
            resultado = subprocess.run(
                ["npm", "audit", "--json"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            try:
                dados_audit = json.loads(resultado.stdout)
                vulnerabilidades = dados_audit.get("vulnerabilidades", {})
                
                contagem_sev = {"critical": 0, "high": 0, "moderate": 0, "low": 0}
                for vuln in vulnerabilidades.values():
                    sev = vuln.get("severity", "low").lower()
                    if sev in contagem_sev:
                        contagem_sev[sev] += 1
                
                if contagem_sev["critical"] > 0:
                    resultados["status"] = "[!!] Vulnerabilidades Críticas"
                    resultados["descobertas"].append({
                        "tipo": "npm audit",
                        "severidade": "critical",
                        "mensagem": f"{contagem_sev['critical']} vulnerabilidades críticas nas dependências"
                    })
                elif contagem_sev["high"] > 0:
                    resultados["status"] = "[!] Vulnerabilidades Altas"
                    resultados["descobertas"].append({
                        "tipo": "npm audit",
                        "severidade": "high",
                        "mensagem": f"{contagem_sev['high']} vulnerabilidades de severidade alta"
                    })
                
                resultados["detalhes_npm_audit"] = contagem_sev
                
            except json.JSONDecodeError:
                pass
                
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
    
    if not resultados["descobertas"]:
        resultados["status"] = "[OK] Verificações de dependências aprovadas"
    
    return resultados


def scan_secrets(project_path: str) -> Dict[str, Any]:
    """
    Valida a ausência de segredos expostos (OWASP A04).
    Verifica: Chaves de API, tokens, senhas, credenciais de nuvem.
    """
    resultados = {
        "ferramenta": "scanner_segredos",
        "descobertas": [],
        "status": "[OK] Nenhum segredo detectado",
        "arquivos_escaneados": 0,
        "por_severidade": {"critical": 0, "high": 0, "medium": 0}
    }
    
    for raiz, dirs, arquivos in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in DIRETORIOS_IGNORADOS]
        
        for arquivo in arquivos:
            ext = Path(arquivo).suffix.lower()
            if ext not in EXTENSOES_CODIGO and ext not in EXTENSOES_CONFIG:
                continue
                
            caminho_arq = Path(raiz) / arquivo
            resultados["arquivos_escaneados"] += 1
            
            try:
                with open(caminho_arq, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read()
                    
                    for padrao, tipo_segredo, severidade in PADROES_SEGREDOS:
                        matches = re.findall(padrao, conteudo, re.IGNORECASE)
                        if matches:
                            resultados["descobertas"].append({
                                "arquivo": str(caminho_arq.relative_to(project_path)),
                                "tipo": tipo_segredo,
                                "severidade": severidade,
                                "quantidade": len(matches)
                            })
                            resultados["por_severidade"][severidade] += len(matches)
                            
            except Exception:
                pass
    
    if resultados["por_severidade"]["critical"] > 0:
        resultados["status"] = "[!!] CRÍTICO: Segredos expostos!"
    elif resultados["por_severidade"]["high"] > 0:
        resultados["status"] = "[!] ALTO: Segredos encontrados"
    elif sum(resultados["por_severidade"].values()) > 0:
        resultados["status"] = "[?] Potenciais segredos detectados"
    
    # Limita descobertas na saída
    resultados["descobertas"] = resultados["descobertas"][:15]
    
    return resultados


def scan_code_patterns(project_path: str) -> Dict[str, Any]:
    """
    Valida padrões de código perigosos (OWASP A05).
    Verifica: Riscos de injeção, XSS, desserialização insegura.
    """
    resultados = {
        "ferramenta": "scanner_padroes",
        "descobertas": [],
        "status": "[OK] Nenhum padrão perigoso",
        "arquivos_escaneados": 0,
        "por_categoria": {}
    }
    
    for raiz, dirs, arquivos in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in DIRETORIOS_IGNORADOS]
        
        for arquivo in arquivos:
            ext = Path(arquivo).suffix.lower()
            if ext not in EXTENSOES_CODIGO:
                continue
                
            caminho_arq = Path(raiz) / arquivo
            resultados["arquivos_escaneados"] += 1
            
            try:
                with open(caminho_arq, 'r', encoding='utf-8', errors='ignore') as f:
                    linhas = f.readlines()
                    
                    for num_linha, linha in enumerate(linhas, 1):
                        for padrao, nome, severidade, categoria in PADROES_PERIGOSOS:
                            if re.search(padrao, linha, re.IGNORECASE):
                                resultados["descobertas"].append({
                                    "arquivo": str(caminho_arq.relative_to(project_path)),
                                    "linha": num_linha,
                                    "padrao": nome,
                                    "severidade": severidade,
                                    "categoria": categoria,
                                    "trecho": linha.strip()[:80]
                                })
                                resultados["por_categoria"][categoria] = resultados["por_categoria"].get(categoria, 0) + 1
                                
            except Exception:
                pass
    
    contagem_critica = sum(1 for f in resultados["descobertas"] if f["severidade"] == "critical")
    contagem_alta = sum(1 for f in resultados["descobertas"] if f["severidade"] == "high")
    
    if contagem_critica > 0:
        resultados["status"] = f"[!!] CRÍTICO: {contagem_critica} padrões perigosos"
    elif contagem_alta > 0:
        resultados["status"] = f"[!] ALTO: {contagem_alta} padrões de risco"
    elif resultados["descobertas"]:
        resultados["status"] = "[?] Alguns padrões precisam de revisão"
    
    resultados["descobertas"] = resultados["descobertas"][:20]
    
    return resultados


def scan_configuration(project_path: str) -> Dict[str, Any]:
    """
    Valida configurações de segurança (OWASP A02).
    Verifica: Cabeçalhos de segurança, CORS, modos de depuração.
    """
    resultados = {
        "ferramenta": "scanner_configuracao",
        "descobertas": [],
        "status": "[OK] Configuração segura",
        "verificacoes": {}
    }
    
    # Problemas comuns em arquivos de configuração
    problemas_config = [
        (r'"DEBUG"\s*:\s*true', "Modo Debug ativado", "high"),
        (r'debug\s*=\s*True', "Modo Debug ativado", "high"),
        (r'NODE_ENV.*development', "Modo desenvolvimento em produção", "medium"),
        (r'"CORS_ALLOW_ALL".*true', "CORS permite todas as origens", "high"),
        (r'"Access-Control-Allow-Origin".*\*', "CORS com wildcard (*)", "high"),
        (r'allowCredentials.*true.*origin.*\*', "Combo perigoso de CORS", "critical"),
    ]
    
    for raiz, dirs, arquivos in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in DIRETORIOS_IGNORADOS]
        
        for arquivo in arquivos:
            ext = Path(arquivo).suffix.lower()
            if ext not in EXTENSOES_CONFIG and arquivo not in ['next.config.js', 'webpack.config.js', '.eslintrc.js']:
                continue
                
            caminho_arq = Path(raiz) / arquivo
            
            try:
                with open(caminho_arq, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read()
                    
                    for padrao, problema, severidade in problemas_config:
                        if re.search(padrao, conteudo, re.IGNORECASE):
                            resultados["descobertas"].append({
                                "arquivo": str(caminho_arq.relative_to(project_path)),
                                "problema": problema,
                                "severidade": severidade
                            })
                            
            except Exception:
                pass
    
    # Verifica cabeçalhos de segurança
    arquivos_header = ["next.config.js", "next.config.mjs", "middleware.ts", "nginx.conf"]
    for ah in arquivos_header:
        if (Path(project_path) / ah).exists():
            resultados["verificacoes"]["config_headers_seguranca"] = True
            break
    else:
        resultados["verificacoes"]["config_headers_seguranca"] = False
        resultados["descobertas"].append({
            "problema": "Configuração de cabeçalhos de segurança não encontrada",
            "severidade": "medium",
            "recomendacao": "Configure cabeçalhos CSP, HSTS, X-Frame-Options"
        })
    
    if any(f["severidade"] == "critical" for f in resultados["descobertas"]):
        resultados["status"] = "[!!] CRÍTICO: Problemas de configuração"
    elif any(f["severidade"] == "high" for f in resultados["descobertas"]):
        resultados["status"] = "[!] ALTO: Revisão de configuração necessária"
    elif resultados["descobertas"]:
        resultados["status"] = "[?] Pequenos problemas de configuração"
    
    return resultados


# ============================================================================
#  PRINCIPAL (MAIN)
# ============================================================================

def run_full_scan(project_path: str, scan_type: str = "all") -> Dict[str, Any]:
    """Executa as varreduras de validação de segurança."""
    
    relatorio = {
        "projeto": project_path,
        "data_hora": datetime.now().isoformat(),
        "tipo_varredura": scan_type,
        "scans": {},
        "resumo": {
            "total_descobertas": 0,
            "criticas": 0,
            "altas": 0,
            "status_geral": "[OK] SEGURO"
        }
    }
    
    scanners = {
        "deps": ("dependencias", scan_dependencies),
        "secrets": ("segredos", scan_secrets),
        "patterns": ("padroes_codigo", scan_code_patterns),
        "config": ("configuracao", scan_configuration),
    }
    
    for chave, (nome, scanner) in scanners.items():
        if scan_type == "all" or scan_type == chave:
            resultado = scanner(project_path)
            relatorio["scans"][nome] = resultado
            
            qtd_descobertas = len(resultado.get("descobertas", []))
            relatorio["resumo"]["total_descobertas"] += qtd_descobertas
            
            for descoberta in resultado.get("descobertas", []):
                sev = descoberta.get("severidade", "low")
                if sev == "critical":
                    relatorio["resumo"]["criticas"] += 1
                elif sev == "high":
                    relatorio["resumo"]["altas"] += 1
    
    # Determina o status geral
    if relatorio["resumo"]["criticas"] > 0:
        relatorio["resumo"]["status_geral"] = "[!!] PROBLEMAS CRÍTICOS ENCONTRADOS"
    elif relatorio["resumo"]["altas"] > 0:
        relatorio["resumo"]["status_geral"] = "[!] RISCO ALTO IDENTIFICADO"
    elif relatorio["resumo"]["total_descobertas"] > 0:
        relatorio["resumo"]["status_geral"] = "[?] REVISÃO RECOMENDADA"
    
    return relatorio


def main():
    parser = argparse.ArgumentParser(
        description="Validar princípios de segurança (OWASP) no projeto"
    )
    parser.add_argument("project_path", nargs="?", default=".", help="Diretório do projeto para varredura")
    parser.add_argument("--scan-type", choices=["all", "deps", "secrets", "patterns", "config"],
                        default="all", help="Tipo de varredura a executar")
    parser.add_argument("--output", choices=["json", "summary"], default="json",
                        help="Formato de saída")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.project_path):
        print(json.dumps({"erro": f"Diretório não encontrado: {args.project_path}"}, ensure_ascii=False))
        sys.exit(1)
    
    resultado = run_full_scan(args.project_path, args.scan_type)
    
    if args.output == "summary":
        print(f"\n{'='*60}")
        print(f"Varredura de Segurança: {resultado['projeto']}")
        print(f"{'='*60}")
        print(f"Status Geral: {resultado['resumo']['status_geral']}")
        print(f"Total de Descobertas: {resultado['resumo']['total_descobertas']}")
        print(f"  Críticas: {resultado['resumo']['criticas']}")
        print(f"  Altas: {resultado['resumo']['altas']}")
        print(f"{'='*60}\n")
        
        for nome_scan, result_scan in resultado['scans'].items():
            print(f"\n{nome_scan.upper()}: {result_scan['status']}")
            for f in result_scan.get('descobertas', [])[:5]:
                print(f"  - {f}")
    else:
        print(json.dumps(resultado, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()