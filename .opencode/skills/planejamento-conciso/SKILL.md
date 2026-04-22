--- 
name: planejamento-conciso
description: "Use quando um usuário solicitar um plano para uma tarefa de programação, para gerar uma lista de verificação clara, acionável e atômica."
risk: desconhecido
source: comunidade
date_added: "27/02/2026"
---

# Planejamento Conciso

## Objetivo

Transformar uma solicitação do usuário em um **plano único e acionável** com etapas atômicas.

## Fluxo de Trabalho

### 1. Analisar o Contexto

- Ler o `README.md`, a documentação e os arquivos de código relevantes.

- Identificar restrições (linguagem, frameworks, testes).

### 2. Interação Mínima

- Fazer **no máximo 1 a 2 perguntas** e somente se forem realmente bloqueantes.

- Fazer suposições razoáveis ​​para incógnitas não bloqueantes.

### 3. Gerar Plano

Use a seguinte estrutura:

- **Abordagem**: 1 a 3 frases sobre o quê e porquê.

- **Escopo**: Tópicos com marcadores para "Dentro" e "Fora".

- **Itens de Ação**: Uma lista de 6 a 10 tarefas atômicas e ordenadas (Verbo primeiro).

- **Validação**: Pelo menos um item para teste.

## Modelo de Plano

```markdown
# Plano

<Abordagem de alto nível>

## Escopo

- Entrada:
- Saída:

## Itens de Ação

[ ] <Etapa 1: Descoberta>
[ ] <Etapa 2: Implementação>
[ ] <Etapa 3: Implementação>
[ ] <Etapa 4: Validação/Teste>
[ ] <Etapa 5: Implantação/Confirmação>

## Questões em Aberto

- <Questão 1 (máx. 3)>
```

## Diretrizes da Lista de Verificação

- **Atômico**: Cada etapa deve ser uma única unidade lógica de trabalho.

- **Verbo primeiro**: "Adicionar...", "Refatorar...", "Verificar...".

- **Concreto**: Nomeie arquivos ou módulos específicos sempre que possível.

## Quando Usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.