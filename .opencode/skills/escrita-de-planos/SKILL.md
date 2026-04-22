---
name: escrita_de_planos
description: Planejamento estruturado de tarefas com decomposição clara, dependências e critérios de verificação. Use ao implementar, refatorar ou realizar qualquer trabalho com múltiplas etapas.
tools: Ler, Glob, Grep
---

# Escrita de Planos

> Fonte: obra/superpowers

## Visão Geral
Esta habilidade fornece um framework para dividir o trabalho em tarefas claras e acionáveis, com critérios de verificação.

## Princípios de Quebra de Tarefas

### 1. Tarefas Pequenas e Focadas
- Cada tarefa deve levar de 2 a 5 minutos
- Um resultado claro por tarefa
- Verificável de forma independente

### 2. Verificação Clara
- Como você sabe que terminou?
- O que pode ser checado/testado?
- Qual é a saída esperada?

### 3. Ordem Lógica
- Dependências identificadas
- Trabalho em paralelo quando possível
- Caminho crítico destacado
- **Fase X: Verificação é SEMPRE a ÚLTIMA**

### 4. Nomeação Dinâmica na Raiz do Projeto
- Arquivos de plano são salvos como `{task-slug}.md` na RAIZ DO PROJETO
- Nome derivado da tarefa (ex.: “add auth” → `auth-feature.md`)
- **NUNCA** dentro de `.claude/`, `docs/` ou pastas temporárias

## Princípios de Planejamento (NÃO Templates!)

> 🔴 **NÃO há templates fixos. Cada plano é ÚNICO para a tarefa.**

### Princípio 1: Mantenha CURTO

| ❌ Errado | ✅ Certo |
|----------|----------|
| 50 tarefas com sub-subtarefas | 5–10 tarefas claras no máximo |
| Cada micro-passo listado | Apenas itens acionáveis |
| Descrições verbosas | Uma linha por tarefa |

> **Regra:** Se o plano tiver mais de 1 página, ele está longo demais. Simplifique.

---

### Princípio 2: Seja ESPECÍFICO, não Genérico

| ❌ Errado | ✅ Certo |
|----------|----------|
| “Configurar projeto” | “Executar `npx create-next-app`” |
| “Adicionar autenticação” | “Instalar next-auth, criar `/api/auth/[...nextauth].ts`” |
| “Estilizar a UI” | “Adicionar classes do Tailwind em `Header.tsx`” |

> **Regra:** Cada tarefa deve ter um resultado claro e verificável.

---

### Princípio 3: Conteúdo Dinâmico Baseado no Tipo de Projeto

**Para NOVO PROJETO:**
- Qual stack tecnológica? (decidir primeiro)
- Qual é o MVP? (funcionalidades mínimas)
- Qual será a estrutura de pastas?

**Para ADIÇÃO DE FUNCIONALIDADE:**
- Quais arquivos serão afetados?
- Quais dependências são necessárias?
- Como verificar que funciona?

**Para CORREÇÃO DE BUG:**
- Qual é a causa raiz?
- Qual arquivo/linha alterar?
- Como testar a correção?

---

### Princípio 4: Scripts São Específicos do Projeto

> 🔴 **NÃO copie e cole comandos de script. Escolha com base no tipo de projeto.**

| Tipo de Projeto | Scripts Relevantes |
|-----------------|-------------------|
| Frontend/React | `ux_audit.py`, `accessibility_checker.py` |
| Backend/API | `api_validator.py`, `security_scan.py` |
| Mobile | `mobile_audit.py` |
| Banco de Dados | `schema_validator.py` |
| Full-stack | Combinação dos acima conforme o que foi alterado |

**Errado:** Adicionar todos os scripts em todo plano  
**Certo:** Apenas scripts relevantes para ESTA tarefa

---

### Princípio 5: Verificação é Simples

| ❌ Errado | ✅ Certo |
|----------|----------|
| “Verificar se o componente funciona corretamente” | “Executar `npm run dev`, clicar no botão, ver o toast” |
| “Testar a API” | “`curl localhost:3000/api/users` retorna 200” |
| “Checar estilos” | “Abrir o navegador e verificar se o toggle de dark mode funciona” |

---

## Estrutura do Plano (Flexível, Não Fixa!)

```

# [Nome da Tarefa]

## Objetivo

Uma frase: O que estamos construindo/corrigindo?

## Tarefas

* [ ] Tarefa 1: [Ação específica] → Verificar: [Como checar]
* [ ] Tarefa 2: [Ação específica] → Verificar: [Como checar]
* [ ] Tarefa 3: [Ação específica] → Verificar: [Como checar]

## Concluído Quando

* [ ] [Critério principal de sucesso]

```

> **É só isso.** Sem fases, sem subseções, a menos que seja realmente necessário.  
> Mantenha o mínimo. Adicione complexidade apenas quando preciso.

## Observações
[Quaisquer considerações importantes]

---

## Boas Práticas (Referência Rápida)

1. **Comece pelo objetivo** — O que estamos construindo/corrigindo?
2. **Máx. 10 tarefas** — Se passar disso, quebre em múltiplos planos
3. **Cada tarefa verificável** — Critérios claros de “feito”
4. **Específico do projeto** — Nada de templates copiados
5. **Atualize conforme avança** — Marque `[x]` quando concluir

---

## Quando Usar

- Novo projeto do zero
- Adição de funcionalidade
- Correção de bug (se complexa)
- Refatoração envolvendo múltiplos arquivos
```
