# Princípios do GraphQL

> Consultas flexíveis para dados complexos e interconectados.

---

## Quando Usar

```

✅ Bom encaixe:
├── Dados complexos e interconectados
├── Múltiplas plataformas de frontend
├── Clientes precisam de consultas flexíveis
├── Requisitos de dados em constante evolução
└── Reduzir over-fetching é importante

❌ Mau encaixe:
├── Operações CRUD simples
├── Uso intenso de upload de arquivos
├── Cache HTTP é importante
└── Equipe sem familiaridade com GraphQL

```

---

## Princípios de Design de Schema

```

Princípios:
├── Pense em grafos, não em endpoints
├── Projete para evoluir (sem versionamento)
├── Use connections para paginação
├── Seja específico nos tipos (evite "data" genérico)
└── Trate nulabilidade com cuidado

```

---

## Considerações de Segurança

```

Proteja-se contra:
├── Ataques de profundidade de query → Defina profundidade máxima
├── Complexidade de query → Calcule custo das consultas
├── Abuso de batching → Limite tamanho do batch
├── Introspecção → Desabilite em produção

```

---

## Boas Práticas Essenciais

- Defina limites claros de profundidade e complexidade
- Monitore queries mais custosas
- Use autenticação e autorização por campo quando necessário
- Evite schemas genéricos e pouco expressivos
- Documente bem o schema para o time de frontend
```

