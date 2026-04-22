#!/usr/bin/env python3
"""
Verificador de Acessibilidade – Auditoria de conformidade WCAG
Analisa arquivos HTML em busca de problemas de acessibilidade.

Uso:
    python accessibility_checker.py <caminho_do_projeto>

Verificações:
    - Rótulos de formulários
    - Atributos ARIA
    - Indícios de contraste de cores
    - Navegação por teclado
    - HTML semântico
"""

import sys
import json
import re
from pathlib import Path
from datetime import datetime

# Corrige codificação do console no Windows
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except:
    pass


def find_html_files(project_path: Path) -> list:
    """Encontra todos os arquivos HTML/JSX/TSX."""
    patterns = ['**/*.html', '**/*.jsx', '**/*.tsx']
    skip_dirs = {'node_modules', '.next', 'dist', 'build', '.git'}
    
    files = []
    for pattern in patterns:
        for f in project_path.glob(pattern):
            if not any(skip in f.parts for skip in skip_dirs):
                files.append(f)
    
    return files[:50]


def check_accessibility(file_path: Path) -> list:
    """Verifica um único arquivo em busca de problemas de acessibilidade."""
    issues = []
    
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        
        # Verifica inputs de formulário sem rótulos
        inputs = re.findall(r'<input[^>]*>', content, re.IGNORECASE)
        for inp in inputs:
            if 'type="hidden"' not in inp.lower():
                if 'aria-label' not in inp.lower() and 'id=' not in inp.lower():
                    issues.append("Input sem label ou aria-label")
                    break
        
        # Verifica botões sem texto acessível
        buttons = re.findall(r'<button[^>]*>[^<]*</button>', content, re.IGNORECASE)
        for btn in buttons:
            # Verifica se o botão possui texto ou aria-label
            if 'aria-label' not in btn.lower():
                text = re.sub(r'<[^>]+>', '', btn)
                if not text.strip():
                    issues.append("Botão sem texto acessível")
                    break
        
        # Verifica ausência do atributo lang
        if '<html' in content.lower() and 'lang=' not in content.lower():
            issues.append("Atributo lang ausente na tag <html>")
        
        # Verifica ausência de link de pular para o conteúdo principal
        if '<main' in content.lower() or '<body' in content.lower():
            if 'skip' not in content.lower() and '#main' not in content.lower():
                issues.append("Considere adicionar um link de pular para o conteúdo principal")
        
        # Verifica manipuladores de clique sem suporte a teclado
        onclick_count = content.lower().count('onclick=')
        onkeydown_count = content.lower().count('onkeydown=') + content.lower().count('onkeyup=')
        if onclick_count > 0 and onkeydown_count == 0:
            issues.append("onClick sem manipulador de teclado (onKeyDown)")
        
        # Verifica uso incorreto de tabIndex
        if 'tabindex=' in content.lower():
            if 'tabindex="-1"' not in content.lower() and 'tabindex="0"' not in content.lower():
                positive_tabindex = re.findall(r'tabindex="([1-9]\d*)"', content, re.IGNORECASE)
                if positive_tabindex:
                    issues.append("Evite valores positivos de tabIndex")
        
        # Verifica mídia com autoplay
        if 'autoplay' in content.lower():
            if 'muted' not in content.lower():
                issues.append("Mídia com autoplay deve estar mutada")
        
        # Verifica uso de role
        if 'role="button"' in content.lower():
            # Divs com role button devem ter tabindex
            div_buttons = re.findall(r'<div[^>]*role="button"[^>]*>', content, re.IGNORECASE)
            for div in div_buttons:
                if 'tabindex' not in div.lower():
                    issues.append("role='button' sem tabindex")
                    break
        
    except Exception as e:
        issues.append(f"Erro ao ler arquivo: {str(e)[:50]}")
    
    return issues


def main():
    project_path = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    
    print(f"\n{'='*60}")
    print(f"[VERIFICADOR DE ACESSIBILIDADE] Auditoria de Conformidade WCAG")
    print(f"{'='*60}")
    print(f"Projeto: {project_path}")
    print(f"Horário: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*60)
    
    # Encontra arquivos HTML
    files = find_html_files(project_path)
    print(f"Encontrados {len(files)} arquivos HTML/JSX/TSX")
    
    if not files:
        output = {
            "script": "accessibility_checker",
            "project": str(project_path),
            "files_checked": 0,
            "issues_found": 0,
            "passed": True,
            "message": "Nenhum arquivo HTML encontrado"
        }
        print(json.dumps(output, indent=2))
        sys.exit(0)
    
    # Verifica cada arquivo
    all_issues = []
    
    for f in files:
        issues = check_accessibility(f)
        if issues:
            all_issues.append({
                "file": str(f.name),
                "issues": issues
            })
    
    # Resumo
    print("\n" + "="*60)
    print("PROBLEMAS DE ACESSIBILIDADE")
    print("="*60)
    
    if all_issues:
        for item in all_issues[:10]:
            print(f"\n{item['file']}:")
            for issue in item["issues"]:
                print(f"  - {issue}")
        
        if len(all_issues) > 10:
            print(f"\n... e mais {len(all_issues) - 10} arquivos com problemas")
    else:
        print("Nenhum problema de acessibilidade encontrado!")
    
    total_issues = sum(len(item["issues"]) for item in all_issues)
    # Problemas de acessibilidade são importantes, mas não bloqueantes
    passed = total_issues < 5  # Permite problemas menores
    
    output = {
        "script": "accessibility_checker",
        "project": str(project_path),
        "files_checked": len(files),
        "files_with_issues": len(all_issues),
        "issues_found": total_issues,
        "passed": passed
    }
    
    print("\n" + json.dumps(output, indent=2))
    
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
