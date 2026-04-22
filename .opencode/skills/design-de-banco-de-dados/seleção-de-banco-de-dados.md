# Seleção de Banco de Dados (2026)

> Escolha o banco de dados com base no contexto, não por padrão.

## Árvore de Decisão

```

Quais são seus requisitos?
│
├── Recursos relacionais completos necessários
│   ├── Auto-hospedado → PostgreSQL
│   └── Serverless → Neon, Supabase
│
├── Deploy em edge / Latência ultra-baixa
│   └── Turso (SQLite em edge)
│
├── IA / Busca vetorial
│   └── PostgreSQL + pgvector
│
├── Simples / Embarcado / Local
│   └── SQLite
│
└── Distribuição global
└── PlanetScale, CockroachDB, Turso

```

## Comparação

| Banco de Dados | Melhor Para | Trade-offs |
|---------------|------------|------------|
| **PostgreSQL** | Recursos completos, queries complexas | Requer infraestrutura |
| **Neon** | PostgreSQL serverless, branching | Complexidade do PG |
| **Turso** | Edge, baixa latência | Limitações do SQLite |
| **SQLite** | Simples, embarcado, local | Escrita por um único processo |
| **PlanetScale** | MySQL, escala global | Não suporta foreign keys |

## Perguntas a Fazer

1. Qual é o ambiente de deploy?
2. Quão complexas são as queries?
3. Edge ou serverless é importante?
4. É necessário busca vetorial?
5. Precisa de distribuição global?
```

