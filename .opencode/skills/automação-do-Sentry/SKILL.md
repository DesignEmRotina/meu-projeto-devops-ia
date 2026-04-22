--- 
name: automação-do-Sentry
description: "Automatize tarefas do Sentry via Rube MCP (Composio): gerencie problemas/eventos, configure alertas, acompanhe versões, monitore projetos e equipes. Sempre pesquise primeiro as ferramentas para encontrar os esquemas atuais."
risk: crítico
source: comunidade
date_add: "27/02/2026"
---

# Automação do Sentry via Rube MCP

Automatize o rastreamento de erros e as operações de monitoramento do Sentry por meio do kit de ferramentas Sentry da Composio via Rube MCP.

## Pré-requisitos

- O Rube MCP deve estar conectado (RUBE_SEARCH_TOOLS disponível)
- Conexão ativa com o Sentry via `RUBE_MANAGE_CONNECTIONS` com o toolkit `sentry`
- Sempre chame `RUBE_SEARCH_TOOLS` primeiro para obter os esquemas de ferramentas atuais

## Configuração

**Obtenha o Rube MCP**: Adicione `https://rube.app/mcp` como um servidor MCP na configuração do seu cliente. Não são necessárias chaves de API — basta adicionar o endpoint e funcionará.

1. Verifique se o Rube MCP está disponível confirmando se `RUBE_SEARCH_TOOLS` responde.
2. Chame `RUBE_MANAGE_CONNECTIONS` com o toolkit `sentry`.
3. Se a conexão não estiver ATIVA, siga o link de autenticação retornado para concluir o OAuth do Sentry.
4. Confirme se o status da conexão está ATIVO antes de executar qualquer fluxo de trabalho.

## Fluxos de Trabalho Principais

### 1. Investigar Problemas

**Quando usar**: O usuário deseja encontrar, inspecionar ou priorizar problemas de erro.

**Sequência de ferramentas**:
1. `SENTRY_LIST_AN_ORGANIZATIONS_ISSUES` - Lista os problemas em toda a organização [Obrigatório]
2. `SENTRY_GET_ORGANIZATION_ISSUE_DETAILS` - Obtém informações detalhadas sobre um problema específico [Opcional]
3. `SENTRY_LIST_AN_ISSUES_EVENTS` - Exibe eventos de erro individuais para um problema [Opcional]
4. `SENTRY_RETRIEVE_AN_ISSUE_EVENT` - Obter detalhes completos do evento com rastreamento de pilha [Opcional]
5. `SENTRY_RETRIEVE_ISSUE_TAG_DETAILS` - Inspecionar a distribuição de tags para um problema [Opcional]

**Parâmetros principais**:
- `organization_id_or_slug`: Identificador da organização
- `issue_id`: ID numérico do problema
- `query`: Consulta de pesquisa (por exemplo, `is:unresolved`, `assigned:me`, `browser:Chrome`)
- `sort`: Ordem de classificação (`date`, `new`, `freq`, `priority`)
- `statsPeriod`: Janela de tempo para estatísticas (`24h`, `14d`, etc.)

**Armadilhas**:
- `organization_id_or_slug` é o slug da organização (por exemplo, 'my-org'), não o nome de exibição nome
- Os IDs de problema são numéricos; não os confunda com os IDs de evento, que são UUIDs.
- A sintaxe de consulta usa o formato de pesquisa do Sentry: `is:unresolved`, `assigned:me`, `!has:release`
- Os eventos dentro de um problema podem ter rastreamentos de pilha diferentes; Inspecione eventos individuais para obter detalhes

### 2. Gerenciar Problemas do Projeto

**Quando usar**: O usuário deseja visualizar problemas específicos de um projeto

**Sequência de ferramentas**:
1. `SENTRY_RETRIEVE_ORGANIZATION_PROJECTS` - Listar projetos para encontrar o slug do projeto [Pré-requisito]
2. `SENTRY_RETRIEVE_PROJECT_ISSUES_LIST` - Listar problemas de um projeto específico [Obrigatório]
3. `SENTRY_RETRIEVE_ISSUE_EVENTS_BY_ID` - Obter eventos de um problema específico [Opcional]

**Parâmetros principais**:
- `organization_id_or_slug`: Identificador da organização
- `project_id_or_slug`: Identificador do projeto
- `query`: String de filtro de pesquisa
- `statsPeriod`: Período de estatísticas

**Armadilhas**:
- Os slugs dos projetos são diferentes dos nomes de exibição dos projetos
- Sempre resolva os nomes dos projetos para slugs via RETRIEVE_ORGANIZATION_PROJECTS primeiro
- Listas de problemas com escopo de projeto podem ter paginação diferente de listas com escopo de organização

### 3. Configurar Regras de Alerta

**Quando usar**: O usuário deseja criar ou gerenciar regras de alerta para um projeto

**Sequência de ferramentas**:
1. `SENTRY_RETRIEVE_ORGANIZATION_PROJECTS` - Encontrar o projeto para o alerta [Pré-requisito]
2. `SENTRY_RETRIEVE_PROJECT_RULES_BY_ORG_AND_PROJECT_ID` - Listar as regras existentes [Opcional]
3. `SENTRY_CREATE_PROJECT_RULE_FOR_ALERTS` - Criar uma nova regra de alerta [Obrigatório]
4. `SENTRY_CREATE_ORGANIZATION_ALERT_RULE` - Criar um alerta de métrica em nível de organização [Alternativo]
5. `SENTRY_UPDATE_ORGANIZATION_ALERT_RULES` - Atualizar regras de alerta existentes [Opcional]
6. `SENTRY_RETRIEVE_ALERT_RULE_DETAILS` - Inspecionar regra de alerta específica [Opcional]
7. `SENTRY_GET_PROJECT_RULE_DETAILS` - Obter detalhes da regra em nível de projeto [Opcional]

**Parâmetros principais**:
- `name`: Nome da regra de alerta
- `conditions`: Matriz de condições de acionamento
- `actions`: Matriz de ações a serem executadas quando acionadas
- `filters`: Matriz de filtros de eventos
- `frequency`: Frequência de acionamento (em minutos)
- `actionMatch`: 'all', 'any' ou 'none' para correspondência de condição

**Armadilhas**:
- Regras em nível de projeto (CREATE_PROJECT_RULE) e alertas de métricas em nível de organização (CREATE_ORGANIZATION_ALERT_RULE) são diferentes
- Condições, ações e filtros usam esquemas JSON específicos; Consulte a documentação do Sentry para os tipos válidos.
- `frequency` está em minutos; definir um valor muito baixo causa fadiga de alertas.
- Os valores padrão de `actionMatch` podem variar; defina-os explicitamente para evitar comportamentos inesperados.

### 4. Gerenciar Versões

**Quando usar**: O usuário deseja criar, rastrear ou gerenciar versões de lançamento

**Sequência de ferramentas**:
1. `SENTRY_LIST_ORGANIZATION_RELEASES` - Listar versões existentes [Opcional]
2. `SENTRY_CREATE_RELEASE_FOR_ORGANIZATION` - Criar uma nova versão [Obrigatório]
3. `SENTRY_UPDATE_RELEASE_DETAILS_FOR_ORGANIZATION` - Atualizar metadados da versão [Opcional]
4. `SENTRY_CREATE_RELEASE_DEPLOY_FOR_ORG` - Registrar uma implantação para uma versão [Opcional]
5. `SENTRY_UPLOAD_RELEASE_FILE_TO_ORGANIZATION` - Carregar mapas de origem ou arquivos [Opcional]

**Parâmetros principais**:
- `version`: String da versão de lançamento (ex.: '1.0.0', commit) SHA)
- `projects`: Array de slugs de projeto aos quais esta versão pertence
- `dateReleased`: Timestamp da versão (ISO 8601)
- `environment`: Nome do ambiente de implantação (por exemplo, 'produção', 'staging')

**Armadilhas**:
- As versões de lançamento devem ser únicas dentro de uma organização
- Os lançamentos podem abranger vários projetos; use o array `projects`
- Implantar uma versão é diferente de criá-la; Use CREATE_RELEASE_DEPLOY
- Os uploads de mapas de origem exigem que a versão exista primeiro

### 5. Monitorar Organização e Equipes

**Quando usar**: O usuário deseja visualizar a estrutura da organização, as equipes ou as listas de membros

**Sequência de ferramentas**:
1. `SENTRY_GET_ORGANIZATION_DETAILS` ou `SENTRY_GET_ORGANIZATION_BY_ID_OR_SLUG` - Obter informações da organização [Obrigatório]
2. `SENTRY_LIST_TEAMS_IN_ORGANIZATION` - Listar todas as equipes [Opcional]
3. `SENTRY_LIST_ORGANIZATION_MEMBERS` - Listar os membros da organização [Opcional]
4. `SENTRY_GET_PROJECT_LIST` - Listar todos os projetos acessíveis [Opcional]

**Parâmetros principais**:
- `organization_id_or_slug`: Identificador da organização
- `cursor`: Cursor de paginação para resultados extensos Configurações

**Armadilhas**:
- Os slugs da organização são identificadores seguros para URLs, não nomes de exibição
- As listas de membros podem ser paginadas; siga a paginação do cursor
- A visibilidade da equipe e dos membros depende das permissões do usuário autenticado

### 6. Gerenciar Monitores (Monitoramento Cron)

**Quando usar**: O usuário deseja atualizar a configuração de monitoramento de tarefas cron

**Sequência de ferramentas**:
1. `SENTRY_UPDATE_A_MONITOR` - Atualizar a configuração do monitor [Obrigatório]

**Parâmetros principais**:
- `organization_id_or_slug`: Identificador da organização
- `monitor_id_or_slug`: Identificador do monitor
- `name`: Nome de exibição do monitor
- `schedule`: Expressão ou intervalo de agendamento cron
- `checkin_margin`: Período de tolerância em minutos para check-ins atrasados
- `max_runtime`: Tempo máximo de execução esperado em minutos

**Armadilhas**:
- Os slugs do monitor são gerados automaticamente a partir do nome; Use o slug para chamadas de API
- As alterações de agendamento entram em vigor imediatamente
- A ausência de check-ins aciona alertas após o período de margem

## Padrões Comuns

### Resolução de ID

**Nome da organização -> Slug**:
```
1. Chame SENTRY_GET_ORGANIZATION_DETAILS
2. Extraia o campo slug da resposta
```

**Nome do projeto -> Slug**:
```
1. Chame SENTRY_RETRIEVE_ORGANIZATION_PROJECTS
2. Encontre o projeto pelo nome e extraia o slug
```

### Paginação

- O Sentry usa paginação baseada em cursor com cabeçalhos `Link`
- Verifique a resposta em busca de valores de cursor
- Passe o cursor na próxima solicitação até que não haja mais páginas

### Sintaxe da Consulta de Busca

- `is:unresolved` - Problemas não resolvidos
- `is:resolved` - Problemas resolvidos
- `assigned:me` - Atribuído ao usuário atual
- `assigned:team-slug` - Atribuído a uma equipe
- `!has:release` - Problemas sem lançamento
- `first-release:1.0.0` - Problemas vistos pela primeira vez no lançamento
- `times-seen:>100` - Visto mais de 100 vezes
- `browser:Chrome` - Filtrar por tag do navegador

## Problemas Conhecidos

**Formatos de ID**:
- Organização: use o slug (ex.: 'minha-org'), não o nome de exibição
- Projeto: use o slug (ex.: 'meu-projeto'), não o nome de exibição
- IDs de problemas: números inteiros
- IDs de eventos: UUIDs (strings hexadecimais de 32 caracteres)

**Permissões**:
- Os escopos dos tokens da API devem corresponder às operações que estão sendo realizadas
- Operações em nível de organização exigem permissões em nível de organização
- Operações em nível de projeto exigem acesso ao projeto

**Limites de Taxa**:
- O Sentry impõe limites de taxa por organização
- Implemente um mecanismo de espera para respostas 429
- Operações em lote devem ser realizadas de forma escalonada

## Referência Rápida

| Tarefa | Slug da Ferramenta | Parâmetros Principais |

|------|-----------|------------|

| Listar problemas da organização | SENTRY_LIST_AN_ORGANIZATIONS_ISSUES | organization_id_or_slug, query | | Obter detalhes da issue | SENTRY_GET_ORGANIZATION_ISSUE_DETAILS | organization_id_or_slug, issue_id |

| Listar eventos da issue | SENTRY_LIST_AN_ISSUES_EVENTS | issue_id |

| Obter detalhes do evento | SENTRY_RETRIEVE_AN_ISSUE_EVENT | organization_id_or_slug, event_id |

| Listar issues do projeto | SENTRY_RETRIEVE_PROJECT_ISSUES_LIST | organization_id_or_slug, project_id_or_slug |

| Listar projetos | SENTRY_RETRIEVE_ORGANIZATION_PROJECTS | organization_id_or_slug |

| Obter detalhes da organização | SENTRY_GET_ORGANIZATION_DETAILS | organization_id_or_slug |

| Listar equipes | SENTRY_LIST_TEAMS_IN_ORGANIZATION | id_ou_slug_da_organização |
| Listar membros | SENTRY_LIST_ORGANIZATION_MEMBERS | id_ou_slug_da_organização |
| Criar regra de alerta | SENTRY_CREATE_PROJECT_RULE_FOR_ALERTS | id_ou_slug_da_organização, id_ou_slug_do_projeto |
| Criar alerta de métrica | SENTRY_CREATE_ORGANIZATION_ALERT_RULE | id_ou_slug_da_organização |
| Criar release | SENTRY_CREATE_RELEASE_FOR_ORGANIZATION | id_ou_slug_da_organização, versão |
| Implantar release | SENTRY_CREATE_RELEASE_DEPLOY_FOR_ORG | id_ou_slug_da_organização, versão |
| Listar releases | SENTRY_LIST_ORGANIZATION_RELEASES | id_ou_slug_da_organização |
| Atualizar monitor | SENTRY_UPDATE_A_MONITOR | organization_id_or_slug, monitor_id_or_slug |

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.

