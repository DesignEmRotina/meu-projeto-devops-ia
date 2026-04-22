---
name: monitor-do-Azure
description: Azure Monitor completo – métricas, logs, traces, Application Insights, OpenTelemetry, Alerts, Workbooks, Logs Ingestion API e IaC. Observabilidade end-to-end para aplicações e infraestrutura Azure.
risk: safe
source: official + Design Em Rotina
date_added: '2026-04-15'
---

# Azure Monitor – Skill Universal e Completa

**Azure Monitor** é a solução oficial de observabilidade da Microsoft Azure. Esta skill cobre **todas** as camadas: métricas, logs, traces distribuídos, Application Insights, Logs Ingestion API, alertas, workbooks, OpenTelemetry e provisionamento via IaC (Terraform/Bicep), seguindo as melhores práticas do Azure Well-Architected Framework e SRE.

## Quando Usar Esta Skill
- Projetos que exigem observabilidade completa em produção (SLOs, alertas proativos, detecção de anomalias).
- Durante a fase de Implementação-Deploy, Health Check Validation ou Operações.
- Quando for necessário enviar logs customizados via Logs Ingestion API.
- Para integrar OpenTelemetry em aplicações Python, .NET, Node.js ou Java.
- Para criar dashboards, workbooks e alertas via código (GitOps).

## Pré-requisitos
1. Log Analytics Workspace
2. Data Collection Endpoint (DCE) + Data Collection Rule (DCR) (para Logs Ingestion)
3. Application Insights (opcional, mas recomendado)
4. Permissões: `Monitoring Contributor` + `Log Analytics Contributor`
5. Azure CLI ou Terraform/Bicep configurado

## Autenticação (padrão recomendado)

```python
from azure.identity import DefaultAzureCredential
from azure.monitor.ingestion import LogsIngestionClient

credential = DefaultAzureCredential()
client = LogsIngestionClient(
    endpoint=os.environ["AZURE_DCE_ENDPOINT"],
    credential=credential
)

1. Logs Ingestion API (Custom Logs)
import os
from azure.monitor.ingestion import LogsIngestionClient
from azure.identity import DefaultAzureCredential
import json

client = LogsIngestionClient(
    endpoint=os.environ["AZURE_DCE_ENDPOINT"],
    credential=DefaultAzureCredential()
)

rule_id = os.environ["AZURE_DCR_RULE_ID"]
stream_name = os.environ["AZURE_DCR_STREAM_NAME"]

# Exemplo de logs customizados
logs = [
    {
        "TimeGenerated": "2026-04-15T10:00:00Z",
        "Computer": "app-server-01",
        "Level": "Information",
        "Message": "Pedido processado com sucesso",
        "UserId": "user-123",
        "DurationMs": 245
    }
]

client.upload(rule_id=rule_id, stream_name=stream_name, logs=logs)

Suporte a JSON, erro parcial e retry automático (igual à skill original, mantido e aprimorado).

2. Application Insights + OpenTelemetry (Traces + Métricas)
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry import configure_azure_monitor

# Configuração automática completa
configure_azure_monitor(
    connection_string=os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"]
)

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("minha_operacao"):
    # seu código aqui
    pass
	
3. Métricas Customizadas + Alerts
Use azure-monitor-query ou SDK para métricas.
Exemplo de KQL para alertas:
customMetrics
| where name == "pedidos_processados"
| summarize avg(value) by bin(timestamp, 5m)

4. IaC – Terraform (GitOps Ready)
resource "azurerm_log_analytics_workspace" "main" {
  name                = "${var.project}-law"
  location            = var.location
  resource_group_name = var.resource_group_name
  sku                 = "PerGB2018"
  retention_in_days   = 90
}

resource "azurerm_application_insights" "main" {
  name                = "${var.project}-appinsights"
  location            = var.location
  resource_group_name = var.resource_group_name
  workspace_id        = azurerm_log_analytics_workspace.main.id
  application_type    = "web"
}

resource "azurerm_monitor_diagnostic_setting" "all" {
  name                       = "full-diagnostics"
  target_resource_id         = azurerm_linux_web_app.main.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.main.id

  enabled_log { category = "AppServiceHTTPLogs" }
  metric { category = "AllMetrics" }
}

Tabelas de Referência
Client Types
ClientUso RecomendadoLogsIngestionClientEnvio de logs customizadosLogsIngestionClient (aio)Alto throughput assíncronoAzureMonitorQueryClientConsultas KQL avançadasconfigure_azure_monitorOpenTelemetry + App Insights

Key Concepts
ConceitoDescriçãoDCEData Collection Endpoint – URL de ingestãoDCRData Collection Rule – define schema, transformação e destinoStreamNome do fluxo dentro do DCR (Custom-MinhaTabela_CL)Application InsightsAPM completo (requests, dependencies, exceptions, traces)OpenTelemetryPadrão aberto para traces distribuídos

Best Practices (Design Em Rotina)

Sempre use DefaultAzureCredential e GitOps (Terraform/Bicep).
Defina SLOs antes de criar alertas.
Use sampling inteligente e retention de 90 dias (balance custo × necessidade).
Inclua TimeGenerated em todos os logs customizados.
Monitore o custo de ingestão via azure-monitor-cost-optimizer (skill complementar).
Integre com engenheiro-de-observabilidade e resposta-a-incidentes.
Sempre valide com health-check-validation após deploy.

When to Use
Use esta skill sempre que o projeto envolver Azure Monitor completo (métricas + logs + traces + alertas). Ideal para Health Check, Detecção de Anomalias, Resposta a Incidentes e provisionamento de IaC.
Limitations

Não substitui validação manual em ambientes de produção.
Para clouds soberanos (Government, China), configure authority explicitamente.
Pergunte ao usuário se faltarem credenciais, DCR ou connection string.

	
