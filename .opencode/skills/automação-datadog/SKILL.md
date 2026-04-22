--- 
name: automação-datadog
description: "Automatize tarefas do Datadog via Rube MCP (Composio): consulte métricas, pesquise logs, gerencie monitores/painéis, crie eventos e tempos de inatividade. Sempre pesquise primeiro as ferramentas para os esquemas atuais."
risk: crítico
source: comunidade
date_add: "27/02/2026"
---

# Automação do Datadog via Rube MCP

Automatize as operações de monitoramento e observabilidade do Datadog por meio do conjunto de ferramentas Datadog da Composio via Rube MCP.

## Pré-requisitos

- O Rube MCP deve estar conectado (RUBE_SEARCH_TOOLS disponível)
- Conexão ativa com o Datadog via `RUBE_MANAGE_CONNECTIONS` com o toolkit `datadog`
- Sempre chame `RUBE_SEARCH_TOOLS` primeiro para obter os esquemas de ferramentas atuais

## Configuração

**Obtenha o Rube MCP**: Adicione `https://rube.app/mcp` como um servidor MCP na configuração do seu cliente. Não são necessárias chaves de API — basta adicionar o endpoint e funcionará.

1. Verifique se o Rube MCP está disponível confirmando se `RUBE_SEARCH_TOOLS` responde.
2. Chame `RUBE_MANAGE_CONNECTIONS` com o toolkit `datadog`.
3. Se a conexão não estiver ATIVA, siga o link de autenticação retornado para concluir a autenticação do Datadog.
4. Confirme se o status da conexão está ATIVO antes de executar qualquer fluxo de trabalho.

## Fluxos de Trabalho Principais

### 1. Consultar e Explorar Métricas

**Quando usar**: O usuário deseja consultar dados de métricas ou listar as métricas disponíveis.

**Sequência de ferramentas**:
1. `DATADOG_LIST_METRICS` - Lista os nomes das métricas disponíveis [Opcional]
2. `DATADOG_QUERY_METRICS` - Consulta dados de séries temporais de métricas [Obrigatório]

**Parâmetros principais**:
- `query`: String de consulta de métricas do Datadog (por exemplo, `avg:system.cpu.user{host:web01}`)
- `from`: Timestamp inicial (Unix) (em segundos da época Unix)
- `to`: Timestamp final (em segundos da época Unix)
- `q`: String de busca para listar métricas

**Armadilhas**:
- A sintaxe da consulta segue o formato de consulta de métricas do Datadog: `aggregation:metric_name{tag_filters}`
- `from` e `to` são timestamps da época Unix em segundos, não em milissegundos
- Agregações válidas: `avg`, `sum`, `min`, `max`, `count`
- Os filtros de tags usam chaves: `{host:web01,env:prod}`
- O intervalo de tempo não deve exceder os limites de retenção do Datadog para o tipo de métrica

### 2. Pesquisar e Analisar Logs

**Quando usar**: O usuário deseja pesquisar entradas de log ou listar índices de log

**Sequência de ferramentas**:
1. `DATADOG_LIST_LOG_INDEXES` - Lista os índices de log disponíveis [Opcional]
2. `DATADOG_SEARCH_LOGS` - Pesquisar logs com consulta e filtros [Obrigatório]

**Parâmetros principais**:
- `query`: Consulta de pesquisa de logs usando a sintaxe de consulta de logs do Datadog
- `from`: Hora de início (ISO 8601 ou timestamp Unix)
- `to`: Hora de término (ISO 8601 ou timestamp Unix)
- `sort`: Ordem de classificação ('asc' ou 'desc')
- `limit`: Número de entradas de log a serem retornadas

**Armadilhas**:
- As consultas de log usam a sintaxe de pesquisa de logs do Datadog: `service:web status:error`
- A pesquisa é limitada aos logs retidos dentro do período de retenção configurado
- Grandes conjuntos de resultados exigem paginação; verifique os tokens de cursor/página
- Os índices de log controlam o roteamento e a retenção; Filtrar por índice, se conhecido

### 3. Gerenciar Monitores

**Quando usar**: O usuário deseja criar, atualizar, silenciar ou inspecionar monitores

**Sequência de ferramentas**:
1. `DATADOG_LIST_MONITORS` - Lista todos os monitores com filtros [Obrigatório]
2. `DATADOG_GET_MONITOR` - Obtém detalhes específicos do monitor [Opcional]
3. `DATADOG_CREATE_MONITOR` - Cria um novo monitor [Opcional]
4. `DATADOG_UPDATE_MONITOR` - Atualiza a configuração do monitor [Opcional]
5. `DATADOG_MUTE_MONITOR` - Silencia um monitor temporariamente [Opcional]
6. `DATADOG_UNMUTE_MONITOR` - Reativa um monitor silenciado [Opcional]

**Parâmetros principais**:
- `monitor_id`: ID numérico do monitor
- `name`: Nome de exibição do monitor
- `type`: Tipo de monitor ('alerta de métrica', (por exemplo, 'verificação de serviço', 'alerta de log', 'alerta de consulta', etc.)
- `query`: Consulta do monitor que define a condição do alerta
- `message`: Mensagem de notificação com @menções
- `tags`: Array de strings de tags
- `thresholds`: Valores de limite de alerta (`crítico`, `aviso`, `ok`)

**Armadilhas**:
- O `type` do monitor deve corresponder ao tipo da consulta; incompatibilidades causam falhas na criação
- `message` aceita @menções para notificações (por exemplo, `@slack-channel`, `@pagerduty`)
- Os limites variam de acordo com o tipo do monitor; monitores de métricas precisam de `crítico` no mínimo
- Silenciar um monitor suprime as notificações, mas o monitor ainda é avaliado
- Os IDs dos monitores são números inteiros

### 4. Gerenciar Painéis

**Quando usar**: O usuário deseja listar, visualizar, atualizar ou excluir painéis

**Sequência de ferramentas**:
1. `DATADOG_LIST_DASHBOARDS` - Lista todos os painéis [Obrigatório]
2. `DATADOG_GET_DASHBOARD` - Obtém a definição completa do painel [Opcional]
3. `DATADOG_UPDATE_DASHBOARD` - Atualiza o layout ou os widgets do painel [Opcional]
4. `DATADOG_DELETE_DASHBOARD` - Remove um painel (irreversível) [Opcional]

**Parâmetros principais**:
- `dashboard_id`: String de identificação do painel
- `title`: Título do painel
- `layout_type`: 'ordered' (grade) ou 'free' (posicionamento livre)
- `widgets`: Array de objetos de definição de widgets
- `description`: Descrição do painel

**Armadilhas**:
- Os IDs dos painéis são Cadeias alfanuméricas (ex.: 'abc-def-ghi'), não numéricas
- `layout_type` não pode ser alterado após a criação; é necessário recriar o painel
- As definições de widgets são objetos aninhados complexos; obtenha primeiro um painel existente para entender a estrutura
- A exclusão é permanente; Não há como desfazer

### 5. Criar Eventos e Gerenciar Períodos de Inatividade

**Quando usar**: O usuário deseja publicar eventos ou agendar períodos de inatividade para manutenção

**Sequência de ferramentas**:
1. `DATADOG_LIST_EVENTS` - Listar eventos existentes [Opcional]
2. `DATADOG_CREATE_EVENT` - Publicar um novo evento [Obrigatório]
3. `DATADOG_CREATE_DOWNTIME` - Agendar um período de inatividade para manutenção [Opcional]

**Parâmetros principais para eventos**:
- `title`: Título do evento
- `text`: Texto do evento (compatível com Markdown)
- `alert_type`: Gravidade do evento ('erro', 'aviso', 'informação', 'sucesso')
- `tags`: Array de strings de tags

**Parâmetros principais para períodos de inatividade**:
- `scope`: Escopo da tag para o período de inatividade (ex.: `host:web01`)
- `start`: Iniciar tempo (época Unix)
- `end`: Hora de término (época Unix; omita para indefinido)
- `message`: Descrição da indisponibilidade
- `monitor_id`: Monitor específico para indisponibilidade (opcional, omita para baseado em escopo)

**Armadilhas**
- O `text` do evento suporta o formato Markdown do Datadog, incluindo @menções
- O escopo das indisponibilidades usa a sintaxe de tags: `host:web01`, `env:staging`
- Omitir o `end` cria uma indisponibilidade indefinida; sempre defina uma hora de término para manutenção
- O `monitor_id` da indisponibilidade restringe-se a um único monitor; O escopo se aplica a todos os monitores correspondentes

### 6. Gerenciar Hosts e Rastreamentos

**Quando usar**: O usuário deseja listar os hosts da infraestrutura ou inspecionar rastreamentos distribuídos

**Sequência de ferramentas**:
1. `DATADOG_LIST_HOSTS` - Lista todos os hosts que reportam [Obrigatório]
2. `DATADOG_GET_TRACE_BY_ID` - Obtém um rastreamento distribuído específico [Opcional]

**Parâmetros principais**:
- `filter`: String de filtro para busca de hosts
- `sort_field`: Classifica os hosts por campo (ex.: 'name', 'apps', 'cpu')
- `sort_dir`: Direção da classificação ('asc' ou 'desc')
- `trace_id`: ID do rastreamento distribuído para consulta

**Armadilhas**:
- A lista de hosts inclui todos os hosts que reportam ao Datadog dentro do período de retenção
- Os IDs de rastreamento são longas strings numéricas; Garantir correspondência exata
- Hosts que param de reportar são retidos por um período configurado antes da remoção

## Padrões Comuns

### Sintaxe de Consulta de Monitoramento

**Alertas de métricas**:
```
avg(últimos_5m):avg:system.cpu.user{env:prod} > 90
```

**Alertas de logs**:
```
logs("service:web status:error").index("main").rollup("count").last("5m") > 10
```

### Filtragem por tags

- Tags usam o formato `chave:valor`: `host:web01`, `env:prod`, `service:api`
- Múltiplas tags: `{host:web01,env:prod}` (lógica AND)

- Caractere curinga: `host:web*`

### Paginação

- Use `page` e `page_size` ou paginação baseada em deslocamento, dependendo do endpoint
- Verifique a resposta para Contagem total para determinar se existem mais páginas
- Continue até que todos os resultados sejam recuperados

## Armadilhas Conhecidas

**Carimbos de data/hora**:
- A maioria dos endpoints usa segundos Unix (não milissegundos)
- Alguns endpoints aceitam ISO 8601; verifique o esquema da ferramenta
- Os intervalos de tempo devem ser razoáveis ​​(não anos de dados)

**Sintaxe da Consulta**:
- Consultas de métricas: `aggregation:metric{tags}`
- Consultas de logs: pares `field:value`
- As consultas de monitoramento variam de acordo com o tipo; consulte a documentação do Datadog

**Limites de Taxa**:
- A API do Datadog possui limites de taxa por endpoint
- Implemente um mecanismo de espera (backoff) para respostas 429
- Agrupe operações sempre que possível

## Referência Rápida

| Tarefa | Slug da Ferramenta | Parâmetros Principais |

|------|-----------|------------|

| Consultar métricas | DATADOG_QUERY_METRICS | consulta, de, para |

| Listar métricas | DATADOG_LIST_METRICS | q |

| Pesquisar logs | DATADOG_SEARCH_LOGS | consulta, de, para, limite |

| Listar índices de log | DATADOG_LIST_LOG_INDEXES | (nenhum) |

| Listar monitores | DATADOG_LIST_MONITORS | tags |

| Obter monitor | DATADOG_GET_MONITOR | monitor_id |

| Criar monitor | DATADOG_CREATE_MONITOR | nome, tipo, consulta, mensagem |

| Atualizar monitor | DATADOG_UPDATE_MONITOR | monitor_id |

| Silenciar monitor | DATADOG_MUTE_MONITOR | monitor_id | | Ativar monitor de som | DATADOG_UNMUTE_MONITOR | monitor_id |

| Listar painéis | DATADOG_LIST_DASHBOARDS | (nenhum) |

| Obter painel | DATADOG_GET_DASHBOARD | dashboard_id |

| Atualizar painel | DATADOG_UPDATE_DASHBOARD | dashboard_id, título, widgets |

| Excluir painel | DATADOG_DELETE_DASHBOARD | dashboard_id |

| Listar eventos | DATADOG_LIST_EVENTS | início, fim |

| Criar evento | DATADOG_CREATE_EVENT | título, texto, tipo_de_alerta |

| Criar tempo de inatividade | DATADOG_CREATE_DOWNTIME | escopo, início, fim |

| Listar hosts | DATADOG_LIST_HOSTS | filtro, campo_de_classificação |

| Obter rastreamento | DATADOG_GET_TRACE_BY_ID | trace_id |

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.

