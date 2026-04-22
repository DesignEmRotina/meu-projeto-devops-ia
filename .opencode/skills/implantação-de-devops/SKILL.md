---
name: implantação-de-devops
description: "DevOps e deploy de aplicações — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como código e monitoramento."
risk: crítico
source: comunidade
date_add: '06/03/2026'
autor: Renat
tags: devops, docker, ci-cd, aws, terraform, github-actions
---

# DEVOPS-DEPLOY — Da Ideia para Produção

## Visão geral

DevOps e implantação de aplicativos — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como código e monitoramento. Ativar para: dockerizar aplicação, configurar pipeline CI/CD, deploy na AWS, Lambda, ECS, configurar GitHub Actions, Terraform, rollback, implantação blue-green, verificações de integridade, alertas.

## Quando usar esta habilidade

- Quando você precisar de assistência especializada neste domínio

## Não use esta habilidade quando

- A tarefa não estiver relacionada à implantação DevOps
- Uma ferramenta mais simples e específica puder lidar com a solicitação
- O usuário precisar de assistência geral sem conhecimento especializado no domínio

## Como funciona

> "Mova-se rápido e não quebre as coisas." — Engenharia de elite não é lenta.

> É rápida e confiável ao mesmo tempo.

---

## Dockerfile otimizado (Python)

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .

EXECUTE pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Docker Compose (Local de Desenvolvimento)

```yaml
version: "3.9"
services:

app:

build: .

portas: ["8000:8000"]

ambiente:

- ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}

volumes:

- .:/app

depende de: [db, redis]

db:

imagem: postgres:15

ambiente:

POSTGRES_DB: auri

POSTGRES_USER: auri

POSTGRES_PASSWORD: ${DB_PASSWORD}

volumes:

- pgdata:/var/lib/postgresql/data

redis:

imagem: redis:7-alpine
volumes:

pgdata:
```

---

## Modelo Sam (Serverless)

```yaml

## Template.Yaml

AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globais:

Função:
Tempo limite: 30
Tempo de execução: python3.11

Ambiente:

Variáveis:

ANTHROPIC_API_KEY: !Ref AnthropicApiKey

DYNAMODB_TABLE: !Ref AuriTable

Recursos:

AuriFunction:

Tipo: AWS::Serverless::Function

Propriedades:

CodeUri: src/

Handler: lambda_function.handler

MemorySize: 512

Políticas:

- DynamoDBCrudPolicy:

TableName: !Ref AuriTable

AuriTable:

Tipo: AWS::DynamoDB::Table

Propriedades:

TableName: auri-users

BillingMode: PAY_PER_REQUEST

Definições de atributos:

- AttributeName: userId

AttributeType: S

KeySchema:

- AttributeName: userId

KeyType: HASH

TimeToLiveSpecification:

AttributeName: TTL 
Habilitado: verdadeiro
```

## Implantar comandos

```bash

## Construir e implantar

Sam construir
sam implantar --guided # primeira vez
sam implantar # implanta a seguir

## Implantar Rapido (Sem Confirmação)

sam implantar --no-confirm-changeset --no-fail-on-empty-changeset

## Ver Logs Em Tempo Real

sam logs -n AuriFunction --tail

## Deletar pilha

Sam excluir
```

---

## .Github/Workflows/Deploy.Yml

nome: Implantar Auri

em:

push:

branches: [main]

pull_request:

branches: [main]

jobs:

teste:

executa em: ubuntu-latest

etapas:

- uses: actions/checkout@v4

- uses: actions/setup-python@v5

com: { python-version: "3.11" }

- run: pip install -r requirements.txt

- run: pytest tests/ -v --cov=src --cov-report=xml

- uses: codecov/codecov-action@v4

segurança:

executa em: ubuntu-latest

etapas:

- uses: actions/checkout@v4

- run: pip install bandit safety

- run: bandit -r src/ -ll

- run: safety check -r requirements.txt

implantar:

necessita de: [teste, segurança]

se: github.ref == 'refs/heads/main'
runs-on: ubuntu-latest

steps:

- uses: actions/checkout@v4

- uses: aws-actions/setup-sam@v2

- uses: aws-actions/configure-aws-credentials@v4

with:
aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
aws-region: us-east-1

- run: sam build

- run: sam deploy --no-confirm-changeset

- name: Notificar Telegram em caso de sucesso

run: |

curl -s -X POST "https://api.telegram.org/bot${{ secrets.TELEGRAM_BOT_TOKEN }}/sendMessage" \

-d "chat_id=${{ secrets.TELEGRAM_CHAT_ID }}" \

-d "text=Auri implantado com sucesso! Commit: ${{ github.sha }}"
```

---

## Endpoint de Verificação de Saúde

```python
from fastapi import FastAPI
import time, os

app = FastAPI()
START_TIME = time.time()

@app.get("/health")
async def health():

return {

"status": "healthy",

"uptime_seconds": time.time() - START_TIME,

"version": os.environ.get("APP_VERSION", "unknown"),

"environment": os.environ.get("ENV", "production")

}
```

## Alertas do CloudWatch

```python
import boto3

def create_error_alarm(function_name: str, sns_topic_arn: str):

cw = boto3.client("cloudwatch")

cw.put_metric_alarm(

AlarmName=f"{function_name}-errors",

MetricName="Errors",

Namespace="AWS/Lambda",

Dimensions=[{"Name": "FunctionName", "Value": function_name}],

Period=300,

EvaluationPeriods=1,

Threshold=5,

ComparisonOperator="GreaterThanThreshold",

AlarmActions=[sns_topic_arn],

TreatMissingData="notBreaching"

)
```

---

## 5. Checklist De Produção

- [] Variáveis ​​de ambiente via Secrets Manager (nunca codificado)
- [] Resposta do endpoint de verificação de integridade
- [ ] Logs estruturados (JSON) com request_id
- [] Limitação de taxa configurada
- [ ] CORS restrito a domínios autorizados
- [ ] DynamoDB com backup automático ativado
- [ ] Lambda com timeout adequado (10-30s)
- [] Alarmes CloudWatch para erros e latência
- [] Plano de reversão documentado
- [ ] Teste de carga antes do lançamento

---

## 6. Comandos

| Comando | Ação |
|--------|------|
| `/docker-setup` | Dockeriza uma aplicação |
| `/sam-deploy` | Implantação completa no AWS Lambda |
| `/ci-cd-setup` | Configurar o pipeline do GitHub Actions |
| `/monitoring-setup` | Configurar CloudWatch e alertas |

| `/production-checklist` | Lista de verificação pré-lançamento |

| `/rollback` | Plano de rollback para versão anterior |

## Melhores Práticas

- Forneça um contexto claro e específico sobre seu projeto e requisitos
- Revise todas as sugestões antes de aplicá-las ao código de produção
- Combine com outras habilidades complementares para uma análise abrangente

## Armadilhas Comuns

- Usar esta habilidade para tarefas fora de sua área de especialização
- Aplicar recomendações sem entender seu contexto específico
- Não fornecer contexto suficiente do projeto para uma análise precisa