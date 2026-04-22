# Seleção de Stack Tecnológico (2026)

> Tecnologias padrão e alternativas para aplicações web.

## Stack Padrão (Web App — 2026)

```yaml
Frontend:
  framework: Next.js 16 (Estável)
  linguagem: TypeScript 5.7+
  estilização: Tailwind CSS v4
  estado: React 19 Actions / Server Components
  bundler: Turbopack (Estável para Desenvolvimento)

Backend:
  runtime: Node.js 23
  framework: Next.js API Routes / Hono (para Edge)
  validação: Zod / TypeBox

Banco de Dados:
  principal: PostgreSQL
  orm: Prisma / Drizzle
  hospedagem: Supabase / Neon

Autenticação:
  provedor: Auth.js (v5) / Clerk

Monorepo:
  ferramenta: Turborepo 2.0
```

---

## Opções Alternativas

| Necessidade               | Padrão | Alternativa                  |
| ------------------------- | ------ | ---------------------------- |
| Tempo real                | –      | Supabase Realtime, Socket.io |
| Armazenamento de arquivos | –      | Cloudinary, S3               |
| Pagamentos                | Stripe | LemonSqueezy, Paddle         |
| E-mail                    | –      | Resend, SendGrid             |
| Busca                     | –      | Algolia, Typesense           |

---
