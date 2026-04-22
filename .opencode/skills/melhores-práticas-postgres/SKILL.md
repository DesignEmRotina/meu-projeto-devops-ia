--- 
name: melhores-práticas-postgres
description: "Otimização de desempenho e melhores práticas do Postgres da Supabase. Use esta habilidade ao escrever, revisar ou otimizar consultas Postgres, projetos de esquema ou configurações de banco de dados."
risk: seguro
source: comunidade
date_add: "2026-02-27"
---

# Melhores Práticas do Postgres da Supabase

Guia abrangente de otimização de desempenho para Postgres, mantido pela Supabase. Contém regras em 8 categorias, priorizadas por impacto para orientar a otimização automatizada de consultas e o projeto de esquemas.

## Quando usar
Consulte estas diretrizes ao:
- Escrever consultas SQL ou projetar esquemas
- Implementar índices ou otimização de consultas
- Analisar problemas de desempenho do banco de dados
- Configurar pool de conexões ou escalonamento
- Otimizar para recursos específicos do Postgres
- Trabalhar com Segurança em Nível de Linha (RLS)

## Categorias de Regras por Prioridade

| Prioridade | Categoria | Impacto | Prefixo |

|----------|----------|--------|--------|
| 1 | Desempenho de Consultas | CRÍTICO | `query-` |

| 2 | Gerenciamento de Conexões | CRÍTICO | `conn-` |

| 3 | Segurança e RLS | CRÍTICO | `security-` |

| 4 | Design de Esquema | ALTO | `schema-` |

| 5 | Concorrência e Bloqueio | MÉDIO-ALTO | `lock-` |

| 6 | Padrões de Acesso a Dados | MÉDIO | `data-` |

| 7 | Monitoramento e Diagnóstico | BAIXO-MÉDIO | `monitor-` |

| 8 | Recursos Avançados | BAIXO | `advanced-` |

## Como usar

Leia os arquivos de regras individuais para obter explicações detalhadas e exemplos de SQL:

```
regras/query-missing-indexes.md
regras/schema-partial-indexes.md
regras/_sections.md
```

Cada arquivo de regra contém:
- Breve explicação sobre a importância da regra
- Exemplo de SQL incorreto com explicação
- Exemplo de SQL correto com explicação
- Saída opcional do EXPLAIN ou métricas
- Contexto e referências adicionais
- Notas específicas do Supabase (quando aplicável)

## Documento completo compilado

Para o guia completo com todas as regras expandidas: `AGENTS.md`

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.