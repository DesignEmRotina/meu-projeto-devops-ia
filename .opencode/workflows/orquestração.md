# Workflow de Orquestração  
**Coordenação Inteligente de Agentes e Subagentes**  
**Design Em Rotina** – Sistema DevOps + Engenharia de Contexto (2026)
**Nome do Workflow:** `/orquestração`  
**Objetivo:** Analisar qualquer requisição do usuário em linguagem natural e rotear de forma automática e determinística para o **melhor Agente Orquestrador** (principal) ou **Subagente especialista**, garantindo alinhamento com a fase do ciclo DevOps, o contexto do projeto e os princípios de Engenharia de Contexto definidos nos guias mestres.  
**Versão:** 1.0 (baseada nos documentos: Arquitetura de Pastas Global, Guia de Entregáveis DevOps, Guia Mestre de Engenharia de Contexto, Agentes e Subagentes Essenciais e Guia de Conceitos)  
**Autor:** Eng. Senior – Desenvolvedor, Arquiteto e Analista Sênior de Software  
**Data:** 17 de abril de 2026  
**Localização:** `.opencode/workflows/orquestração.md`  
**Compatibilidade:** OpenCode, Cursor, VS Code + Claude Code, Windsurf, Trae, Aider e qualquer ambiente agentic que suporte MCP (Model Context Protocol) e roteamento via skills.



## 1. Objetivo e Princípios de Design

Este workflow é o **cérebro de roteamento** do ecossistema de agentes da Design Em Rotina. Ele implementa o padrão de Roteamento Inteligente combinado com **Engenharia de Contexto** para:

- Evitar ambiguidade e latência desnecessária de token;
- Garantir que cada requisição seja entregue ao agente/subagente com maior expertise para a fase atual do ciclo DevOps;
- Manter consistência com as regras canônicas (`canonical/`), contratos (`contracts/`) e memória (`memory/`);
- Suportar delegação hierárquica (Agente Orquestrador → Subagente) ou direta (quando a requisição é granular);
- Ser **idempotente**, **auditável** e **RAG-ready** (todos os artefatos gerados são indexados automaticamente).

**Fontes de referência utilizadas na concepção (conforme seu perfil de Engenheiro Sênior):**
- Livro *Designing Agentic Systems* (Harrison Chase, 2025) – padrões de orchestration e routing;
- Artigo “Context Engineering for Production Agents” (arXiv:2507.13334);
- Documentação oficial Anthropic – Tool Use & Multi-Agent Orchestration Patterns;
- Guia Interno da Design Em Rotina (os 5 documentos anexados).

---

## 2. Fluxo de Execução (Mermaid)

```mermaid
flowchart TD
    A[Requisição do Usuário\nlinguagem natural] --> B[Passo 1: Análise Contextual\n+ RAG sobre memory/long-term + canonical/]
    B --> C{Classificar Fase DevOps?}
    C -->|Concepção/Pré-venda| D[CONCEPCAO_AGENTE.md\n→ Subagentes específicos]
    C -->|Planejamento| E[PLANEJAMENTO_AGENTE.md\n→ Subagentes de PM/PO/Arquitetura]
    C -->|Desenvolvimento| F[DESENVOLVIMENTO_AGENTE.md\n→ Especialistas Frontend/Backend/DB]
    C -->|Teste/Qualidade| G[TESTE_AGENTE.md\n→ Subagentes de Testes/Segurança]
    C -->|Implantação/Deploy| H[IMPLANTACAO_AGENTE.md\n→ Subagentes IaC/Automação/Rollback]
    C -->|Operações/Monitoramento| I[OPERACOES_E_MONITORAMENTO_AGENTE.md\n→ Subagentes de Observabilidade]
    C -->|Requisição Transversal\n(performance, segurança, documentação)| J[Agente Orquestrador da fase atual\n+ Subagente especializado]
    D --> K[Preparar Contexto\n(memory + contracts + docs)]
    E --> K
    F --> K
    G --> K
    H --> K
    I --> K
    J --> K
    K --> L[Delegar via MCP\n+ Injetar prompt com contexto curado]
    L --> M[Registrar log em .opencode/logs/atual/]
    M --> N[Retornar ID da sessão para rastreabilidade]
```

---

## 3. Lógica de Decisão (Tabela de Roteamento Determinística)

O workflow **sempre** executa as seguintes verificações na ordem abaixo (prioridade decrescente):

| Prioridade | Critério de Detecção (palavras-chave / intenção) | Fase | Agente Orquestrador Principal | Subagente(s) Recomendado(s) | Observação |
|------------|--------------------------------------------------|------|-------------------------------|-----------------------------|----------|
| 1          | "qualificar lead", "proposta", "contrato", "discovery", "briefing", "pré-venda" | Concepção | `CONCEPCAO_AGENTE.md` | QUALIFICACAO_LEADS / ANALISE_NECESSIDADES / GERACAO_PROPOSTAS / FORMALIZACAO_CONTRATUAL | Usa `memory/short-term` + DEN |
| 2          | "planejar", "backlog", "requisitos", "arquitetura", "cronograma", "estimativa", "MoSCoW", "product owner", "stack" | Planejamento | `PLANEJAMENTO_AGENTE.md` | ARQUITETURA_SUBAGENTE / ESTIMATIVA_CRONOGRAMA / PRODUCT_MANAGER / PRODUCT_OWNER / PROJECT_PLANNER_STACK / ESPECIALISTA_EM_SEO_E_GEO | Prioriza `canonical/visao-objetivos-restricoes.md` |
| 3          | "desenvolver", "criar código", "frontend", "backend", "API", "componente", "mobile", "jogo", "refatorar", "documentar" | Desenvolvimento | `DESENVOLVIMENTO_AGENTE.md` | ESPECIALISTA_FRONTEND / ESPECIALISTA_BACKEND / ESPECIALISTA_SHARED_API / ARQUITETO_BANCO_DE_DADOS / DOCUMENTACAO_CODIGO / ARQUEOLOGO_DE_CÓDIGO / DESENVOLVEDOR_MOBILE / DESENVOLVEDOR_DE_JOGOS | Verifica `src/` existente |
| 4          | "testar", "caso de teste", "executar testes", "bug", "debug", "performance", "segurança", "penetração", "QA" | Teste | `TESTE_AGENTE.md` | GERACAO_CASOS_TESTE / EXECUCAO_TESTES / ANALISE_FALHAS_DIAGNOSTICO / TESTES_PERFORMANCE_SEGURANCA / ENGENHARIA_DE_AUTOMACAO_QA / TESTADOR_DE_PENETRACAO / AUDITOR_DE_SEGURANÇA | Usa `tests/` e `baselines-seguranca-desempenho.md` |
| 5          | "deploy", "implantar", "produção", "IaC", "rollback", "health check" | Implantação | `IMPLANTACAO_AGENTE.md` | IAC_PROVISIONING / AUTOMACAO_DE_DEPLOY / HEALTH_CHECK_VALIDATION / ROLLBACK_AND_RECOVERY | Verifica `infraestrutura/` |
| 6          | "monitorar", "anomalia", "incidente", "observabilidade", "DevOps", "gargalo" | Operações | `OPERACOES_E_MONITORAMENTO_AGENTE.md` | MONITORAMENTO_INFRA / MONITORAMENTO_APLICACAO / DETECCAO_ANOMALIAS / RESPOSTA_INCIDENTES / ENGENHEIRO_DEVOPS / PERFORMACE_OTIMIZADOR | Usa `logs/` + `memory/long-term` |
| 7 (transversal) | "otimizar performance", "segurança", "documentação", "refatorar", "depurar" | Qualquer fase | Agente da fase atual | PERFORMACE_OTIMIZADOR / DEPURAÇÃO / ARQUEOLOGO_DE_CÓDIGO / AUDITOR_DE_SEGURANÇA | Subagente pode ser chamado diretamente |

**Regra de desempate:**  
Se a requisição tocar mais de uma fase → delegar ao **Agente Orquestrador da fase mais avançada** no ciclo DevOps e notificar o usuário.

---

## 4. Passos Detalhados de Execução (para Agentes)

1. **Análise Contextual** (obrigatório)  
   - Consultar `memory/short-term/sessao-atual.jsonl` + `memory/long-term/conhecimento-projeto/`  
   - Ler `canonical/` (glossário, padrões, visao-objetivos-restricoes)  
   - Verificar `contracts/` e `docs/interno/`

2. **Classificação** (usar LLM com few-shot do próprio workflow)

3. **Preparação do Prompt de Delegação** (template interno)  
   ```markdown
   Você é o [NOME_DO_AGENTE_SUBAGENTE].  
   Requisição do usuário: "{user_request}"
   Contexto injetado: [resumo curado de 200-400 tokens]
   Regras canônicas: [referências específicas]
   Execute sua skill e retorne resultado estruturado (JSON + explicação).
   ```

4. **Invocação via MCP** (ou comando nativo da IDE)

5. **Log e Feedback**  
   - Gravar em `.opencode/logs/atual/sessao-YYYYMMDD-HHMM.jsonl`  
   - Atualizar `memory/long-term/execuções-historicas/`

---

## 5. Exemplos Few-Shot (para treinamento do roteador)

**Exemplo 1:**  
Requisição: “Quero criar o componente de login com Next.js + Tailwind”  
→ Roteamento: `DESENVOLVIMENTO_AGENTE.md` → `ESPECIALISTA_FRONTEND_SUBAGENTE.md`

**Exemplo 2:**  
Requisição: “Preciso de um plano de testes de performance e segurança antes do deploy”  
→ Roteamento: `TESTE_AGENTE.md` → `TESTES_PERFORMANCE_SEGURANCA_SUBAGENTE.md`

**Exemplo 3:**  
Requisição: “Analise o backlog e defina a stack técnica”  
→ Roteamento: `PLANEJAMENTO_AGENTE.md` → `PROJECT_PLANNER_STACK_SUBAGENTE.md`

---

## 6. Integração com o Ecossistema

- **Skills:** Usa `brainstorm/`, `escrita-de-planos/`, `verificação-e-validação/`
- **Memory:** Sempre injeta resumo de `resumo-contexto-ativo.md`
- **Logs:** Todo roteamento é auditado
- **Workflows relacionados:** `/brainstorm`, `/plano`, `/teste`, `/implantação`
- **Scripts:** Pode chamar `.opencode/scripts/agentic/resumo-logs.sh` após execução

---

## 7. Como Usar este Workflow

No terminal da IDE ou prompt do agente mestre:
```
/orquestração
[descreva sua requisição aqui]
```

Ou simplesmente mencione o workflow em qualquer conversa – o agente de orquestração (ou o roteador global) o invocará automaticamente.

**Este arquivo é a fonte única de verdade para o roteamento.**  
Qualquer alteração deve ser versionada via Git e refletida nos agentes principais.

**Pronto para produção.**  
Mantenha a consistência, escalabilidade e performance como sempre priorizamos na Design Em Rotina.
```