--- 
name: configurações-teste-ab
description: "Guia estruturado para configurar testes A/B com etapas obrigatórias para hipóteses, métricas e prontidão para execução."
risk: desconhecido
source: comunidade
date_added: "27/02/2026"
---

# Configuração de Teste A/B

## 1️⃣ Objetivo e Escopo

Garantir que cada teste A/B seja **válido, rigoroso e seguro** antes que uma única linha de código seja escrita.

- Impede a "espiada"
- Garante o poder estatístico
- Bloqueia hipóteses inválidas

---

## 2️⃣ Pré-requisitos

Você precisa ter:

- Um problema claro do usuário
- Acesso a uma fonte de análise
- Volume de tráfego estimado aproximadamente

### Lista de verificação da qualidade da hipótese

Uma hipótese válida inclui:

- Observação ou evidência
- Mudança única e específica
- Expectativa direcional
- Público-alvo definido
- Critérios de sucesso mensuráveis

---

### 3️⃣ Bloqueio da hipótese (Controle rígido)

Antes de projetar variantes ou métricas, você DEVE:

- Apresentar a **hipótese final**
- Especificar:

- Público-alvo

- Métrica principal

- Direção esperada do efeito

- Efeito mínimo detectável (EMD)

Pergunte explicitamente:

> “Esta é a hipótese final que estamos adotando para este teste?”

**NÃO prossiga até a confirmação.**

---

### 4️⃣ Pressupostos e Verificação de Validade (Obrigatório)

Liste explicitamente os pressupostos sobre:

- Estabilidade do tráfego
- Independência do usuário
- Confiabilidade das métricas
- Qualidade da randomização
- Fatores externos (sazonalidade, campanhas, lançamentos)

Se os pressupostos forem fracos ou violados:

- Avise o usuário
- Recomende o adiamento ou a reformulação do teste

---

### 5️⃣ Seleção do Tipo de Teste

Escolha o teste válido mais simples:

- **Teste A/B** – alteração única, duas variantes
- **Teste A/B/n** – múltiplas variantes, requer tráfego mais alto
- **Teste Multivariado (MVT)** – efeitos de interação, tráfego muito alto
- **Teste de URL Dividida** – grandes alterações estruturais

Use **Teste A/B** por padrão, a menos que haja um motivo claro para usar outro.

---

### 6️⃣ Definição de Métricas

#### Métrica Primária (Obrigatória)

- Métrica única usada para avaliar o sucesso
- Diretamente ligada à hipótese
- Pré-definida e congelada antes do lançamento

#### Métricas Secundárias

- Fornecem contexto
- Explicam _por que_ os resultados ocorreram
- Não devem substituir a métrica primária

#### Métricas de Segurança

- Métricas que não devem se degradar
- Usadas para evitar resultados negativos prejudiciais
- Acionam a interrupção do teste se forem significativamente negativas

---

### 7️⃣ Tamanho e Duração da Amostra

Defina antecipadamente:

- Taxa de base
- MDE (Erro Médio Diário)
- Nível de significância (normalmente 95%)
- Poder estatístico (normalmente 80%)

Estime:

- Tamanho da amostra necessário por variante
- Duração esperada do teste

**NÃO prossiga sem uma estimativa realista do tamanho da amostra.**

---

### 8️⃣ Etapa de Preparação para Execução (Parada Obrigatória)

Você pode prosseguir para a implementação **somente se todas as seguintes condições forem verdadeiras:**

- A hipótese está definida
- A métrica primária está congelada
- O tamanho da amostra foi calculado
- A duração do teste foi definida
- As salvaguardas foram estabelecidas
- O rastreamento foi verificado

Se algum item estiver faltando, pare e resolva o problema.

---

## Executando o Teste

### Durante o Teste

**FAÇA:**

- Monitore a integridade técnica
- Documente os fatores externos

**NÃO FAÇA:**

- Interrompa o teste prematuramente devido a resultados "aparentemente bons"
- Altere as variantes no meio do teste
- Adicione novas fontes de tráfego
- Redefina os critérios de sucesso

---

## Analisando os Resultados

### Disciplina de Análise

Ao interpretar os resultados:

- NÃO generalize além da população testada
- NÃO afirme causalidade além da mudança testada
- NÃO ignore falhas nos mecanismos de segurança
- Separe a significância estatística do julgamento de negócios

### Resultados da Interpretação

| Resultado | Ação |

| -------------------- | -------------------------------------- |

| Resultado positivo significativo | Considere o lançamento |

| Resultado negativo significativo | Rejeite a variante, documente o aprendizado |

| Resultado inconclusivo | Considere mais tráfego ou uma mudança mais ousada |

| Falha no mecanismo de segurança | Não lance, mesmo que a versão principal seja bem-sucedida |

---

## Documentação e Aprendizado

### Registro de Teste (Obrigatório)

Documentar:

- Hipótese
- Variantes
- Métricas
- Tamanho da amostra vs. alcançado
- Resultados
- Decisão
- Aprendizados
- Ideias para acompanhamento

Armazene os registros em um local compartilhado e pesquisável para evitar falhas repetidas.

---

## Condições de Recusa (Segurança)

Recusar o teste se:

- A taxa de referência for desconhecida e não puder ser estimada
- O tráfego for insuficiente para detectar o MDE (Evento de Detecção de Múltiplas Variáveis)
- A métrica principal não estiver definida
- Múltiplas variáveis ​​forem alteradas sem um planejamento adequado
- A hipótese não puder ser claramente enunciada

Explique o motivo e recomende os próximos passos.

---

## Princípios-chave (Inegociáveis)

- Uma hipótese por teste
- Uma métrica principal
- Comprometa-se antes do lançamento
- Sem espiar
- Aprender em vez de vencer
- Rigor estatístico em primeiro lugar

---

## Lembrete final

O teste A/B não se trata de provar que as ideias estão certas.

Trata-se de **aprender a verdade com confiança**.

Se você sentir a tentação de apressar, simplificar ou “apenas tentar” —
esse é o sinal para **diminuir o ritmo e verificar o planejamento novamente**.

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.