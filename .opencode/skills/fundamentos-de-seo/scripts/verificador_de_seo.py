#!/usr/bin/env python3
"""
Verificador de SEO - Auditoria de Otimização para Motores de Busca
Verifica páginas HTML/JSX/TSX em busca de boas práticas de SEO.

OBJETIVO:
    - Verificar meta tags, títulos e descrições
    - Checar tags Open Graph para compartilhamento social
    - Validar a hierarquia de cabeçalhos (H1, H2, etc.)
    - Verificar acessibilidade de imagens (atributos alt)

O QUE ELE ANALISA:
    - Arquivos HTML (páginas web reais)
    - Arquivos JSX/TSX (componentes de página React)
    - Apenas arquivos que provavelmente são páginas PÚBLICAS

Uso:
    python verificador_seo.py <caminho_do_projeto>
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


# Diretórios para ignorar
DIR_IGNORADOS = {
    'node_modules', '.next', 'dist', 'build', '.git', '.github',
    '__pycache__', '.vscode', '.idea', 'coverage', 'test', 'tests',
    '__tests__', 'spec', 'docs', 'documentation', 'examples'
}

# Padrões de arquivos para pular (não são páginas)
PADROES_PULAR = [
    'config', 'setup', 'util', 'helper', 'hook', 'context', 'store',
    'service', 'api', 'lib', 'constant', 'type', 'interface', 'mock',
    '.test.', '.spec.', '_test.', '_spec.'
]


def eh_arquivo_de_pagina(caminho_arquivo: Path) -> bool:
    """Verifica se este arquivo é provavelmente uma página voltada ao público."""
    nome = caminho_arquivo.name.lower()
    tronco = caminho_arquivo.stem.lower()
    
    # Pula arquivos de utilitários ou configuração
    if any(skip in nome for skip in PADROES_PULAR):
        return False
    
    # Verifica o caminho - páginas em diretórios específicos são provavelmente páginas
    partes = [p.lower() for p in caminho_arquivo.parts]
    dirs_pagina = ['pages', 'app', 'routes', 'views', 'screens']
    
    if any(d in partes for d in dirs_pagina):
        return True
    
    # Indicadores de nome de arquivo para páginas
    nomes_pagina = ['page', 'index', 'home', 'about', 'contact', 'blog', 
                    'post', 'article', 'product', 'landing', 'layout']
    
    if any(p in tronco for p in nomes_pagina):
        return True
    
    # Arquivos HTML são geralmente páginas
    if caminho_arquivo.suffix.lower() in ['.html', '.htm']:
        return True
    
    return False


def buscar_paginas(caminho_projeto: Path) -> list:
    """Encontra arquivos de página para verificar."""
    padroes = ['**/*.html', '**/*.htm', '**/*.jsx', '**/*.tsx']
    
    arquivos = []
    for padrao in padroes:
        for f in caminho_projeto.glob(padrao):
            # Pula diretórios excluídos
            if any(skip in f.parts for skip in DIR_IGNORADOS):
                continue
            
            # Verifica se é provavelmente uma página
            if eh_arquivo_de_pagina(f):
                arquivos.append(f)
    
    return arquivos[:50]  # Limite de 50 arquivos


def verificar_pagina(caminho_arquivo: Path) -> dict:
    """Verifica uma única página em busca de problemas de SEO."""
    problemas = []
    
    try:
        conteudo = caminho_arquivo.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        return {"arquivo": str(caminho_arquivo.name), "problemas": [f"Erro: {e}"]}
    
    # Detecta se este é um arquivo de layout/template (possui componente Head ou tag head)
    eh_layout = 'Head>' in conteudo or '<head' in conteudo.lower()
    
    # 1. Tag de Título
    tem_titulo = '<title' in conteudo.lower() or 'title=' in conteudo or 'Head>' in conteudo
    if not tem_titulo and eh_layout:
        problemas.append("Tag <title> ausente")
    
    # 2. Meta descrição
    tem_descricao = 'name="description"' in conteudo.lower() or 'name=\'description\'' in conteudo.lower()
    if not tem_descricao and eh_layout:
        problemas.append("Meta descrição (description) ausente")
    
    # 3. Tags Open Graph (Social)
    tem_og = 'og:' in conteudo or 'property="og:' in conteudo.lower()
    if not tem_og and eh_layout:
        problemas.append("Tags Open Graph (redes sociais) ausentes")
    
    # 4. Hierarquia de Cabeçalhos - múltiplos H1s
    h1_encontrados = re.findall(r'<h1[^>]*>', conteudo, re.I)
    if len(h1_encontrados) > 1:
        problemas.append(f"Múltiplas tags H1 detectadas ({len(h1_encontrados)}) - Use apenas uma por página")
    
    # 5. Imagens sem alt
    padrao_img = r'<img[^>]+>'
    imgs = re.findall(padrao_img, conteudo, re.I)
    for img in imgs:
        if 'alt=' not in img.lower():
            problemas.append("Imagem sem atributo 'alt' (prejudica acessibilidade e SEO)")
            break
        if 'alt=""' in img or "alt=''" in img:
            problemas.append("Imagem com atributo 'alt' vazio")
            break
    
    return {
        "arquivo": str(caminho_arquivo.name),
        "problemas": problemas
    }


def main():
    caminho_alvo = sys.argv[1] if len(sys.argv) > 1 else "."
    caminho_projeto = Path(caminho_alvo).resolve()
    
    print(f"\n{'='*60}")
    print(f"   VERIFICADOR DE SEO - Auditoria de Otimização Web")
    print(f"{'='*60}")
    print(f"Projeto: {caminho_projeto}")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-"*60)
    
    # Busca páginas
    paginas = buscar_paginas(caminho_projeto)
    
    if not paginas:
        print("\n[!] Nenhuma página encontrada.")
        print("    Buscando por: HTML, JSX, TSX nos diretórios pages/app/routes")
        saida = {"script": "verificador_seo", "arquivos_verificados": 0, "aprovado": True}
        print("\n" + json.dumps(saida, indent=2, ensure_ascii=False))
        sys.exit(0)
    
    print(f"Encontrados {len(paginas)} arquivos de página para analisar\n")
    
    # Verifica cada página
    todos_problemas = []
    for f in paginas:
        resultado = verificar_pagina(f)
        if resultado["problemas"]:
            todos_problemas.append(resultado)
    
    # Resumo
    print("=" * 60)
    print("RESULTADOS DA ANÁLISE DE SEO")
    print("=" * 60)
    
    if todos_problemas:
        # Agrupa por tipo de problema
        contagem_problemas = {}
        for item in todos_problemas:
            for prob in item["problemas"]:
                contagem_problemas[prob] = contagem_problemas.get(prob, 0) + 1
        
        print("\nResumo de Ocorrências:")
        for prob, total in sorted(contagem_problemas.items(), key=lambda x: -x[1]):
            print(f"  [{total}] {prob}")
        
        print(f"\nArquivos afetados ({len(todos_problemas)}):")
        for item in todos_problemas[:5]:
            print(f"  - {item['arquivo']}")
        if len(todos_problemas) > 5:
            print(f"  ... e mais {len(todos_problemas) - 5} arquivos")
    else:
        print("\n[OK] Nenhum problema de SEO encontrado!")
    
    total_problemas = sum(len(item["problemas"]) for item in todos_problemas)
    passou = total_problemas == 0
    
    saida = {
        "script": "verificador_seo",
        "projeto": str(caminho_projeto),
        "arquivos_verificados": len(paginas),
        "arquivos_com_problemas": len(todos_problemas),
        "total_de_problemas": total_problemas,
        "aprovado": passou
    }
    
    print("\n" + json.dumps(saida, indent=2, ensure_ascii=False))
    
    sys.exit(0 if passou else 1)


if __name__ == "__main__":
    main()