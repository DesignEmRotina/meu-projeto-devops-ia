---
name: verificação-e-validação
description: Procedimentos automáticos de controle de qualidade, lint e análise estática. Use após CADA modificação de código para garantir correção de sintaxe e aderência aos padrões do projeto. Dispara por palavras-chave: lint, format, check, validate, types, static analysis.
risk: desconhecido
source: comunidade
date_added: 27/02/2026
---

# Skill de Lint e Validação

> **OBRIGATÓRIO:** Execute as ferramentas de validação apropriadas após TODA alteração de código.  
> Não finalize uma tarefa até que o código esteja livre de erros.

---

## Procedimentos por Ecossistema

### Node.js / TypeScript
1. **Lint/Fix:** `npm run lint` ou `npx eslint "path" --fix`
2. **Tipos:** `npx tsc --noEmit`
3. **Segurança:** `npm audit --audit-level=high`

### Python
1. **Linter (Ruff):** `ruff check "path" --fix` (Rápido e moderno)
2. **Segurança (Bandit):** `bandit -r "path" -ll`
3. **Tipos (MyPy):** `mypy "path"`

---

## O Ciclo de Qualidade

1. **Escrever/Editar Código**
2. **Executar Auditoria:** `npm run lint && npx tsc --noEmit`
3. **Analisar Relatório:** Verificar a seção **"FINAL AUDIT REPORT"**
4. **Corrigir & Repetir:** Submeter código com falhas no **FINAL AUDIT** **NÃO é permitido**

---

## Tratamento de Erros

- Se o `lint` falhar: Corrija imediatamente os problemas de estilo ou sintaxe.
- Se o `tsc` falhar: Corrija os erros de tipagem antes de prosseguir.
- Se nenhuma ferramenta estiver configurada: Verifique a raiz do projeto por  
  `.eslintrc`, `tsconfig.json`, `pyproject.toml` e **sugira a criação de um deles**.

---

**Regra Estrita:**  
Nenhum código deve ser commitado ou reportado como **"concluído"** sem passar por todas essas verificações.

---

## Scripts

| Script | Finalidade | Comando |
|-------|------------|---------|
| `scripts/executor_de_lint.py` | Verificação unificada de lint | `python scripts/executor_de_lint.py <project_path>` |
| `scripts/cobertura_de_tipos.py` | Análise de cobertura de tipos | `python scripts/cobertura_de_tipos.py <project_path>` |
