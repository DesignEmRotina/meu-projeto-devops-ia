--- 
name: implantação-vercel
description: Conhecimento especializado para implantação no Vercel com Next.js
risk: seguro
source: vibeship-spawner-skills (Apache 2.0)
date_add: 27/02/2026
---

# Implantação no Vercel

Conhecimento especializado para implantação no Vercel com Next.js

## Recursos

- vercel
- deployment
- edge-functions
- serverless
- environment-variables

## Pré-requisitos

- Skills necessárias: nextjs-app-router

## Padrões

### Configuração de Variáveis ​​de Ambiente

Configure corretamente as variáveis ​​de ambiente para todos os ambientes

**Quando usar**: Configurando um novo projeto no Vercel

// Três ambientes no Vercel:

// - Desenvolvimento (local)

// - Pré-visualização (implantações de PR)

// - Produção (branch principal)

// No Vercel Painel de controle:
// Configurações → Variáveis ​​de ambiente

// Variáveis ​​PÚBLICAS (expostas ao navegador)
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...

// Variáveis ​​PRIVADAS (somente no servidor)
SUPABASE_SERVICE_ROLE_KEY=eyJ... // Nunca NEXT_PUBLIC_!

DATABASE_URL=postgresql://...

// Valores por ambiente:
// Produção: Banco de dados real, chaves de API de produção
// Pré-visualização: Banco de dados de staging, chaves de API de teste
// Desenvolvimento: Valores locais/de desenvolvimento (também em .env.local)

// No código, verifique o ambiente:
const isProduction = process.env.VERCEL_ENV === 'production'
const isPreview = process.env.VERCEL_ENV === 'preview'

### Funções Edge vs. Serverless

Escolha o runtime certo para suas rotas de API

**Quando usar**: Criação de rotas de API ou middleware

// EDGE RUNTIME - Inicializações a frio rápidas, APIs limitadas
// Bom para: Verificações de autenticação, redirecionamentos, transformações simples

// app/api/hello/route.ts
export const runtime = 'edge'

export async function GET() {

return Response.json({ message: 'Olá do Edge!' })
}

// middleware.ts (sempre edge)
export function middleware(request: NextRequest) {

// Verificações de autenticação rápidas aqui
}

// SERVERLESS (Node.js) - APIs Node completas, inicialização a frio mais lenta
// Bom para: Consultas a banco de dados, operações com arquivos, computação pesada

// app/api/users/route.ts
export const runtime = 'nodejs' // Padrão, pode ser omitido

export async function GET() {

const users = await db.query('SELECT * FROM users')

return Response.json(users)
}

### Otimização de Build

Otimize o build para implantações mais rápidas e pacotes menores

**Quando usar**: Preparando para a implantação em produção

// next.config.js
/** @type {import('next').NextConfig} const nextConfig = {

// Minimizar a saída

output: 'standalone', // Para Docker/hospedagem própria

// Otimização de imagem

images: {

remotePatterns: [

{ hostname: 'your-cdn.com' },

],

},

// Analisador de pacotes (somente para desenvolvedores)

// npm install @next/bundle-analyzer

...(process.env.ANALYZE === 'true' && {

webpack: (config) => {

const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer')

config.plugins.push(new BundleAnalyzerPlugin())

return config

},

}),
}

// Reduzir o tamanho da função serverless:
// - Usar importações dinâmicas para bibliotecas pesadas
// - Verificar o pacote com: npx @next/bundle-analyzer

### Fluxo de Trabalho de Implantação de Pré-visualização

Use implantações de pré-visualização para revisões de Pull Requests

**Quando usar**: Configurando o fluxo de trabalho de desenvolvimento da equipe

// Cada Pull Request recebe automaticamente uma URL de pré-visualização exclusiva

// Proteja as implantações de pré-visualização com senha:
// Painel do Vercel → Configurações → Proteção de Implantação

// Use variáveis ​​de ambiente diferentes para pré-visualização:
// - PRÉ-VISUALIZAÇÃO: Usar banco de dados de staging
// - PRODUÇÃO: Usar banco de dados de produção

// No código, detecte a pré-visualização:
if (process.env.VERCEL_ENV === 'preview') {

/ Exibir banner "Pré-visualização"

// Usar processador de pagamento de teste

// Desativar análise
}

// URL de pré-visualização de comentários no PR (automático com a integração do Vercel com o GitHub)

### Configuração de Domínio Personalizado

Configure domínios personalizados com SSL adequado

**Quando usar**: Para produção

// No Painel do Vercel → Domínios

// Adicione domínios:

// - example.com (raiz)

// - www.example.com (subdomínio)

// Configuração de DNS (no seu registrador):
// Tipo: A, Nome: @, Valor: 76.76.21.21
// Tipo: CNAME, Nome: www, Valor: cname.vercel-dns.com

// Redirecionar www para raiz (ou vice-versa):
// O Vercel lida com isso automaticamente

// Em next.config.js para redirecionamentos:
module.exports = {

async redirects() {

return [

{
source: '/old-page',

destination: '/new-page',

permanent: true, // 308

},

]

},
}

## Limitações Críticas

### NEXT_PUBLIC_ expõe segredos ao navegador

Gravidade: CRÍTICA

Situação: Uso do prefixo NEXT_PUBLIC_ para chaves de API sensíveis

Sintomas:
- Segredos visíveis nas Ferramentas de Desenvolvedor do navegador → Fontes
- Auditoria de segurança encontra chaves expostas
- Acesso inesperado à API de fontes desconhecidas

Por que isso causa problemas:
Variáveis ​​com o prefixo NEXT_PUBLIC_ são incorporadas ao pacote JavaScript
durante a compilação. Qualquer pessoa pode visualizá-las nas Ferramentas de Desenvolvedor do navegador.

Isso inclui todos os seus usuários e potenciais invasores.

Correção recomendada:

Use NEXT_PUBLIC_ somente para valores verdadeiramente públicos:

// É SEGURO usar NEXT_PUBLIC_
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ... // A chave anônima foi projetada para ser pública
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...
NEXT_PUBLIC_GA_ID=G-XXXXXXX

// NUNCA use NEXT_PUBLIC_
SUPABASE_SERVICE_ROLE_KEY=eyJ... // Acesso total ao banco de dados!

STRIPE_SECRET_KEY=sk_live_... // Pode cobrar com cartão!

DATABASE_URL=postgresql://... // Acesso direto ao banco de dados!

JWT_SECRET=... // Pode forjar tokens!

// Acessar variáveis ​​exclusivas do servidor em:
// - Componentes do servidor (roteador de aplicativos)
// - Rotas da API
// - Ações do servidor ('usar servidor')
// - getServerSideProps (roteador de páginas)

### Implantações de pré-visualização usando banco de dados de produção

Gravidade: ALTA

Situação: Não configurar variáveis ​​de ambiente separadas para pré-visualização

Sintomas:
- Dados de teste aparecendo em produção
- Dados de produção corrompidos após a fusão do PR
- Usuários visualizando contas/conteúdo de teste

Por que isso causa problemas:
As implantações de pré-visualização executam código não testado. Se elas usam o banco de dados de produção,
um bug em um PR pode corromper os dados de produção. Além disso, os testadores podem criar
dados de teste que aparecem em produção.

Solução recomendada:

Configure bancos de dados separados para cada ambiente:

// No Painel do Vercel → Configurações → Variáveis ​​de Ambiente

// Produção (somente ambiente de produção):
DATABASE_URL=postgresql://prod-host/prod-db

// Pré-visualização (somente ambiente de pré-visualização):
DATABASE_URL=postgresql://staging-host/staging-db

// Ou use os bancos de dados de ramificação do Vercel:
// - Neon, PlanetScale e Supabase suportam bancos de dados de ramificação
// - Crie automaticamente um banco de dados de pré-visualização para cada PR

// Para o Supabase, crie um projeto de teste:
// Produção:
NEXT_PUBLIC_SUPABASE_URL=https://prod-xxx.supabase.co

// Pré-visualização:
NEXT_PUBLIC_SUPABASE_URL=https://staging-xxx.supabase.co

### Função serverless muito grande, lenta e inativa Início

Gravidade: ALTA

Situação: Rota da API ou componente do servidor com carregamento inicial lento

Sintomas:
- A primeira requisição leva de 3 a 10+ segundos
- Requisições subsequentes são rápidas
- Erro de limite de tamanho da função excedido
- A implantação falha com erro de tamanho

Motivo da falha:
As funções serverless do Vercel têm um limite de 50 MB (compactado).

Funções grandes significam inicializações lentas (1 a 5+ segundos).

Dependências pesadas como Puppeteer e Sharp podem causar isso.

Correção recomendada:

Reduzir o tamanho da função:

// 1. Usar importações dinâmicas para bibliotecas pesadas
export async function GET() {

const sharp = await import('sharp') // Carrega somente quando necessário
// ...
}

// 2. Mova o processamento pesado para a borda ou para um serviço externo
export const runtime = 'edge' // Inicialização a frio muito menor e mais rápida

// 3. Verifique o tamanho do pacote
// npx @next/bundle-analyzer
// Procure por grandes dependências

// 4. Use serviços externos para tarefas pesadas
// - Processamento de imagens: Cloudinary, imgix
// - Geração de PDF: serviço de API
// - Puppeteer: Browserless.io

// 5. Divida em várias funções
// /api/heavy-task/start - Enfileire a tarefa
// /api/heavy-task/status - Verifique o progresso

### O runtime de borda não possui APIs do Node.js

Gravidade: ALTA

Situação: Usando APIs do Node.js em funções do runtime de borda

Sintomas:
- X não está definido em tempo de execução
- Não foi possível encontrar o módulo fs
- Funciona localmente, falha em produção
- Falha no middleware

Por que isso acontece:
O ambiente de execução do Edge roda em V8, não em Node.js. Muitas APIs do Node estão faltando:
fs, path, crypto (parcial), child_process e a maioria dos módulos nativos.

Seu código falhará em tempo de execução com a mensagem "X não está definido".

Correção recomendada:

Verifique a compatibilidade da API antes de usar o Edge:

// SUPORTADO no Edge:
// - fetch, Request, Response
// - crypto.subtle (Web Crypto)
// - TextEncoder, TextDecoder
// - URL, URLSearchParams
// - Headers, FormData
// - setTimeout, setInterval

// NÃO SUPORTADO no Edge:
// - fs, path, os
// - Buffer (use Uint8Array)
// - crypto.createHash (use crypto.subtle)
// - A maioria dos pacotes npm com dependências nativas

// Se você precisar de APIs do Node.js:
export const runtime = 'nodejs' // Use o runtime do Node em vez disso

// Para hash criptográfico no Edge:
// INCORRETO
import { createHash } from 'crypto' // Falha no Edge

// CORRETO
async function hash(message: string) {

const encoder = new TextEncoder()

const data = encoder.encode(message)

const hashBuffer = await crypto.subtle.digest('SHA-256', data)

return Array.from(new Uint8Array(hashBuffer))

.map(b => b.toString(16).padStart(2, '0'))

.join('')
}

### Tempo limite da função causa operações incompletas

Gravidade: MÉDIA

Situação: Operações de longa duração atingindo o tempo limite

Sintomas:
- Tarefa atingiu o tempo limite após X segundos
- Operações incompletas no banco de dados
- Uploads parciais de arquivos
- Função interrompida durante a execução

Motivo da falha:
O Vercel possui limites de tempo limite:
- Hobby: 10 segundos
- Pro: 60 segundos (pode aumentar para 300)
- Enterprise: 900 segundos

Operações Aqueles que ultrapassarem esse limite serão mortos durante a execução.

Correção recomendada:

Lidar adequadamente com operações longas:

// 1. Retornar antecipadamente, processar de forma assíncrona
export async function POST(request: Request) {

const data = await request.json()

// Enfileirar para processamento em segundo plano

await queue.add('process-data', data)

// Retornar imediatamente
return Response.json({ status: 'queued' })
}

// 2. Usar streaming para respostas longas
export async function GET() {
const stream = new ReadableStream({

async start(controller) {

for (const chunk of generateChunks()) {

controller.enqueue(chunk)

await sleep(100) // Evita timeout

}

controller.close()

}

})

return new Response(stream)
}

// 3. Usar serviços externos para processamento pesado
// - Acionar função serverless, retornar ID da tarefa
// - Processar em segundo plano (Ingest, Trigger.dev)
// - O cliente verifica a conclusão

// 4. Aumentar o tempo limite (plano Pro)
// vercel.json:
{

"functions": {

"app/api/slow/route.ts": {

"maxDuration": 60

}
}
}

### Variável de ambiente ausente em tempo de execução, mas presente na compilação

Gravidade: MÉDIA

Situação: A variável de ambiente funciona na compilação, mas está indefinida em tempo de execução

Sintomas:
- A variável de ambiente está indefinida em produção
- O valor não muda após a atualização no painel
- Funciona em desenvolvimento, mas o valor está incorreto em produção
- Requer reimplementação para atualizar o valor

Por que isso causa o problema:
Algumas variáveis ​​de ambiente estão disponíveis apenas no momento da compilação (codificadas no pacote).

Se você espera um valor em tempo de execução, mas ele foi incorporado na compilação, você obtém
o valor de tempo de compilação ou indefinido.

Correção recomendada:

Entenda quando as variáveis ​​de ambiente são lidas:

// TEMPO DE COMPILAÇÃO (incorporadas ao pacote):
// - Variáveis ​​NEXT_PUBLIC_*
// - next.config.js
// - generateStaticParams
// - Páginas estáticas

// TEMPO DE EXECUÇÃO (lidas a cada requisição):
// - Componentes do servidor (sem cache)
// - Rotas da API
// - Ações do servidor
// - Middleware

// Para forçar a leitura em tempo de execução:
export const dynamic = 'force-dynamic'

// Para configurações que devem ser lidas em tempo de execução:
// Não use NEXT_PUBLIC_, leia no servidor e passe para o cliente

// Verifique quais variáveis ​​de ambiente você precisa:
// Compilação: URLs, chaves públicas, flags de recursos (se estáticas)
// Tempo de execução: Segredos, URLs do banco de dados, configurações específicas do usuário

### Erros de CORS ao chamar rotas da API de domínios diferentes

Gravidade: MÉDIO

Situação: Frontend em domínio diferente não consegue acessar rotas da API

Sintomas:
- Erro de política CORS no console do navegador
- Ausência do cabeçalho Access-Control-Allow-Origin
- Requisições funcionam no Postman, mas não no navegador
- Funciona com a mesma origem, mas falha com origens diferentes

Motivo do problema:
Por padrão, os navegadores bloqueiam requisições de origens diferentes. O Vercel não
adiciona cabeçalhos CORS automaticamente. Se o seu frontend estiver em um domínio diferente
(ou localhost em ambiente de desenvolvimento), as requisições falham.

Correção recomendada:

Adicionar cabeçalhos CORS às rotas da API:

// app/api/data/route.ts
export async function GET(request: Request) {

const data = await fetchData()

return Response.json(data, {
headers: {
'Access-Control-Allow-Origin': '*', // Ou domínio específico
'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
'Access-Control-Allow-Headers': 'Content-Type, Authorization',

},

})

}

// Lidar com solicitações de pré-voo
export async function OPTIONS() {
return new Response(null, {
headers: {

'Access-Control-Allow-Origin': '*',

'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
'Access-Control-Allow-Headers': 'Content-Type, Authorization',

},

})
}

// Ou use next.config.js para todas as rotas:
module.exports = {

async headers() {
return [

{
source: '/api/:path*',

headers: [

{ key: 'Access-Control-Allow-Origin', value: '*' },

],

},

]

},
}

### Página exibe dados desatualizados após a implantação

Gravidade: MÉDIA

Situação: Dados atualizados não aparecem após nova implantação

Sintomas:
- Conteúdo antigo é exibido após a implantação
- Alterações não ficam visíveis imediatamente
- Usuários diferentes veem versões diferentes
- Os dados são atualizados, mas a página não

Por que isso acontece:
O Vercel usa cache de forma agressiva. Páginas estáticas são armazenadas em cache na borda.

Até mesmo páginas dinâmicas podem ser armazenadas em cache se não estiverem configuradas corretamente. Versões antigas em cache são exibidas até que o cache expire ou seja limpo.

Correção recomendada:

Controlar o comportamento do cache:

// Forçar a não utilização de cache (sempre atualizado)
export const dynamic = 'force-dynamic'
export const revalidate = 0

// ISR - revalidar a cada 60 segundos
export const revalidate = 60

// Revalidação sob demanda (após mutação)
import { revalidatePath, revalidateTag } from 'next/cache'

// Na ação do servidor:
async function updatePost(id: string) {

await db.post.update({ ... })

revalidatePath(`/posts/${id}`) // Limpar esta página
revalidateTag('posts') // Limpar todas as páginas com esta tag
}

// Limpeza via API (gancho de implantação):
// POST https://your-site.vercel.app/api/revalidate?path=/posts

// Verificar cache nos cabeçalhos da resposta:
// x-vercel-cache: HIT = servido do cache
// x-vercel-cache: MISS = gerado recentemente

## Verificações de Validação

### Segredo na variável NEXT_PUBLIC

Gravidade: CRÍTICA

Mensagem: Segredo exposto pelo prefixo NEXT_PUBLIC_. Isso ficará visível no navegador.

Ação corretiva: Remova o prefixo NEXT_PUBLIC_ e acesse apenas no código do servidor.

### URL do Vercel codificada

Gravidade: AVISO

Mensagem: URL do Vercel codificada. Use a variável de ambiente VERCEL_URL.

Ação corretiva: Use process.env.VERCEL_URL ou NEXT_PUBLIC_VERCEL_URL

### API Node.js no ambiente de execução Edge

Gravidade: ERRO

Mensagem: Módulo Node.js usado no ambiente de execução Edge. fs/path não disponível no Edge.

Ação corretiva: Use runtime = 'nodejs' ou remova as dependências do Node.js

### Rota da API sem cabeçalhos CORS

Gravidade: AVISO

Mensagem: Rotas da API sem cabeçalhos CORS podem falhar em solicitações de origem cruzada.

Ação corretiva: Adicione o cabeçalho Access-Control-Allow-Origin se a API for chamada de outros domínios

### Rota da API sem tratamento de erros

Gravidade: AVISO

Mensagem: Rota da API sem bloco try/catch. Erros não tratados retornam 500 sem detalhes.

Ação corretiva: Envolva o código em um bloco try/catch e retorne as respostas de erro apropriadas.

### Leitura de Segredo em Contexto Estático

Gravidade: AVISO

Mensagem: Segredo do servidor acessado durante a geração estática. O valor está incorporado à compilação.

Ação corretiva: Mova o acesso ao segredo para o código em tempo de execução ou use NEXT_PUBLIC_ para valores públicos.

### Importação de Pacote Grande

Gravidade: AVISO

Mensagem: Pacote grande importado. Pode causar inicializações lentas. Considere alternativas.

Ação corretiva: Use lodash-es com tree shaking, date-fns em vez de moment, @aws-sdk/client-* em vez de aws-sdk.

### Página Dinâmica Sem Configuração de Revalidação

Gravidade: AVISO

Mensagem: Página dinâmica sem configuração de revalidação. Considere definir uma estratégia de revalidação.

Ação de correção: Adicione `export const revalidate = 60` para ISR ou `0` para nenhum cache.

## Colaboração

### Gatilhos de Delegação

- next.js|app router|pages|server components -> nextjs-app-router (A implantação requer padrões do Next.js)
- database|supabase|backend -> supabase-backend (A implantação requer banco de dados)
- auth|authentication|session -> nextjs-supabase-auth (A implantação requer configuração de autenticação)
- monitoring|logs|errors|analytics -> analytics-architecture (A implantação requer monitoramento)

### Lançamento em Produção

Habilidades: vercel-deployment, nextjs-app-router, supabase-backend, nextjs-supabase-auth

Fluxo de trabalho:

```
1. Configuração do aplicativo (nextjs-app-router)
2. Configuração do banco de dados (supabase-backend)
3. Configuração de autenticação (nextjs-supabase-auth)
4. Implantação (vercel-deployment)
```

### Pipeline de CI/CD

Habilidades: vercel-deployment, devops, engenharia de QA

Fluxo de trabalho:

```
1. Automação de testes (engenharia de QA)
2. Configuração do pipeline (devops)
3. Estratégia de implantação (vercel-deployment)
```

## Habilidades Relacionadas

Funciona bem com: `nextjs-app-router`, `supabase-backend`

## Quando Usar
- O usuário menciona ou implica: Vercel
- O usuário menciona ou implica: deploy
- O usuário menciona ou implica: implantação
- O usuário menciona ou implica: hospedagem
- O usuário menciona ou implica: produção
- O usuário menciona ou implica: variáveis ​​de ambiente
- O usuário menciona ou implica: função edge
- O usuário menciona ou implica: função serverless

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.
