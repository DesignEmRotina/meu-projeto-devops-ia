--- 
name: correção-de-testes
description: "Identifique e corrija sistematicamente todos os testes com falha usando estratégias de agrupamento inteligentes. Use quando solicitar explicitamente a correção de testes ("corrija estes testes", "faça os testes passarem"), relatar falhas de teste ("os testes estão falhando", "o conjunto de testes está quebrado") ou concluir a implementação e desejar que os testes passem."
risk: seguro
source: comunidade
date_add: "2026-02-27"
---

# Correção de Testes

Identifique e corrija sistematicamente todos os testes com falha usando estratégias de agrupamento inteligentes.

## Quando usar
- Solicita explicitamente a correção de testes ("corrija estes testes", "faça os testes passarem")
- Relata falhas de teste ("os testes estão falhando", "o conjunto de testes está quebrado")
- Conclui a implementação e deseja que os testes passem
- Menciona falhas de CI/CD devido a testes

## Abordagem Sistemática

### 1. Execução Inicial de Testes

Execute `make test` para identificar todos os testes com falha.

Analise a saída para:

- Número total de falhas
- Tipos e padrões de erros
- Módulos/arquivos afetados

### 2. Agrupamento Inteligente de Erros

Agrupe falhas semelhantes por:

- **Tipo de erro**: ImportError, AttributeError, AssertionError, etc.

- **Módulo/arquivo**: O mesmo arquivo causando múltiplas falhas de teste
- **Causa raiz**: Dependências ausentes, alterações na API, impactos de refatoração

Priorize os grupos por:

- Número de testes afetados (do de maior impacto para o de maior impacto)
- Ordem de dependência (corrija a infraestrutura antes da funcionalidade)

### 3. Processo Sistemático de Correção

Para cada grupo (começando pelo de maior impacto):

1. **Identifique a causa raiz**

- Leia o código relevante

- Verifique as alterações recentes com `git diff`

- Compreenda o padrão do erro

2. **Implemente a correção**

- Use a ferramenta Editar para alterações no código

- Siga as convenções do projeto (consulte CLAUDE.md)

- Faça alterações mínimas e focadas

3. **Verificar correção**

- Execute um subconjunto de testes para este grupo

- Use marcadores pytest ou padrões de arquivo:

``bash

uv run pytest tests/caminho/para/arquivo_de_teste.py -v

uv run pytest -k "padrão" -v

``

- Certifique-se de que o grupo seja aprovado antes de prosseguir

4. **Passar para o próximo grupo**

### 4. Estratégia de ordem de correção

**Infraestrutura primeiro:**

- Erros de importação
- Dependências ausentes
- Problemas de configuração

**Em seguida, alterações na API:**

- Alterações na assinatura da função
- Reorganização do módulo
- Variáveis/funções renomeadas

**Finalmente, problemas de lógica:**

- Falhas de asserção
- Bugs na lógica de negócios
- Tratamento de casos extremos

### 5. Verificação final

Após todos os grupos corrigidos:

- Execute o conjunto completo de testes: `make test`

- Verifique se não há regressões
- Verifique se a cobertura de testes permanece intacta

## Boas práticas

- Corrija um grupo por vez tempo
- Execute testes focados após cada correção
- Use `git diff` para entender as alterações recentes
- Procure padrões nas falhas
- Não passe para o próximo grupo até que o atual seja aprovado
- Mantenha as alterações mínimas e focadas

## Exemplo de Fluxo de Trabalho

Usuário: "Os testes estão falhando após minha refatoração"

1. Execute `make test` → 15 falhas identificadas
2. Agrupe os erros:

- 8 ImportErrors (módulo renomeado)

- 5 AttributeErrors (assinatura da função alterada)

- 2 AssertionErrors (bugs de lógica)
3. Corrija os ImportErrors primeiro → Execute o subconjunto → Verifique
4. Corrija os AttributeErrors → Execute o subconjunto → Verifique
5. Corrija os AssertionErrors → Execute o subconjunto → Verifique
6. Execute o conjunto completo → Todos aprovados ✓