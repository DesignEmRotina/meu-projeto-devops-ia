--- 
name: automação-de-criação
description: "Automatize tarefas do Make (Integromat) via Rube MCP (Composio): operações, enumerações, consultas de idioma e fuso horário. Sempre busque primeiro nas ferramentas os esquemas atuais."
risk: crítico
source: comunidade
date_add: "2026-02-27"
---

# Automação do Make via Rube MCP

Automatize operações do Make (anteriormente Integromat) através do toolkit Make da Composio via Rube MCP.

## Pré-requisitos

- O Rube MCP deve estar conectado (RUBE_SEARCH_TOOLS disponível)
- Conexão ativa com o Make via `RUBE_MANAGE_CONNECTIONS` com o toolkit `make`
- Sempre chame `RUBE_SEARCH_TOOLS` primeiro para obter os esquemas de ferramentas atuais

## Configuração

**Obtenha o Rube MCP**: Adicione `https://rube.app/mcp` como um servidor MCP na configuração do seu cliente. Não são necessárias chaves de API — basta adicionar o endpoint e funciona.

1. Verifique se o Rube MCP está disponível confirmando se `RUBE_SEARCH_TOOLS` responde.
2. Chame `RUBE_MANAGE_CONNECTIONS` com o toolkit `make`.
3. Se a conexão não estiver ATIVA, siga o link de autenticação retornado para concluir a autenticação do Make.
4. Confirme se o status da conexão está ATIVO antes de executar qualquer fluxo de trabalho.

## Fluxos de Trabalho Principais

### 1. Obter Dados de Operações

**Quando usar**: O usuário deseja recuperar logs de operações ou dados de uso de cenários do Make.

**Sequência de ferramentas**:
1. `MAKE_GET_OPERATIONS` - Recuperar registros de operações [Obrigatório]

**Parâmetros principais**:
- Verificar o esquema atual via RUBE_SEARCH_TOOLS para filtros disponíveis.
- Pode incluir filtros de intervalo de datas, ID do cenário ou status.

**Armadilhas**:
- Os dados de operações podem ser paginados; Verificar tokens de paginação
- Os filtros de data devem corresponder ao formato esperado do esquema
- Grandes conjuntos de resultados devem ser filtrados por intervalo de datas ou cenário

### 2. Listar idiomas disponíveis

**Quando usar**: O usuário deseja visualizar os idiomas suportados para cenários ou interfaces do Make

**Sequência de ferramentas**:
1. `MAKE_LIST_ENUMS_LANGUAGES` - Obter todos os códigos de idioma suportados [Obrigatório]

**Parâmetros principais**:
- Nenhum parâmetro obrigatório; retorna a lista completa de idiomas

**Armadilhas**:
- Os códigos de idioma seguem o formato de localidade padrão (por exemplo, 'en', 'fr', 'de')
- A lista é estática e raramente muda; Armazenar resultados em cache quando possível

### 3. Listar fusos horários disponíveis

**Quando usar**: O usuário deseja visualizar os fusos horários suportados para agendamento de cenários de criação

**Sequência de ferramentas**:
1. `MAKE_LIST_ENUMS_TIMEZONES` - Obter todos os identificadores de fuso horário suportados [Obrigatório]

**Parâmetros principais**:
- Nenhum parâmetro obrigatório; retorna a lista completa de fusos horários

**Armadilhas**:
- Os identificadores de fuso horário usam o formato IANA (por exemplo, 'America/New_York', 'Europe/London')
- A lista é estática e raramente muda; Armazene os resultados em cache sempre que possível
- Use essas strings de fuso horário exatas ao configurar os agendamentos de cenários

### 4. Consulta de Configuração de Cenários

**Quando usar**: O usuário precisa configurar os cenários com os valores corretos de idioma e fuso horário

**Sequência de ferramentas**:
1. `MAKE_LIST_ENUMS_LANGUAGES` - Obtenha códigos de idioma válidos [Obrigatório]
2. `MAKE_LIST_ENUMS_TIMEZONES` - Obtenha identificadores de fuso horário válidos [Obrigatório]

**Parâmetros principais**:
- Nenhum parâmetro é necessário para nenhuma das chamadas

**Armadilhas**:
- Sempre verifique os valores de idioma e fuso horário em relação a esses enums antes de usá-los na configuração
- Usar valores inválidos na configuração de cenários causará erros
## Padrões Comuns

### Validação de Enum

Antes de configurar quaisquer propriedades de cenário do Make que aceitem idioma ou fuso horário:
```
1. Chame MAKE_LIST_ENUMS_LANGUAGES ou MAKE_LIST_ENUMS_TIMEZONES
2. Verifique se o valor desejado existe na lista retornada
3. Use o valor exato da string da lista de enum
```

### Monitoramento de Operações

```
1. Chame MAKE_GET_OPERATIONS com filtros de intervalo de datas
2. Analise a contagem de operações, status e taxas de erro
3. Identifique operações com falha para solução de problemas
```

### Estratégia de Cache para Enums

Como as listas de idioma e fuso horário são estáticas:
```
1. Chame MAKE_LIST_ENUMS_LANGUAGES uma vez no início do fluxo de trabalho
2. Armazene os resultados na memória ou no cache local
3. Valide as entradas do usuário em relação aos valores em cache
4. Atualize o cache somente ao iniciar um novo fluxo de trabalho Sessão
```

### Fluxo de Trabalho de Análise de Operações

Para monitoramento da integridade do cenário:
```
1. Chame MAKE_GET_OPERATIONS com o intervalo de datas mais recente
2. Agrupe as operações por ID do cenário
3. Calcule as taxas de sucesso/falha por cenário
4. Identifique cenários com altas taxas de erro
5. Relate as descobertas ao usuário ou canal de notificação
```

### Integração com Outros Kits de Ferramentas

Os fluxos de trabalho do Make geralmente se conectam a outros aplicativos. Componha fluxos de trabalho com várias ferramentas:
```
1. Chame RUBE_SEARCH_TOOLS para encontrar ferramentas para o aplicativo de destino
2. Conecte os conjuntos de ferramentas necessários por meio de RUBE_MANAGE_CONNECTIONS
3. Use os dados de operações do Make para entender os padrões de execução do fluxo de trabalho
4. Execute fluxos de trabalho equivalentes diretamente por meio dos conjuntos de ferramentas de aplicativos individuais
```

## Problemas Conhecidos

**Conjunto de Ferramentas Limitado**:
- O conjunto de ferramentas Make no Composio atualmente possui ferramentas limitadas (operações, idiomas, fusos horários)
- Para gerenciamento completo de cenários (criação, edição e execução de cenários), considere usar a API nativa do Make
- Sempre chame RUBE_SEARCH_TOOLS para verificar se há novas ferramentas disponíveis
- O conjunto de ferramentas pode ser expandido ao longo do tempo; verifique periodicamente

**Dados de Operações**:
- Os registros de operações podem ter um volume significativo para contas ativas
- Sempre filtre por intervalo de datas para evitar a busca de dados excessivos
- A contagem de operações está relacionada aos níveis de preços e ao uso de cotas do Make
- Operações com falha devem ser investigadas; Podem indicar problemas de configuração de cenário

**Análise de Resposta**:
- Os dados de resposta podem estar aninhados sob a chave `data`
- Listas de enumeração retornam arrays de objetos com campos de código e rótulo
- Os dados de operações incluem metadados aninhados sobre a execução do cenário
- Analise de forma defensiva com alternativas para campos opcionais

**Limites de Taxa**:
- A API Make possui limites de taxa por token de API
- Evite chamadas repetidas e rápidas para o mesmo endpoint
- Armazene em cache os resultados da enumeração (idiomas, fusos horários), pois eles raramente mudam
- As consultas de operações devem usar intervalos de datas específicos

**Autenticação**:
- A API Make usa autenticação baseada em token
- Os tokens podem ter escopos de permissão diferentes
- Alguns dados de operações podem ser restritos com base no escopo do token
- Verifique se o usuário autenticado tem acesso à organização de destino

## Referência Rápida

| Tarefa | Slug da Ferramenta | Parâmetros Principais |

|------|-----------|------------|

| Obter operações | MAKE_GET_OPERATIONS | (verifique o esquema para filtros) |

| Listar idiomas | MAKE_LIST_ENUMS_LANGUAGES | (nenhum) |

| Listar fusos horários | MAKE_LIST_ENUMS_TIMEZONES | (nenhum) |

## Notas Adicionais

### Abordagens Alternativas

Como o kit de ferramentas Make possui recursos limitados, considere estas alternativas para casos de uso comuns do Make:

| Caso de Uso do Make | Abordagem Alternativa |

|--------------|---------------------|
| Acionar um cenário | Use o webhook nativo do Make ou o endpoint da API diretamente |

| Criar um cenário | Use a API de gerenciamento de cenários do Make diretamente |

| Agendar execução | Use RUBE_MANAGE_RECIPE_SCHEDULE com fluxos de trabalho compostos |

| Fluxo de trabalho com múltiplos aplicativos | Componha ferramentas individuais do kit de ferramentas via RUBE_MULTI_EXECUTE_TOOL |

| Transformação de dados | Use RUBE_REMOTE_WORKBENCH para processamento complexo |

### Criando Fluxos de Trabalho Equivalentes

Em vez de depender exclusivamente do conjunto de ferramentas do Make, crie automações equivalentes diretamente:
1. Identifique os aplicativos envolvidos no seu cenário do Make
2. Pesquise as ferramentas de cada aplicativo usando RUBE_SEARCH_TOOLS
3. Conecte todos os conjuntos de ferramentas necessários
4. Crie o fluxo de trabalho passo a passo usando as ferramentas individuais de cada aplicativo
5. Salve como uma receita usando RUBE_CREATE_UPDATE_RECIPE para reutilização

## Quando Usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.