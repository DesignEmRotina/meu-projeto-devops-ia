# Otimização de Consultas

> Problema N+1, EXPLAIN ANALYZE e prioridades de otimização.

## Problema N+1

```

O que é N+1?
├── 1 consulta para buscar os registros pais
├── N consultas para buscar os registros relacionados
└── Extremamente lento!

Soluções:
├── JOIN → Consulta única com todos os dados
├── Eager loading → ORM gerencia os JOINs
├── DataLoader → Agrupamento e cache (GraphQL)
└── Subquery → Buscar relacionamentos em uma única consulta

```

## Mentalidade de Análise de Consultas

```

Antes de otimizar:
├── Execute EXPLAIN ANALYZE na consulta
├── Procure por Seq Scan (varredura completa da tabela)
├── Compare linhas estimadas vs linhas reais
└── Identifique índices ausentes

```

## Prioridades de Otimização

1. **Adicionar índices ausentes** (problema mais comum)
2. **Selecionar apenas as colunas necessárias** (evite SELECT *)
3. **Usar JOINs adequados** (evite subqueries quando possível)
4. **Limitar o quanto antes** (paginação no nível do banco)
5. **Cache** (quando fizer sentido)
```
