# Guia de Implementação dos Padrões do App Router do Next.js

Este arquivo contém padrões detalhados, listas de verificação e exemplos de código referenciados pela skill.

# Padrões do App Router do Next.js

Padrões abrangentes para a arquitetura App Router do Next.js 14+, Componentes de Servidor e desenvolvimento full-stack moderno com React.

## Quando usar esta skill

- Criar novos aplicativos Next.js com App Router
- Migrar do Pages Router para o App Router
- Implementar Componentes de Servidor e streaming
- Configurar rotas paralelas e interceptadas
- Otimizar a busca e o cache de dados
- Criar funcionalidades full-stack com Server Actions

## Conceitos principais

### 1. Modos de renderização

| Modo | Onde | Quando usar |

|------|-------|-------------|

| **Componentes de Servidor** | Somente servidor | Busca de dados, computação pesada, segredos |

| **Componentes de Cliente** | Navegador | Interatividade, hooks, APIs do navegador |
| **Estático** | Tempo de compilação | Conteúdo que raramente muda |

| **Dinâmico** | Tempo de requisição | Dados personalizados ou em tempo real |

| **Streaming** | Progressivo | Páginas grandes, fontes de dados lentas |

### 2. Convenções de Arquivos

```
app/
├── layout.tsx # Wrapper da interface do usuário compartilhada
├── page.tsx # Interface de rota
├── loading.tsx # Interface de carregamento (Suspense)
├── error.tsx # Limite de erro
├── not-found.tsx # Interface de erro 404
├── route.ts # Endpoint da API
├── template.tsx # Layout remontado
├── default.tsx # Rota alternativa paralela
└── opengraph-image.tsx # Geração de imagem OG
```

## Início Rápido


```typescript
// app/layout.tsx
import { Inter } from 'next/font/google'
import { Providers } from './providers'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: { default: 'My App', template: '%s | My App' },
  description: 'Built with Next.js App Router',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}

// app/page.tsx - Server Component by default
async function getProducts() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600 }, // ISR: revalidate every hour
  })
  return res.json()
}

export default async function HomePage() {
  const products = await getProducts()

  return (
    <main>
      <h1>Products</h1>
      <ProductGrid products={products} />
    </main>
  )
}
```

## Patterns

### Pattern 1: Server Components with Data Fetching

```typescript
// app/products/page.tsx
import { Suspense } from 'react'
import { ProductList, ProductListSkeleton } from '@/components/products'
import { FilterSidebar } from '@/components/filters'

interface SearchParams {
  category?: string
  sort?: 'price' | 'name' | 'date'
  page?: string
}

export default async function ProductsPage({
  searchParams,
}: {
  searchParams: Promise<SearchParams>
}) {
  const params = await searchParams

  return (
    <div className="flex gap-8">
      <FilterSidebar />
      <Suspense
        key={JSON.stringify(params)}
        fallback={<ProductListSkeleton />}
      >
        <ProductList
          category={params.category}
          sort={params.sort}
          page={Number(params.page) || 1}
        />
      </Suspense>
    </div>
  )
}

// components/products/ProductList.tsx - Server Component
async function getProducts(filters: ProductFilters) {
  const res = await fetch(
    `${process.env.API_URL}/products?${new URLSearchParams(filters)}`,
    { next: { tags: ['products'] } }
  )
  if (!res.ok) throw new Error('Failed to fetch products')
  return res.json()
}

export async function ProductList({ category, sort, page }: ProductFilters) {
  const { products, totalPages } = await getProducts({ category, sort, page })

  return (
    <div>
      <div className="grid grid-cols-3 gap-4">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
      <Pagination currentPage={page} totalPages={totalPages} />
    </div>
  )
}
```

### Pattern 2: Client Components with 'use client'

```typescript
// components/products/AddToCartButton.tsx
'use client'

import { useState, useTransition } from 'react'
import { addToCart } from '@/app/actions/cart'

export function AddToCartButton({ productId }: { productId: string }) {
  const [isPending, startTransition] = useTransition()
  const [error, setError] = useState<string | null>(null)

  const handleClick = () => {
    setError(null)
    startTransition(async () => {
      const result = await addToCart(productId)
      if (result.error) {
        setError(result.error)
      }
    })
  }

  return (
    <div>
      <button
        onClick={handleClick}
        disabled={isPending}
        className="btn-primary"
      >
        {isPending ? 'Adding...' : 'Add to Cart'}
      </button>
      {error && <p className="text-red-500 text-sm">{error}</p>}
    </div>
  )
}
```

### Pattern 3: Server Actions

```typescript
// app/actions/cart.ts
'use server'

import { revalidateTag } from 'next/cache'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

export async function addToCart(productId: string) {
  const cookieStore = await cookies()
  const sessionId = cookieStore.get('session')?.value

  if (!sessionId) {
    redirect('/login')
  }

  try {
    await db.cart.upsert({
      where: { sessionId_productId: { sessionId, productId } },
      update: { quantity: { increment: 1 } },
      create: { sessionId, productId, quantity: 1 },
    })

    revalidateTag('cart')
    return { success: true }
  } catch (error) {
    return { error: 'Failed to add item to cart' }
  }
}

export async function checkout(formData: FormData) {
  const address = formData.get('address') as string
  const payment = formData.get('payment') as string

  // Validate
  if (!address || !payment) {
    return { error: 'Missing required fields' }
  }

  // Process order
  const order = await processOrder({ address, payment })

  // Redirect to confirmation
  redirect(`/orders/${order.id}/confirmation`)
}
```

### Pattern 4: Parallel Routes

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
  analytics,
  team,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
}) {
  return (
    <div className="dashboard-grid">
      <main>{children}</main>
      <aside className="analytics-panel">{analytics}</aside>
      <aside className="team-panel">{team}</aside>
    </div>
  )
}

// app/dashboard/@analytics/page.tsx
export default async function AnalyticsSlot() {
  const stats = await getAnalytics()
  return <AnalyticsChart data={stats} />
}

// app/dashboard/@analytics/loading.tsx
export default function AnalyticsLoading() {
  return <ChartSkeleton />
}

// app/dashboard/@team/page.tsx
export default async function TeamSlot() {
  const members = await getTeamMembers()
  return <TeamList members={members} />
}
```

### Pattern 5: Intercepting Routes (Modal Pattern)

```typescript
// File structure for photo modal
// app/
// ├── @modal/
// │   ├── (.)photos/[id]/page.tsx  # Intercept
// │   └── default.tsx
// ├── photos/
// │   └── [id]/page.tsx            # Full page
// └── layout.tsx

// app/@modal/(.)photos/[id]/page.tsx
import { Modal } from '@/components/Modal'
import { PhotoDetail } from '@/components/PhotoDetail'

export default async function PhotoModal({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const photo = await getPhoto(id)

  return (
    <Modal>
      <PhotoDetail photo={photo} />
    </Modal>
  )
}

// app/photos/[id]/page.tsx - Full page version
export default async function PhotoPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const photo = await getPhoto(id)

  return (
    <div className="photo-page">
      <PhotoDetail photo={photo} />
      <RelatedPhotos photoId={id} />
    </div>
  )
}

// app/layout.tsx
export default function RootLayout({
  children,
  modal,
}: {
  children: React.ReactNode
  modal: React.ReactNode
}) {
  return (
    <html>
      <body>
        {children}
        {modal}
      </body>
    </html>
  )
}
```

### Pattern 6: Streaming with Suspense

```typescript
// app/product/[id]/page.tsx
import { Suspense } from 'react'

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params

  // This data loads first (blocking)
  const product = await getProduct(id)

  return (
    <div>
      {/* Immediate render */}
      <ProductHeader product={product} />

      {/* Stream in reviews */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews productId={id} />
      </Suspense>

      {/* Stream in recommendations */}
      <Suspense fallback={<RecommendationsSkeleton />}>
        <Recommendations productId={id} />
      </Suspense>
    </div>
  )
}

// These components fetch their own data
async function Reviews({ productId }: { productId: string }) {
  const reviews = await getReviews(productId) // Slow API
  return <ReviewList reviews={reviews} />
}

async function Recommendations({ productId }: { productId: string }) {
  const products = await getRecommendations(productId) // ML-based, slow
  return <ProductCarousel products={products} />
}
```

### Pattern 7: Route Handlers (API Routes)

```typescript
// app/api/products/route.ts
import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams
  const category = searchParams.get('category')

  const products = await db.product.findMany({
    where: category ? { category } : undefined,
    take: 20,
  })

  return NextResponse.json(products)
}

export async function POST(request: NextRequest) {
  const body = await request.json()

  const product = await db.product.create({
    data: body,
  })

  return NextResponse.json(product, { status: 201 })
}

// app/api/products/[id]/route.ts
export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params
  const product = await db.product.findUnique({ where: { id } })

  if (!product) {
    return NextResponse.json(
      { error: 'Product not found' },
      { status: 404 }
    )
  }

  return NextResponse.json(product)
}
```

### Pattern 8: Metadata and SEO

```typescript
// app/products/[slug]/page.tsx
import { Metadata } from 'next'
import { notFound } from 'next/navigation'

type Props = {
  params: Promise<{ slug: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params
  const product = await getProduct(slug)

  if (!product) return {}

  return {
    title: product.name,
    description: product.description,
    openGraph: {
      title: product.name,
      description: product.description,
      images: [{ url: product.image, width: 1200, height: 630 }],
    },
    twitter: {
      card: 'summary_large_image',
      title: product.name,
      description: product.description,
      images: [product.image],
    },
  }
}

export async function generateStaticParams() {
  const products = await db.product.findMany({ select: { slug: true } })
  return products.map((p) => ({ slug: p.slug }))
}

export default async function ProductPage({ params }: Props) {
  const { slug } = await params
  const product = await getProduct(slug)

  if (!product) notFound()

  return <ProductDetail product={product} />
}
```

## Caching Strategies

### Data Cache

```typescript
// No cache (always fresh)
fetch(url, { cache: 'no-store' })

// Cache forever (static)
fetch(url, { cache: 'force-cache' })

// ISR - revalidate after 60 seconds
fetch(url, { next: { revalidate: 60 } })

// Tag-based invalidation
fetch(url, { next: { tags: ['products'] } })

// Invalidate via Server Action
'use server'
import { revalidateTag, revalidatePath } from 'next/cache'

export async function updateProduct(id: string, data: ProductData) {
  await db.product.update({ where: { id }, data })
  revalidateTag('products')
  revalidatePath('/products')
}
```

## Boas Práticas

### Recomendações
- **Comece com Componentes de Servidor** - Adicione 'use client' somente quando necessário
- **Localize a busca de dados** - Busque os dados onde eles são usados
- **Use limites de Suspense** - Habilite o streaming para dados lentos
- **Aproveite rotas paralelas** - Estados de carregamento independentes
- **Use Ações de Servidor** - Para mutações com aprimoramento progressivo

### O que NÃO fazer
- **Não passe dados serializáveis** - Limitações de limite Servidor → Cliente
- **Não use hooks em Componentes de Servidor** - Sem useState, useEffect
- **Não busque dados em Componentes de Cliente** - Use Componentes de Servidor ou React Query
- **Não aninhe layouts em excesso** - Cada layout adiciona à árvore de componentes
- **Não ignore estados de carregamento** - Sempre forneça loading.tsx ou Suspense

## Recursos

- [Next.js App Router] Documentação](https://nextjs.org/docs/app)
- [RFC de Componentes de Servidor](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md)
- [Templates Vercel](https://vercel.com/templates/next.js)