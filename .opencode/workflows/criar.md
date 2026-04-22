deescrição: Criar comando de nova aplicação. Aciona a skill construtor-de-aplicativo e inicia um diálogo interativo com o usuário.

# /criar – Criar Aplicação

$ARGUMENTS

---

## Tarefa

Este comando inicia um novo processo de criação de aplicação.

### Etapas:

1. **Análise da Solicitação**
   - Entender o que o usuário deseja
   - Se faltarem informações, usar a skill `memória-de-conversação` para perguntar

2. **Planejamento do Projeto**
   - Usar o agente `planejamento-conciso` para divisão de tarefas
   - Definir a stack tecnológica
   - Planejar a estrutura de arquivos
   - Criar o arquivo de planejamento e prosseguir para a construção

3. **Construção da Aplicação (Após Aprovação)**
   - Orquestrar com a skill `construtor-de-aplicativo`
   - Coordenar agentes especialistas:
     - `arquiteto-de-banco-de-dados` → Esquema de banco de dados
     - `especialista-em-backend` → API
     - `especialista-em-frontend` → Interface (UI)

4. **Preview**
   - Iniciar com visualização automática ao concluir
   - Apresentar a URL ao usuário

---

## Exemplos de Uso

```

/criar site de blog
/criar app de e-commerce com listagem de produtos e carrinho
/criar app de tarefas
/criar clone do Instagram
/criar sistema de CRM com gerenciamento de clientes

```

---

## Antes de Começar

Se a solicitação não estiver clara, faça estas perguntas:
- Que tipo de aplicação?
- Quais são as funcionalidades básicas?
- Quem irá utilizá-la?

Use valores padrão e adicione detalhes depois.
```
