# Princípios de Formato de Resposta

> Consistência é fundamental — escolha um formato e mantenha-o em toda a API.

---

## Padrões Comuns

```

Escolha um:
├── Padrão Envelope ({ success, data, error })
├── Dados Diretos (retornar apenas o recurso)
└── HAL / JSON:API (hipermídia)

```

---

## Resposta de Erro

```

Deve incluir:
├── Código do erro (para tratamento programático)
├── Mensagem para o usuário (exibição)
├── Detalhes (debug, erros por campo)
├── ID da requisição (suporte e rastreabilidade)
└── NÃO incluir detalhes internos (segurança!)

```

> ⚠️ **Importante:**  
> Nunca exponha stack traces, mensagens internas ou dados sensíveis em ambientes públicos.

---

## Tipos de Paginação

| Tipo | Melhor Para | Compromissos (Trade-offs) |
|------|------------|---------------------------|
| **Offset** | Simples, permite pular páginas | Performance ruim em grandes volumes |
| **Cursor** | Grandes volumes de dados | Não permite pular páginas |
| **Keyset** | Performance crítica | Exige chave ordenável |

---

### Perguntas para Seleção

Antes de escolher o tipo de paginação, pergunte:

1. Qual o tamanho do dataset?
2. O usuário precisa pular para páginas específicas?
3. Os dados mudam com frequência?

---

## Boas Práticas Essenciais

- Padronize o formato de resposta em toda a API
- Documente o formato escolhido (OpenAPI/Swagger)
- Retorne erros estruturados e previsíveis
- Use códigos HTTP corretos + payload consistente
- Facilite o debug sem comprometer a segurança
```
