descrição: Exibir status do projeto e dos agentes. Acompanhamento de progresso e painel de status.
---

# /status - Mostrar Status

$ARGUMENTS

---

## Tarefa

Exibir o status atual do projeto e dos agentes.

### O que é exibido

1. **Informações do Projeto**
   - Nome e caminho do projeto
   - Stack tecnológica
   - Funcionalidades atuais

2. **Painel de Status dos Agentes**
   - Quais agentes estão em execução
   - Quais tarefas foram concluídas
   - Trabalho pendente

3. **Estatísticas de Arquivos**
   - Quantidade de arquivos criados
   - Quantidade de arquivos modificados

4. **Status do Preview**
   - Servidor em execução ou não
   - URL
   - Verificação de saúde

---

## Exemplo de Saída

```

=== Status do Projeto ===

📁 Projeto: my-ecommerce
📂 Caminho: C:/projects/my-ecommerce
🏷️ Tipo: nextjs-ecommerce
📊 Status: ativo

🔧 Stack Tecnológica:
Framework: next.js
Banco de Dados: postgresql
Autenticação: clerk
Pagamento: stripe

✅ Funcionalidades (5):
• product-listing
• cart
• checkout
• user-auth
• order-history

⏳ Pendentes (2):
• admin-panel
• email-notifications

📄 Arquivos: 73 criados, 12 modificados

=== Status dos Agentes ===

✅ arquiteto-de-banco-de-dados → Concluído
✅ ESPECIALISTA_BACKEND_SUBAGENTE     → Concluído
🔄 ESPECIALISTA_FRONTEND_SUBAGENTE    → Componentes do dashboard (60%)
⏳ ARQUITETO_BANCO_DE_DADOS_SUBAGENTE → Aguardando

=== Preview ===

🌐 URL: [http://localhost:3000](http://localhost:3000)
💚 Saúde: OK

```

---

## Técnico

O comando de status utiliza os seguintes scripts:
- `python .opencode/scripts/gerenciador_de_sessões.py status`
- `python .opencode/scripts/visualização_automática.py status`
```
