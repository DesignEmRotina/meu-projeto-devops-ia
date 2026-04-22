--- 
name: aws-serverless
description: Habilidade especializada para construir aplicações serverless prontas para produção na AWS. Abrange funções Lambda, API Gateway, DynamoDB, SQS/SNS, padrões orientados a eventos, implantação SAM/CDK e otimização de inicialização a frio.
risk: desconhecido
source: vibeship-spawner-skills (Apache 2.0)
date_add: 27/02/2026
---

# AWS Serverless

Habilidade especializada para construir aplicações serverless prontas para produção na AWS.

Abrange funções Lambda, API Gateway, DynamoDB, padrões orientados a eventos SQS/SNS,
implantação SAM/CDK e otimização de inicialização a frio.

## Princípios

- Dimensionar corretamente a memória e o tempo limite (medir antes de otimizar)
- Minimizar inicializações a frio para cargas de trabalho sensíveis à latência
- Usar SnapStart para funções Java/.NET
- Preferir a API HTTP à API REST para casos de uso simples
- Projetar para falhas com filas de mensagens não entregues (DLQs) e novas tentativas
- Manter os pacotes de implantação pequenos
- Usar variáveis ​​de ambiente para configuração
- Implementar registro estruturado com IDs de correlação

## Padrões

### Padrão Lambda Handler

Estrutura adequada de função Lambda com tratamento de erros

**Quando usar**: Qualquer implementação de função Lambda, manipuladores de API, processadores de eventos, tarefas agendadas

```javascript
// Node.js Lambda Handler
// handler.js

// Initialize outside handler (reused across invocations)
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

// Handler function
exports.handler = async (event, context) => {
  // Optional: Don't wait for event loop to clear (Node.js)
  context.callbackWaitsForEmptyEventLoop = false;

  try {
    // Parse input based on event source
    const body = typeof event.body === 'string'
      ? JSON.parse(event.body)
      : event.body;

    // Business logic
    const result = await processRequest(body);

    // Return API Gateway compatible response
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(result)
    };
  } catch (error) {
    console.error('Error:', JSON.stringify({
      error: error.message,
      stack: error.stack,
      requestId: context.awsRequestId
    }));

    return {
      statusCode: error.statusCode || 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: error.message || 'Internal server error'
      })
    };
  }
};

async function processRequest(data) {
  // Your business logic here
  const result = await docClient.send(new GetCommand({
    TableName: process.env.TABLE_NAME,
    Key: { id: data.id }
  }));
  return result.Item;
}
```

```python
# Python Lambda Handler
# handler.py

import json
import os
import logging
import boto3
from botocore.exceptions import ClientError

# Initialize outside handler (reused across invocations)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    try:
        # Parse input
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})

        # Business logic
        result = process_request(body)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(result)
        }

    except ClientError as e:
        logger.error(f"DynamoDB error: {e.response['Error']['Message']}")
        return error_response(500, 'Database error')

    except json.JSONDecodeError:
        return error_response(400, 'Invalid JSON')

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return error_response(500, 'Internal server error')

def process_request(data):
    response = table.get_item(Key={'id': data['id']})
    return response.get('Item')

def error_response(status_code, message):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'error': message})
    }
```

### Melhores práticas

- Inicialize os clientes fora do manipulador (reutilizados em invocações subsequentes)
- Sempre retorne o formato de resposta correto do API Gateway
- Registre logs com JSON estruturado para o CloudWatch Insights
- Inclua o ID da solicitação nos logs de erro para rastreamento

### Padrão de integração do API Gateway

Integração de API REST e API HTTP com Lambda

**Quando usar**: Criação de APIs REST com suporte do Lambda, necessidade de endpoints HTTP para funções

```yaml
# template.yaml (SAM)
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Runtime: nodejs20.x
    Timeout: 30
    MemorySize: 256
    Environment:
      Variables:
        TABLE_NAME: !Ref ItemsTable

Resources:
  # HTTP API (recommended for simple use cases)
  HttpApi:
    Type: AWS::Serverless::HttpApi
    Properties:
      StageName: prod
      CorsConfiguration:
        AllowOrigins:
          - "*"
        AllowMethods:
          - GET
          - POST
          - DELETE
        AllowHeaders:
          - "*"

  # Lambda Functions
  GetItemFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/get.handler
      Events:
        GetItem:
          Type: HttpApi
          Properties:
            ApiId: !Ref HttpApi
            Path: /items/{id}
            Method: GET
      Policies:
        - DynamoDBReadPolicy:
            TableName: !Ref ItemsTable

  CreateItemFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/create.handler
      Events:
        CreateItem:
          Type: HttpApi
          Properties:
            ApiId: !Ref HttpApi
            Path: /items
            Method: POST
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref ItemsTable

  # DynamoDB Table
  ItemsTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST

Outputs:
  ApiUrl:
    Value: !Sub "https://${HttpApi}.execute-api.${AWS::Region}.amazonaws.com/prod"
```

```javascript
// src/handlers/get.js
const { getItem } = require('../lib/dynamodb');

exports.handler = async (event) => {
  const id = event.pathParameters?.id;

  if (!id) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: 'Missing id parameter' })
    };
  }

  const item = await getItem(id);

  if (!item) {
    return {
      statusCode: 404,
      body: JSON.stringify({ error: 'Item not found' })
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify(item)
  };
};
```

### Estrutura

project/
├── template.yaml # Modelo SAM
├── src/
│ ├── handlers/
│ │ ├── get.js
│ │ ├── create.js
│ │ └── delete.js
│ └── lib/
│ └── dynamodb.js
└── events/

└── event.json # Eventos de teste

### Comparação de API

- API HTTP:

- Menor latência (~10ms)

- Menor custo (50-70% mais barato)

- Mais simples, com menos recursos
- Melhor Para: A maioria das APIs REST
- Rest_api:

- Mais recursos (cache, validação de requisições, WAF)

- Planos de uso e chaves de API

- Transformação de requisição/resposta

- Ideal para: APIs complexas, recursos corporativos

### Padrão SQS Orientado a Eventos

Lambda acionada pelo SQS para processamento assíncrono confiável

**Quando usar**: Processamento desacoplado e assíncrono, necessidade de lógica de repetição e DLQ, processamento de mensagens em lotes
```yaml
# template.yaml
Resources:
  ProcessorFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/processor.handler
      Events:
        SQSEvent:
          Type: SQS
          Properties:
            Queue: !GetAtt ProcessingQueue.Arn
            BatchSize: 10
            FunctionResponseTypes:
              - ReportBatchItemFailures  # Partial batch failure handling

  ProcessingQueue:
    Type: AWS::SQS::Queue
    Properties:
      VisibilityTimeout: 180  # 6x Lambda timeout
      RedrivePolicy:
        deadLetterTargetArn: !GetAtt DeadLetterQueue.Arn
        maxReceiveCount: 3

  DeadLetterQueue:
    Type: AWS::SQS::Queue
    Properties:
      MessageRetentionPeriod: 1209600  # 14 days
```

```javascript
// src/handlers/processor.js
exports.handler = async (event) => {
  const batchItemFailures = [];

  for (const record of event.Records) {
    try {
      const body = JSON.parse(record.body);
      await processMessage(body);
    } catch (error) {
      console.error(`Failed to process message ${record.messageId}:`, error);
      // Report this item as failed (will be retried)
      batchItemFailures.push({
        itemIdentifier: record.messageId
      });
    }
  }

  // Return failed items for retry
  return { batchItemFailures };
};

async function processMessage(message) {
  // Your processing logic
  console.log('Processing:', message);

  // Simulate work
  await saveToDatabase(message);
}
```

```python
# Python version
import json
import logging

logger = logging.getLogger()

def handler(event, context):
    batch_item_failures = []

    for record in event['Records']:
        try:
            body = json.loads(record['body'])
            process_message(body)
        except Exception as e:
            logger.error(f"Failed to process {record['messageId']}: {e}")
            batch_item_failures.append({
                'itemIdentifier': record['messageId']
            })

    return {'batchItemFailures': batch_item_failures}
```

### Melhores práticas

- Defina o VisibilityTimeout para 6 vezes o tempo limite do Lambda
- Use ReportBatchItemFailures para falhas parciais em lote
- Sempre configure uma fila de mensagens não lidas (DLQ) para mensagens problemáticas
- Processe as mensagens de forma idempotente

### Padrão DynamoDB Streams

Reaja a alterações em tabelas do DynamoDB com o Lambda

**Quando usar**: Reações em tempo real a alterações de dados, replicação entre regiões, registro de auditoria, notificações

```yaml
# template.yaml
Resources:
  ItemsTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: items
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES

  StreamProcessorFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/stream.handler
      Events:
        Stream:
          Type: DynamoDB
          Properties:
            Stream: !GetAtt ItemsTable.StreamArn
            StartingPosition: TRIM_HORIZON
            BatchSize: 100
            MaximumRetryAttempts: 3
            DestinationConfig:
              OnFailure:
                Destination: !GetAtt StreamDLQ.Arn

  StreamDLQ:
    Type: AWS::SQS::Queue
```

```javascript
// src/handlers/stream.js
exports.handler = async (event) => {
  for (const record of event.Records) {
    const eventName = record.eventName;  // INSERT, MODIFY, REMOVE

    // Unmarshall DynamoDB format to plain JS objects
    const newImage = record.dynamodb.NewImage
      ? unmarshall(record.dynamodb.NewImage)
      : null;
    const oldImage = record.dynamodb.OldImage
      ? unmarshall(record.dynamodb.OldImage)
      : null;

    console.log(`${eventName}: `, { newImage, oldImage });

    switch (eventName) {
      case 'INSERT':
        await handleInsert(newImage);
        break;
      case 'MODIFY':
        await handleModify(oldImage, newImage);
        break;
      case 'REMOVE':
        await handleRemove(oldImage);
        break;
    }
  }
};

// Use AWS SDK v3 unmarshall
const { unmarshall } = require('@aws-sdk/util-dynamodb');
```

### Stream_view_types

- KEYS_ONLY: Only key attributes
- NEW_IMAGE: After modification
- OLD_IMAGE: Before modification
- NEW_AND_OLD_IMAGES: Both before and after

### Padrão de Otimização de Inicialização a Frio

Minimize a latência de inicialização a frio do Lambda

**Quando usar**: Aplicações sensíveis à latência, APIs voltadas para o usuário, funções com alto tráfego

## 1. Otimize o tamanho do pacote
```javascript
// Use modular AWS SDK v3 imports
// GOOD - only imports what you need
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');

// BAD - imports entire SDK
const AWS = require('aws-sdk');  // Don't do this!
```

## 2. Use SnapStart (Java/.NET)

```yaml
# template.yaml
Resources:
  JavaFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: com.example.Handler::handleRequest
      Runtime: java21
      SnapStart:
        ApplyOn: PublishedVersions  # Enable SnapStart
      AutoPublishAlias: live
```

## 3. Right-size Memory

```yaml
# More memory = more CPU = faster init
Resources:
  FastFunction:
    Type: AWS::Serverless::Function
    Properties:
      MemorySize: 1024  # 1GB gets full vCPU
      Timeout: 30
```

## 4. Provisioned Concurrency (when needed)

```yaml
Resources:
  CriticalFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/critical.handler
      AutoPublishAlias: live

  ProvisionedConcurrency:
    Type: AWS::Lambda::ProvisionedConcurrencyConfig
    Properties:
      FunctionName: !Ref CriticalFunction
      Qualifier: live
      ProvisionedConcurrentExecutions: 5
```

## 5. Keep Init Light

```python
# GOOD - Lazy initialization
_table = None

def get_table():
    global _table
    if _table is None:
        dynamodb = boto3.resource('dynamodb')
        _table = dynamodb.Table(os.environ['TABLE_NAME'])
    return _table

def handler(event, context):
    table = get_table()  # Only initializes on first use
    # ...
```

### Prioridade de Otimização

- 1: Reduzir o tamanho do pacote (maior impacto)
- 2: Usar SnapStart para Java/.NET
- 3: Aumentar a memória para inicialização mais rápida
- 4: Adiar importações pesadas
- 5: Provisionar concorrência (último recurso)

### Padrão de Desenvolvimento Local SAM

Testes e depuração locais com a CLI do SAM

**Quando usar**: Desenvolvimento e testes locais, depuração de funções Lambda, teste local do API Gateway
```bash
# Install SAM CLI
pip install aws-sam-cli

# Initialize new project
sam init --runtime nodejs20.x --name my-api

# Build the project
sam build

# Run locally
sam local start-api

# Invoke single function
sam local invoke GetItemFunction --event events/get.json

# Local debugging (Node.js with VS Code)
sam local invoke --debug-port 5858 GetItemFunction

# Deploy
sam deploy --guided
```

```json
// events/get.json (test event)
{
  "pathParameters": {
    "id": "123"
  },
  "httpMethod": "GET",
  "path": "/items/123"
}
```

```json
// .vscode/launch.json (for debugging)
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to SAM CLI",
      "type": "node",
      "request": "attach",
      "address": "localhost",
      "port": 5858,
      "localRoot": "${workspaceRoot}/src",
      "remoteRoot": "/var/task/src",
      "protocol": "inspector"
    }
  ]
}
```
### Comandos

- Sam_build: Criar pacotes de implantação do Lambda
- Sam_local_start_api: Iniciar o API Gateway local
- Sam_local_invoke: Invocar uma única função
- Sam_deploy: Implantar na AWS
- Sam_logs: Monitorar logs do CloudWatch

### Padrão Serverless do CDK

Infraestrutura como código com o AWS CDK

**Quando usar**: Infraestrutura complexa além do Lambda, Preferência por linguagens de programação em vez de YAML, Necessidade de estruturas reutilizáveis

```typescript
// lib/api-stack.ts
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';

export class ApiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB Table
    const table = new dynamodb.Table(this, 'ItemsTable', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // For dev only
    });

    // Lambda Function
    const getItemFn = new lambda.Function(this, 'GetItemFunction', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'get.handler',
      code: lambda.Code.fromAsset('src/handlers'),
      environment: {
        TABLE_NAME: table.tableName,
      },
      memorySize: 256,
      timeout: cdk.Duration.seconds(30),
    });

    // Grant permissions
    table.grantReadData(getItemFn);

    // API Gateway
    const api = new apigateway.RestApi(this, 'ItemsApi', {
      restApiName: 'Items Service',
      defaultCorsPreflightOptions: {
        allowOrigins: apigateway.Cors.ALL_ORIGINS,
        allowMethods: apigateway.Cors.ALL_METHODS,
      },
    });

    const items = api.root.addResource('items');
    const item = items.addResource('{id}');

    item.addMethod('GET', new apigateway.LambdaIntegration(getItemFn));

    // Output API URL
    new cdk.CfnOutput(this, 'ApiUrl', {
      value: api.url,
    });
  }
}
```

```bash
# CDK commands
npm install -g aws-cdk
cdk init app --language typescript
cdk synth    # Generate CloudFormation
cdk diff     # Show changes
cdk deploy   # Deploy to AWS
```

## Problemas Graves

### Fase de Inicialização a Frio Agora Cobrada (Agosto de 2025)

Gravidade: ALTA

Situação: Execução de funções Lambda em produção

Sintomas:
Aumento inexplicável nos custos do Lambda (10-50% a mais).

A fatura inclui cobranças pela inicialização da função.

Funções com lógica de inicialização complexa custam mais do que o esperado.

Motivo da falha:
A partir de 1º de agosto de 2025, a AWS cobra a fase de inicialização da mesma forma que cobra a duração da invocação.
Anteriormente, a inicialização a frio não era cobrada pela duração total.

Isso afeta funções com:
- Carregamento pesado de dependências (pacotes grandes)
- Código de inicialização lento
- Inicializações a frio frequentes (baixo tráfego ou baixa concorrência)

As inicializações a frio agora impactam diretamente sua fatura, e não apenas a latência.

Solução recomendada:

## Meça sua fase de inicialização
```bash
# Check CloudWatch Logs for INIT_REPORT
# Look for Init Duration in milliseconds

# Example log line:
# INIT_REPORT Init Duration: 423.45 ms
```

## Reduce INIT duration

```javascript
// 1. Minimize package size
// Use tree shaking, exclude dev dependencies
// npm prune --production

// 2. Lazy load heavy dependencies
let heavyLib = null;
function getHeavyLib() {
  if (!heavyLib) {
    heavyLib = require('heavy-library');
  }
  return heavyLib;
}

// 3. Use AWS SDK v3 modular imports
const { S3Client } = require('@aws-sdk/client-s3');
// NOT: const AWS = require('aws-sdk');
```

## Use SnapStart for Java/.NET

```yaml
Resources:
  JavaFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: java21
      SnapStart:
        ApplyOn: PublishedVersions
```

## Monitor cold start frequency

```javascript
// Track cold starts with custom metric
let isColdStart = true;

exports.handler = async (event) => {
  if (isColdStart) {
    console.log('COLD_START');
    // CloudWatch custom metric here
    isColdStart = false;
  }
  // ...
};
```

### Lambda Timeout Misconfiguration

Severity: HIGH

Situation: Running Lambda functions, especially with external calls

Symptoms:
Function times out unexpectedly.
"Task timed out after X seconds" in logs.
Partial processing with no response.
Silent failures with no error caught.

Why this breaks:
Default Lambda timeout is only 3 seconds. Maximum is 15 minutes.

Common timeout causes:
- Default timeout too short for workload
- Downstream service taking longer than expected
- Network issues in VPC
- Infinite loops or blocking operations
- S3 downloads larger than expected

Lambda terminates at timeout without graceful shutdown.

Recommended fix:

## Set appropriate timeout

```yaml
# template.yaml
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Timeout: 30  # Seconds (max 900)
      # Set to expected duration + buffer
```

## Implement timeout awareness

```javascript
exports.handler = async (event, context) => {
  // Get remaining time
  const remainingTime = context.getRemainingTimeInMillis();

  // If running low on time, fail gracefully
  if (remainingTime < 5000) {
    console.warn('Running low on time, aborting');
    throw new Error('Insufficient time remaining');
  }

  // For long operations, check periodically
  for (const item of items) {
    if (context.getRemainingTimeInMillis() < 10000) {
      // Save progress and exit gracefully
      await saveProgress(processedItems);
      throw new Error('Timeout approaching, saved progress');
    }
    await processItem(item);
  }
};
```

## Set downstream timeouts

```javascript
const axios = require('axios');

// Always set timeouts on HTTP calls
const response = await axios.get('https://api.example.com/data', {
  timeout: 5000  // 5 seconds
});
```

### Out of Memory (OOM) Crash

Severity: HIGH

Situation: Lambda function processing data

Symptoms:
Function stops abruptly without error.
CloudWatch logs appear truncated.
"Max Memory Used" hits configured limit.
Inconsistent behavior under load.

Why this breaks:
When Lambda exceeds memory allocation, AWS forcibly terminates
the runtime. This happens without raising a catchable exception.

Common causes:
- Processing large files in memory
- Memory leaks across invocations
- Buffering entire response bodies
- Heavy libraries consuming too much memory

Recommended fix:

## Increase memory allocation

```yaml
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      MemorySize: 1024  # MB (128-10240)
      # More memory = more CPU too
```

## Stream large data

```javascript
// BAD - loads entire file into memory
const data = await s3.getObject(params).promise();
const content = data.Body.toString();

// GOOD - stream processing
const { S3Client, GetObjectCommand } = require('@aws-sdk/client-s3');
const s3 = new S3Client({});

const response = await s3.send(new GetObjectCommand(params));
const stream = response.Body;

// Process stream in chunks
for await (const chunk of stream) {
  await processChunk(chunk);
}
```

## Monitor memory usage

```javascript
exports.handler = async (event, context) => {
  const used = process.memoryUsage();
  console.log('Memory:', {
    heapUsed: Math.round(used.heapUsed / 1024 / 1024) + 'MB',
    heapTotal: Math.round(used.heapTotal / 1024 / 1024) + 'MB'
  });
  // ...
};
```

## Use Lambda Power Tuning

```bash
# Find optimal memory setting
# https://github.com/alexcasalboni/aws-lambda-power-tuning
```


### Atraso na inicialização a frio de funções Lambda em VPC

Gravidade: MÉDIA

Situação: Funções Lambda em VPC acessando recursos privados

Sintomas:
Inicializações a frio extremamente lentas (antes levavam mais de 10 segundos, agora levam cerca de 100 ms).

Tempo limite excedido na primeira invocação após o período de inatividade.

As funções funcionam em VPC, mas são lentas em comparação com o ambiente não-VPC.

Motivo do problema:
Funções Lambda em VPC precisam de Interfaces de Rede Elásticas (ENIs).

A AWS melhorou isso significativamente com as ENIs Hyperplane, mas:

- A primeira inicialização a frio em VPC ainda apresenta sobrecarga
- Problemas com o Gateway NAT podem causar tempos limite excedidos
- Configuração incorreta do grupo de segurança bloqueia o tráfego
- A resolução de DNS pode ser lenta

Solução recomendada:

## Verificar a configuração da VPC
```yaml
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      VpcConfig:
        SecurityGroupIds:
          - !Ref LambdaSecurityGroup
        SubnetIds:
          - !Ref PrivateSubnet1
          - !Ref PrivateSubnet2  # Multiple AZs

  LambdaSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Lambda SG
      VpcId: !Ref VPC
      SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0  # Allow HTTPS outbound
```

## Use VPC endpoints for AWS services

```yaml
# Avoid NAT Gateway for AWS service calls
DynamoDBEndpoint:
  Type: AWS::EC2::VPCEndpoint
  Properties:
    ServiceName: !Sub com.amazonaws.${AWS::Region}.dynamodb
    VpcId: !Ref VPC
    RouteTableIds:
      - !Ref PrivateRouteTable
    VpcEndpointType: Gateway

S3Endpoint:
  Type: AWS::EC2::VPCEndpoint
  Properties:
    ServiceName: !Sub com.amazonaws.${AWS::Region}.s3
    VpcId: !Ref VPC
    VpcEndpointType: Gateway
```

## Use VPC somente quando necessário

Não conecte o Lambda a uma VPC a menos que você precise de:
- Acesso ao RDS/ElastiCache na VPC
- Acesso a instâncias EC2 privadas
- Requisitos de conformidade

A maioria dos serviços da AWS pode ser acessada sem VPC.

### Loop de Eventos do Node.js Não Limpo

Gravidade: MÉDIA

Situação: Função Lambda do Node.js com callbacks ou timers

Sintomas:
A função leva o tempo limite completo para retornar.

"Tempo limite da tarefa excedido" mesmo que a lógica tenha sido concluída.

Cobrança extra por tempo ocioso.

Por que isso causa o problema:
Por padrão, o Lambda espera que o loop de eventos do Node.js esteja vazio
antes de retornar. Se você tiver:
- setTimeout/setInterval não resolvido
- Conexões de banco de dados pendentes
- Callbacks pendentes

O Lambda espera até o tempo limite, mesmo que sua resposta esteja pronta.

Correção recomendada:

## Diga à função Lambda para não esperar pelo loop de eventos
```javascript
exports.handler = async (event, context) => {
  // Don't wait for event loop to clear
  context.callbackWaitsForEmptyEventLoop = false;

  // Your code here
  const result = await processRequest(event);

  return {
    statusCode: 200,
    body: JSON.stringify(result)
  };
};
```

## Close connections properly

```javascript
// For database connections, use connection pooling
// or close connections explicitly

const mysql = require('mysql2/promise');

exports.handler = async (event, context) => {
  context.callbackWaitsForEmptyEventLoop = false;

  const connection = await mysql.createConnection({...});
  try {
    const [rows] = await connection.query('SELECT * FROM users');
    return { statusCode: 200, body: JSON.stringify(rows) };
  } finally {
    await connection.end();  // Always close
  }
};
```

### API Gateway Payload Size Limits

Severity: MEDIUM

Situation: Returning large responses or receiving large requests

Symptoms:
"413 Request Entity Too Large" error
"Execution failed due to configuration error: Malformed Lambda proxy response"
Response truncated or failed

Why this breaks:
API Gateway has hard payload limits:
- REST API: 10 MB request/response
- HTTP API: 10 MB request/response
- Lambda itself: 6 MB sync response, 256 KB async

Exceeding these causes failures that may not be obvious.

Recommended fix:

## For large file uploads

```javascript
// Use presigned S3 URLs instead of passing through API Gateway

const { S3Client, PutObjectCommand } = require('@aws-sdk/client-s3');
const { getSignedUrl } = require('@aws-sdk/s3-request-presigner');

exports.handler = async (event) => {
  const s3 = new S3Client({});

  const command = new PutObjectCommand({
    Bucket: process.env.BUCKET_NAME,
    Key: `uploads/${Date.now()}.file`
  });

  const uploadUrl = await getSignedUrl(s3, command, { expiresIn: 300 });

  return {
    statusCode: 200,
    body: JSON.stringify({ uploadUrl })
  };
};
```

## For large responses

```javascript
// Store in S3, return presigned download URL
exports.handler = async (event) => {
  const largeData = await generateLargeReport();

  await s3.send(new PutObjectCommand({
    Bucket: process.env.BUCKET_NAME,
    Key: `reports/${reportId}.json`,
    Body: JSON.stringify(largeData)
  }));

  const downloadUrl = await getSignedUrl(s3,
    new GetObjectCommand({
      Bucket: process.env.BUCKET_NAME,
      Key: `reports/${reportId}.json`
    }),
    { expiresIn: 3600 }
  );

  return {
    statusCode: 200,
    body: JSON.stringify({ downloadUrl })
  };
};
```


### Loop infinito ou invocação recursiva

Gravidade: ALTA

Situação: Função Lambda acionada por eventos

Sintomas:

Custos descontrolados.

Milhares de invocações em minutos.

Os logs do CloudWatch mostram invocações repetidas.

A função Lambda está gravando no bucket/tabela de origem que a aciona.

Por que isso falha:
O Lambda pode ser acionado acidentalmente:
- Um gatilho do S3 grava de volta no mesmo bucket
- ​​Um gatilho do DynamoDB atualiza a mesma tabela
- O SNS publica no tópico que o aciona
- Step Functions com tratamento de erros incorreto

Correção recomendada:

## Usar buckets/prefixos diferentes

```yaml
# Gatilho do S3 com filtro de prefixo
Eventos:

S3Event:

Tipo: S3

Propriedades:

Bucket: !Ref InputBucket

Eventos: s3:ObjectCreated:*

Filtro:

S3Key:

Regras:

- Nome: prefixo

Valor: uploads/ # Acionar somente em uploads/

# Saída para um bucket ou prefixo diferente
# OutputBucket ou prefixo processed/
```

## Adicionar verificações de idempotência

```javascript
exports.handler = async (event) => {

for (const record of event.Records) {

const key = record.s3.object.key;

// Ignorar se este for um arquivo processado

if (key.startsWith('processed/')) {
console.log('Ignorando arquivo já processado:', key);

continue;

}

// Processar e gravar em um local diferente

await processFile(key);

await writeToS3(`processed/${key}`, result);

}
};

```

## Configurar concorrência reservada como disjuntor

```yaml
Recursos:

FunçãoRisco:

Tipo: AWS::Serverless::Function

Propriedades:

ExecuçõesConcorrentesReservadas: 10 # Máximo de 10 execuções paralelas

# Limita o impacto de invocações descontroladas
```

## Monitorar com alarmes do CloudWatch

```yaml
AlarmeDeInvocação:

Tipo: AWS::CloudWatch::Alarm

Propriedades:

NomeDaMétrica: Invocações

Namespace: AWS/Lambda

Estatística: Soma

Período: 60
PeríodosDeEvaliação: 1

Limite: 1000 # Alerta se >1000 invocações/min

OperadorDeComparação: MaiorQueLimite
```

## Verificações de Validação

### Credenciais da AWS Codificadas

Gravidade: ERRO

As credenciais da AWS nunca devem ser codificadas diretamente no código.

Mensagem: Chave de acesso da AWS codificada diretamente no código. Use funções do IAM ou variáveis ​​de ambiente.

### Chave Secreta da AWS no Código-Fonte

Gravidade: ERRO

As chaves secretas devem ser protegidas pelo Secrets Manager ou por variáveis ​​de ambiente.

Mensagem: Chave secreta da AWS codificada diretamente no código. Use funções do IAM ou o Secrets Manager.

### Política do IAM Excessivamente Permissiva

Gravidade: AVISO

Evite permissões curinga em funções do IAM do Lambda.

Mensagem: Política do IAM excessivamente permissiva. Use o princípio do menor privilégio.

### Manipulador do Lambda Sem Tratamento de Erros

Gravidade: AVISO

Os manipuladores do Lambda devem ter blocos try/catch para lidar com erros de forma elegante.

Mensagem: Manipulador do Lambda sem tratamento de erros. Adicione blocos try/catch.

### Ausência de `callbackWaitsForEmptyEventLoop`

Gravidade: INFO

Os manipuladores do Node.js devem definir `callbackWaitsForEmptyEventLoop`.

Mensagem: Considere definir `context.callbackWaitsForEmptyEventLoop = false`.

### Configuração de memória padrão

Gravidade: INFO

O valor padrão de 128 MB pode ser insuficiente para muitas cargas de trabalho.

Mensagem: Usando 128 MB de memória padrão. Considere aumentar para obter melhor desempenho.

### Configuração de tempo limite baixo

Gravidade: WARNING

Um tempo limite muito baixo pode causar falhas inesperadas.

Mensagem: Um tempo limite de 1 a 3 segundos pode ser insuficiente. Aumente se estiver fazendo chamadas externas.

### Ausência de configuração de fila de mensagens não entregues (DLQ)

Gravidade: WARNING

Funções assíncronas devem ter uma DLQ para invocações com falha.

Mensagem: Nenhuma DLQ configurada. Adicione para invocações assíncronas.

### Importando o SDK completo da AWS v2

Gravidade: AVISO

Importe clientes específicos do SDK da AWS v3 para pacotes menores

Mensagem: Importando o SDK completo da AWS. Use importações modulares do SDK v3 para pacotes menores.

### Nome da tabela do DynamoDB codificado

Gravidade: AVISO

Os nomes das tabelas devem vir de variáveis ​​de ambiente

Mensagem: Nome da tabela codificado. Use variáveis ​​de ambiente para portabilidade.

## Colaboração

### Gatilhos de Delegação

- O usuário precisa de computação sem servidor no GCP -> gcp-cloud-run (Cloud Run para contêineres, Cloud Functions para eventos)
- O usuário precisa de computação sem servidor no Azure -> azure-functions (Azure Functions, Logic Apps)
- O usuário precisa de design de banco de dados -> postgres-wizard (design de RDS ou uso de padrões do DynamoDB)
- O usuário precisa de autenticação -> auth-specialist (Cognito, autorizadores do API Gateway)
- O usuário precisa de fluxos de trabalho complexos -> workflow-automation (Step Functions, EventBridge)
- O usuário precisa de integração com IA -> llm-architect (Lambda chamando Bedrock ou LLMs externos)

## Quando usar
Use esta habilidade quando a solicitação corresponder claramente aos recursos e padrões descritos acima.

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente. - Pare e peça esclarecimentos se faltarem informações necessárias, permissões, limites de segurança ou critérios de sucesso.



