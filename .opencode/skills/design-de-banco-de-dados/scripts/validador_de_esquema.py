#!/usr/bin/env python3
"""
Validador de Esquema - Validação de esquema de banco de dados
Valida esquemas Prisma e verifica problemas comuns.

Uso:
    python validador_esquema.py <caminho_do_projeto>

Verificações:
    - Sintaxe do esquema Prisma
    - Relações ausentes
    - Recomendações de índices
    - Convenções de nomenclatura
"""

import sys
import json
import re
from pathlib import Path
from datetime import datetime

# Corrige a codificação do console no Windows
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except:
    pass


def buscar_arquivos_esquema(caminho_projeto: Path) -> list:
    """Encontra arquivos de esquema de banco de dados."""
    esquemas = []
    
    # Esquema Prisma
    arquivos_prisma = list(caminho_projeto.glob('**/prisma/schema.prisma'))
    esquemas.extend([('prisma', f) for f in arquivos_prisma])
    
    # Arquivos de esquema Drizzle
    arquivos_drizzle = list(caminho_projeto.glob('**/drizzle/*.ts'))
    arquivos_drizzle.extend(caminho_projeto.glob('**/schema/*.ts'))
    for f in arquivos_drizzle:
        if 'schema' in f.name.lower() or 'table' in f.name.lower():
            esquemas.append(('drizzle', f))
    
    return esquemas[:10]  # Limite de arquivos


def validar_esquema_prisma(caminho_arquivo: Path) -> list:
    """Valida o arquivo de esquema Prisma."""
    problemas = []
    
    try:
        conteudo = caminho_arquivo.read_text(encoding='utf-8', errors='ignore')
        
        # Encontra todos os modelos (models)
        modelos = re.findall(r'model\s+(\w+)\s*{([^}]+)}', conteudo, re.DOTALL)
        
        for nome_modelo, corpo_modelo in modelos:
            # Verifica convenção de nomenclatura (PascalCase)
            if not nome_modelo[0].isupper():
                problemas.append(f"O modelo '{nome_modelo}' deve seguir o padrão PascalCase")
            
            # Verifica campo de ID
            if '@id' not in corpo_modelo and 'id' not in corpo_modelo.lower():
                problemas.append(f"O modelo '{nome_modelo}' pode estar sem o campo @id")
            
            # Verifica campos createdAt/updatedAt
            if 'createdAt' not in corpo_modelo and 'created_at' not in corpo_modelo:
                problemas.append(f"O modelo '{nome_modelo}' não possui o campo createdAt (recomendado)")
            
            # Verifica sugestões de @@index
            # Procura por campos que terminam em Id (chaves estrangeiras comuns)
            chaves_estrangeiras = re.findall(r'(\w+Id)\s+\w+', corpo_modelo)
            for fk in chaves_estrangeiras:
                if f'@@index([{fk}])' not in conteudo and f'@@index(["{fk}"])' not in conteudo:
                    problemas.append(f"Considere adicionar @@index([{fk}]) para melhor desempenho de consulta em {nome_modelo}")
        
        # Verifica definições de Enum
        enums = re.findall(r'enum\s+(\w+)\s*{', conteudo)
        for nome_enum in enums:
            if not nome_enum[0].isupper():
                problemas.append(f"O Enum '{nome_enum}' deve seguir o padrão PascalCase")
        
    except Exception as e:
        problemas.append(f"Erro ao ler o esquema: {str(e)[:50]}")
    
    return problemas


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else "."
    caminho_projeto = Path(alvo).resolve()
    
    print(f"\n{'='*60}")
    print(f"[VALIDADOR DE ESQUEMA] Validação de Banco de Dados")
    print(f"{'='*60}")
    print(f"Projeto: {caminho_projeto}")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-"*60)
    
    # Busca arquivos de esquema
    esquemas = buscar_arquivos_esquema(caminho_projeto)
    print(f"Encontrados {len(esquemas)} arquivos de esquema")
    
    if not esquemas:
        saida = {
            "script": "validador_esquema",
            "projeto": str(caminho_projeto),
            "esquemas_verificados": 0,
            "problemas_encontrados": 0,
            "aprovado": True,
            "mensagem": "Nenhum arquivo de esquema encontrado"
        }
        print(json.dumps(saida, indent=2, ensure_ascii=False))
        sys.exit(0)
    
    # Valida cada esquema
    todos_problemas = []
    
    for tipo_esquema, caminho_arquivo in esquemas:
        print(f"\nValidando: {caminho_arquivo.name} ({tipo_esquema})")
        
        if tipo_esquema == 'prisma':
            problemas = validar_esquema_prisma(caminho_arquivo)
        else:
            problemas = []  # Validação para Drizzle poderia ser adicionada aqui
        
        if problemas:
            todos_problemas.append({
                "arquivo": str(caminho_arquivo.name),
                "tipo": tipo_esquema,
                "problemas": problemas
            })
    
    # Resumo
    print("\n" + "="*60)
    print("PROBLEMAS IDENTIFICADOS NO ESQUEMA")
    print("="*60)
    
    if todos_problemas:
        for item in todos_problemas:
            print(f"\n{item['arquivo']} ({item['tipo']}):")
            for prob in item["problemas"][:5]:  # Limite de 5 por arquivo na tela
                print(f"  - {prob}")
            if len(item["problemas"]) > 5:
                print(f"  ... e mais {len(item['problemas']) - 5} problemas")
    else:
        print("Nenhum problema de esquema encontrado!")
    
    total_problemas = sum(len(item["problemas"]) for item in todos_problemas)
    # Problemas de esquema são avisos, não necessariamente falhas críticas de execução
    passou = True
    
    saida = {
        "script": "validador_esquema",
        "projeto": str(caminho_projeto),
        "esquemas_verificados": len(esquemas),
        "problemas_encontrados": total_problemas,
        "aprovado": passou,
        "detalhes": todos_problemas
    }
    
    print("\n" + json.dumps(saida, indent=2, ensure_ascii=False))
    
    sys.exit(0)


if __name__ == "__main__":
    main()