#!/usr/bin/env python3
"""
Gerenciador de Sessão - Antigravity Kit
======================================
Analisa o estado do projeto, detecta a stack tecnológica, acompanha estatísticas
de arquivos e fornece um resumo da sessão atual.

Uso:
    python .agent/scripts/gerenciador_de_sessões.py status [path]
    python .agent/scripts/gerenciador_de_sessões.py info [path]
"""

import os
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List

def get_project_root(path: str) -> Path:
    return Path(path).resolve()

def analyze_package_json(root: Path) -> Dict[str, Any]:
    pkg_file = root / "package.json"
    if not pkg_file.exists():
        return {"type": "desconhecido", "dependencies": {}}
    
    try:
        with open(pkg_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        deps = data.get("dependencies", {})
        dev_deps = data.get("devDependencies", {})
        all_deps = {**deps, **dev_deps}
        
        stack = []
        if "next" in all_deps: stack.append("Next.js")
        elif "react" in all_deps: stack.append("React")
        elif "vue" in all_deps: stack.append("Vue")
        elif "svelte" in all_deps: stack.append("Svelte")
        elif "express" in all_deps: stack.append("Express")
        elif "nestjs" in all_deps or "@nestjs/core" in all_deps: stack.append("NestJS")
        
        if "tailwindcss" in all_deps: stack.append("Tailwind CSS")
        if "prisma" in all_deps: stack.append("Prisma")
        if "typescript" in all_deps: stack.append("TypeScript")
        
        return {
            "name": data.get("name", "sem-nome"),
            "version": data.get("version", "0.0.0"),
            "stack": stack,
            "scripts": list(data.get("scripts", {}).keys())
        }
    except Exception as e:
        return {"erro": str(e)}

def count_files(root: Path) -> Dict[str, int]:
    stats = {"criados": 0, "modificados": 0, "total": 0}
    # Contagem simples por enquanto; rastreamento completo exigiria git diff ou histórico detalhado
    exclude = {".git", "node_modules", ".next", "dist", "build", ".agent", ".gemini", "__pycache__"}
    
    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in exclude]
        stats["total"] += len(files)
        
    return stats

def detect_features(root: Path) -> List[str]:
    # Heurística: analisar nomes de pastas dentro de src/
    features = []
    src = root / "src"
    if src.exists():
        possible_dirs = ["components", "modules", "features", "app", "pages", "services"]
        for d in possible_dirs:
            p = src / d
            if p.exists() and p.is_dir():
                # Listar subpastas como possíveis funcionalidades
                for child in p.iterdir():
                    if child.is_dir():
                        features.append(child.name)
    return features[:10]  # Limitar às 10 principais

def print_status(root: Path):
    info = analyze_package_json(root)
    stats = count_files(root)
    features = detect_features(root)
    
    print("\n=== Status do Projeto ===")
    print(f"\n📁 Projeto: {info.get('name', root.name)}")
    print(f"📂 Caminho: {root}")
    print(f"🏷️  Tipo: {', '.join(info.get('stack', ['Genérico']))}")
    print(f"📊 Status: Ativo")
    
    print("\n🔧 Stack Tecnológica:")
    for tech in info.get('stack', []):
        print(f"   • {tech}")
        
    print(f"\n✅ Módulos/Funcionalidades Detectados ({len(features)}):")
    for feat in features:
        print(f"   • {feat}")
    if not features:
        print("   (Nenhum módulo de funcionalidade distinto detectado)")
        
    print(f"\n📄 Arquivos: {stats['total']} arquivos totais rastreados")
    print("\n=========================\n")

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Sessão")
    parser.add_argument("command", choices=["status", "info"], help="Comando a ser executado")
    parser.add_argument("path", nargs="?", default=".", help="Caminho do projeto")
    
    args = parser.parse_args()
    root = get_project_root(args.path)
    
    if args.command == "status":
        print_status(root)
    elif args.command == "info":
        print(json.dumps(analyze_package_json(root), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
