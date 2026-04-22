#!/usr/bin/env python3
"""
Test Runner - Execução unificada de testes e relatório de cobertura
Executa testes e gera relatório de cobertura com base no tipo do projeto.

Uso:
    python test_runner.py <caminho_do_projeto> [--coverage]

Suporta:
    - Node.js: npm test, jest, vitest
    - Python: pytest, unittest
"""

import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime

# Corrige encoding do console no Windows
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except:
    pass


def detect_test_framework(project_path: Path) -> dict:
    """Detecta o framework de testes e os comandos apropriados."""
    result = {
        "type": "unknown",
        "framework": None,
        "cmd": None,
        "coverage_cmd": None
    }
    
    # Projeto Node.js
    package_json = project_path / "package.json"
    if package_json.exists():
        result["type"] = "node"
        try:
            pkg = json.loads(package_json.read_text(encoding='utf-8'))
            scripts = pkg.get("scripts", {})
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            
            # Verifica script de teste
            if "test" in scripts:
                result["framework"] = "npm test"
                result["cmd"] = ["npm", "test"]
                
                # Tenta detectar framework específico para cobertura
                if "vitest" in deps:
                    result["framework"] = "vitest"
                    result["coverage_cmd"] = ["npx", "vitest", "run", "--coverage"]
                elif "jest" in deps:
                    result["framework"] = "jest"
                    result["coverage_cmd"] = ["npx", "jest", "--coverage"]
            elif "vitest" in deps:
                result["framework"] = "vitest"
                result["cmd"] = ["npx", "vitest", "run"]
                result["coverage_cmd"] = ["npx", "vitest", "run", "--coverage"]
            elif "jest" in deps:
                result["framework"] = "jest"
                result["cmd"] = ["npx", "jest"]
                result["coverage_cmd"] = ["npx", "jest", "--coverage"]
                
        except:
            pass
    
    # Projeto Python
    if (project_path / "pyproject.toml").exists() or (project_path / "requirements.txt").exists():
        result["type"] = "python"
        result["framework"] = "pytest"
        result["cmd"] = ["python", "-m", "pytest", "-v"]
        result["coverage_cmd"] = ["python", "-m", "pytest", "--cov", "--cov-report=term-missing"]
    
    return result


def run_tests(cmd: list, cwd: Path) -> dict:
    """Executa os testes e retorna os resultados."""
    result = {
        "passed": False,
        "output": "",
        "error": "",
        "tests_run": 0,
        "tests_passed": 0,
        "tests_failed": 0
    }
    
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=300  # Timeout de 5 minutos para testes
        )
        
        result["output"] = proc.stdout[:3000] if proc.stdout else ""
        result["error"] = proc.stderr[:500] if proc.stderr else ""
        result["passed"] = proc.returncode == 0
        
        # Tenta extrair contagem de testes a partir da saída
        output = proc.stdout or ""
        
        # Padrão Jest/Vitest: "Tests: X passed, Y failed, Z total"
        if "passed" in output.lower() and "failed" in output.lower():
            import re
            match = re.search(r'(\d+)\s+passed', output, re.IGNORECASE)
            if match:
                result["tests_passed"] = int(match.group(1))
            match = re.search(r'(\d+)\s+failed', output, re.IGNORECASE)
            if match:
                result["tests_failed"] = int(match.group(1))
            result["tests_run"] = result["tests_passed"] + result["tests_failed"]
        
        # Padrão Pytest: "X passed, Y failed"
        if "pytest" in str(cmd):
            import re
            match = re.search(r'(\d+)\s+passed', output)
            if match:
                result["tests_passed"] = int(match.group(1))
            match = re.search(r'(\d+)\s+failed', output)
            if match:
                result["tests_failed"] = int(match.group(1))
            result["tests_run"] = result["tests_passed"] + result["tests_failed"]
        
    except FileNotFoundError:
        result["error"] = f"Comando não encontrado: {cmd[0]}"
    except subprocess.TimeoutExpired:
        result["error"] = "Timeout após 300s"
    except Exception as e:
        result["error"] = str(e)
    
    return result


def main():
    project_path = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    with_coverage = "--coverage" in sys.argv
    
    print(f"\n{'='*60}")
    print(f"[TEST RUNNER] Execução Unificada de Testes")
    print(f"{'='*60}")
    print(f"Projeto: {project_path}")
    print(f"Cobertura: {'ativada' if with_coverage else 'desativada'}")
    print(f"Horário: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Detecta o framework de testes
    test_info = detect_test_framework(project_path)
    print(f"Tipo: {test_info['type']}")
    print(f"Framework: {test_info['framework']}")
    print("-"*60)
    
    if not test_info["cmd"]:
        print("Nenhum framework de testes encontrado para este projeto.")
        output = {
            "script": "test_runner",
            "project": str(project_path),
            "type": test_info["type"],
            "framework": None,
            "passed": True,
            "message": "Nenhum teste configurado"
        }
        print(json.dumps(output, indent=2))
        sys.exit(0)
    
    # Escolhe o comando
    cmd = test_info["coverage_cmd"] if with_coverage and test_info["coverage_cmd"] else test_info["cmd"]
    
    print(f"Executando: {' '.join(cmd)}")
    print("-"*60)
    
    # Executa os testes
    result = run_tests(cmd, project_path)
    
    # Exibe saída (truncada)
    if result["output"]:
        lines = result["output"].split("\n")
        for line in lines[:30]:
            print(line)
        if len(lines) > 30:
            print(f"... ({len(lines) - 30} linhas adicionais)")
    
    # Resumo
    print("\n" + "="*60)
    print("RESUMO")
    print("="*60)
    
    if result["passed"]:
        print("[PASS] Todos os testes passaram")
    else:
        print("[FAIL] Alguns testes falharam")
        if result["error"]:
            print(f"Erro: {result['error'][:200]}")
    
    if result["tests_run"] > 0:
        print(
            f"Testes: {result['tests_run']} no total, "
            f"{result['tests_passed']} passaram, "
            f"{result['tests_failed']} falharam"
        )
    
    output = {
        "script": "test_runner",
        "project": str(project_path),
        "type": test_info["type"],
        "framework": test_info["framework"],
        "tests_run": result["tests_run"],
        "tests_passed": result["tests_passed"],
        "tests_failed": result["tests_failed"],
        "passed": result["passed"]
    }
    
    print("\n" + json.dumps(output, indent=2))
    
    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
