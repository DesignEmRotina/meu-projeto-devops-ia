#!/usr/bin/env python3
"""
Validador de API - Verifica endpoints de API quanto às melhores práticas.
Valida especificações OpenAPI, formatos de resposta e problemas comuns.
"""
import sys
import json
import re
from pathlib import Path

# Corrige a codificação do console no Windows para saída Unicode
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    pass  # Versões de Python < 3.7

def buscar_arquivos_api(caminho_projeto: Path) -> list:
    """Encontra arquivos relacionados à API."""
    padroes = [
        "**/*api*.ts", "**/*api*.js", "**/*api*.py",
        "**/routes/*.ts", "**/routes/*.js", "**/routes/*.py",
        "**/controllers/*.ts", "**/controllers/*.js",
        "**/endpoints/*.ts", "**/endpoints/*.py",
        "**/*.openapi.json", "**/*.openapi.yaml",
        "**/swagger.json", "**/swagger.yaml",
        "**/openapi.json", "**/openapi.yaml"
    ]
    
    arquivos = []
    for padrao in padroes:
        arquivos.extend(caminho_projeto.glob(padrao))
    
    # Exclui node_modules, .git, etc.
    return [f for f in arquivos if not any(x in str(f) for x in ['node_modules', '.git', 'dist', 'build', '__pycache__'])]

def verificar_especificacao_openapi(caminho_arquivo: Path) -> dict:
    """Verifica especificações OpenAPI/Swagger."""
    problemas = []
    aprovados = []
    
    try:
        conteudo = caminho_arquivo.read_text(encoding='utf-8')
        
        if caminho_arquivo.suffix == '.json':
            spec = json.loads(conteudo)
        else:
            # Verificação básica de YAML
            if 'openapi:' in conteudo or 'swagger:' in conteudo:
                aprovados.append("[OK] Versão OpenAPI/Swagger definida")
            else:
                problemas.append("[X] Nenhuma versão de OpenAPI encontrada")
            
            if 'paths:' in conteudo:
                aprovados.append("[OK] Seção 'paths' (rotas) existe")
            else:
                problemas.append("[X] Nenhuma rota definida")
            
            if 'components:' in conteudo or 'definitions:' in conteudo:
                aprovados.append("[OK] Componentes de Schema definidos")
            
            return {'arquivo': str(caminho_arquivo), 'aprovados': aprovados, 'problemas': problemas, 'tipo': 'openapi'}
        
        # Verificações em JSON OpenAPI
        if 'openapi' in spec or 'swagger' in spec:
            aprovados.append("[OK] Versão OpenAPI definida")
        
        if 'info' in spec:
            if 'title' in spec['info']:
                aprovados.append("[OK] Título da API definido")
            if 'version' in spec['info']:
                aprovados.append("[OK] Versão da API definida")
            if 'description' not in spec['info']:
                problemas.append("[!] Descrição da API ausente")
        
        if 'paths' in spec:
            qtd_rotas = len(spec['paths'])
            aprovados.append(f"[OK] {qtd_rotas} endpoints definidos")
            
            # Verifica cada rota
            for rota, metodos in spec['paths'].items():
                for metodo, detalhes in metodos.items():
                    if metodo in ['get', 'post', 'put', 'patch', 'delete']:
                        if 'responses' not in detalhes:
                            problemas.append(f"[X] {metodo.upper()} {rota}: Nenhuma resposta definida")
                        if 'summary' not in detalhes and 'description' not in detalhes:
                            problemas.append(f"[!] {metodo.upper()} {rota}: Sem descrição/resumo")
        
    except Exception as e:
        problemas.append(f"[X] Erro de processamento: {e}")
    
    return {'arquivo': str(caminho_arquivo), 'aprovados': aprovados, 'problemas': problemas, 'tipo': 'openapi'}

def verificar_codigo_api(caminho_arquivo: Path) -> dict:
    """Verifica o código da API em busca de problemas comuns."""
    problemas = []
    aprovados = []
    
    try:
        conteudo = caminho_arquivo.read_text(encoding='utf-8')
        
        # Verifica tratamento de erros
        padroes_erro = [
            r'try\s*{', r'try:', r'\.catch\(',
            r'except\s+', r'catch\s*\('
        ]
        tem_tratamento_erro = any(re.search(p, conteudo) for p in padroes_erro)
        if tem_tratamento_erro:
            aprovados.append("[OK] Tratamento de erros presente")
        else:
            problemas.append("[X] Nenhum tratamento de erro encontrado")
        
        # Verifica códigos de status HTTP
        padroes_status = [
            r'status\s*\(\s*\d{3}\s*\)', r'statusCode\s*[=:]\s*\d{3}',
            r'HttpStatus\.', r'status_code\s*=\s*\d{3}',
            r'\.status\(\d{3}\)', r'res\.status\('
        ]
        tem_status = any(re.search(p, conteudo) for p in padroes_status)
        if tem_status:
            aprovados.append("[OK] Códigos de status HTTP utilizados")
        else:
            problemas.append("[!] Nenhum código de status HTTP explícito")
        
        # Verifica validação de entrada
        padroes_validacao = [
            r'validate', r'schema', r'zod', r'joi', r'yup',
            r'pydantic', r'@Body\(', r'@Query\('
        ]
        tem_validacao = any(re.search(p, conteudo, re.I) for p in padroes_validacao)
        if tem_validacao:
            aprovados.append("[OK] Validação de entrada presente")
        else:
            problemas.append("[!] Nenhuma validação de entrada detectada")
        
        # Verifica middleware de autenticação
        padroes_auth = [
            r'auth', r'jwt', r'bearer', r'token',
            r'middleware', r'guard', r'@Authenticated'
        ]
        tem_auth = any(re.search(p, conteudo, re.I) for p in padroes_auth)
        if tem_auth:
            aprovados.append("[OK] Autenticação/Autorização detectada")
        
        # Verifica limitação de taxa (Rate Limiting)
        padroes_rate = [r'rateLimit', r'throttle', r'rate.?limit']
        tem_rate = any(re.search(p, conteudo, re.I) for p in padroes_rate)
        if tem_rate:
            aprovados.append("[OK] Rate limiting presente")
        
        # Verifica logging
        padroes_log = [r'console\.log', r'logger\.', r'logging\.', r'log\.']
        tem_logging = any(re.search(p, conteudo) for p in padroes_log)
        if tem_logging:
            aprovados.append("[OK] Logging (registros) presente")
        
    except Exception as e:
        problemas.append(f"[X] Erro de leitura: {e}")
    
    return {'arquivo': str(caminho_arquivo), 'aprovados': aprovados, 'problemas': problemas, 'tipo': 'code'}

def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else "."
    caminho_projeto = Path(alvo)
    
    print("\n" + "=" * 60)
    print("  VALIDADOR DE API - Verificação de Boas Práticas")
    print("=" * 60 + "\n")
    
    arquivos_api = buscar_arquivos_api(caminho_projeto)
    
    if not arquivos_api:
        print("[!] Nenhum arquivo de API encontrado.")
        print("    Buscando em: routes/, controllers/, api/, openapi.json/yaml")
        sys.exit(0)
    
    resultados = []
    for caminho_arquivo in arquivos_api[:15]:  # Limite para evitar logs excessivos
        nome_arquivo = caminho_arquivo.name.lower()
        if 'openapi' in nome_arquivo or 'swagger' in nome_arquivo:
            resultado = verificar_especificacao_openapi(caminho_arquivo)
        else:
            resultado = verificar_codigo_api(caminho_arquivo)
        resultados.append(resultado)
    
    # Exibe resultados
    total_problemas = 0
    total_aprovados = 0
    
    for res in resultados:
        print(f"\n[ARQUIVO] {res['arquivo']} [{res['tipo']}]")
        for item in res['aprovados']:
            print(f"   {item}")
            total_aprovados += 1
        for item in res['problemas']:
            print(f"   {item}")
            if item.startswith("[X]"):
                total_problemas += 1
    
    print("\n" + "=" * 60)
    print(f"[RESUMO] {total_aprovados} aprovados, {total_problemas} problemas críticos")
    print("=" * 60)
    
    if total_problemas == 0:
        print("[OK] Validação de API aprovada")
        sys.exit(0)
    else:
        print("[X] Corrija os problemas críticos antes do deploy")
        sys.exit(1)

if __name__ == "__main__":
    main()