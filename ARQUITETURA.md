# Guia Completo da Arquitetura de Pastas  
**Template Universal para Desenvolvimento Inteligente com IA**  
**Design Em Rotina** – Sistema DevOps + Engenharia de Contexto (2026)

**Autor:** Eng. Senior [Seu Nome] – Desenvolvedor, Arquiteto e Analista Sênior de Software  
**Versão:** 1.0 (baseada nos 5 documentos anexados: Guia de Entregáveis DevOps, Guia Mestre de Engenharia de Contexto, Agentes e Subagentes, Guia de Conceitos e Guia para Sistema Inteligente)  
**Data:** 26 de fevereiro de 2026  
**Compatibilidade:** OpenCode, Cursor, VS Code + Claude Code, Windsurf, Trae, Antigravity, Aider e qualquer IDE/agentic AI que suporte `.opencode/`, `.agent/` e regras .mdc

---

## Objetivo do Template

Este template cria uma **arquitetura de pastas universal** que transforma qualquer projeto em um **sistema de desenvolvimento inteligente** alinhado 100 % aos seus guias internos.  

- **Separação rigorosa** entre código da aplicação (`src/`) e contexto de IA (`.opencode/`)  
- **RAG-ready** por padrão (todos os arquivos internos são vetores de contexto)  
- **Zero poluição de token** nos prompts dos agentes  
- **Git-friendly** e versionável  
- **Pré-preenchido** com regras, skills, workflows e agentes extraídos diretamente dos documentos anexados  

---

## Estrutura Completa de Pastas e Comentários Breves

```bash
meu-projeto-devops-ia/                                     # Raiz do repositório Git (fonte única de verdade)
.opencode/
	├──	agents/
		├── CONCEPCAO_AGENTE.md                        # Orquestrador principal dessa fase (Agente de Concepção)
		├── QUALIFICACAO_LEADS_SUBAGENTE.md            # Subagente de Qualificação de Leads
		├── ANALISE_NECESSIDADES_SUBAGENTE.md          # Subagente de Análise de Necessidades
		├── GERACAO_PROPOSTAS_SUBAGENTE.md             # Subagente de Geração de Propostas
		├── FORMALIZACAO_CONTRATUAL_SUBAGENTE.md       # Subagente de Formalização Contratual
		├── PLANEJAMENTO_AGENTE.md                     # Orquestrador principal dessa fase (Agente de Planejamento)
		├── ARQUITETURA_SUBAGENTE.md                   # Subagente de Arquitetura
		├── ESTIMATIVA_CRONOGRAMA_SUBAGENTE.md         # Subagente de Estimativa e Cronograma
		├── PRODUCT_MANAGER_SUBAGENTE.md               # Subagente principal de Product Manager para Fase de Planejamento
		├── PRODUCT_OWNER_SUBAGENTE.md                 # Subagente de Product Owner para priorização
		├── PROJECT_PLANNER_STACK_SUBAGENTE.md         # Subagente de Project Plannfer para stack
		├── ESPECIALISTA_EM_SEO_E_GEO.md               # Subagente de SEO e GEO para planejamento do conteúdo de visual para melhor posição em pesquisas
		├── DESENVOLVIMENTO_AGENTE.md                  # Orquestrador principal (Agente de Desenvolvimento)
		├── ESPECIALISTA_FRONTEND_SUBAGENTE.md         # Subagente de Geração de Código (Frontend)
		├── ESPECIALISTA_BACKEND_SUBAGENTE.md          # Subagente de Geração de Código (Backend)
		├── ESPECIALISTA_SHARED_API_SUBAGENTE.md       # Subagente de Geração de Código (Shared/API)
		├── ARQUITETO_BANCO_DE_DADOS_SUBAGENTE.md      # Subagente de Orquestração de Banco de Dados (Database)
		├── DEPURAÇÃO_SUBAGENTE.md                     # Subagente de Debugger para falhas/stack traces	
		├── PERFORMACE_OTIMIZADOR_SUBAGENTE.md         # Subagente de Performance Optimizer para otimização
		├── DOCUMENTACAO_CODIGO_SUBAGENTE.md           # Subagente de Documentação de Código
		├── ARQUEOLOGO_DE_CÓDIGO_SUBAGENTE.md          # Subagente de Code Archaeologist para análise para entender o que fazem, listar padrões de código e sugere atualizações
		├── DESENVOLVEDOR_MOBILE_SUBAGENTE.md          # Subagente de Mobile Developer (condicional para apps mobile)
		├── DESENVOLVEDOR_DE_JOGOS_SUBAGENTE.md        # Subagente de Desenvolvedor de Jogos (condicional para criação de jogos)
		├── TESTE_AGENTE.md                            # Orquestrador principal (Agente de Qualidade / Agente de Teste)
		├── GERACAO_CASOS_TESTE_SUBAGENTE.md           # Subagente de Geração de Casos de Teste
		├── EXECUCAO_TESTES_SUBAGENTE.md               # Subagente de Execução de Testes
		├── ANALISE_FALHAS_DIAGNOSTICO_SUBAGENTE.md    # Subagente de Análise de Falhas e Diagnóstico
		├── TESTES_PERFORMANCE_SEGURANCA_SUBAGENTE.md  # Subagente de Testes de Performance-Segurança
		├── ENGENHARIA_DE_AUTOMACAO_QA_SUBAGENTE.md    # Subagente de Engenheria de Automação QA
		├── TESTADOR_DE_PENETRACAO_SUBAGENTE.md        # Subagente de Penetration Tester para segurança
		├── AUDITOR_DE_SEGURANÇA_SUBAGENTE.md          # Subagente de Security Auditor para revisão estática
		├── IMPLANTACAO_AGENTE.md                      # Orquestrador principal (Agente de Deploy / Implementação)
		├── IAC_PROVISIONING_SUBAGENTE.md			   # Subagente de Atribuir Permissões Baseadas em Funções
        ├── AUTOMACAO_DE_DEPLOY_SUBAGENTE.md           # Subagente de Processo de Software Entre Ambientes Automaticamente
        ├── HEALTH_CHECK_VALIDATION_SUBAGENTE.md       # Subagente de Verificação do Status Operacional dos Serviços e suas Dependências
        ├── ROLLBACK_AND_RECOVERY_SUBAGENTE.md		   # Subagente de Desfeita de Alterações e Recuperação com Reconstrução
		├── OPERACOES_E_MONITORAMENTO_AGENTE.md        # Orquestrador principal (Agente de Operações e Monitoramento)
		├── MONITORAMENTO_INFRA_SUBAGENTE.md           # Subagente de Monitoramento de Infraestrutura
		├── MONITORAMENTO_APLICACAO_SUBAGENTE.md       # Subagente de Monitoramento de Aplicação
		├── DETECCAO_ANOMALIAS_SUBAGENTE.md            # Subagente de Detecção de Anomalias
		├── RESPOSTA_INCIDENTES_SUBAGENTE.md           # Subagente de Resposta a Incidentes
		├── ENGENHEIRO_DEVOPS_SUBAGENTE.md             # Subagente principal de DevOps Engineer para operações
		├── PERFORMACE_OTIMIZADOR_SUBAGENTE.md         # Subagente de Performance Optimizer para análise de gargalos		
	├──	canonical/                                     # Padrões canônicos, templates, guias, conveções, diagramas, etc...
        ├── glosario.md                            	   # Definições oficiais de termos de negócio, acrônimos e jargões do cliente/projeto
        ├── guia-estilo.md                             # Regras de estilo a serem aplicados
        ├── padroes-codigo.md                          # Padrões de codificação globais (frontend + backend + DB + commits)
        ├── convenções-nomenclatura.md                 # Todas as regras de nomenclatura (pastas, arquivos, variáveis, tabelas, branches...)
        ├── templates.md                               # Todos os templates importantes juntos (user-story, api-endpoint, pr-template, release-notes...)
        ├── exemplos-fewshot.md                        # Exemplos canônicos diversos (few-shot planning, code-gen, refactoring, etc.)
        ├── diagramas-arquitetura.md                   # Todos os diagramas de referência em Mermaid/PlantUML (um por seção com título)
        ├── baselines-seguranca-desempenho.md          # Métricas de referência, SLAs típicos, limites de latência, coverage mínima...
        ├── visao-objetivos-restricoes.md              # Objetivos e restrições sobre o projeto, alcaçando o desejado mantendo a consistência 
	├── contracts/
 		├── contratos-de-api.yaml                      # Contrato principal de interfaces (APIs internas + externas)
 		├── contratos-dados.yaml                       # Schemas de dados, payloads, eventos (consistência de domínio)
 		├── SLAs-e-nao-funcionais.md                   # SLAs + requisitos não-funcionais críticos (uptime, latência, segurança resumida)
 		└── limites-legais-e-de-escopo.md              # Limites de escopo + cláusulas legais chave (evita features fora do combinado) 
	└── logs/                                          # Logs de execução dos agentes (sempre gitignored)
        ├── README.md                                  # Explicação do que está aqui + como consultar
        ├── atual/                                     # Logs da sessão / run atual (limpo periodicamente)
            ├── sessao-20260227-1820.jsonl             # Exemplo: log da sessão atual (JSON Lines)
            └── agentes-ativos.json                    # Estado resumido dos agentes em execução
    	├── diario/                                    # Rotação diária (ou semanal/mensal)
    		├── DD-MM-AAAA/
            	├── PLANEJAMENTO_AGENTE.md.log
             	├── DESENVOLVIMENTO_AGENTE.md.log
             	└── errors-20260227.jsonl
    	├── arquivado/                                 # Logs antigos (compactados ou movidos manualmente)
     		└── AAAA-MM/
     		    └── semana-08.tar.gz                   # Exemplo de compactação para economia de espaço
    	    └── sumarios/                              # Resumos gerados por agente de curadoria (opcional)
				└── sumario-semanal-2026-s08.md   		
	└── memory/                                        # Memória de longo e curto prazo dos agentes (RAG + persistência)
		├── README.md                                  # Documentação: como usar, políticas, exemplos de query
		├── short-term/                                # Memória volátil – sessão atual (gitignore!)
			├── sessao-atual.jsonl                     # Histórico da conversa/sessão atual (JSON Lines)
      		├── resumo-contexto-ativo.md               # Resumo compactado gerado pelo agente (para incluir no prompt)
       		└── estado-temporario-agente.json          # Estado transitório (ex: variáveis ativas do agente mestre)
		├── long-term/                                 # Memória persistente – versionável no Git
			├── conhecimento-projeto/                  # Fatos e preferências do projeto atual
				├── fatos-projeto.md                   # Fatos canônicos extraídos (ex: stack escolhida, domain rules)
            	└── preferencias-cliente.md            # Preferências recorrentes do cliente (ex: UI style, tech constraints)
            ├── execuções-historicas/                  # Resumos de execuções passadas (episodic memory)
				├── execução-20260227-uuid123.md       # Resumo de uma run completa (decisões, erros, lições)
				└── resumos-semanais/                  # Agregados semanais/mensais para visão longa
			├── lições-aprendidas/                     # Lições aprendidas e anti-patterns
				├── lições-db.md            	       # Banco de lições (formato tabela ou bullet points)
            	└── padrões-erros.md        	       # Padrões de erro recorrentes + mitigações
			└── linhas-base/                           # Métricas de referência acumuladas
                └── linhas-basee-performace.json       # Evolução de métricas (coverage, latência, etc.)
	└── scripts/                                       # Scripts utilitários e automações executáveis (local + CI)
		├── README.md                                  # Documentação: como rodar, dependências, exemplos
		├── setup/                                     # Scripts de inicialização e ambiente (uma vez só ou on-demand)
			├── iniciar.sh                             # Instala dependências globais, cria .env.example, etc.
			└── instalar-hooks.sh                      # Instala Git hooks (pre-commit, commit-msg)
		├── dev/                                       # Scripts para desenvolvimento diário (dev loop)
			├── start-local.sh                         # Inicia stack local (frontend + backend + db)
			├── correçao-lint.sh                       # Lint + auto-fix (eslint, prettier, stylelint)
			├── teste-watch.sh                         # Testes em watch mode + coverage
			└── resetar-prisma.sh                      # Reseta DB local + seed + migrate (dev only)
    	├──	db/                                        # Scripts relacionados a banco de dados (Prisma ou similar)
			├── migrate.sh                             # Prisma migrate dev + generate
			├── seed.sh          			           # Seed de dados iniciais (idempotente)
		├── agentic/                                   # Scripts que interagem diretamente com agentes IA
			├── cura-de-memoria.sh                     # Compacta e limpa memória (short/long-term)
			├── validar-contracts.sh                   # Valida schemas OpenAPI + JSON Schema
			└── resumo-logs.sh                         # Gera resumo semanal de logs agentic
		├── ci/                                        # Scripts chamados por GitHub Actions (idempotentes, sem side-effects)
    		├── instalar-denp.sh                       # npm ci com cache awareness
    		└── cobertura-relatório.sh                 # Envia cobertura para Codecov/Sonar
		├── utils/                                     # Funções reutilizáveis (sourced por outros scripts)
			└── comum.sh                               # Variáveis, funções de log, error handling
			└── limpeza.sh                             # Limpa caches, node_modules, temp files (manutenção)				
    └── skills/                                  	   # Skills modulares reutilizáveis (padrão Anthropic/Claude + agentic)
		├── README.md                                  # Visão geral, como criar/usar skills, exemplos
		skill-name/
			├── SKILL.md                               # Descrição, frontmatter, instruções, few-shot examples
			├── templates/           			       # Modelos de código/arquivos (opcional)
			├── exemplos/             			       # Casos reais antes/depois (opcional)
			└── scripts/                               # Scripts bash/python auxiliares (opcional)
			└── recursos/                              # Recursos complementares da skill
    └── tools/                              		   # Registro centralizado de todas as ferramentas, APIs, plugins e protocolos
		├── README.md                                  # Visão geral, como registrar nova tool, políticas de uso
		├── registry/                    		       # Catálogo principal (machine-readable)
			├── registro-ferramenta.json               # JSON principal com todas as tools registradas
			└── registro-ferramenta.yaml               # Alternativa YAML (mais legível para humanos)
		├── apis/                                      # Documentação e contratos de APIs externas/internas
		├── plugins/                                   # Plugins para IDEs, editores, CI, etc.
		├── lsp/                                       # Configurações e schemas de Language Servers
		├── mcp/                                       # Model Context Protocol (Chama ferramentas externas)
		└── monitoring/                  		       # Ferramentas de observabilidade
			├── sentry.md                              # Configuração SDK + DSN placeholder
			└── datadog.md                             # Integração APM + logs								
    └── workflows/                                     # Comandos rápidos 
		├── README.md                                  # Visão geral, de cada comando rápidos
		├── /brainstorm                                # Explora opções antes da implementação
		├── /criar                                     # Criar nova aplicação 
		├── /depurar                                   # Depuração Sistemática
		├── /implantação                               # Implanta o projeto
		├── /melhorar							       # Melhora o código existente
		├── /orquestração                              # Coordena melhor agente/subagente para a requisição
		├── /plano                                     # Criar Detalhamento de Tarefas
		├── /pre-visualizar                            # Criar Visualizar alterações localmente
		├── /status                                    # Checka Status Atual do Projeto
		├── /teste                                     # Gera e Roda Testes
├── docs/                                              # Entregáveis DevOps (Guia de Entregáveis por Fase)
    ├── cliente/                                       # Documentos para o cliente (DR, Release Notes, SLA...)
        ├── proposta-comercial-tecnica.md              # Proposta formal (escopo, cronograma, investimento)
        ├── contrato-prestacao-servico.md              # Versão final assinada (ou rascunho para assinatura)	
		├── matriz-rastreabilidade-fase.md             # Matriz de Restreabilidade
		├── documento-de-requisitos-produto-PRD.md     # Documento de Requisitos completo (DR)
		├── backlog-produto-moscow.md                  # Backlog priorizado MoSCoW (versão cliente)
		├── arquitetura-alto-nivel.md                  # Diagramas + descrição de arquitetura de alto nível
		├── wireframes-prototipos/                     # Pasta com imagens ou links para wireframes 
		|── manual-usuario-inicial.md                  # Guia de início rápido (Documentação para o usuário final.)
		├── release-notes-v1.0.0.md                    # Notas de lançamento (funcionalidades, correções)
		├── guia-inicio-rapido.md                      # Quick Start para o usuário final
		├── relatorio-testes.md                        # Sumário dos resultados dos testes (unitários, integração, sistema, aceitação).
		├── sla-acordo-nivel-servico.md                # Acordo de Nível de Serviço formal
	├── interno/                                       # Artefatos internos essenciais de contexto (RAG-ready, rastreabilidade e aprendizado)
		├── den-briefing-detalhado.md     			   # Documento de Entendimento de Necessidades (resumo discovery + personas + jornadas)
		├── dr-estruturado.json            			   # Documento de Requisitos (DR) em formato JSON/YAML → ouro para RAG do Agente de Planejamento
		├── backlog-moscow-estruturado.yaml    		   # Backlog priorizado MoSCoW com estimativas e responsáveis (parseável por IA)
		├── matriz-rastreabilidade.md           	   # Matriz única e evolutiva: requisitos ↔ casos de uso ↔ testes ↔ código (atualizada ao longo do ciclo)
		├── conograma-total.md                         # Tempo total do conograma com sprints, requisitos e tarefas
		├── padroes-codificacao-interno.md    		   # Regras internas complementares ao canonical/ (ex.: padrões específicos do projeto)
		├── cobertura-codigo-historico.json    		   # Evolução da cobertura de testes (por build/release) → usado por Agente de Qualidade
		├── casos-teste-estruturados.yaml      		   # Casos de teste em formato parseável (para geração automática e validação)
		├── checklist-liberacao.md         			   # Checklist de gates de release (usado por Agente de Entrega)
		├── plano-rollback.md               		   # Procedimentos de reversão (crítico para segurança)
		├── logs-implantacao-resumo.md         		   # Resumo cronológico de deploys (sucesso/falha + versão) → para auditoria rápida
		├── baselines-monitoramento.json       		   # Modelos de baseline (latência, erro rate, uptime) → alimenta Detecção de Anomalias
		└── playbooks-incidentes.md            		   # Playbooks resumidos de resposta a incidentes (usado por Agente de Operações)
	├──	documentação-do-código/						   # Documentação de Código
├── src/                                               # Código da aplicação – Clean Architecture / Vertical Slice
    ├── frontend/                                      # React/Next.js/Vue (o que o projeto usar)
    ├── backend/                                       # Node, Python, Go, Java...
	├── database/                                      # Schemas, migrations, seeds (Liquibase, Flyway, Prisma...)	
    ├── api/                                           # OpenAPI/Swagger + contratos
	├── tests/	     								   # Testes automatizados (unit, integration, e2e, performance)											  
    └── shared/                                        # Código compartilhado (utils, types, domain)
├── assets/                                            # Imagens, ícones, textos, vídeos, referencias e wireframes (Assets do Guia de Conceitos)	
	├── imagens/
	├── icones/ 
  	├── texto/ 
	├── vídeos/
	├── referencias/
	├── wireframes/
├── infraestrutura/                                    # IaC (Terraform, Ansible, Docker, Kubernetes manifests)
├── PRDs/											   # Product Requirements Document		
├── ARQUITETURA.md                                     # Este arquivo que você está lendo
├── AGENTS.md                                          # Regras do projeto (para Agentes LLM ler imediatamente)
├── README.md                                          # Visão geral do projeto
├── .gitignore                                         # Ignora logs/, *.env, memory/short-term/, etc.
 		