#!/usr/bin/env python3
"""
GEO Checker - Auditoria de Generative Engine Optimization (GEO)
Verifica CONTEÚDO WEB PÚBLICO para prontidão de citação por IA.

OBJETIVO:
    - Analisar páginas que serão INDEXADAS por motores de IA (ChatGPT, Perplexity, etc.)
    - Verificar dados estruturados, informações de autor, datas e seções de FAQ
    - Ajudar o conteúdo a ranquear melhor em respostas geradas por IA

O QUE ELE VERIFICA:
    - Arquivos HTML (páginas web reais)
    - Arquivos JSX/TSX (componentes de páginas React)
    - NÃO verifica arquivos Markdown (são documentação técnica, não conteúdo público)

USO:
    python geo_checker.py <caminho_do_projeto>
"""
import sys
import re
import json
from pathlib import Path

# Corrige encoding do console no Windows
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    pass


# Diretórios a ignorar (não são conteúdo público)
SKIP_DIRS = {
    'node_modules', '.next', 'dist', 'build', '.git', '.github',
    '__pycache__', '.vscode', '.idea', 'coverage', 'test', 'tests',
    '__tests__', 'spec', 'docs', 'documentation'
}

# Arquivos a ignorar (não são páginas públicas)
SKIP_FILES = {
    'jest.config', 'webpack.config', 'vite.config', 'tsconfig',
    'package.json', 'package-lock', 'yarn.lock', '.eslintrc',
    'tailwind.config', 'postcss.config', 'next.config'
}


def is_page_file(file_path: Path) -> bool:
    """Verifica se o arquivo provavelmente é uma página pública."""
    name = file_path.stem.lower()
    
    # Ignora arquivos de configuração/utilitários
    if any(skip in name for skip in SKIP_FILES):
        return False
    
    # Ignora arquivos de teste
    if name.endswith('.test') or name.endswith('.spec'):
        return False
    if name.startswith('test_') or name.startswith('spec_'):
        return False
    
    # Indicadores comuns de páginas
    page_indicators = [
        'page', 'index', 'home', 'about', 'contact', 'blog',
        'post', 'article', 'product', 'service', 'landing'
    ]
    
    # Verifica se está em diretórios comuns de páginas (Next.js, etc.)
    parts = [p.lower() for p in file_path.parts]
    if 'pages' in parts or 'app' in parts or 'routes' in parts:
        return True
    
    # Verifica indicadores no nome do arquivo
    if any(ind in name for ind in page_indicators):
        return True
    
    # Arquivos HTML normalmente são páginas
    if file_path.suffix.lower() == '.html':
        return True
    
    return False


def find_web_pages(project_path: Path) -> list:
    """Localiza apenas páginas web públicas."""
    patterns = ['**/*.html', '**/*.htm', '**/*.jsx', '**/*.tsx']
    
    files = []
    for pattern in patterns:
        for f in project_path.glob(pattern):
            # Ignora diretórios excluídos
            if any(skip in f.parts for skip in SKIP_DIRS):
                continue
            
            # Verifica se é provavelmente uma página
            if is_page_file(f):
                files.append(f)
    
    return files[:30]  # Limite de 30 páginas


def check_page(file_path: Path) -> dict:
    """Analisa uma única página web em busca de elementos GEO."""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        return {
            'file': str(file_path.name),
            'passed': [],
            'issues': [f"Erro: {e}"],
            'score': 0
        }
    
    issues = []
    passed = []
    
    # 1. Dados Estruturados JSON-LD (crítico para IA)
    if 'application/ld+json' in content:
        passed.append("Dados estruturados JSON-LD encontrados")
        if '"@type"' in content:
            if 'Article' in content:
                passed.append("Schema de Article presente")
            if 'FAQPage' in content:
                passed.append("Schema de FAQ presente")
            if 'Organization' in content or 'Person' in content:
                passed.append("Schema de entidade presente")
    else:
        issues.append("Nenhum dado estruturado JSON-LD (IA prefere conteúdo estruturado)")
    
    # 2. Estrutura de Headings
    h1_count = len(re.findall(r'<h1[^>]*>', content, re.I))
    h2_count = len(re.findall(r'<h2[^>]*>', content, re.I))
    
    if h1_count == 1:
        passed.append("Apenas um H1 (tópico claro)")
    elif h1_count == 0:
        issues.append("Nenhum H1 - tópico da página pouco claro")
    else:
        issues.append(f"Múltiplos H1 ({h1_count}) - confuso para IA")
    
    if h2_count >= 2:
        passed.append(f"{h2_count} subtítulos H2 (boa estrutura)")
    else:
        issues.append("Adicione mais H2 para facilitar leitura por IA")
    
    # 3. Atribuição de Autor (sinal E-E-A-T)
    author_patterns = ['author', 'byline', 'written-by', 'contributor', 'rel="author"']
    has_author = any(p in content.lower() for p in author_patterns)
    if has_author:
        passed.append("Informação de autor encontrada")
    else:
        issues.append("Nenhuma informação de autor (IA prefere conteúdo atribuído)")
    
    # 4. Data de Publicação (sinal de atualidade)
    date_patterns = ['datePublished', 'dateModified', 'datetime=', 'pubdate', 'article:published']
    has_date = any(re.search(p, content, re.I) for p in date_patterns)
    if has_date:
        passed.append("Data de publicação encontrada")
    else:
        issues.append("Nenhuma data de publicação (atualidade é importante para IA)")
    
    # 5. Seção de FAQ (altamente citável)
    faq_patterns = [r'<details', r'faq', r'frequently.?asked', r'"FAQPage"']
    has_faq = any(re.search(p, content, re.I) for p in faq_patterns)
    if has_faq:
        passed.append("Seção de FAQ detectada (alto potencial de citação)")
    
    # 6. Listas (conteúdo estruturado)
    list_count = len(re.findall(r'<(ul|ol)[^>]*>', content, re.I))
    if list_count >= 2:
        passed.append(f"{list_count} listas (conteúdo estruturado)")
    
    # 7. Tabelas (dados comparativos)
    table_count = len(re.findall(r'<table[^>]*>', content, re.I))
    if table_count >= 1:
        passed.append(f"{table_count} tabela(s) (dados comparativos)")
    
    # 8. Reconhecimento de Entidade (E-E-A-T) - NOVO 2025
    entity_patterns = [
        r'"@type"\s*:\s*"Organization"',
        r'"@type"\s*:\s*"LocalBusiness"',
        r'"@type"\s*:\s*"Brand"',
        r'itemtype.*schema\.org/(Organization|Person|Brand)',
        r'rel="author"'
    ]
    has_entity = any(re.search(p, content, re.I) for p in entity_patterns)
    if has_entity:
        passed.append("Reconhecimento de entidade/marca (E-E-A-T)")
    
    # 9. Estatísticas ou Dados Originais (ímã de citação) - NOVO 2025
    stat_patterns = [
        r'\d+%',
        r'\$[\d,]+',
        r'study\s+(shows|found)',
        r'according to',
        r'data\s+(shows|reveals)',
        r'\d+x\s+(faster|better|more)',
        r'(million|billion|trillion)',
    ]
    stat_matches = sum(1 for p in stat_patterns if re.search(p, content, re.I))
    if stat_matches >= 2:
        passed.append("Estatísticas/dados originais (alto valor para IA)")
    
    # 10. Respostas diretas / conversacionais - NOVO 2025
    direct_answer_patterns = [
        r'is defined as',
        r'refers to',
        r'means that',
        r'the answer is',
        r'in short,',
        r'simply put,',
        r'<dfn'
    ]
    has_direct = any(re.search(p, content, re.I) for p in direct_answer_patterns)
    if has_direct:
        passed.append("Padrões de resposta direta (compatível com LLMs)")
    
    # Cálculo da pontuação
    total = len(passed) + len(issues)
    score = (len(passed) / total * 100) if total > 0 else 0
    
    return {
        'file': str(file_path.name),
        'passed': passed,
        'issues': issues,
        'score': round(score)
    }


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    target_path = Path(target).resolve()
    
    print("\n" + "=" * 60)
    print("  GEO CHECKER - Auditoria de Prontidão para Citação por IA")
    print("=" * 60)
    print(f"Projeto: {target_path}")
    print("-" * 60)
    
    # Localiza apenas páginas web
    pages = find_web_pages(target_path)
    
    if not pages:
        print("\n[!] Nenhuma página pública encontrada.")
        print("    Procurando por: HTML, JSX, TSX em diretórios pages/app")
        print("    Ignorando: docs, testes, configs, node_modules")
        output = {"script": "geo_checker", "pages_found": 0, "passed": True}
        print("\n" + json.dumps(output, indent=2))
        sys.exit(0)
    
    print(f"Foram encontradas {len(pages)} páginas públicas para análise\n")
    
    # Analisa cada página
    results = []
    for page in pages:
        result = check_page(page)
        results.append(result)
    
    # Exibe resultados
    for result in results:
        status = "[OK]" if result['score'] >= 60 else "[!]"
        print(f"{status} {result['file']}: {result['score']}%")
        if result['issues'] and result['score'] < 60:
            for issue in result['issues'][:2]:
                print(f"    - {issue}")
    
    # Pontuação média
    avg_score = sum(r['score'] for r in results) / len(results) if results else 0
    
    print("\n" + "=" * 60)
    print(f"PONTUAÇÃO GEO MÉDIA: {avg_score:.0f}%")
    print("=" * 60)
    
    if avg_score >= 80:
        print("[OK] Excelente - Conteúdo muito bem otimizado para IA")
    elif avg_score >= 60:
        print("[OK] Bom - Algumas melhorias recomendadas")
    elif avg_score >= 40:
        print("[!] Precisa melhorar - Adicione elementos estruturados")
    else:
        print("[X] Ruim - Conteúdo precisa de otimização GEO")
    
    # Saída em JSON
    output = {
        "script": "geo_checker",
        "project": str(target_path),
        "pages_checked": len(results),
        "average_score": round(avg_score),
        "passed": avg_score >= 60
    }
    print("\n" + json.dumps(output, indent=2))
    
    sys.exit(0 if avg_score >= 60 else 1)


if __name__ == "__main__":
    main()
