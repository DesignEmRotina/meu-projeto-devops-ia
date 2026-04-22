---
descrição: Comando de depuração. Ativa o modo DEBUG para investigação sistemática de problemas.
---
```

# /depurar – Investigação Sistemática de Problemas

$ARGUMENTS

---

## Objetivo

Este comando ativa o modo **DEBUG** para investigação sistemática de issues, erros ou comportamentos inesperados.

---

## Comportamento

Quando `/depurar` é acionado:

1. **Coletar informações**

   * Mensagem de erro
   * Passos para reprodução
   * Comportamento esperado vs. comportamento atual
   * Alterações recentes

2. **Formar hipóteses**

   * Listar possíveis causas
   * Ordenar por probabilidade

3. **Investigar de forma sistemática**

   * Testar cada hipótese
   * Verificar logs e fluxo de dados
   * Usar método de eliminação

4. **Corrigir e prevenir**

   * Aplicar a correção
   * Explicar a causa raiz
   * Adicionar medidas de prevenção

---

## Formato de Saída

````markdown
## 🔍 Debug: [Problema]

### 1. Sintoma
[O que está acontecendo]

### 2. Informações Coletadas
- Erro: `[mensagem de erro]`
- Arquivo: `[caminho do arquivo]`
- Linha: [número da linha]

### 3. Hipóteses
1. ❓ [Causa mais provável]
2. ❓ [Segunda possibilidade]
3. ❓ [Causa menos provável]

### 4. Investigação

**Testando hipótese 1:**
[O que foi verificado] → [Resultado]

**Testando hipótese 2:**
[O que foi verificado] → [Resultado]

### 5. Causa Raiz
🎯 **[Explicação do porquê isso aconteceu]**

### 6. Correção
```[linguagem]
// Antes
[código com problema]

// Depois
[código corrigido]
````

### 7. Prevenção

🛡️ [Como evitar que isso aconteça no futuro]

```

---

## Exemplos

```

/depurar login não funciona
/depurar API retorna 500
/depurar formulário não envia
/depurar dados não estão sendo salvos

```

---

## Princípios-chave

- **Perguntar antes de assumir** – obter o contexto completo do erro  
- **Testar hipóteses** – não chutar aleatoriamente  
- **Explicar o porquê** – não apenas o que corrigir  
- **Evitar recorrência** – adicionar testes, validações
```
