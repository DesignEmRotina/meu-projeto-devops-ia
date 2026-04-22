# Coordenação de Agentes

> Como o **App Builder** orquestra os agentes especialistas.

## Pipeline de Agentes

```
┌─────────────────────────────────────────────────────────────┐
│                 APP BUILDER (Orquestrador)                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    PROJECT PLANNER                          │
│  • Decomposição de tarefas                                  │
│  • Grafo de dependências                                    │
│  • Planejamento da estrutura de arquivos                    │
│  • Criar {task-slug}.md na raiz do projeto (OBRIGATÓRIO)    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│            CHECKPOINT: VERIFICAÇÃO DO PLANO                 │
│  🔴 VERIFICAR: {task-slug}.md existe na raiz do projeto?    │
│  🔴 Se NÃO → PARAR → Criar o arquivo de plano primeiro     │
│  🔴 Se SIM → Prosseguir para os agentes especialistas       │
└─────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ ARQUITETO DE    │ │ ESPECIALISTA    │ │ ESPECIALISTA    │
│ BANCO DE DADOS  │ │ BACKEND         │ │ FRONTEND        │
│                 │ │                 │ │                 │
│ • Design do     │ │ • Rotas de API  │ │ • Componentes   │
│   esquema       │ │ • Controllers  │ │ • Páginas       │
│ • Migrations    │ │ • Middleware   │ │ • Estilização   │
│ • Seed data     │ │                 │ │                 │
└─────────────────┘ └─────────────────┘ └─────────────────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│               FASE PARALELA (Opcional)                      │
│  • Security Auditor → Verificação de vulnerabilidades       │
│  • Test Engineer → Testes unitários                          │
│  • Performance Optimizer → Análise de bundle                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   DEVOPS ENGINEER                           │
│  • Configuração de ambiente                                 │
│  • Deploy de preview                                        │
│  • Health check                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Ordem de Execução

| Fase | Agente(s)                       | Paralelo? | Pré-requisito         | CHECKPOINT                   |
| ---- | ------------------------------- | --------- | --------------------- | ---------------------------- |
| 0    | Socratic Gate                   | ❌         | –                     | ✅ Fazer 3 perguntas          |
| 1    | Project Planner                 | ❌         | Perguntas respondidas | ✅ **PLAN.md criado**         |
| 1.5  | **VERIFICAÇÃO DO PLANO**        | ❌         | PLAN.md existe        | ✅ **Arquivo existe na raiz** |
| 2    | Arquiteto de Banco de Dados     | ❌         | Plano pronto          | Esquema definido             |
| 3    | Especialista Backend            | ❌         | Esquema pronto        | Rotas de API criadas         |
| 4    | Especialista Frontend           | ✅         | API pronta (parcial)  | Componentes de UI prontos    |
| 5    | Security Auditor, Test Engineer | ✅         | Código pronto         | Testes e auditoria aprovados |
| 6    | DevOps Engineer                 | ❌         | Todo o código pronto  | Deploy pronto                |

> 🔴 **CRÍTICO:** A fase **1.5** é **OBRIGATÓRIA**. Nenhum agente especialista pode prosseguir sem a verificação do **PLAN.md**.
