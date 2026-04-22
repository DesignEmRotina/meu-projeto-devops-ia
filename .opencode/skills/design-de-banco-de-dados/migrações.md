# Princípios de Migrations

> Estratégia segura de migração para mudanças sem downtime.

## Estratégia de Migração Segura

```

Para mudanças sem downtime:
│
├── Adicionar coluna
│   └── Criar como NULL → popular dados (backfill) → adicionar NOT NULL
│
├── Remover coluna
│   └── Parar de usar → fazer deploy → remover coluna
│
├── Adicionar índice
│   └── CREATE INDEX CONCURRENTLY (não bloqueante)
│
└── Renomear coluna
└── Criar nova → migrar dados → deploy → remover antiga

```

## Filosofia de Migração

- Nunca faça mudanças quebráveis em um único passo
- Teste migrations primeiro em uma cópia dos dados
- Sempre tenha um plano de rollback
- Execute migrations dentro de transações quando possível

## Bancos de Dados Serverless

### Neon (PostgreSQL Serverless)

| Recurso | Benefício |
|--------|-----------|
| Scale to zero | Redução de custos |
| Branching instantâneo | Desenvolvimento / preview |
| PostgreSQL completo | Compatibilidade total |
| Autoscaling | Suporte a picos de tráfego |

### Turso (SQLite em Edge)

| Recurso | Benefício |
|--------|-----------|
| Execução em edge | Latência ultra baixa |
| Compatível com SQLite | Simplicidade |
| Plano gratuito generoso | Economia |
| Distribuição global | Performance |
```
