descrição: Brainstorming estruturado para projetos e funcionalidades. Explora múltiplas opções antes da implementação.
---

# /brainstorm – Exploração Estruturada de Ideias

$ARGUMENTS

---

## Objetivo

Este comando ativa o modo **BRAINSTORM** para exploração estruturada de ideias. Use quando precisar analisar opções antes de se comprometer com uma implementação.

---

## Comportamento

Quando `/brainstorm` é acionado:

1. **Entender o objetivo**
   - Qual problema estamos resolvendo?
   - Quem é o usuário?
   - Quais restrições existem?

2. **Gerar opções**
   - Fornecer pelo menos 3 abordagens diferentes
   - Cada uma com prós e contras
   - Considerar soluções não convencionais

3. **Comparar e recomendar**
   - Resumir os trade-offs
   - Dar uma recomendação com justificativa

---

## Formato de Saída

```markdown
## 🧠 Brainstorm: [Tópico]

### Contexto
[Breve descrição do problema]

---

### Opção A: [Nome]
[Descrição]

✅ **Prós:**
- [benefício 1]
- [benefício 2]

❌ **Contras:**
- [desvantagem 1]

📊 **Esforço:** Baixo | Médio | Alto

---

### Opção B: [Nome]
[Descrição]

✅ **Prós:**
- [benefício 1]

❌ **Contras:**
- [desvantagem 1]
- [desvantagem 2]

📊 **Esforço:** Baixo | Médio | Alto

---

### Opção C: [Nome]
[Descrição]

✅ **Prós:**
- [benefício 1]

❌ **Contras:**
- [desvantagem 1]

📊 **Esforço:** Baixo | Médio | Alto

---

## 💡 Recomendação

**Opção [X]** porque [justificativa].

Qual direção você gostaria de explorar?
````

---

## Exemplos

```
/brainstorm sistema de autenticação
/brainstorm gerenciamento de estado para formulário complexo
/brainstorm esquema de banco de dados para app social
/brainstorm estratégia de cache
```

---

## Princípios-Chave

* **Sem código** – isto é sobre ideias, não implementação
* **Visual quando útil** – use diagramas para arquitetura
* **Trade-offs honestos** – não esconda a complexidade
* **Decisão do usuário** – apresente opções e deixe o usuário decidir

