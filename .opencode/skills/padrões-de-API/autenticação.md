# Padrões de Autenticação

> Escolha o padrão de autenticação com base no caso de uso.

---

## Guia de Seleção

| Padrão | Melhor Para |
|-------|-------------|
| **JWT** | Stateless, microsserviços |
| **Sessão** | Web tradicional, simples |
| **OAuth 2.0** | Integração com terceiros |
| **API Keys** | Comunicação servidor-para-servidor, APIs públicas |
| **Passkey** | Autenticação moderna sem senha (2025+) |

---

## Princípios do JWT

```

Importante:
├── Sempre validar a assinatura
├── Verificar expiração
├── Incluir apenas claims mínimos
├── Usar expiração curta + refresh tokens
└── Nunca armazenar dados sensíveis no JWT

```

---

## Boas Práticas de Segurança

- Use HTTPS obrigatoriamente
- Armazene tokens de forma segura (HttpOnly / Secure)
- Revogue tokens comprometidos
- Implemente rotação de chaves
- Monitore tentativas de autenticação suspeitas
```
