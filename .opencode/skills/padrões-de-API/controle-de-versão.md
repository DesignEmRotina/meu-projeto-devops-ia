# Estratégias de Versionamento

> Planeje a evolução da API desde o primeiro dia.

---

## Fatores de Decisão

| Estratégia | Implementação | Trade-offs |
|-----------|---------------|------------|
| **URI** | /v1/users | Claro, fácil de cachear |
| **Header** | Accept-Version: 1 | URLs mais limpas, descoberta mais difícil |
| **Query** | ?version=1 | Fácil de adicionar, porém desorganizado |
| **Nenhuma** | Evoluir com cuidado | Ideal para APIs internas, arriscado para públicas |

---

## Filosofia de Versionamento

```

Considere:
├── API pública? → Versionar na URI
├── Apenas uso interno? → Pode não precisar de versionamento
├── GraphQL? → Normalmente sem versões (schema evolutivo)
├── tRPC? → Tipos garantem compatibilidade

```

---

## Boas Práticas

- Nunca quebre compatibilidade sem aviso
- Deprecie versões antigas gradualmente
- Documente mudanças e migrações
- Use versionamento semântico quando possível
- Combine versionamento com testes automatizados
