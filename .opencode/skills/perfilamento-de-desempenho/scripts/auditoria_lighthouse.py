#!/usr/bin/env python3
"""
Skill: performance-profiling
Script: lighthouse_audit.py
Objetivo: Executar auditoria de performance do Lighthouse em uma URL
Uso: python lighthouse_audit.py https://example.com
Saída: JSON com pontuações de performance
Nota: Requer Lighthouse CLI (npm install -g lighthouse)
"""
import subprocess
import json
import sys
import os
import tempfile

def run_lighthouse(url: str) -> dict:
    """Executa a auditoria do Lighthouse na URL."""
    try:
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            output_path = f.name
        
        result = subprocess.run(
            [
                "lighthouse",
                url,
                "--output=json",
                f"--output-path={output_path}",
                "--chrome-flags=--headless",
                "--only-categories=performance,accessibility,best-practices,seo"
            ],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if os.path.exists(output_path):
            with open(output_path, 'r') as f:
                report = json.load(f)
            os.unlink(output_path)
            
            categories = report.get("categories", {})
            return {
                "url": url,
                "scores": {
                    "performance": int(categories.get("performance", {}).get("score", 0) * 100),
                    "accessibility": int(categories.get("accessibility", {}).get("score", 0) * 100),
                    "best_practices": int(categories.get("best-practices", {}).get("score", 0) * 100),
                    "seo": int(categories.get("seo", {}).get("score", 0) * 100)
                },
                "summary": get_summary(categories)
            }
        else:
            return {
                "error": "O Lighthouse não conseguiu gerar o relatório",
                "stderr": result.stderr[:500]
            }
            
    except subprocess.TimeoutExpired:
        return {"error": "A auditoria do Lighthouse excedeu o tempo limite"}
    except FileNotFoundError:
        return {
            "error": "Lighthouse CLI não encontrado. Instale com: npm install -g lighthouse"
        }

def get_summary(categories: dict) -> str:
    """Gera um resumo com base nas pontuações."""
    perf = categories.get("performance", {}).get("score", 0) * 100
    if perf >= 90:
        return "[OK] Performance excelente"
    elif perf >= 50:
        return "[!] Precisa de melhorias"
    else:
        return "[X] Performance ruim"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Uso: python lighthouse_audit.py <url>"}))
        sys.exit(1)
    
    result = run_lighthouse(sys.argv[1])
    print(json.dumps(result, indent=2))
