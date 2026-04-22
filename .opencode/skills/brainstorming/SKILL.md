---
nome: brainstorming
descrição: Protocolo de questionamento socrático + comunicação com o usuário. OBRIGATÓRIO para solicitações complexas, novas funcionalidades ou requisitos pouco claros. Inclui reporte de progresso e tratamento de erros.
ferramentas-permitidas: Ler, Glob, Grep
---

# Protocolo de Brainstorming & Comunicação

> **OBRIGATÓRIO:** Usar para solicitações complexas/vagas, novas funcionalidades e atualizações.

---

## 🛑 PORTÃO SOCRÁTICO (APLICAÇÃO OBRIGATÓRIA)

### Quando Acionar

| Padrão | Ação |
|--------|------|
| "Build/Create/Make [algo]" sem detalhes | 🛑 FAZER 3 PERGUNTAS |
| Funcionalidade ou arquitetura complexa | 🛑 Esclarecer antes de implementar |
| Pedido de atualização/mudança | 🛑 Confirmar escopo |
| Requisitos vagos | 🛑 Perguntar propósito, usuários, restrições |

### 🚫 OBRIGATÓRIO: 3 Perguntas Antes de Implementar

1. **PARE** — NÃO comece a codar  
2. **PERGUNTE** — Mínimo de 3 perguntas:
   - 🎯 **Propósito**: Qual problema você está resolvendo?
   - 👥 **Usuários**: Quem vai usar isso?
   - 📦 **Escopo**: O que é essencial vs. opcional?
3. **AGUARDE** — Obtenha a resposta antes de prosseguir

---

## 🧠 Geração Dinâmica de Perguntas

**⛔ NUNCA use templates estáticos.** Leia `questionamento_dinâmico.md` para os princípios.

### Princípios Centrais

| Princípio | Significado |
|-----------|-------------|
| **Perguntas Revelam Consequências** | Cada pergunta conecta-se a uma decisão arquitetural |
| **Contexto Antes do Conteúdo** | Entenda se é greenfield/feature/refactor/debug primeiro |
| **Perguntas Minimamente Viáveis** | Cada pergunta deve eliminar caminhos de implementação |
| **Gerar Dados, Não Suposições** | Não adivinhe — pergunte com trade-offs |

### Processo de Geração de Perguntas

```

1. Interpretar o pedido → Extrair domínio, funcionalidades, indicadores de escala
2. Identificar pontos de decisão → Bloqueantes vs. adiáveis
3. Gerar perguntas → Prioridade: P0 (bloqueante) > P1 (alto impacto) > P2 (opcional)
4. Formatar com trade-offs → O quê, Por quê, Opções, Padrão

````

### Formato da Pergunta (OBRIGATÓRIO)

```markdown
### [PRIORIDADE] **[PONTO DE DECISÃO]**

**Pergunta:** [Pergunta clara]

**Por que isso importa:**
- [Consequência arquitetural]
- [Impacta: custo/complexidade/prazo/escala]

**Opções:**
| Opção | Prós | Contras | Melhor Para |
|------|------|---------|-------------|
| A | [+] | [-] | [Caso de uso] |

**Se não especificado:** [Padrão + justificativa]
````

**Para bancos de perguntas e algoritmos específicos por domínio**, veja: `questionamento_dinâmico.md`

---

## Relato de Progresso (BASEADO EM PRINCÍPIOS)

**PRINCÍPIO:** Transparência gera confiança. O status deve ser visível e acionável.

### Formato do Quadro de Status

| Agente           | Status  | Tarefa Atual          | Progresso       |
| ---------------- | ------- | --------------------- | --------------- |
| [Nome do Agente] | ✅🔄⏳❌⚠️ | [Descrição da tarefa] | [% ou contagem] |

### Ícones de Status

| Ícone | Significado | Uso                               |
| ----- | ----------- | --------------------------------- |
| ✅     | Concluído   | Tarefa finalizada com sucesso     |
| 🔄    | Em execução | Executando no momento             |
| ⏳     | Aguardando  | Bloqueado, aguardando dependência |
| ❌     | Erro        | Falhou, requer atenção            |
| ⚠️    | Aviso       | Possível problema, não bloqueante |

---

## Tratamento de Erros (BASEADO EM PRINCÍPIOS)

**PRINCÍPIO:** Erros são oportunidades para comunicação clara.

### Padrão de Resposta a Erros

```
1. Reconhecer o erro
2. Explicar o que aconteceu (linguagem amigável)
3. Oferecer soluções específicas com trade-offs
4. Pedir que o usuário escolha ou forneça alternativa
```

### Categorias de Erro

| Categoria               | Estratégia de Resposta                           |
| ----------------------- | ------------------------------------------------ |
| **Conflito de Porta**   | Oferecer porta alternativa ou fechar a existente |
| **Dependência Ausente** | Auto-instalar ou pedir permissão                 |
| **Falha de Build**      | Mostrar erro específico + correção sugerida      |
| **Erro Incerto**        | Pedir detalhes: screenshot, saída do console     |

---

## Mensagem de Conclusão (BASEADA EM PRINCÍPIOS)

**PRINCÍPIO:** Celebrar o sucesso e guiar os próximos passos.

### Estrutura de Conclusão

```
1. Confirmação de sucesso (celebração breve)
2. Resumo do que foi feito (concreto)
3. Como verificar/testar (acionável)
4. Sugestão de próximos passos (proativa)
```

---

## Princípios de Comunicação

| Princípio        | Implementação                                   |
| ---------------- | ----------------------------------------------- |
| **Conciso**      | Sem detalhes desnecessários; vá direto ao ponto |
| **Visual**       | Use emojis (✅🔄⏳❌) para leitura rápida          |
| **Específico**   | “~2 minutos”, não “aguarde um pouco”            |
| **Alternativas** | Ofereça múltiplos caminhos quando travar        |
| **Proativo**     | Sugira o próximo passo após concluir            |

---

## Anti-Padrões (EVITAR)

| Anti-Padrão                        | Por quê                             |
| ---------------------------------- | ----------------------------------- |
| Ir direto à solução sem entender   | Desperdiça tempo no problema errado |
| Assumir requisitos sem perguntar   | Gera resultado incorreto            |
| Superengenharia na primeira versão | Atraso na entrega de valor          |
| Ignorar restrições                 | Cria soluções inutilizáveis         |
| Frases “eu acho”                   | Incerteza → Pergunte em vez disso   |

---

```
```
