---
name: especialista-em-Drizzle-Orm
description: "Especialista em Drizzle ORM para TypeScript — design de esquema, consultas relacionais, migrações e integração com bancos de dados serverless. Use ao criar camadas de banco de dados com tipagem estática usando Drizzle."
risk: seguro
source: comunidade
date_add: "04/03/2026"
---

# Especialista em Drizzle ORM

Você é um especialista em Drizzle ORM com experiência em produção. Você ajuda desenvolvedores a criar camadas de banco de dados com tipagem estática e alto desempenho usando Drizzle ORM com TypeScript. Você conhece design de esquema, a API de consultas relacionais, migrações do Drizzle Kit e integrações com Next.js, tRPC e bancos de dados serverless (Neon, PlanetScale, Turso, Supabase).

## Quando usar esta habilidade

- Use quando o usuário solicitar a configuração do Drizzle ORM em um projeto novo ou existente
- Use ao projetar esquemas de banco de dados com a abordagem TypeScript-first do Drizzle
- Use ao escrever consultas relacionais complexas (joins, subconsultas, agregações)
- Use ao configurar ou solucionar problemas de migrações do Drizzle Kit
- Use ao integrar o Drizzle com o Next.js App Router, tRPC ou Hono
- Use ao otimizar o desempenho do banco de dados (instruções preparadas, processamento em lote, pool de conexões)
- Use ao migrar do Prisma, TypeORM ou Knex para o Drizzle

## Conceitos principais

### Por que o Drizzle?

O Drizzle ORM é um ORM TypeScript-first que gera zero sobrecarga de tempo de execução. Ao contrário do Prisma (que usa um binário de mecanismo de consulta), o Drizzle compila para SQL puro — tornando-o ideal para ambientes de execução de borda e computação sem servidor. Principais vantagens:

- **API semelhante a SQL**: Se você conhece SQL, conhece o Drizzle
- **Zero dependências**: Pacote pequeno, funciona no Cloudflare Workers, Vercel Edge e Deno
- **Inferência de tipo completa**: Esquema → tipos → consultas são todos conectados em tempo de compilação
- **API de consulta relacional**: Inclusões aninhadas semelhantes ao Prisma sem problemas N+1

## Padrões de projeto de esquema

### Definições de tabela

```typescript
// db/schema.ts
import { pgTable, text, integer, timestamp, boolean, uuid, pgEnum } from "drizzle-orm/pg-core";

import { relations } from "drizzle-orm";

// Enums
export const roleEnum = pgEnum("role", ["admin", "user", "moderator"]);

// Tabela de usuários
export const users = pgTable("users", {

id: uuid("id").defaultRandom().primaryKey(),

email: text("email").notNull().unique(),

name: text("name").notNull(),

role: roleEnum("role").default("user").notNull(),

createdAt: timestamp("created_at").defaultNow().notNull(),

updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

// Tabela de posts com chave estrangeira
export const posts = pgTable("posts", {

id: uuid("id").defaultRandom().primaryKey(),

title: text("title").notNull(),

content: text("content"),

published: boolean("published").default(false).notNull(),

authorId: uuid("author_id").references(() => users.id, { onDelete: "cascade" }).notNull(),

createdAt: timestamp("created_at").defaultNow().notNull(),
});

``

### Relações

```typescript
// db/relations.ts
export const usersRelations = relations(users, ({ many }) => ({

posts: many(posts),
}));

export const postsRelations = relations(posts, ({ one }) => ({

author: one(users, {

fields: [posts.authorId],

references: [users.id],

}),
}));

``

### Inferência de Tipos

```typescript
// Inferir tipos diretamente do seu esquema — sem necessidade de arquivos de tipo separados
import type { InferSelectModel, InferInsertModel } from "drizzle-orm";

export type User = InferSelectModel<typeof users>;

export type NewUser = InferInsertModel<typeof users>;

export type Post = InferSelectModel<typeof posts>;

export type NewPost = InferInsertModel<typeof posts>;

``

## Padrões de Consulta

### Consultas SELECT (API semelhante a SQL)

```typescript
import { eq, and, like, desc, count, sql } from "drizzle-orm";

// Seleção básica
const allUsers = await db.select().from(users);

// Filtrada com condições
const admins = await db.select().from(users).where(eq(users.role, "admin"));

// Seleção parcial (apenas colunas específicas)
const emails = await db.select({ email: users.email }).from(users);

// Consulta de junção
const postsWithAuthors = await db

.select({

title: posts.title,

authorName: users.name,

})

.from(posts)

.innerJoin(users, eq(posts.authorId, users.id))

.where(eq(posts.published, true))

.orderBy(desc(posts.createdAt))

.limit(10);

// Agregação
const postCounts = await db

.select({
authorId: posts.authorId,

postCount: count(posts.id),

})

.from(posts)

.groupBy(posts.authorId);
```

### Consultas Relacionais (API semelhante ao Prisma)

```typescript
// Inclusões aninhadas — Drizzle resolve em uma única consulta
const usersWithPosts = await db.query.users.findMany({
with: {
posts: {
where: eq(posts.published, true),
orderBy: [desc(posts.createdAt)],

limit: 5,
},
},
});

// Encontra um usuário com dados aninhados
const user = await db.query.users.findFirst({
where: eq(users.id, userId),
with: { posts: true },
});
```

### Inserir, Atualizar, Excluir

```typescript
// Inserir com retorno
const [newUser] = await db

.insert(users)

.values({ email: "dev@example.com", name: "Dev" })

.returning();

// Inserção em lote
await db.insert(posts).values([

{ title: "Post 1", authorId: newUser.id },

{ title: "Post 2", authorId: newUser.id },
]);

// Atualizar
await db.update(users).set({ name: "Updated" }).where(eq(users.id, userId));

// Excluir
await db.delete(posts).where(eq(posts.authorId, userId));
```

### Transações

```typescript
const result = await db.transaction(async (tx) => {

const [user] = await tx.insert(users).values({ email, name }).returning();

await tx.insert(posts).values({ title: "Postagem de Boas-vindas", authorId: user.id });

return user;
});

```

## Fluxo de Trabalho de Migração (Drizzle Kit)

### Configuração

```typescript
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({

schema: "./db/schema.ts",

out: "./drizzle",

dialect: "postgresql",

dbCredentials: {

url: process.env.DATABASE_URL!,

},
});

``

### Comandos

```bash
# Gerar SQL de migração a partir das alterações de esquema
npx drizzle-kit generate

# Enviar esquema diretamente para o banco de dados (somente para desenvolvimento — ignora arquivos de migração)
npx drizzle-kit push

# Executar migrações pendentes (produção)
npx drizzle-kit migrate

# Abrir o Drizzle Studio (navegador de banco de dados com interface gráfica)
npx drizzle-kit studio
```

## Configuração do Cliente de Banco de Dados

### PostgreSQL (Neon Serverless)

```typescript
// db/index.ts
import { drizzle } from "drizzle-orm/neon-http";
import { neon } from "@neondatabase/serverless";

import * as schema from "./schema";

const sql = neon(process.env.DATABASE_URL!);

export const db = drizzle(sql, { schema });

``

### SQLite (Turso/LibSQL)

```typescript
import { drizzle } from "drizzle-orm/libsql";

import { createClient } from "@libsql/client";

import * as schema from "./schema";

const client = createClient({
url: process.env.TURSO_DATABASE_URL!,
authToken: process.env.TURSO_AUTH_TOKEN,
});

export const db = drizzle(client, { schema });
```

### MySQL (PlanetScale)

```typescript
import { drizzle } from "drizzle-orm/planetscale-serverless";

import { Client } from "@planetscale/database";

import * as schema from "./schema";

const client = new Client({ url: process.env.DATABASE_URL! });

export const db = drizzle(client, { schema });

``

## Otimização de Desempenho

### Instruções Preparadas

```typescript
// Preparar uma vez, executar várias vezes
const getUserById = db.query.users

.findFirst({

where: eq(users.id, sql.placeholder("id")),

})

.prepare("get_user_by_id");

// Executar com parâmetros
const user = await getUserById.execute({ id: "abc-123" });
```

### Operações em Lote

```typescript
// Use db.batch() para múltiplas consultas independentes em uma única requisição
const [allUsers, recentPosts] = await db.batch([

db.select().from(users),

db.select().from(posts).orderBy(desc(posts.createdAt)).limit(10),
]);

```

### Indexação no Esquema

```typescript
import { index, uniqueIndex } from "drizzle-orm/pg-core";

export const posts = pgTable(

"posts",

{

id: uuid("id").defaultRandom().primaryKey(),

title: text("title").notNull(),

authorId: uuid("author_id").references(() => users.id).notNull(),

createdAt: timestamp("created_at").defaultNow().notNull(),

},

(table) => [
index("posts_author_idx").on(table.authorId),

index("posts_created_idx").on(table.createdAt),

]

```

## Integração com Next.js

### Uso do Componente de Servidor

```typescript
// app/users/page.tsx (Componente de Servidor React)
import { db } from "@/db";

import { users } from "@/db/schema";

export default async function UsersPage() {

const allUsers = await db.select().from(users);

return (

<ul>

{allUsers.map((u) => (
<li key={u.id}>{u.name}</li>

))}

</ul>

);

}
```

### Ação do Servidor

```typescript
// app/actions.ts
"use server";

import { db } from "@/db";

import { users } from "@/db/schema";

export async function createUser(formData: FormData) {

const name = formData.get("name") as string;

const email = formData.get("email") as string;

await db.insert(users).values({ name, email });

## Boas Práticas

- ✅ **Faça:** Mantenha todas as definições de esquema em um único arquivo `db/schema.ts` ou divida-as por domínio (`db/schema/users.ts`, `db/schema/posts.ts`)
- ✅ **Faça:** Use `InferSelectModel` e `InferInsertModel` para segurança de tipos em vez de interfaces manuais
- ✅ **Faça:** Use a API de consulta relacional (`db.query.*`) para dados aninhados para evitar problemas N+1
- ✅ **Faça:** Use instruções preparadas para consultas executadas com frequência em produção
- ✅ **Faça:** Use `drizzle-kit generate` + `migrate` em produção (nunca use `push`)
- ✅ **Faça:** Passe `{ schema }` para `drizzle()` para habilitar a API de consulta relacional
- ❌ **Não faça:** `drizzle-kit push` em produção — pode causar perda de dados
- ❌ **Não faça:** Escrever SQL puro quando o construtor de consultas do Drizzle suporta a operação
- ❌ **Não faça:** Esquecer de definir `relations()` se você quiser usar `db.query.*` com `with`
- ❌ **Não faça:** Criar uma nova conexão de banco de dados por solicitação em ambientes serverless — use o pool de conexões

## Solução de problemas

**Problema:** `db.query.tableName` não está definido
**Solução:** Passe todos os objetos de esquema (incluindo relações) para `drizzle()`: `drizzle(client, { schema })`

**Problema:** Conflitos de migração após alterações de esquema
**Solução:** Execute `npx drizzle-kit generate` para criar uma nova migração e, em seguida, `npx drizzle-kit migrate`

**Problema:** Erros de tipo em `.returning()` com MySQL
**Solução:** O MySQL não suporta `RETURNING`. Use `.execute()` e leia `insertId` do resultado.