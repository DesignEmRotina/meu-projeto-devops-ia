# Seleção de Estilo de API (2026)

> REST vs GraphQL vs tRPC — Em qual situação usar cada um?

---

## Árvore de Decisão

```

Quem são os consumidores da API?
│
├── API pública / Múltiplas plataformas
│   └── REST + OpenAPI (maior compatibilidade)
│
├── Necessidades de dados complexas / Múltiplos frontends
│   └── GraphQL (consultas flexíveis)
│
├── Frontend + Backend em TypeScript (monorepo)
│   └── tRPC (type safety ponta a ponta)
│
├── Tempo real / Orientado a eventos
│   └── WebSocket + AsyncAPI
│
└── Microsserviços internos
└── gRPC (performance) ou REST (simplicidade)

```

---

## Comparação

| Fator | REST | GraphQL | tRPC |
|------|------|---------|------|
| **Melhor para** | APIs públicas | Apps complexos | Monorepos em TS |
| **Curva de aprendizado** | Baixa | Média | Baixa (se usar TS) |
| **Over/Under fetching** | Comum | Resolvido | Resolvido |
| **Type safety** | Manual (OpenAPI) | Baseado em schema | Automático |
| **Cache** | Nativo do HTTP | Complexo | Baseado no cliente |

---

## Perguntas para Seleção

Antes de decidir, responda:

1. Quem são os consumidores da API?
2. O frontend é feito em TypeScript?
3. Quão complexos são os relacionamentos de dados?
4. Cache é um fator crítico?
5. A API é pública ou interna?
```
