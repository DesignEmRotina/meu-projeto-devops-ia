---
name: detector-de-anomalias-azure-ai
description: Azure AI Anomaly Detector completo – detecção univariada, multivariada e de pontos de mudança em séries temporais. Suporte a SDKs Java, Python, .NET e REST API + integração com Azure Monitor.
risk: safe
source: official Microsoft + Design Em Rotina
date_added: '2026-04-15'
---

# Azure AI Anomaly Detector – Skill Universal e Completa (PT-BR)

**Azure AI Anomaly Detector** é o serviço de IA da Microsoft para detecção automática de anomalias em séries temporais (univariada e multivariada).  

**⚠️ AVISO IMPORTANTE DE DEPRECIAÇÃO**  
O serviço será **descontinuado em 1º de outubro de 2026**. Recomenda-se planejar a migração para soluções alternativas (Azure Monitor + OpenTelemetry + custom models) o quanto antes.

Esta skill é **universal** (independente de linguagem) e cobre:
- Detecção univariada (batch e streaming)
- Detecção multivariada (até 300+ variáveis correlacionadas)
- Detecção de pontos de mudança (change point)
- Integração nativa com Azure Monitor
- Exemplos em **Java, Python e .NET**
- Provisionamento via IaC (Terraform/Bicep)

## Quando Usar Esta Skill
- Monitoramento de métricas de aplicação, KPIs, sensores IoT ou dados financeiros.
- Detecção proativa de anomalias em produção (integração com `DETECCAO_ANOMALIAS_SUBAGENTE`).
- Análise de séries temporais durante Health Check ou Resposta a Incidentes.
- Projetos que precisam de detecção multivariada (múltiplos sinais correlacionados).

## Pré-requisitos
1. Recurso **Anomaly Detector** provisionado no Azure.
2. Endpoint e chave de API (ou Managed Identity).
3. Dados em formato de série temporal (timestamp + valor).
4. (Opcional) Integração com Log Analytics / Azure Monitor.

## Variáveis de Ambiente Recomendadas
```bash
AZURE_ANOMALY_DETECTOR_ENDPOINT=https://<seu-recurso>.cognitiveservices.azure.com/
AZURE_ANOMALY_DETECTOR_API_KEY=<sua-chave>
# Ou use DefaultAzureCredential (recomendado em produção)
```

## 1. Criação do Client (Multi-linguagem)

### Java (SDK oficial)
```java
import com.azure.ai.anomalydetector.AnomalyDetectorClientBuilder;
import com.azure.core.credential.AzureKeyCredential;

String endpoint = System.getenv("AZURE_ANOMALY_DETECTOR_ENDPOINT");
String key = System.getenv("AZURE_ANOMALY_DETECTOR_API_KEY");

var client = new AnomalyDetectorClientBuilder()
    .credential(new AzureKeyCredential(key))
    .endpoint(endpoint)
    .buildMultivariateClient();   // ou .buildUnivariateClient()
```

### Python (SDK oficial)
```python
from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.core.credentials import AzureKeyCredential

client = AnomalyDetectorClient(
    endpoint=os.environ["AZURE_ANOMALY_DETECTOR_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["AZURE_ANOMALY_DETECTOR_API_KEY"])
)
```

### .NET (SDK oficial)
```csharp
using Azure.AI.AnomalyDetector;

var client = new AnomalyDetectorClient(
    new Uri(endpoint),
    new AzureKeyCredential(key)
);
```

## 2. Padrões Principais

### Univariada – Detecção em Lote (Batch)
```java
// Java example (similar em Python/.NET)
UnivariateDetectionOptions options = new UnivariateDetectionOptions(series)
    .setGranularity(TimeGranularity.DAILY)
    .setSensitivity(95);

UnivariateEntireDetectionResult result = univariateClient.detectUnivariateEntireSeries(options);
```

### Univariada – Último Ponto (Streaming)
```java
UnivariateLastDetectionResult last = univariateClient.detectUnivariateLastPoint(options);
if (last.isAnomaly()) { ... }
```

### Detecção de Ponto de Mudança (Change Point)
```java
UnivariateChangePointDetectionResult change = univariateClient.detectUnivariateChangePoint(changeOptions);
```

### Multivariada – Treinamento + Inferência
(Exemplo completo em Java, Python e .NET disponível no repositório oficial).

## 3. Integração com Azure Monitor (Recomendada)
- Envie logs de anomalias via **Logs Ingestion API** (`azure-monitor` skill).
- Use **Application Insights** + OpenTelemetry para traces.
- Crie alertas automáticos no Azure Monitor baseados nos resultados do Anomaly Detector.

## Melhores Práticas (Microsoft + Design Em Rotina)

1. **Dados mínimos**: Univariada precisa de pelo menos 12 pontos; multivariada de 300+.
2. **Granularidade**: Alinhe `TimeGranularity` com a frequência real dos dados.
3. **Sensibilidade**: Comece com 85–95 e ajuste com base em falsos positivos.
4. **Janela deslizante (Multivariada)**: 200–1000 dependendo da complexidade.
5. **GitOps**: Provisionamento via Terraform/Bicep + IaC.
6. **Custo**: Monitore consumo de transações (S0 tier tem 20.000 grátis/mês).
7. **Segurança**: Use `DefaultAzureCredential` e Private Endpoints.

## Gerenciamento de Modelos (Multivariada)
- Listar modelos
- Ver status do treinamento
- Excluir modelo (obrigatório após uso)

## Tratamento de Erros
Sempre capture `HttpResponseException` / `HttpResponseError` e logue com Azure Monitor.

## Frases de Ativação (Trigger Phrases)
- “detecção de anomalia Azure”
- “anomaly detector univariada/multivariada”
- “detecção de mudança de tendência”
- “análise de série temporal IA”
- “Azure AI Anomaly Detector”

## When to Use / Limitações
- Use apenas quando a tarefa envolver detecção de anomalias em séries temporais.
- **Não** substitui validação em ambiente real ou revisão por especialista.
- Devido à descontinuação em out/2026, avise o usuário sobre migração.
- Peça esclarecimento se faltarem dados, endpoint ou permissões.

---
