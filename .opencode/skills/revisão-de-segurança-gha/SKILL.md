---
name: revisão-de-segurança-gha
description: "Encontre vulnerabilidades exploráveis ​​em fluxos de trabalho do GitHub Actions. Cada descoberta DEVE incluir um cenário de exploração concreto — se você não conseguir reproduzir o ataque, não o reporte."
risk: seguro
source: comunidade
date_add: 16/03/2026
---

<!--
Padrões de ataque e exemplos do mundo real extraídos da análise da campanha HackerBot Claw
por StepSecurity (2025): https://www.stepsecurity.io/blog/hackerbot-claw-github-actions-exploitation
-->

# Análise de Segurança do GitHub Actions

Encontre vulnerabilidades exploráveis ​​em fluxos de trabalho do GitHub Actions. Cada descoberta DEVE incluir um cenário de exploração concreto — se você não conseguir reproduzir o ataque, não o reporte.

Esta habilidade codifica padrões de ataque de exploits reais do GitHub Actions — não teoria genérica de CI/CD.

## Quando usar

- Você está revisando fluxos de trabalho do GitHub Actions em busca de vulnerabilidades de segurança exploráveis.

- A tarefa exige rastrear um caminho de ataque concreto, desde um invasor externo até a execução do fluxo de trabalho ou a exposição de segredos.

- Você precisa de uma revisão de segurança de arquivos de fluxo de trabalho, ações compostas ou scripts relacionados a fluxos de trabalho, com base apenas em evidências.

## Escopo

Revise os fluxos de trabalho fornecidos (arquivo, diff ou repositório). Pesquise o código-fonte conforme necessário para rastrear caminhos de ataque completos antes de gerar o relatório.

### Arquivos para revisão

- `.github/workflows/*.yml` — todas as definições de fluxo de trabalho
- `action.yml` / `action.yaml` — ações compostas no repositório
- `.github/actions/*/action.yml` — ações locais reutilizáveis
- Arquivos de configuração carregados pelos fluxos de trabalho: `CLAUDE.md`, `AGENTS.md`, `Makefile`, scripts shell em `.github/`

### Fora do escopo

- Fluxos de trabalho em outros repositórios (observe apenas a dependência)
- Permissões de instalação do GitHub App (observe se relevante)

## Modelo de ameaça

Relate apenas vulnerabilidades exploráveis ​​por um **atacante externo** — alguém **sem** acesso de escrita ao repositório. O atacante pode abrir PRs a partir de forks, criar issues e postar comentários. Ele não pode enviar alterações para branches, acionar `workflow_dispatch` ou executar fluxos de trabalho manualmente.

**Não sinalize** vulnerabilidades que exigem acesso de escrita para serem exploradas:
- Injeção de entrada em `workflow_dispatch` — requer acesso de escrita para ser acionada
- Injeção de expressão em fluxos de trabalho somente com `push` em branches protegidas
- Injeção de entrada em `workflow_call` onde todos os chamadores são internos
- Segredos em fluxos de trabalho somente com `workflow_dispatch`/`schedule`

## Confiança

Relate apenas descobertas com **ALTA** e **MÉDIA** confiança. Não relate problemas teóricos.

| Confiança | Critérios | Ação |

|---|---|---|

| **ALTA** | Caminho de ataque completo rastreado, explorável confirmado | Relatar com cenário de exploração e correção |

| **MÉDIA** | Caminho de ataque parcialmente confirmado, vínculo incerto | Relatar como necessitando de verificação |

| **BAIXA** | Teórica ou mitigada em outro lugar | Não relatar |

Para cada descoberta de ALTA RISCO, forneça todos os cinco elementos:

1. **Ponto de entrada** — Como o atacante entra? (fork de PR, comentário em issue, nome da branch, etc.)
2. **Carga útil** — O que o atacante envia? (código/YAML/entrada)
3. **Mecanismo de execução** — Como a carga útil é executada? (expansão de expressão, checkout + script, etc.)
4. **Impacto** — O que o atacante ganha? (roubo de token, execução de código, acesso de escrita ao repositório)
5. **Esboço de PoC** — Passos concretos que um atacante seguiria

Se você não conseguir construir todos os cinco elementos, reporte como MÉDIO (precisa de verificação).

---

## Etapa 1: Classificar Gatilhos e Carregar Referências

Para cada fluxo de trabalho, identifique os gatilhos e carregue a referência apropriada:

| Gatilho / Padrão | Carregar Referência |

|---|---|

| `pull_request_target` | `references/pwn-request.md` |
| `issue_comment` com análise de comando | `references/comment-triggered-commands.md` |
| `${{ }}` em blocos `run:` | `references/expression-injection.md` |
| PATs / chaves de implantação / credenciais elevadas | `references/credential-escalation.md` |
| Carregamento de código PR e arquivo de configuração via CI | `references/ai-prompt-injection-via-ci.md` |
| Ações de terceiros (especialmente não fixadas) | `references/supply-chain.md` |
| Uso de bloco `permissions:` ou segredos | `references/permissions-and-secrets.md` |
| Uso de runners auto-hospedados, cache/artefatos | `references/runner-infrastructure.md` |
| Qualquer descoberta confirmada | `references/real-world-attacks.md` |

Carregar referências seletivamente — apenas o que for relevante para os gatilhos encontrados.

## Etapa 2: Verificar Classes de Vulnerabilidade

### Verificação 1: Solicitação de Pwn

O fluxo de trabalho usa `pull_request_target` E faz checkout do código do fork?

- Procure por `actions/checkout` com `ref:` apontando para o cabeçalho do PR
- Procure por ações locais (`./.github/actions/`) que viriam do fork
- Verifique se alguma etapa `run:` executa código do PR que foi feito o checkout

### Verificação 2: Injeção de Expressão

Expressões `${{ }}` são usadas dentro de blocos `run:` em fluxos de trabalho acionáveis ​​externamente?

- Mapeie cada expressão `${{ }}` em cada etapa `run:`
- Confirme se o valor é controlado pelo atacante (título do PR, nome da branch, corpo do comentário — não IDs numéricos, SHAs ou nomes de repositórios)
- Confirme se a expressão está em um bloco `run:`, não em `if:`, `with:` ou em um bloco `env:` no nível do job

### Verificação 3: Execução de Comandos Não Autorizados

Um fluxo de trabalho acionado por `issue_comment` executa comandos sem autorização?

- Existe uma verificação de `author_association`?

- Qualquer usuário do GitHub pode acionar o comando?

- O manipulador de comandos também usa expressões injetáveis?

### Verificação 4: Elevação de Credenciais

Credenciais elevadas (PATs, chaves de implantação) são acessíveis a código não confiável?

- Qual é o raio de explosão de cada segredo?

- Um fluxo de trabalho comprometido poderia roubar tokens de longa duração?

### Verificação 5: Envenenamento de Arquivos de Configuração

O fluxo de trabalho carrega configurações de arquivos fornecidos pelo PR?

- Instruções do agente de IA: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`
- Configuração de compilação: `Makefile`, scripts de shell

### Verificação 6: Cadeia de Suprimentos

As ações de terceiros estão fixadas com segurança?

### Verificação 7: Permissões e Segredos

As permissões do fluxo de trabalho são mínimas? Os segredos têm escopo adequado?

### Verificação 8: Infraestrutura do Runner

Os runners, caches ou artefatos auto-hospedados são usados ​​com segurança?

## Padrões Seguros (Não Sinalizar)

Antes de reportar, verifique se o padrão é realmente seguro:

| Padrão | Por que é seguro |

|---|---|

| `pull_request_target` SEM checkout do código do fork | Nunca executa código do atacante |

| `${{ github.event.pull_request.number }}` em `run:` | Somente numérico — não injetável |
| `${{ github.repository }}` / `github.repository_owner` | O proprietário do repositório controla isso |
| `${{ secrets.* }}` | Não é um vetor de injeção de expressão |
| `${{ }}` em condições `if:` | Avaliado pelo tempo de execução do Actions, não pelo shell |
| `${{ }}` em entradas `with:` | Passado como parâmetros de string, não avaliado pelo shell |
| Ações fixadas no SHA completo | Referência imutável |
| Gatilho `pull_request` (não `_target`) | Executa no contexto de fork com token somente leitura |
| Qualquer expressão em `workflow_dispatch`/`schedule`/`push` para branches protegidos | Requer acesso de escrita — fora do modelo de ameaça | **Diferença importante:** `${{ }}` é perigoso em blocos `run:` (expansão de shell), mas seguro em `if:`, `with:` e `env:` no nível do job/etapa (avaliação em tempo de execução das ações).

## Etapa 3: Validar antes de relatar

Antes de incluir qualquer descoberta, leia o YAML do fluxo de trabalho e rastreie todo o caminho do ataque:

1. **Leia o fluxo de trabalho completo** — não confie apenas na saída do grep
2. **Rastreie o gatilho** — confirme o evento e verifique as condições `if:` que controlam a execução
3. **Rastreie a expressão/checkout** — confirme se está em um bloco `run:` ou se realmente faz referência a código de fork
4. **Confirme o controle do atacante** — verifique se o valor corresponde a algo definido por um atacante externo
5. **Verifique as mitigações existentes** — encapsulamento de variáveis ​​de ambiente, verificações de associação de autor, permissões restritas, fixação de SHA

Se algum link estiver quebrado, marque como MÉDIO (precisa de verificação) ou descarte a descoberta. **Se nenhuma verificação resultar em constatação, informe zero constatações.** Não invente problemas.**

## Etapa 4: Relatar Resultados

````markdown
## Revisão de Segurança do GitHub Actions

### Resultados

### [GHA-001] [Título] (Gravidade: Crítica/Alta/Média)
- **Fluxo de Trabalho**: `.github/workflows/release.yml:15`
- **Gatilho**: `pull_request_target`
- **Confiança**: ALTA — confirmada por meio de rastreamento de caminho de ataque
- **Cenário de Exploração**:

1. [Ataque passo a passo]
- **Impacto**: [O que o atacante ganha]
- **Correção**: [Código que corrige o problema]

### Necessita de Verificação
[Itens de confiança MÉDIA com explicação do que verificar]

### Revisado e Aprovado
[Fluxos de trabalho revisados ​​e considerados seguros]
````

Se não houver resultados: "Nenhum explorável" Vulnerabilidades identificadas. Todos os fluxos de trabalho foram revisados ​​e aprovados.