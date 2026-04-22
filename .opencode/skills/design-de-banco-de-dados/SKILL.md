---
nome: design_de_banco_de_dados
descrição: Princípios de design de banco de dados e tomada de decisão. Modelagem de schema, estratégia de indexação, escolha de ORM, bancos de dados serverless.
ferramentas-permitidas: Ler, Escrever, Editar, Glob, Grep
---

# Design de Banco de Dados

> **Aprenda a PENSAR, não a copiar padrões de SQL.**

## 🎯 Regra de Leitura Seletiva

**Leia APENAS os arquivos relevantes para a solicitação!**  
Consulte o mapa de conteúdo e encontre exatamente o que você precisa.

| Arquivo | Descrição | Quando Ler |
|--------|-----------|------------|
| `seleção-de-banco-de-dados.md` | PostgreSQL vs Neon vs Turso vs SQLite | Escolha do banco de dados |
| `seleção-de-ORM.md` | Drizzle vs Prisma vs Kysely | Escolha do ORM |
| `design-de-esquema.md` | Normalização, PKs, relacionamentos | Modelagem do schema |
| `indexação.md` | Tipos de índices, índices compostos | Ajuste de performance |
| `otimização.md` | N+1, EXPLAIN ANALYZE | Otimização de queries |
| `migrações.md` | Migrations seguras, DBs serverless | Alterações de schema |

---

## ⚠️ Princípio Central

- PERGUNTE ao usuário sobre preferências de banco quando não estiver claro
- Escolha banco de dados e ORM com base no CONTEXTO
- Não padronize PostgreSQL para tudo

---

## Checklist de Decisão

Antes de modelar o schema:

- [ ] Perguntou ao usuário sobre preferência de banco?
- [ ] Escolheu o banco adequado para ESTE contexto?
- [ ] Considerou o ambiente de deploy?
- [ ] Planejou a estratégia de indexação?
- [ ] Definiu os tipos de relacionamento?

---

## Anti-Patterns

❌ Usar PostgreSQL por padrão em apps simples (SQLite pode ser suficiente)  
❌ Ignorar indexação  
❌ Usar `SELECT *` em produção  
❌ Armazenar JSON quando dados estruturados são mais adequados  
❌ Ignorar queries N+1
