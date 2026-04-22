--- 
name: painéis-do-grafana
description: "Crie e gerencie dashboards do Grafana prontos para produção para uma observabilidade abrangente do sistema."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Dashboards do Grafana

Crie e gerencie dashboards do Grafana prontos para produção para uma observabilidade abrangente do sistema.

## Não use esta habilidade quando

- A tarefa não estiver relacionada a dashboards do Grafana
- Você precisar de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Objetivo

Projetar dashboards eficazes do Grafana para monitorar aplicativos, infraestrutura e métricas de negócios.

## Use esta habilidade quando

- Visualizar métricas do Prometheus
- Criar dashboards personalizados
- Implementar dashboards de SLO (Objetivo de Nível de Serviço)
- Monitorar infraestrutura
- Acompanhar KPIs de negócios

## Princípios de Design de Dashboards

### 1. Hierarquia da Informação
```
┌─────────────────────────────────────┐
│ Métricas Críticas (Números Grandes) │
├──────────────────────────────────────┤
│ Principais Tendências (Séries Temporais) │
├──────────────────────────────────────┤
│ Métricas detalhadas (Tabelas/Mapas de calor) │
└───────────────────────────────────────┘
```

### 2. Método RED (Serviços)
- **Taxa** - Requisições por segundo
- **Erros** - Taxa de erros
- **Duração** - Latência/tempo de resposta

### 3. Método USE (Recursos)
- **Utilização** - % de tempo em que o recurso está ocupado
- **Saturação** - Comprimento da fila/tempo de espera
- **Erros** - Contagem de erros

## Estrutura do Painel

### Monitoramento de API Painel de Controle

```json
{

"dashboard": {

"title": "Monitoramento de API",

"tags": ["api", "production"],

"timezone": "browser",

"refresh": "30s",

"panels": [

"title": "Taxa de Requisições",

"type": "graph",

"targets": [
"expr": "sum(rate(http_requests_total[5m])) by (service)",

"legendFormat": "{{service}}"

"}
",

"gridPos": {"x": 0, "y": 0, "w": 12, "h": 8}

"}",

"title": "Taxa de Erro %",

"type": "graph",

"targets": [
"expr": "(sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m]))) * 100",

"legendFormat": "Taxa de Erro"

}

],

"alert": {

"conditions": [

{
"evaluator": {"params": [5], "type": "gt"},

"operator": {"type": "and"},

"query": {"params": ["A", "5m", "now"]},

"type": "query"

}

]

},

"gridPos": {"x": 12, "y": 0, "w": 12, "h": 8}

},

{
"title": "Latência P95",

"type": "gráfico",

"alvos": [

{

"expr": "histograma_quantil(0.95, soma(taxa(http_request_duration_seconds_bucket[5m])) por (le, serviço))",

"formato_legenda": "{{serviço}}"

}

],

"gridPos": {"x": 0, "y": 8, "w": 24, "h": 8}

}

]

}
}
```
**Referência:** Consulte `assets/api-dashboard.json`

## Tipos de Painel

### 1. Painel de Estatísticas (Valor Único)
```json
{

"type": "stat",

"title": "Total de Requisições",

"targets": [{

"expr": "sum(http_requests_total)"

}],

"options": {

"reduceOptions": {

"values": false,

"calcs": ["lastNotNull"]

},

"orientation": "auto",

"textMode": "auto",

"colorMode": "value"

},

"fieldConfig": {

"defaults": {

"thresholds": {

"mode": "absolute",

"steps": [

{"value": 0, "color": "green"},
{"value": 80, "color": "yellow"},

{"value": 90, "color": "red"}

]

}

}

}
}
```

### 2. Gráfico de Série Temporal
```json
{
"type": "graph",

"title": "Uso da CPU",

"targets": [{

"expr": "100 - (avg by (instance) (rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"

}],

"yaxes": [
{"format": "percent", "max": 100, "min": 0},

{"format": "short"}

]
}
```

### 3. Painel de Tabela
```json
{

"type": "table",

"title": "Status do Serviço",

"targets": [{

"expr": "up",

"format": "table",

"instant": true

}],

"transformations": [

{

"id": "organize",

"options": {

"excludeByName": {"Time": true},

"indexByName": {},

"renameByName": {

"instance": "Instance",

"job": "Service",

"Value": "Status"

}

}
}
]
}
```

### 4. Heatmap
```json
{

"type": "heatmap",

"title": "Latency Heatmap",

"targets": [{

"expr": "sum(rate(http_request_duration_seconds_bucket[5m])) by (le)",
"format": "heatmap"

}],

"dataFormat": "tsbuckets",

"yAxis": {

"format": "s"

}
}
```

## Variáveis

### Variáveis ​​de Consulta
```json
{

"templating": {

"list": [

{
"name": "namespace",

"type": "query",

"datasource": "Prometheus",

"query": "label_values(kube_pod_info, namespace)",

"refresh": 1,

"multi": false

},

{
"name": "service",

"type": "query",

"datasource": "Prometheus",

"query": "label_values(kube_service_info{namespace=\"$namespace\"}, service)",

"refresh": 1,
"multi": true

}

]

}
}
```

### Usar variáveis ​​em consultas
```
sum(rate(http_requests_total{namespace="$namespace", service=~"$service"}[5m]))
```

## Alertas em painéis

```json

{
"alert": {

"name": "Alta taxa de erros",

"conditions": [

{
"evaluator": {

"params": [5],

"type": "gt"

},

"operator": {"type": "and"},

"query": {

"params": ["A", "5m", "now"]

},

"reducer": {"type": "avg"},

"type": "query"

}

],

"executionErrorState": "alerting",
"for": "5m",

"frequency": "1m",

"message": "Error rate is above 5%",

"noDataState": "no_data",

"notifications": [
{"uid": "slack-channel"}

]

}
}
```
## Provisionamento de Dashboards

**dashboards.yml:**
```yaml
apiVersion: 1

providers:

- name: 'default'

orgId: 1

folder: 'General'

type: file

disableDeletion: false

updateIntervalSeconds: 10

allowUiUpdates: true

options:

path: /etc/grafana/dashboards
```

## Padrões Comuns de Dashboards

### Dashboard de Infraestrutura

**Painéis Principais:**
- Utilização da CPU por nó
- Uso de memória por nó
- E/S de disco
- Tráfego de rede
- Contagem de pods por namespace
- Status do nó

**Referência:** Consulte `assets/infrastructure-dashboard.json`

### Dashboard de Banco de Dados

**Painéis Principais:**
- Consultas por segundo
- Uso do pool de conexões
- Latência de consulta (P50, P95, P99)
- Conexões ativas
- Tamanho do banco de dados
- Atraso na replicação
- Consultas lentas

**Referência:** Consulte `assets/database-dashboard.json`

### Painel de controle do aplicativo

**Painéis principais:**
- Taxa de requisições
- Taxa de erros
- Tempo de resposta (percentis)
- Usuários/sessões ativos
- Taxa de acertos no cache
- Comprimento da fila

## Boas práticas

1. **Comece com modelos** (painéis de controle da comunidade Grafana)
2. **Use nomes consistentes** para painéis e variáveis
3. **Agrupe métricas relacionadas** em linhas
4. **Defina intervalos de tempo apropriados** (padrão: últimas 6 horas)
5. **Use variáveis** para maior flexibilidade
6. **Adicione descrições aos painéis** para contextualizar
7. **Configure as unidades** corretamente
8. **Defina limites significativos** para as cores
9. **Use cores consistentes** em todos os painéis
10. **Teste com diferentes intervalos de tempo**

## Painel de controle como código

### Terraform Provisionamento

```hcl
resource "grafana_dashboard" "api_monitoring" {

config_json = file("${path.module}/dashboards/api-monitoring.json")

folder = grafana_folder.monitoring.id
}

resource "grafana_folder" "monitoring" {

title = "Monitoramento de Produção"
}
```

### Provisionamento Ansible

```yaml
- name: Deploy Grafana dashboards

copy:

src: "{{ item }}"

dest: /etc/grafana/dashboards/

with_fileglob:

- "dashboards/*.json"

notify: restart grafana
```
## Arquivos de Referência

- `assets/api-dashboard.json` - Painel de monitoramento de API
- `assets/infrastructure-dashboard.json` - Painel de infraestrutura
- `assets/database-dashboard.json` - Painel de monitoramento de banco de dados
- `references/dashboard-design.md` - Guia de design de painéis

## Skills Relacionadas

- `prometheus-configuration` - Para coleta de métricas
- `slo-implementation` - Para painéis de SLO

## Limitações
- Use esta skill somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.
