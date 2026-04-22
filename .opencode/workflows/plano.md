descrição: Criar plano de projeto usando o agente PLANEJAMENTO_AGENTE. Nenhuma escrita de código — apenas geração do arquivo de plano.
---

# /plano - Modo de Planejamento de Projeto

$ARGUMENTS

---

## 🔴 REGRAS CRÍTICAS

1. **NENHUMA ESCRITA DE CÓDIGO** – Este comando cria apenas o arquivo de plano
2. **Usar o agente PLANEJAMENTO_AGENTE** – usar o modo de Planejamento nativo do Agente
3. **Portão Socrático** – Fazer perguntas de esclarecimento antes do planejamento
4. **Nomeação Dinâmica** – O arquivo de plano deve ser nomeado com base na tarefa

---

## Tarefa

Usar o agente `PLANEJAMENTO_AGENTE` com o seguinte contexto:

```

CONTEXTO:

* Pedido do Usuário: $ARGUMENTS
* Modo: SOMENTE PLANEJAMENTO (sem código)
* Saída: docs/interno/PLAN-{task-slug}.md (nomeação dinâmica)

REGRAS DE NOMEAÇÃO:

1. Extrair 2–3 palavras-chave do pedido
2. Minúsculas, separadas por hífen
3. Máximo de 30 caracteres
4. Exemplo: "e-commerce cart" → PLAN-ecommerce-cart.md

REGRAS:

1. Seguir planejador-de-projeto.md Fase -1 (Verificação de Contexto)
2. Seguir planejador-de-projeto.md Fase 0 (Portão Socrático)
3. Criar PLAN-{slug}.md com a quebra de tarefas
4. NÃO escrever nenhum arquivo de código
5. REPORTAR o nome exato do arquivo criado

```

---

## Saída Esperada

| Entregável | Local |
|------------|-------|
| Plano do Projeto | `docs/PLAN-{task-slug}.md` |
| Quebra de Tarefas | Dentro do arquivo de plano |
| Atribuição de Agentes | Dentro do arquivo de plano |
| Checklist de Verificação | Fase X dentro do arquivo de plano |

---

## Após o Planejamento

Informar ao usuário:
```

[OK] Plano criado: docs/interno/PLAN-{slug}.md

Próximos passos:

* Revisar o plano
* Executar `/criar` para iniciar a implementação
* Ou modificar o plano manualmente

```

---

## Exemplos de Nomeação

| Pedido | Arquivo de Plano |
|-------|------------------|
| `/plano site de e-commerce com carrinho` | `docs/interno/PLAN-ecommerce-cart.md`         |
| `/plano aplicativo móvel para fitness`   | `docs/interno/PLAN-fitness-app.md`            |
| `/plano adicionar recurso de modo escuro`| `docs/interno/PLAN-dark-mode.md`              |
| `/plano corrigir bug de autenticação`    | `docs/interno/PLAN-auth-fix.md`               |
| `/plano Painel de controle SaaS`         | `docs/interno/PLAN-saas-dashboard.md`         |

---

## Uso

```

/plano site de e-commerce com carrinho
/plano aplicativo móvel para monitoramento de atividades físicas
/plano painel de controle SaaS com análises

```