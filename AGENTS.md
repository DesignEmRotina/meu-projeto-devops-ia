# AGENTS.md — Regras Universais do Projeto DevOps IA

> **LEIA ESTE ARQUIVO IMEDIATAMENTE** antes de qualquer ação.
> Este documento é a **fonte única de verdade** para todos os agentes LLM, subagentes, orquestradores e ferramentas que operam neste repositório.
> Qualquer instrução neste arquivo **sobrepõe** defaults de modelo, prompts do sistema e configurações de tool.

---

## Índice

1. [Identidade e Propósito do Projeto](#1-identidade-e-propósito-do-projeto)
2. [Princípios Fundamentais](#2-princípios-fundamentais)
3. [Estrutura de Agentes e Hierarquia](#3-estrutura-de-agentes-e-hierarquia)
4. [Fases do Ciclo de Vida e Orquestradores](#4-fases-do-ciclo-de-vida-e-orquestradores)
5. [Protocolo de Invocação de Subagentes](#5-protocolo-de-invocação-de-subagentes)
6. [Arquivos Canônicos e Contratos](#6-arquivos-canônicos-e-contratos)
7. [Memória de Agentes](#7-memória-de-agentes)
8. [Logs e Rastreabilidade](#8-logs-e-rastreabilidade)
9. [Scripts e Automações](#9-scripts-e-automações)
10. [Skills Modulares](#10-skills-modulares)
11. [Ferramentas e MCP](#11-ferramentas-e-mcp)
12. [Workflows e Comandos Rápidos](#12-workflows-e-comandos-rápidos)
13. [Documentação e Entregáveis](#13-documentação-e-entregáveis)
14. [Padrões de Código e Qualidade](#14-padrões-de-código-e-qualidade)
15. [Segurança e Compliance](#15-segurança-e-compliance)
16. [Regras de Git e Versionamento](#16-regras-de-git-e-versionamento)
17. [Onboarding de Novo Agente](#17-onboarding-de-novo-agente)

---

## 1. Identidade e Propósito do Projeto

```yaml
projeto: meu-projeto-devops-ia
repositório: github.com/<org>/meu-projeto-devops-ia
raiz: meu-projeto-devops-ia/
config_agentes: .opencode/
fonte_da_verdade: AGENTS.md  # este arquivo
```

Este repositório hospeda uma **plataforma DevOps orientada a IA** com agentes especializados cobrindo todo o ciclo de vida de software — da concepção ao monitoramento em produção. A arquitetura segue **Clean Architecture / Vertical Slice** com orquestradores por fase e subagentes especializados.

**Missão dos agentes:** executar tarefas de engenharia de software de ponta a ponta com qualidade profissional, rastreabilidade total e interoperabilidade entre fases, sem perder contexto entre sessões.

---

## 2. Princípios Fundamentais

Todos os agentes DEVEM seguir estes princípios, sem exceção:

### 2.1 — Leia Antes de Agir
- Antes de qualquer tarefa, leia os arquivos relevantes em `.opencode/canonical/` e `.opencode/contracts/`.
- Consulte `docs/interno/dr-estruturado.json` e `docs/interno/backlog-moscow-estruturado.yaml` para contexto de requisitos.
- Nunca assuma — sempre verifique o estado real dos arquivos.

### 2.2 — Contexto Antes de Código
- Toda geração de código ou artefato deve ser precedida da leitura de:
  - `.opencode/canonical/padroes-codigo.md`
  - `.opencode/canonical/convenções-nomenclatura.md`
  - `.opencode/canonical/guia-estilo.md`

### 2.3 — Rastreabilidade Obrigatória
- Toda decisão relevante deve ser registrada em `.opencode/logs/atual/` (formato JSONL).
- Toda mudança de requisito ou escopo deve atualizar `docs/interno/matriz-rastreabilidade.md`.

### 2.4 — Falhe Explicitamente
- Quando um agente não tem informação suficiente para agir com segurança, ele DEVE parar e solicitar esclarecimento ao orquestrador pai ou ao usuário — nunca inventar dados.

### 2.5 — Idempotência
- Scripts e agentes de deploy devem ser **idempotentes**: executar N vezes produz o mesmo resultado que executar uma vez.

### 2.6 — Segurança por Padrão
- Nenhum agente deve escrever credenciais, tokens ou secrets em arquivos versionados.
- Use sempre variáveis de ambiente ou vault. Consulte `.opencode/canonical/baselines-seguranca-desempenho.md`.

### 2.7 — Separação de Responsabilidades
- Cada agente/subagente tem escopo bem definido. Nunca um subagente deve executar responsabilidade de outro sem delegação explícita do orquestrador.

---

## 3. Estrutura de Agentes e Hierarquia

```
USUÁRIO / SISTEMA
      │
      ▼
┌────────────────────────────────────────────┐
│          ORQUESTRADOR DE FASE              │
│  (ex: DESENVOLVIMENTO_AGENTE.md)           │
│  - Lê AGENTS.md e canonical/               │
│  - Decompõe tarefas em subtarefas          │
│  - Delega para subagentes especializados   │
│  - Consolida resultados                    │
│  - Registra log + atualiza memória         │
└────────────────────────────────────────────┘
      │              │              │
      ▼              ▼              ▼
 SUBAGENTE_A   SUBAGENTE_B   SUBAGENTE_C
 (especialista) (especialista) (especialista)
```

### Regras de Hierarquia

| Nível | Papel | Pode invocar |
|-------|-------|--------------|
| 0 | Usuário/Sistema | Qualquer orquestrador de fase |
| 1 | Orquestrador de Fase | Subagentes da sua fase + leitura de canonical/ |
| 2 | Subagente | Somente suas ferramentas definidas; NÃO invoca outros subagentes diretamente |
| 3 | Script/Tool | Execução atômica, sem estado próprio |

> **Regra de ouro:** Subagentes **reportam** ao orquestrador. O orquestrador **decide** se invoca outro subagente.

---

## 4. Fases do Ciclo de Vida e Orquestradores

Cada fase tem um **Orquestrador Principal** (arquivo `*_AGENTE.md`) que coordena os subagentes listados. O orquestrador é a **única entrada e saída** da fase — nunca acione um subagente diretamente sem passar pelo orquestrador de fase.

---

### FASE 1 — Concepção
**Orquestrador:** `.opencode/agents/CONCEPCAO_AGENTE.md`

**Responsabilidades:**
- Qualificar leads e entender necessidades do cliente
- Gerar proposta comercial e técnica
- Conduzir formalização contratual

**Subagentes disponíveis:**

| Arquivo | Especialidade |
|---------|---------------|
| `QUALIFICACAO_LEADS_SUBAGENTE.md` | Qualifica e pontua leads recebidos |
| `ANALISE_NECESSIDADES_SUBAGENTE.md` | Extrai e estrutura necessidades do cliente |
| `GERACAO_PROPOSTAS_SUBAGENTE.md` | Gera `docs/cliente/proposta-comercial-tecnica.md` |
| `FORMALIZACAO_CONTRATUAL_SUBAGENTE.md` | Gera e revisa `docs/cliente/contrato-prestacao-servico.md` |

**Entregáveis obrigatórios ao concluir a fase:**
- [ ] `docs/cliente/proposta-comercial-tecnica.md`
- [ ] `docs/cliente/contrato-prestacao-servico.md`
- [ ] `docs/interno/den-briefing-detalhado.md`
- [ ] `docs/interno/dr-estruturado.json`

---

### FASE 2 — Planejamento
**Orquestrador:** `.opencode/agents/PLANEJAMENTO_AGENTE.md`

**Responsabilidades:**
- Definir arquitetura, stack, cronograma e backlog
- Priorizar requisitos com MoSCoW
- Planejar SEO/GEO para conteúdo visual

**Subagentes disponíveis:**

| Arquivo | Especialidade |
|---------|---------------|
| `ARQUITETURA_SUBAGENTE.md` | Define e documenta arquitetura de alto nível |
| `ESTIMATIVA_CRONOGRAMA_SUBAGENTE.md` | Gera `docs/interno/cronograma-total.md` |
| `PRODUCT_MANAGER_SUBAGENTE.md` | Subagente principal do PM — coordena visão de produto |
| `PRODUCT_OWNER_SUBAGENTE.md` | Prioriza backlog com MoSCoW |
| `PROJECT_PLANNER_STACK_SUBAGENTE.md` | Define stack tecnológica e dependências |
| `ESPECIALISTA_EM_SEO_E_GEO.md` | Planeja conteúdo visual para ranqueamento |

**Entregáveis obrigatórios ao concluir a fase:**
- [ ] `docs/cliente/arquitetura-alto-nivel.md`
- [ ] `docs/cliente/backlog-produto-moscow.md`
- [ ] `docs/interno/backlog-moscow-estruturado.yaml`
- [ ] `docs/interno/cronograma-total.md`
- [ ] `ARQUITETURA.md` (raiz do projeto)
- [ ] `PRDs/` populado com PRDs da sprint inicial

---

### FASE 3 — Desenvolvimento
**Orquestrador:** `.opencode/agents/DESENVOLVIMENTO_AGENTE.md`

**Responsabilidades:**
- Implementar frontend, backend, banco de dados, APIs e código compartilhado
- Documentar código gerado
- Otimizar performance e depurar falhas

**Subagentes disponíveis:**

| Arquivo | Especialidade | Condicional? |
|---------|---------------|--------------|
| `ESPECIALISTA_FRONTEND_SUBAGENTE.md` | React/Next.js/Vue — `src/frontend/` | Não |
| `ESPECIALISTA_BACKEND_SUBAGENTE.md` | Node/Python/Go — `src/backend/` | Não |
| `ESPECIALISTA_SHARED_API_SUBAGENTE.md` | Tipos compartilhados, contratos — `src/shared/` e `src/api/` | Não |
| `ARQUITETO_BANCO_DE_DADOS_SUBAGENTE.md` | Schemas, migrations, seeds — `src/database/` | Não |
| `DEPURAÇÃO_SUBAGENTE.md` | Diagnóstico de falhas e stack traces | Sob demanda |
| `PERFORMACE_OTIMIZADOR_SUBAGENTE.md` | Otimização de gargalos de performance | Sob demanda |
| `DOCUMENTACAO_CODIGO_SUBAGENTE.md` | Gera `docs/documentação-do-código/` | Não |
| `ARQUEOLOGO_DE_CÓDIGO_SUBAGENTE.md` | Analisa código legado, identifica padrões, sugere refatorações | Sob demanda |
| `DESENVOLVEDOR_MOBILE_SUBAGENTE.md` | Apps mobile (iOS/Android/React Native) | ⚠️ Apenas se projeto inclui mobile |
| `DESENVOLVEDOR_DE_JOGOS_SUBAGENTE.md` | Desenvolvimento de jogos | ⚠️ Apenas se projeto é game |

**Entregáveis obrigatórios ao concluir a fase:**
- [ ] Código versionado em `src/` seguindo padrões de `.opencode/canonical/`
- [ ] `docs/documentação-do-código/` atualizada
- [ ] `docs/interno/cobertura-codigo-historico.json` atualizado
- [ ] Contratos de API em `src/api/` e `.opencode/contracts/contratos-de-api.yaml`

---

### FASE 4 — Teste / Qualidade
**Orquestrador:** `.opencode/agents/TESTE_AGENTE.md`

**Responsabilidades:**
- Gerar, executar e analisar todos os tipos de teste
- Garantir cobertura mínima definida em `.opencode/canonical/baselines-seguranca-desempenho.md`
- Realizar testes de segurança e penetração

**Subagentes disponíveis:**

| Arquivo | Especialidade |
|---------|---------------|
| `GERACAO_CASOS_TESTE_SUBAGENTE.md` | Gera casos de teste (`docs/interno/casos-teste-estruturados.yaml`) |
| `EXECUCAO_TESTES_SUBAGENTE.md` | Executa suítes de teste em `src/tests/` |
| `ANALISE_FALHAS_DIAGNOSTICO_SUBAGENTE.md` | Analisa falhas e gera relatório de diagnóstico |
| `TESTES_PERFORMANCE_SEGURANCA_SUBAGENTE.md` | Testes de carga, stress e segurança funcional |
| `ENGENHARIA_DE_AUTOMACAO_QA_SUBAGENTE.md` | Pipeline de automação QA (CI-ready) |
| `TESTADOR_DE_PENETRACAO_SUBAGENTE.md` | Testes de penetração e exploração de vulnerabilidades |
| `AUDITOR_DE_SEGURANÇA_SUBAGENTE.md` | Revisão estática de segurança (SAST) |

**Entregáveis obrigatórios ao concluir a fase:**
- [ ] `docs/cliente/relatorio-testes.md`
- [ ] `docs/interno/casos-teste-estruturados.yaml` atualizado
- [ ] `docs/interno/cobertura-codigo-historico.json` atualizado
- [ ] `docs/interno/checklist-liberacao.md` aprovado

---

### FASE 5 — Deploy / Implantação
**Orquestrador:** `.opencode/agents/IMPLANTACAO_AGENTE.md`

**Responsabilidades:**
- Provisionar infraestrutura via IaC
- Automatizar pipeline de deploy entre ambientes
- Validar saúde pós-deploy
- Executar rollback quando necessário

**Subagentes disponíveis:**

| Arquivo | Especialidade |
|---------|---------------|
| `IAC_PROVISIONING_SUBAGENTE.md` | Terraform/Ansible — `infraestrutura/`; atribuição de permissões RBAC |
| `AUTOMACAO_DE_DEPLOY_SUBAGENTE.md` | CI/CD — promoção automática entre ambientes |
| `HEALTH_CHECK_VALIDATION_SUBAGENTE.md` | Verifica status operacional de serviços e dependências |
| `ROLLBACK_AND_RECOVERY_SUBAGENTE.md` | Executa rollback e recuperação com reconstrução do estado |

**Entregáveis obrigatórios ao concluir a fase:**
- [ ] `docs/interno/logs-implantacao-resumo.md` atualizado
- [ ] `docs/interno/plano-rollback.md` validado
- [ ] `docs/cliente/release-notes-v<X.Y.Z>.md` gerado
- [ ] Health check verde em todos os serviços

---

### FASE 6 — Operações e Monitoramento
**Orquestrador:** `.opencode/agents/OPERACOES_E_MONITORAMENTO_AGENTE.md`

**Responsabilidades:**
- Monitorar infraestrutura e aplicação continuamente
- Detectar anomalias proativamente
- Responder a incidentes com playbooks
- Otimizar performance em produção

**Subagentes disponíveis:**

| Arquivo | Especialidade |
|---------|---------------|
| `MONITORAMENTO_INFRA_SUBAGENTE.md` | Métricas de infraestrutura (CPU, memória, rede, disco) |
| `MONITORAMENTO_APLICACAO_SUBAGENTE.md` | APM — latência, error rate, throughput |
| `DETECCAO_ANOMALIAS_SUBAGENTE.md` | Detecção estatística de anomalias vs. `docs/interno/baselines-monitoramento.json` |
| `RESPOSTA_INCIDENTES_SUBAGENTE.md` | Executa `docs/interno/playbooks-incidentes.md` |
| `ENGENHEIRO_DEVOPS_SUBAGENTE.md` | Subagente principal DevOps — coordenação operacional |
| `PERFORMACE_OTIMIZADOR_SUBAGENTE.md` | Análise de gargalos em produção e recomendações |

**Entregáveis contínuos:**
- [ ] `docs/interno/baselines-monitoramento.json` atualizado a cada release
- [ ] `docs/interno/playbooks-incidentes.md` revisado a cada incidente pós-mortem
- [ ] `.opencode/logs/diario/` populado diariamente

---

## 5. Protocolo de Invocação de Subagentes

### 5.1 — Quando invocar um subagente

O orquestrador DEVE invocar um subagente quando:
- A tarefa requer especialização fora do escopo do orquestrador
- A tarefa é longa o suficiente para merecer contexto isolado
- A tarefa tem entregável bem definido e verificável

### 5.2 — Formato de invocação

Todo orquestrador deve passar o seguinte contexto ao invocar um subagente:

```json
{
  "invocação": {
    "orquestrador": "NOME_AGENTE.md",
    "subagente": "NOME_SUBAGENTE.md",
    "fase": "desenvolvimento",
    "tarefa": "Descrição clara e específica da tarefa",
    "contexto": {
      "arquivos_relevantes": ["src/backend/auth.ts", ".opencode/canonical/padroes-codigo.md"],
      "restrições": ["sem quebrar testes existentes", "usar padrão de erro definido em contracts/"],
      "entregável_esperado": "Função authenticate() com tipos TypeScript e JSDoc"
    },
    "prioridade": "alta | média | baixa",
    "timeout_estimado": "15min"
  }
}
```

### 5.3 — Formato de resposta do subagente

```json
{
  "resposta": {
    "subagente": "NOME_SUBAGENTE.md",
    "status": "concluído | parcial | bloqueado",
    "entregável": "descrição ou caminho do artefato gerado",
    "dependências_pendentes": [],
    "observações": "notas relevantes para o orquestrador",
    "log_entry": ".opencode/logs/atual/sessao-YYYYMMDD-HHMM.jsonl"
  }
}
```

### 5.4 — Subagentes condicionais

Os subagentes marcados com ⚠️ na tabela de cada fase SÓ devem ser invocados se o projeto explicitamente incluir aquele escopo. Verifique `docs/interno/dr-estruturado.json` antes de invocar subagentes condicionais.

---

## 6. Arquivos Canônicos e Contratos

Estes arquivos são **somente leitura para subagentes** e **atualizáveis apenas pelo orquestrador de fase ou pelo usuário**.

### 6.1 — Canonical (`/.opencode/canonical/`)

| Arquivo | Conteúdo | Leitura obrigatória para |
|---------|----------|--------------------------|
| `glosario.md` | Termos oficiais, acrônimos, jargões | Todos os agentes |
| `guia-estilo.md` | Regras de estilo (UI/UX, escrita, código) | Frontend, Documentação |
| `padroes-codigo.md` | Padrões globais de codificação | Todos os subagentes de dev |
| `convenções-nomenclatura.md` | Nomenclatura de pastas, arquivos, variáveis, branches | Todos os agentes |
| `templates.md` | User stories, PR template, release notes, API endpoint | PM, PO, Dev, QA |
| `exemplos-fewshot.md` | Exemplos canônicos de planejamento, geração, refatoração | Todos os agentes |
| `diagramas-arquitetura.md` | Diagramas Mermaid/PlantUML de referência | Arquitetura, Dev, DevOps |
| `baselines-seguranca-desempenho.md` | SLAs, limites de latência, cobertura mínima | QA, Operações, Deploy |
| `visao-objetivos-restricoes.md` | Visão, objetivos e restrições do projeto | Todos os orquestradores |

### 6.2 — Contracts (`/.opencode/contracts/`)

| Arquivo | Conteúdo | Quem valida |
|---------|----------|-------------|
| `contratos-de-api.yaml` | Interfaces de APIs internas e externas (OpenAPI) | Backend, Shared/API, QA |
| `contratos-dados.yaml` | Schemas, payloads, eventos de domínio | Backend, DB, Shared |
| `SLAs-e-nao-funcionais.md` | SLAs, uptime, latência, segurança resumida | QA, Operações, Deploy |
| `limites-legais-e-de-escopo.md` | Limites de escopo e cláusulas legais | Concepção, PM |

> **Regra crítica:** Nenhum agente deve gerar código que viole os contratos em `contracts/`. O script `.opencode/scripts/agentic/validar-contracts.sh` deve ser executado após qualquer alteração de API ou schema.

---

## 7. Memória de Agentes

### 7.1 — Memória de curto prazo (volátil — NÃO versionar)

Localização: `.opencode/memory/short-term/`

| Arquivo | Propósito |
|---------|-----------|
| `sessao-atual.jsonl` | Histórico completo da sessão (JSON Lines) |
| `resumo-contexto-ativo.md` | Resumo compactado para incluir no próximo prompt |
| `estado-temporario-agente.json` | Estado transitório do agente mestre |

**Política:** Limpo ao início de cada nova sessão. Nunca commitar. Incluído no `.gitignore`.

### 7.2 — Memória de longo prazo (persistente — versionar)

Localização: `.opencode/memory/long-term/`

| Arquivo/Pasta | Propósito |
|--------------|-----------|
| `conhecimento-projeto/fatos-projeto.md` | Fatos canônicos extraídos (stack, domain rules) |
| `conhecimento-projeto/preferencias-cliente.md` | Preferências recorrentes do cliente |
| `execuções-historicas/execução-<data>-<uuid>.md` | Resumo de runs completas |
| `resumos-semanais/` | Agregados para visão de longo prazo |
| `lições-aprendidas/lições-db.md` | Banco de lições (formato tabela) |
| `lições-aprendidas/padrões-erros.md` | Padrões de erro recorrentes + mitigações |
| `linhas-base/linhas-base-performance.json` | Evolução de métricas (coverage, latência, etc.) |

### 7.3 — Protocolo de atualização de memória

Ao **iniciar** uma sessão:
1. Leia `memory/short-term/resumo-contexto-ativo.md`
2. Leia `memory/long-term/conhecimento-projeto/fatos-projeto.md`
3. Leia o log da sessão mais recente em `logs/atual/`

Ao **encerrar** uma sessão:
1. Execute `.opencode/scripts/agentic/cura-de-memoria.sh` para compactar short-term
2. Atualize `memory/long-term/execuções-historicas/` com resumo da run
3. Atualize `memory/long-term/lições-aprendidas/lições-db.md` se houver aprendizado novo

---

## 8. Logs e Rastreabilidade

### 8.1 — Estrutura de logs

```
.opencode/logs/
├── atual/                    # Sessão atual
│   ├── sessao-YYYYMMDD-HHMM.jsonl
│   └── agentes-ativos.json
├── diario/                   # Rotação diária
│   └── DD-MM-AAAA/
│       ├── AGENTE.md.log
│       └── errors-YYYYMMDD.jsonl
├── arquivado/                # Compactados
│   └── AAAA-MM/
│       └── semana-NN.tar.gz
└── sumarios/
    └── sumario-semanal-YYYY-sNN.md
```

### 8.2 — Formato JSONL obrigatório

Cada entrada de log DEVE seguir este schema:

```json
{
  "timestamp": "2026-02-27T18:20:00Z",
  "sessao_id": "uuid-v4",
  "agente": "DESENVOLVIMENTO_AGENTE",
  "subagente": "ESPECIALISTA_BACKEND_SUBAGENTE",
  "fase": "desenvolvimento",
  "ação": "geração_de_código | decisão | erro | delegação | conclusão",
  "descrição": "Descrição legível da ação executada",
  "artefatos": ["src/backend/auth.ts"],
  "status": "sucesso | falha | parcial",
  "erro": null,
  "duração_ms": 1200
}
```

### 8.3 — O que DEVE ser logado

- Início e fim de cada invocação de orquestrador/subagente
- Toda decisão de arquitetura ou de escopo
- Todo erro encontrado (com stack trace quando disponível)
- Toda mudança em arquivos de `canonical/`, `contracts/` ou `docs/`
- Resultado de cada execução de script

### 8.4 — .gitignore para logs

Os seguintes padrões DEVEM estar no `.gitignore` raiz:
```
.opencode/logs/atual/
.opencode/logs/diario/
.opencode/memory/short-term/
*.env
*.env.local
*.env.*.local
```

---

## 9. Scripts e Automações

Localização: `.opencode/scripts/`

### 9.1 — Catálogo de scripts

| Script | Quando executar | Idempotente? |
|--------|----------------|--------------|
| `setup/iniciar.sh` | Uma vez na inicialização do projeto | ✅ |
| `setup/instalar-hooks.sh` | Uma vez por clone do repositório | ✅ |
| `dev/start-local.sh` | Início de cada sessão de desenvolvimento | ✅ |
| `dev/correção-lint.sh` | Antes de todo commit | ✅ |
| `dev/teste-watch.sh` | Durante desenvolvimento ativo | ✅ |
| `dev/resetar-prisma.sh` | Apenas em dev, ao resetar banco local | ⚠️ Destrói dados locais |
| `db/migrate.sh` | Após toda alteração de schema | ✅ |
| `db/seed.sh` | Após reset de banco | ✅ |
| `agentic/cura-de-memoria.sh` | Ao fim de cada sessão agentic | ✅ |
| `agentic/validar-contracts.sh` | Após toda alteração de API/schema | ✅ |
| `agentic/resumo-logs.sh` | Semanalmente ou sob demanda | ✅ |
| `ci/instalar-dep.sh` | Apenas em CI/CD (GitHub Actions) | ✅ |
| `ci/cobertura-relatorio.sh` | Apenas em CI/CD pós-testes | ✅ |
| `utils/limpeza.sh` | Manutenção periódica | ✅ |

### 9.2 — Regras para execução de scripts por agentes

- **Nunca execute scripts com `sudo`** a menos que explicitamente documentado no README do script.
- **Sempre verifique o ambiente** (`dev | staging | prod`) antes de executar scripts destrutivos.
- **Scripts de CI** (`ci/`) nunca devem ser executados localmente em produção.
- **Use `utils/comum.sh`** como biblioteca base — ele provê logging padronizado e tratamento de erros.

---

## 10. Skills Modulares

Localização: `.opencode/skills/`

Skills são módulos reutilizáveis que encapsulam expertise específica. Cada skill segue a estrutura:

```
skills/
└── <nome-da-skill>/
    ├── SKILL.md          # Frontmatter + descrição + instruções + few-shot examples
    ├── templates/        # Modelos de código/arquivos (opcional)
    ├── exemplos/         # Casos reais antes/depois (opcional)
    ├── scripts/          # Scripts auxiliares (opcional)
    └── recursos/         # Recursos complementares
```

### Como usar uma skill

1. Leia `SKILL.md` da skill correspondente **antes** de executar a tarefa.
2. Siga o frontmatter (configurações) e os exemplos few-shot.
3. Use os templates em `templates/` como ponto de partida, nunca como código final.

### Como criar uma nova skill

Consulte `.opencode/skills/README.md` para o guia completo. Toda nova skill deve:
- Ter frontmatter válido (nome, versão, autor, data, descrição)
- Incluir pelo menos 2 exemplos few-shot em `SKILL.md`
- Ser registrada em `.opencode/tools/registry/registro-ferramenta.json`

---

## 11. Ferramentas e MCP

Localização: `.opencode/tools/`

### 11.1 — Registro central de ferramentas

Toda ferramenta, plugin, API externa ou protocolo MCP DEVE estar registrado em:
- `.opencode/tools/registry/registro-ferramenta.json` (machine-readable)
- `.opencode/tools/registry/registro-ferramenta.yaml` (human-readable)

### 11.2 — Categorias de ferramentas

| Categoria | Localização | Exemplos |
|-----------|-------------|---------|
| APIs externas | `.opencode/tools/apis/` | Stripe, SendGrid, Auth0 |
| Plugins de IDE/CI | `.opencode/tools/plugins/` | ESLint, Prettier, Husky |
| Language Servers | `.opencode/tools/lsp/` | TypeScript LS, Python LS |
| MCP (Model Context Protocol) | `.opencode/tools/mcp/` | Chamadas a ferramentas externas |
| Observabilidade | `.opencode/tools/monitoring/` | Sentry, Datadog |

### 11.3 — MCP (Model Context Protocol)

O MCP é o protocolo padrão para agentes chamarem ferramentas externas. Configurações em `.opencode/tools/mcp/`.

**Regras de uso:**
- Todo endpoint MCP deve estar documentado antes de ser chamado por um agente.
- Chamadas MCP que alteram estado externo (escrita, deploy, envio de e-mail) requerem confirmação explícita do orquestrador.
- Erros de MCP devem ser logados com o payload completo da request falha.

### 11.4 — Monitoramento

| Ferramenta | Config | Propósito |
|-----------|--------|-----------|
| Sentry | `.opencode/tools/monitoring/sentry.md` | Captura de erros em runtime |
| Datadog | `.opencode/tools/monitoring/datadog.md` | APM + logs centralizados |

---

## 12. Workflows e Comandos Rápidos

Localização: `.opencode/workflows/`

Comandos rápidos para tarefas comuns. Cada comando é um arquivo Markdown com instruções precisas para o agente executor.

| Comando | Arquivo | O que faz |
|---------|---------|-----------|
| `/brainstorm` | `workflows/brainstorm` | Explora opções e alternativas antes da implementação |
| `/criar` | `workflows/criar` | Cria nova aplicação ou módulo a partir do zero |
| `/depurar` | `workflows/depurar` | Depuração sistemática com o `DEPURAÇÃO_SUBAGENTE` |
| `/implantação` | `workflows/implantação` | Dispara o `IMPLANTACAO_AGENTE` completo |
| `/melhorar` | `workflows/melhorar` | Refatora e melhora código existente |
| `/orquestração` | `workflows/orquestração` | Identifica e aciona o melhor agente/subagente para a requisição |
| `/plano` | `workflows/plano` | Cria detalhamento de tarefas (task breakdown) |
| `/pre-visualizar` | `workflows/pre-visualizar` | Inicia ambiente local para preview de alterações |
| `/status` | `workflows/status` | Checa status atual do projeto (cobertura, health, backlog) |
| `/teste` | `workflows/teste` | Aciona `TESTE_AGENTE` para gerar e rodar testes |

### Como usar um comando

```
/depurar src/backend/auth.ts — erro de autenticação com JWT expirado
```

O agente irá:
1. Ler `workflows/depurar`
2. Invocar o orquestrador de fase correto (neste caso, `DESENVOLVIMENTO_AGENTE`)
3. Delegar para `DEPURAÇÃO_SUBAGENTE` com contexto do arquivo
4. Retornar diagnóstico e correção proposta

---

## 13. Documentação e Entregáveis

### 13.1 — Entregáveis para o cliente (`docs/cliente/`)

| Documento | Responsável por gerar | Fase |
|-----------|-----------------------|------|
| `proposta-comercial-tecnica.md` | `GERACAO_PROPOSTAS_SUBAGENTE` | Concepção |
| `contrato-prestacao-servico.md` | `FORMALIZACAO_CONTRATUAL_SUBAGENTE` | Concepção |
| `documento-de-requisitos-produto-PRD.md` | `PRODUCT_MANAGER_SUBAGENTE` | Planejamento |
| `backlog-produto-moscow.md` | `PRODUCT_OWNER_SUBAGENTE` | Planejamento |
| `arquitetura-alto-nivel.md` | `ARQUITETURA_SUBAGENTE` | Planejamento |
| `wireframes-prototipos/` | `ESPECIALISTA_FRONTEND_SUBAGENTE` | Desenvolvimento |
| `manual-usuario-inicial.md` | `DOCUMENTACAO_CODIGO_SUBAGENTE` | Desenvolvimento |
| `relatorio-testes.md` | `TESTE_AGENTE` | Teste |
| `sla-acordo-nivel-servico.md` | `OPERACOES_E_MONITORAMENTO_AGENTE` | Operações |
| `release-notes-v<X.Y.Z>.md` | `IMPLANTACAO_AGENTE` | Deploy |
| `guia-inicio-rapido.md` | `DOCUMENTACAO_CODIGO_SUBAGENTE` | Deploy |
| `matriz-rastreabilidade-fase.md` | Orquestrador da fase | Todas |

### 13.2 — Artefatos internos (`docs/interno/`)

Estes arquivos são RAG-ready — formatados para serem consumidos por agentes.

| Documento | Formato | Mantido por |
|-----------|---------|-------------|
| `den-briefing-detalhado.md` | Markdown | Concepção |
| `dr-estruturado.json` | JSON | Planejamento |
| `backlog-moscow-estruturado.yaml` | YAML | Planejamento |
| `matriz-rastreabilidade.md` | Markdown tabular | Todos (evolutivo) |
| `cronograma-total.md` | Markdown | Planejamento |
| `cobertura-codigo-historico.json` | JSON | QA (por build) |
| `casos-teste-estruturados.yaml` | YAML | QA |
| `checklist-liberacao.md` | Markdown | Deploy |
| `plano-rollback.md` | Markdown | Deploy |
| `logs-implantacao-resumo.md` | Markdown | Deploy |
| `baselines-monitoramento.json` | JSON | Operações |
| `playbooks-incidentes.md` | Markdown | Operações |
| `padroes-codificacao-interno.md` | Markdown | Desenvolvimento |

### 13.3 — Documentação de código (`docs/documentação-do-código/`)

Gerada e mantida pelo `DOCUMENTACAO_CODIGO_SUBAGENTE`. Deve incluir:
- JSDoc/TSDoc para todas as funções públicas
- README por módulo em `src/`
- Diagrama de dependências atualizado em `diagramas-arquitetura.md`

---

## 14. Padrões de Código e Qualidade

### 14.1 — Regras universais de código

Todos os agentes geradores de código DEVEM:

1. **Ler** `.opencode/canonical/padroes-codigo.md` antes de gerar qualquer código.
2. **Seguir** `.opencode/canonical/convenções-nomenclatura.md` rigorosamente.
3. **Validar** via lint antes de finalizar (`scripts/dev/correção-lint.sh`).
4. **Documentar** toda função pública com JSDoc/TSDoc/Docstring.
5. **Escrever testes** ou atualizar testes existentes para código novo.

### 14.2 — Thresholds mínimos de qualidade

Definidos em `.opencode/canonical/baselines-seguranca-desempenho.md`. Valores de referência:

| Métrica | Mínimo aceitável |
|---------|-----------------|
| Cobertura de testes (unit) | 80% |
| Cobertura de testes (integration) | 60% |
| Latência P95 de API | < 300ms |
| Uptime SLA | 99.5% |
| Score de segurança SAST | Sem vulnerabilidades Critical/High |

### 14.3 — Estrutura de código por camada

```
src/
├── frontend/          # React/Next.js/Vue — UI, componentes, páginas
├── backend/           # Node/Python/Go — controllers, services, repositories
├── database/          # Schemas, migrations (Prisma/Liquibase/Flyway), seeds
├── api/               # OpenAPI specs, contratos, middlewares
├── shared/            # Tipos, utils, domain models compartilhados
└── tests/             # unit/, integration/, e2e/, performance/
```

Nenhum agente deve criar arquivos fora desta estrutura sem aprovação do `ARQUITETURA_SUBAGENTE`.

### 14.4 — Assets

```
assets/
├── imagens/
├── icones/
├── texto/
├── videos/
├── referencias/
└── wireframes/
```

Assets de produto devem ser referenciados em `docs/cliente/wireframes-prototipos/` mas armazenados fisicamente em `assets/`.

---

## 15. Segurança e Compliance

### 15.1 — Regras absolutas (sem exceções)

- **NUNCA** commitar arquivos `.env`, secrets, tokens, chaves privadas ou senhas.
- **NUNCA** logar dados de usuário final (PII) em texto claro.
- **NUNCA** expor endpoints sem autenticação em staging ou produção.
- **SEMPRE** usar HTTPS/TLS em todas as comunicações externas.
- **SEMPRE** sanitizar inputs em endpoints públicos.

### 15.2 — Revisão de segurança por fase

| Fase | Revisão obrigatória |
|------|---------------------|
| Planejamento | `ARQUITETURA_SUBAGENTE` revisa threat model |
| Desenvolvimento | `AUDITOR_DE_SEGURANÇA_SUBAGENTE` faz SAST em PRs |
| Teste | `TESTADOR_DE_PENETRACAO_SUBAGENTE` executa pentest |
| Deploy | `HEALTH_CHECK_VALIDATION_SUBAGENTE` valida configurações |
| Operações | `RESPOSTA_INCIDENTES_SUBAGENTE` monitora alertas de segurança |

### 15.3 — Limites legais e de escopo

Consulte `.opencode/contracts/limites-legais-e-de-escopo.md` antes de:
- Implementar qualquer feature não listada no backlog aprovado
- Integrar APIs de terceiros não mencionadas em `contracts/contratos-de-api.yaml`
- Coletar ou processar dados de usuários

---

## 16. Regras de Git e Versionamento

### 16.1 — Branches

Seguir convenção definida em `.opencode/canonical/convenções-nomenclatura.md`:

```
main              — produção (protegida, merge apenas via PR aprovado)
develop           — integração contínua
feature/<slug>    — novas funcionalidades
fix/<slug>        — correções de bug
hotfix/<slug>     — correções urgentes em produção
release/<versão>  — preparação de release
chore/<slug>      — manutenção (deps, config, scripts)
```

### 16.2 — Commits

Formato: **Conventional Commits** (obrigatório, validado pelo hook `instalar-hooks.sh`)

```
<type>(<scope>): <descrição curta em português>

[corpo opcional — o quê e por quê, não o como]

[rodapé: BREAKING CHANGE, closes #issue]
```

Tipos válidos: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

### 16.3 — Pull Requests

Use o template em `.opencode/canonical/templates.md` (seção PR Template).

Todo PR deve:
- [ ] Ter título em Conventional Commits
- [ ] Descrever mudanças e motivação
- [ ] Ter pelo menos 1 reviewer humano
- [ ] Passar em todos os checks de CI
- [ ] Ter cobertura de testes acima do mínimo
- [ ] Não ter conflitos com `develop`

### 16.4 — .gitignore obrigatório

O `.gitignore` na raiz DEVE incluir:

```
# Logs agentic (gerados dinamicamente)
.opencode/logs/atual/
.opencode/logs/diario/

# Memória volátil
.opencode/memory/short-term/

# Ambiente
*.env
*.env.local
*.env.*.local
.env.*

# Dependências
node_modules/
__pycache__/
*.pyc
.venv/

# Build
dist/
build/
.next/
out/

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

## 17. Onboarding de Novo Agente

Se você é um **novo agente** iniciando neste projeto pela primeira vez, execute esta sequência obrigatória:

### Passo 1 — Leitura de contexto (SEMPRE, toda sessão)
```
1. Leia este arquivo: AGENTS.md
2. Leia: .opencode/canonical/visao-objetivos-restricoes.md
3. Leia: .opencode/canonical/glosario.md
4. Leia: .opencode/memory/short-term/resumo-contexto-ativo.md (se existir)
5. Leia: .opencode/memory/long-term/conhecimento-projeto/fatos-projeto.md
```

### Passo 2 — Identificação de fase e papel
```
6. Identifique em qual fase você está operando
7. Leia o arquivo do seu orquestrador de fase em .opencode/agents/
8. Se você é um subagente, identifique quem é seu orquestrador pai
```

### Passo 3 — Leitura de padrões relevantes
```
9. Leia .opencode/canonical/padroes-codigo.md (se vai gerar código)
10. Leia .opencode/canonical/convenções-nomenclatura.md
11. Leia .opencode/contracts/ relevantes para sua tarefa
```

### Passo 4 — Verificação de estado
```
12. Verifique o log mais recente em .opencode/logs/atual/
13. Verifique docs/interno/checklist-liberacao.md (se próximo de deploy)
14. Execute /status para checar saúde geral do projeto (se orquestrador)
```

### Passo 5 — Execução com rastreabilidade
```
15. Execute sua tarefa seguindo este AGENTS.md
16. Logue cada ação relevante em .opencode/logs/atual/sessao-<timestamp>.jsonl
17. Atualize artefatos de memória ao finalizar
```

---

## Referências Rápidas

| Preciso... | Consulte |
|------------|---------|
| Entender termos do projeto | `.opencode/canonical/glosario.md` |
| Saber padrões de código | `.opencode/canonical/padroes-codigo.md` |
| Verificar contratos de API | `.opencode/contracts/contratos-de-api.yaml` |
| Ver diagramas de arquitetura | `.opencode/canonical/diagramas-arquitetura.md` |
| Encontrar templates | `.opencode/canonical/templates.md` |
| Ver exemplos few-shot | `.opencode/canonical/exemplos-fewshot.md` |
| Checar SLAs | `.opencode/contracts/SLAs-e-nao-funcionais.md` |
| Executar deploy | `.opencode/agents/IMPLANTACAO_AGENTE.md` |
| Responder a incidente | `docs/interno/playbooks-incidentes.md` |
| Resetar banco local | `.opencode/scripts/dev/resetar-prisma.sh` |
| Validar schemas | `.opencode/scripts/agentic/validar-contracts.sh` |
| Registrar nova tool | `.opencode/tools/registry/registro-ferramenta.json` |
| Criar nova skill | `.opencode/skills/README.md` |

---

> **Versão:** 1.0.0
> **Mantido por:** Orquestrador do Projeto + Equipe de Engenharia
> **Atualizar quando:** Novo agente adicionado, nova fase criada, mudança de stack, mudança de contrato.
> **Próxima revisão:** A cada release major ou mudança de arquitetura.
