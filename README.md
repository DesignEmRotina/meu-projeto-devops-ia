# {{NOME_DO_PROJETO}}

**Sistema de Desenvolvimento Inteligente com DevOps + Engenharia de Contexto**  
**Design Em Rotina** – Template Universal 2026

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Version](https://img.shields.io/badge/Version-1.0.0-success)](ARQUITETURA.md)  
[![OpenCode](https://img.shields.io/badge/.opencode-Enabled-8A2BE2)](.opencode/)  
[![DevOps](https://img.shields.io/badge/DevOps-8%20Fases-00BFFF)](docs/cliente/)  

## Visão Geral

**{{NOME_DO_PROJETO}}** é uma solução **full-stack** (ou conforme definido na fase de concepção) construída com o framework **Design Em Rotina** – um sistema proprietário de desenvolvimento inteligente que integra **DevOps completo** (8 fases) e **Engenharia de Contexto** avançada.

O projeto foi gerado e orquestrado por **agentes IA especializados** (Agente de Concepção → Planejamento → Desenvolvimento → Teste → Implementação → Operações), garantindo:
- **Separação rigorosa** entre código da aplicação (`src/`) e contexto de IA (`.opencode/`)
- **RAG-ready** por padrão (todo o conhecimento do projeto é vetorizado e acessível aos agentes)
- **Zero poluição de token** nos prompts
- **Padrões de código, segurança, escalabilidade e performance** aplicados automaticamente
- **Rastreabilidade completa** (matriz de requisitos ↔ código ↔ testes)

**Tipo de projeto:** {{ex.: SaaS, E-commerce, Aplicativo Mobile, API Enterprise, etc.}}  
**Stack principal:** {{ex.: Next.js 15 + TypeScript | Node.js + Prisma | etc.}}  
**Status atual:** {{Em Desenvolvimento | Em Produção | MVP Pronto}}  
**Última release:** {{v1.0.0 – 18/04/2026}}

---

## Objetivos do Projeto

{{Liste aqui os objetivos de negócio de alto nível, extraídos do DR ou DEN. Exemplo:}}
- Automatizar o fluxo de {{processo principal}}
- Entregar experiência de usuário {{qualidade desejada}} com performance < 100ms
- Garantir conformidade com {{LGPD / ISO 27001 / etc.}}
- Alcançar cobertura de testes ≥ 90% e SLA de uptime 99.9%

---

## Arquitetura Inteligente (Design Em Rotina)

Este projeto segue **100%** a arquitetura global definida em:

- **[ARQUITETURA.md](./ARQUITETURA.md)** – Estrutura completa de pastas, regras e contratos
- **[AGENTS.md](./AGENTS.md)** – Orquestração completa de Agentes e Subagentes (Concepção → Planejamento → Desenvolvimento → Teste → Implementação → Operações)
- **[.opencode/](./.opencode/)** – Motor de contexto, memória, skills, workflows e logs dos agentes

**Fases DevOps já executadas pelo sistema de IA:**
| Fase              | Status     | Principais Entregáveis Internos                     |
|-------------------|------------|-----------------------------------------------------|
| 0. Pré-Venda/Concepção    | ✅ Concluída | DEN, Proposta, Contrato                                                          |
| 1. Planejamento           | ✅ Concluída | DR estruturado, Backlog MoSCoW, Arquitetura                                      |
| 2. Desenvolvimento        | {{✅ / 🚧}} | Código-fonte + documentação automática                                            |
| 3. Teste                  | {{✅ / 🚧}} | Casos de teste, cobertura, relatórios                                             |
| 4. Implementação/Deploy   | {{✅ / 🚧}} | Release notes, manifestos IaC, Docker/K8s + pipelines CI/CD                       |
| 6. Operação/Monitoramento | {{✅ / 🚧}} | Monitoramento, playbooks de incidente, Baselines, detecção de anomalias           |
---

## 🛠️ Tecnologias e Ferramentas (Stack Escolhida)

{{Substitua pelo stack real do projeto – exemplo abaixo é genérico e pronto para copiar}}

**Frontend:** Next.js 15 (App Router) + TypeScript + Tailwind CSS v4  
**Backend:** Node.js + NestJS ou Express (conforme contrato)  
**Banco de Dados:** PostgreSQL + Prisma ORM  
**Infra:** Docker + Docker Compose + Terraform (IaC)  
**CI/CD:** GitHub Actions (ou GitLab CI)  
**Observabilidade:** Sentry + Prometheus + Grafana  
**Testes:** Vitest + Playwright + Testing Library  
**Documentação:** OpenAPI 3.1 + Swagger UI  

**Padrões aplicados:** Clean Architecture / Vertical Slice + Domain-Driven Design (DDD) + SOLID + TDD onde aplicável.

---

## Como Executar o Projeto Localmente

### Pré-requisitos ex.:
- Node.js ≥ 20
- Docker + Docker Compose
- {{adicione outros conforme stack}}

### Passo a passo

```bash
# 1. Clone o repositório
git clone {{URL_DO_REPO}} {{NOME_DO_PROJETO}}
cd {{NOME_DO_PROJETO}}

# 2. Instale dependências (script automatizado)
./.opencode/scripts/setup/iniciar.sh

# 3. Configure ambiente
cp .env.example .env
# edite .env com suas credenciais

# 4. Inicie stack local (frontend + backend + banco)
./.opencode/scripts/dev/start-local.sh

# 5. Acesse
Frontend → http://localhost:3000
Backend  → http://localhost:3333
Swagger  → http://localhost:3333/api/docs
```

**Scripts úteis (todos em `.opencode/scripts/`):**
- `dev/correcao-lint.sh` – Lint + auto-fix
- `dev/teste-watch.sh` – Testes em watch mode
- `db/migrate.sh` – Prisma migrate + seed

---

## 📁 Estrutura de Pastas (Resumo)

```bash
.
├── .opencode/          # Motor de IA e Contexto (RAG-ready)
├── src/                # Código da aplicação (Clean Architecture)
├── docs/               # Entregáveis DevOps (cliente + interno)
├── infraestrutura/     # IaC
├── assets/             # Imagens, wireframes, brand
├── PRDs/               # Product Requirements
├── ARQUITETURA.md      # Este documento (arquitetura global)
├── AGENTS.md           # Agentes e Subagentes ativos
└── README.md           # Você está aqui
```

**Detalhes completos:** [ARQUITETURA.md](./ARQUITETURA.md)

---

## Agentes IA Ativos Neste Projeto

- **Agente Mestre:** {{Nome do Agente de Desenvolvimento / Planejamento ativo}}
- **Subagentes em execução:** Frontend, Backend, Database, QA, DevOps, etc.
- **Memory:** Long-term (Git) + Short-term (sessão atual)
- **Logs:** `.opencode/logs/`

Todos os agentes seguem as **Skills** e **Rules** definidas no diretório `.opencode/skills/` e `.opencode/canonical/`.

---

## Como Contribuir

1. Leia as regras em **[.opencode/canonical/padroes-codigo.md](.opencode/canonical/padroes-codigo.md)**
2. Crie uma branch: `feature/nome-da-funcionalidade` ou `hotfix/xxx`
3. Use o workflow `/plano` ou `/brainstorm` dos agentes antes de codificar
4. Rode `verificação-e-validação` após cada mudança
5. Abra PR – será revisado automaticamente pelo **Agente de Qualidade**

---

## Licença

Este projeto está licenciado sob a **{{MIT / Proprietária / etc.}}**.  
Veja o arquivo [LICENSE](./LICENSE) para detalhes.

---

## Suporte e Contato

**Design Em Rotina** – Desenvolvimento Inteligente com IA  
**Eng. Senior {{Seu Nome}}** – Arquiteto e Analista Sênior de Software  
Email: {{seu.email@designemrotina.com}}  
Documentação completa: [docs/cliente/guia-inicio-rapido.md](docs/cliente/guia-inicio-rapido.md)

---

**Última atualização:** {{18 de abril de 2026}}  
**Gerado automaticamente pelo Agente de Documentação + Engenharia de Contexto**
```

---