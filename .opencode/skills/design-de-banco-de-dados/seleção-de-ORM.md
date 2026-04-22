# Seleção de ORM (2026)

> Escolha o ORM com base no ambiente de deploy e nas necessidades de DX (Developer Experience).

## Árvore de Decisão

```

Qual é o contexto?
│
├── Deploy em edge / Tamanho do bundle importa
│   └── Drizzle (mais leve, estilo SQL)
│
├── Melhor DX / Abordagem schema-first
│   └── Prisma (migrations, studio)
│
├── Máximo controle
│   └── SQL puro com query builder
│
└── Ecossistema Python
└── SQLAlchemy 2.0 (suporte a async)

```

## Comparação

| ORM | Melhor Para | Trade-offs |
|-----|-------------|------------|
| **Drizzle** | Edge, TypeScript | Mais novo, menos exemplos |
| **Prisma** | DX, gerenciamento de schema | Mais pesado, não ideal para edge |
| **Kysely** | Query builder SQL com type safety | Migrations manuais |
| **SQL puro** | Queries complexas, controle total | Type safety manual |


