# Princípios de Rate Limiting

> Proteja sua API contra abuso e sobrecarga.

---

## Por que usar Rate Limiting

```

Protege contra:
├── Ataques de força bruta
├── Exaustão de recursos
├── Custos excessivos (em modelos pay-per-use)
└── Uso injusto da API

```

---

## Seleção de Estratégia

| Tipo | Como Funciona | Quando Usar |
|-----|---------------|-------------|
| **Token bucket** | Permite picos (burst), reabastece ao longo do tempo | Maioria das APIs |
| **Sliding window** | Distribuição suave das requisições | Limites mais rigorosos |
| **Fixed window** | Contador simples por janela de tempo | Necessidades básicas |

---

## Headers de Resposta

```

Incluir nos headers:
├── X-RateLimit-Limit (máximo de requisições)
├── X-RateLimit-Remaining (requisições restantes)
├── X-RateLimit-Reset (quando o limite será resetado)
└── Retornar HTTP 429 quando o limite for excedido

```

---

## Boas Práticas

- Aplicar limites diferentes por tipo de usuário (anon, auth, admin)
- Combinar rate limiting com autenticação
- Monitorar métricas e ajustar limites
- Usar cache distribuído (Redis) para ambientes escaláveis
- Logar eventos de rate limit excedido
```
