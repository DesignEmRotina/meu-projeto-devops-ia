# Princípios do tRPC

> Segurança de tipos de ponta a ponta para monorepos em TypeScript.

---

## Quando Usar

```

✅ Encaixe perfeito:
├── TypeScript no frontend e no backend
├── Estrutura em monorepo
├── Ferramentas internas
├── Desenvolvimento rápido
└── Segurança de tipos é crítica

❌ Mau encaixe:
├── Clientes que não usam TypeScript
├── API pública
├── Necessidade de convenções REST
└── Backends em múltiplas linguagens

```

---

## Principais Benefícios

```

Por que tRPC:
├── Zero manutenção de schema
├── Inferência de tipos de ponta a ponta
├── Autocomplete da IDE em toda a stack
├── Mudanças na API refletidas instantaneamente
└── Nenhuma etapa de geração de código

```

---

## Padrões de Integração

```

Configurações comuns:
├── Next.js + tRPC (mais comum)
├── Monorepo com tipos compartilhados
├── Remix + tRPC
└── Qualquer frontend + backend em TypeScript

```

---

## Boas Práticas

- Use validação de entrada (ex: Zod) mesmo com tipos
- Restrinja acesso com middleware (auth / roles)
- Evite expor tRPC fora do contexto interno
- Combine com caching no client (React Query)
- Documente contratos mesmo sem schema explícito
```

