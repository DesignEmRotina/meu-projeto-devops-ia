# Princípios REST

> Design de APIs baseado em recursos — **substantivos, não verbos**.

---

## Regras de Nomeação de Recursos

```

Princípios:
├── Use SUBSTANTIVOS, não verbos (recursos, não ações)
├── Use forma PLURAL (/users em vez de /user)
├── Use letras minúsculas com hífen (/user-profiles)
├── Aninhe para representar relacionamentos (/users/123/posts)
└── Mantenha raso (máx. 3 níveis de profundidade)

```

---

## Seleção de Métodos HTTP

| Método | Finalidade | Idempotente? | Corpo (Body)? |
|-------|------------|--------------|---------------|
| **GET** | Ler recurso(s) | Sim | Não |
| **POST** | Criar novo recurso | Não | Sim |
| **PUT** | Substituir recurso inteiro | Sim | Sim |
| **PATCH** | Atualização parcial | Não | Sim |
| **DELETE** | Remover recurso | Sim | Não |

> **Nota:**  
> *Idempotente* significa que múltiplas requisições idênticas produzem o mesmo resultado.

---

## Seleção de Status Codes HTTP

| Situação | Código | Motivo |
|---------|--------|--------|
| Sucesso (leitura) | 200 | Sucesso padrão |
| Criado | 201 | Novo recurso criado |
| Sem conteúdo | 204 | Sucesso, nada a retornar |
| Requisição inválida | 400 | Request malformado |
| Não autorizado | 401 | Autenticação ausente ou inválida |
| Proibido | 403 | Autenticado, sem permissão |
| Não encontrado | 404 | Recurso inexistente |
| Conflito | 409 | Conflito de estado (ex: duplicado) |
| Erro de validação | 422 | Sintaxe válida, dados inválidos |
| Limite excedido | 429 | Muitas requisições |
| Erro no servidor | 500 | Falha do servidor |

---

## Boas Práticas Essenciais

- Use **status codes corretos** sempre
- Não exponha detalhes internos em erros 5xx
- Prefira **PATCH** para atualizações parciais
- Nunca use verbos em endpoints REST
- Padronize respostas em toda a API
```

