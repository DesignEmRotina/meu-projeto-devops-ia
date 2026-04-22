--- 
name: sveltekit
description: "Crie aplicações web full-stack com SvelteKit — roteamento baseado em arquivos, SSR, SSG, rotas de API e ações de formulário em um único framework."
category: frontend
risk: seguro
source: comunidade
date_add: "2026-03-18"
autor: suhaibjanjua
tags: [svelte, sveltekit, fullstack, ssr, ssg, typescript]
---

# Desenvolvimento Full-Stack com SvelteKit

## Visão Geral

SvelteKit é o framework full-stack oficial construído sobre o Svelte. Ele oferece roteamento baseado em arquivos, renderização do lado do servidor (SSR), geração de sites estáticos (SSG), rotas de API e ações progressivas de formulário — tudo com o modelo de reatividade em tempo de compilação do Svelte, que não acarreta nenhuma sobrecarga de tempo de execução para o navegador. Use esta habilidade ao criar aplicativos web modernos e rápidos, onde tanto a experiência do desenvolvedor quanto o desempenho são importantes.

## Quando usar esta habilidade

- Use ao criar um novo aplicativo web full-stack com Svelte
- Use quando precisar de SSR ou SSG com controle preciso por rota
- Use ao migrar um SPA para um framework com recursos de servidor
- Use ao trabalhar em um projeto que precisa de roteamento baseado em arquivos e endpoints de API colocalizados
- Use quando o usuário perguntar sobre as funções `+page.svelte`, `+layout.svelte`, `load` ou ações de formulário

## Como funciona

### Passo 1: Configuração do projeto

```bash
npm create svelte@latest my-app
cd my-app
npm install
npm run dev
```

Escolha **Projeto esqueleto** + **TypeScript** + **ESLint/Prettier** quando solicitado.

Estrutura de diretórios após a criação do scaffolding:

```
src/

routes/

+page.svelte ← Componente raiz da página

+layout.svelte ← Layout raiz (envolve todas as páginas)

+error.svelte ← Limite de erro

lib/

server/ ← Código exclusivo do servidor (nunca incluído no cliente)

components/ ← Componentes compartilhados

app.html ← Estrutura HTML
static/ ← Recursos estáticos
```

### Etapa 2: Roteamento baseado em arquivos

Cada arquivo `+page.svelte` em `src/routes/` mapeia diretamente para uma URL:

```
src/routes/+page.svelte → /
src/routes/about/+page.svelte → /about
src/routes/blog/[slug]/+page.svelte → /blog/:slug
src/routes/shop/[...caminho]/+page.svelte → /shop/* (captura de todos)
```

**Grupos de rotas** (sem segmento de URL): envolva-os na pasta `(grupo)/`.

**Rotas privadas** (não acessíveis como URLs): prefixe com `_` ou `(grupo)`.

### Etapa 3: Carregando dados com funções `load`

Use um arquivo `+page.ts` (universal) ou `+page.server.ts` (somente para servidor) junto com a página:

```typescript
// src/routes/blog/[slug]/+page.server.ts
import { error } from '@sveltejs/kit';

import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, fetch }) => {

const post = await fetch(`/api/posts/${params.slug}`).then(r => r.json());

if (!post) {

error(404, 'Postagem não encontrada');

}

return { post };

};

```

```svelte
<!-- src/routes/blog/[slug]/+page.svelte -->
<script lang="ts">

import type { PageData } from './$types';

export let data: PageData;
</script>

<h1>{data.post.title}</h1>
<article>{@html data.post.content}</article>
```

### Etapa 4: Rotas da API (Endpoints do Servidor)

Crie arquivos `+server.ts` para endpoints no estilo REST:

```typescript
// src/routes/api/posts/+server.ts
import { json } from '@sveltejs/kit';

import type { RequestHandler } from './$types';

export const GET: RequestHandler = async ({ url }) => {

const limit = Number(url.searchParams.get('limit') ?? 10);

const posts = await db.post.findMany({ take: limit });

return json(posts);

};

export const POST: RequestHandler = async ({ request }) => {

const body = await request.json();

const post = await db.post.create({ data: body });

return json(post, { status: 201 });

};

``

### Etapa 5: Ações do Formulário

As ações do formulário são a maneira nativa do SvelteKit de lidar com mutações — sem necessidade de busca no lado do cliente:

```typescript
// src/routes/contact/+page.server.ts
import { fail, redirect } from '@sveltejs/kit';

import type { Actions } from './$types';

export const actions: Actions = {

default: async ({ request }) => {

const data = await request.formData();

const email = data.get('email');

if (!email) {

return fail(400, { email, missing: true });

}

await sendEmail(String(email));

redirect(303, '/thank-you');

}
};

```

```svelte
<!-- src/routes/contact/+page.svelte -->
<script lang="ts">

import { enhance } from '$app/forms';

import type { ActionData } from './$types';

export let form: ActionData;
</script>

<form method="POST" use:enhance>

<input name="email" type="email" />

{#if form?.missing}<p class="error">O e-mail é obrigatório</p termination if}

<button type="submit">Inscrever-se</button>
</form>
```

### Etapa 6: Layouts e Rotas Aninhadas

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">

import type { LayoutData } from './$types';

export let data: LayoutData;
</script>

<nav>

<a href="/">Home</a>

<a href="/blog">Blog</a>

{#if data.user}

<a href="/dashboard">Dashboard</a>

{/if}
</nav>

<slot /> <!-- página filha renderizada aqui -->
```

```typescript
// src/routes/+layout.server.ts
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {

return { user: locals.user ?? null };

};

```

### Etapa 7: Modos de Renderização

Controle a renderização por rota com opções de página:

```typescript
// src/routes/docs/+page.ts
export const prerender = true; // Estático — gerado em tempo de compilação
export const ssr = true; // Padrão — renderizado no servidor por requisição
export const csr = false; // Desativa completamente a hidratação no lado do cliente
```

### Exemplo 1: Rota Protegida do Painel de Controle

```typescript
// src/routes/dashboard/+layout.server.ts
import { redirect } from '@sveltejs/kit';

import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {

if (!locals.user) {

redirect(303, '/login');

}
return { user: locals.user };

};

```

### Exemplo 2: Hooks — Middleware de Sessão

```typescript
// src/hooks.server.ts
import type { Handle } from '@sveltejs/kit';

import { verifyToken } from '$lib/server/auth';

export const handle: Handle = async ({ event, resolve }) => {

const token = event.cookies.get('session');

if (token) {

event.locals.user = await verifyToken(token);

}

return resolve(event);

};

```
### Exemplo 3: Pré-carregamento e Invalidação

```svelte
<script lang="ts">

import { invalidateAll } from '$app/navigation';

async function refresh() {

await invalidateAll(); // Executa novamente todas as funções de carregamento da página

}
</script>

<button on:click={refresh}>Atualizar</button>
```

## Boas Práticas

- ✅ Use `+page.server.ts` para a lógica de banco de dados/autenticação — ela nunca é enviada para o cliente
- ✅ Use `$lib/server/` para módulos compartilhados exclusivos do servidor (cliente de banco de dados, auxiliares de autenticação)
- ✅ Use ações de formulário para mutações em vez de `fetch` no lado do cliente — funciona sem JS
- ✅ Defina todos os valores de retorno de `load` com `$types` gerados (`PageData`, `LayoutData`)
- ✅ Use `event.locals` em hooks para passar o contexto do servidor para as funções de carregamento
- ❌ Não importe código exclusivo do servidor diretamente em `+page.svelte` ou `+layout.svelte`
- ❌ Não armazene estado sensível em stores — use `locals` no servidor
- ❌ Não omita `use:enhance` nos formulários — sem ele, os formulários perdem o aprimoramento progressivo

## Notas de Segurança

- Todo o código em `+page.server.ts`, `+server.ts` e `$lib/server/` é executado exclusivamente no servidor — seguro para consultas ao banco de dados, segredos e validação de sessão.

- Sempre valide e higienize os dados do formulário antes de gravar no banco de dados.

- Use `error(403)` ou `redirect(303)` de `@sveltejs/kit` em vez de retornar objetos de erro brutos.

- Defina `httpOnly: true` e `secure: true` em todos os cookies de autenticação.

- A proteção CSRF é integrada para ações de formulário — não desabilite `checkOrigin` em produção.

## Problemas Comuns

- **Problema:** `Não é possível usar a declaração `import` em um módulo `+page.server.ts`

**Solução:** O arquivo deve ser `.ts` ou `.js`, não `.svelte`. Arquivos do servidor e componentes Svelte são separados.

- **Problema:** O valor do store é `undefined` na primeira renderização do SSR

**Solução:** Preencha o store com o valor de retorno da função `load` (propriedade `data`), não com o `onMount` do lado do cliente.

- **Problema:** A ação do formulário não redireciona após o envio

**Solução:** Use `redirect(303, '/path')` do `@sveltejs/kit`, não um simples `return`. O código 303 é necessário para redirecionamentos POST.

- **Problema:** `locals.user` está indefinido dentro de uma função de carregamento em `+page.server.ts`

**Solução:** Defina `event.locals.user` em `src/hooks.server.ts` antes da chamada de `resolve()`.

## Habilidades Relacionadas

- `@nextjs-app-router-patterns` — Quando você prefere React a Svelte para SSR/SSG
- `@trpc-fullstack` — Adicione segurança de tipo de ponta a ponta às rotas da API do SvelteKit
- `@auth-implementation-patterns` — Padrões de autenticação utilizáveis ​​com hooks do SvelteKit
- `@tailwind-patterns` — Estilizando aplicativos SvelteKit com Tailwind CSS