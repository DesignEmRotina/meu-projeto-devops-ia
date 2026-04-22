# Princípios de Indexação

> Quando e como criar índices de forma eficaz.

## Quando Criar Índices

```

Crie índices para:
├── Colunas usadas em cláusulas WHERE
├── Colunas usadas em JOINs
├── Colunas usadas em ORDER BY
├── Colunas de chaves estrangeiras
└── Restrições UNIQUE

Evite excesso de índices:
├── Tabelas com muitas escritas (inserts mais lentos)
├── Colunas de baixa cardinalidade
├── Colunas raramente consultadas

```

## Seleção do Tipo de Índice

| Tipo | Usar Para |
|------|-----------|
| **B-tree** | Uso geral, igualdade e intervalos |
| **Hash** | Apenas igualdade, mais rápido |
| **GIN** | JSONB, arrays, full-text search |
| **GiST** | Dados geométricos, tipos de intervalo |
| **HNSW / IVFFlat** | Similaridade vetorial (pgvector) |

## Princípios de Índices Compostos

```

A ordem importa em índices compostos:
├── Colunas de igualdade primeiro
├── Colunas de intervalo por último
├── Colunas mais seletivas primeiro
└── Deve refletir o padrão das consultas

```
```
