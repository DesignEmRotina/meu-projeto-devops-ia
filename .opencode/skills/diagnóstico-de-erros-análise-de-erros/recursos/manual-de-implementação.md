# Manual de Implementação de Análise e Resolução de Erros

Este arquivo contém padrões detalhados, listas de verificação e exemplos de código referenciados pela habilidade.

## Detecção e Classificação de Erros

### Taxonomia de Erros

Classifique os erros nessas categorias para orientar sua estratégia de depuração:

**Por Gravidade:**
- **Crítica**: Sistema inoperante, perda de dados, violação de segurança, indisponibilidade total do serviço
- **Alta**: Funcionalidade principal comprometida, impacto significativo no usuário, risco de corrupção de dados
- **Média**: Degradação parcial de funcionalidades, soluções alternativas disponíveis, problemas de desempenho
- **Baixa**: Bugs menores, problemas estéticos, casos extremos com impacto mínimo

**Por Tipo:**
- **Erros de Tempo de Execução**: Exceções, travamentos, falhas de segmentação, desreferências de ponteiro nulo
- **Erros de Lógica**: Comportamento incorreto, cálculos errados, transições de estado inválidas
- **Erros de Integração**: Falhas de API, timeouts de rede, problemas com serviços externos
- **Erros de Desempenho**: Vazamentos de memória, picos de uso da CPU, consultas lentas, esgotamento de recursos
- **Erros de Configuração**: Variáveis ​​de ambiente ausentes, configurações inválidas, incompatibilidade de versões
- **Erros de Segurança**: Falhas de autenticação, violações de autorização, tentativas de injeção

**Por Observabilidade:**
- **Determinístico**: Reproduzível consistentemente com entradas conhecidas
- **Intermitente**: Ocorre esporadicamente, frequentemente relacionado a condições de tempo ou de corrida
- **Ambiental**: Ocorre apenas em ambientes ou configurações específicas
- **Dependente de Carga**: Aparece sob alto tráfego ou pressão de recursos

### Estratégia de Detecção de Erros

Implementar detecção de erros em múltiplas camadas:

1. **Instrumentação em Nível de Aplicação**: Utilizar SDKs de rastreamento de erros (Sentry, DataDog Error Tracking, Rollbar) para capturar automaticamente exceções não tratadas com contexto completo
2. **Endpoints de Verificação de Saúde**: Monitorar os endpoints `/health` e `/ready` para detectar degradação do serviço antes do impacto no usuário
3. **Monitoramento Sintético**: Executar testes automatizados em produção para detectar problemas proativamente
4. **Monitoramento de Usuário Real (RUM)**: Rastrear a experiência real do usuário e erros de front-end
5. **Análise de Padrões de Log**: Use ferramentas SIEM para identificar picos de erros e padrões anômalos
6. **Limiares de APM**: Alerte sobre aumentos na taxa de erros, picos de latência ou quedas de throughput

### Agregação de Erros e Reconhecimento de Padrões

Agrupe erros relacionados para identificar problemas sistêmicos:

- **Impressão Digital**: Agrupe erros por similaridade de rastreamento de pilha, tipo de erro e caminho de código afetado
- **Análise de Tendências**: Monitore a frequência de erros ao longo do tempo para detectar regressões ou problemas emergentes
- **Análise de Correlação**: Vincule erros a implantações, alterações de configuração ou eventos externos
- **Pontuação de Impacto no Usuário**: Priorize com base no número de usuários e sessões afetados
- **Padrões Geográficos/Temporais**: Identifique clusters de erros específicos da região ou baseados em tempo

## Técnicas de Análise de Causa Raiz

### Processo de Investigação Sistemática

Siga esta abordagem estruturada para cada erro:

1. **Reproduza o Erro**: Crie etapas mínimas de reprodução. Se intermitente, identifique as condições que desencadeiam o problema.
2. **Isolar o Ponto de Falha**: Identifique a linha de código ou componente exato onde a falha se origina.
3. **Analise a Cadeia de Chamadas**: Rastreie o código de trás para frente a partir do erro para entender como o sistema chegou ao estado de falha.
4. **Inspecionar o Estado das Variáveis**: Examine os valores no ponto da falha e nas etapas anteriores.
5. **Revisar Alterações Recentes**: Verifique o histórico do Git em busca de modificações recentes nos caminhos de código afetados.
6. **Testar Hipóteses**: Formule teorias sobre a causa e valide-as com experimentos direcionados.

### A Técnica dos Cinco Porquês

Pergunte "por quê?" repetidamente para chegar às causas raiz:

```
Erro: Tempo limite de conexão com o banco de dados excedido após 30 segundos

Por quê? O pool de conexões do banco de dados estava esgotado.
Por quê? Todas as conexões estavam sendo usadas por consultas de longa duração.
Por quê? Um novo recurso introduziu padrões de consulta N+1.
Por quê? O carregamento lento do ORM não estava configurado corretamente.
Por quê? A revisão de código não detectou a regressão de desempenho.

Causa raiz: Processo de revisão de código insuficiente para padrões de consulta de banco de dados.

### Depuração de Sistemas Distribuídos

Para erros em microsserviços e sistemas distribuídos:

- **Rastrear o Caminho da Requisição**: Use IDs de correlação para acompanhar requisições entre serviços
- **Verificar Dependências de Serviço**: Identifique quais serviços upstream/downstream estão envolvidos
- **Analisar Falhas em Cascata**: Determine se o erro é sintoma de uma falha em outro serviço
- **Revisar o Estado do Circuit Breaker**: Verifique se os mecanismos de proteção foram acionados
- **Examinar Filas de Mensagens**: Procure por backpressure, mensagens não entregues ou atrasos no processamento
- **Reconstrução da Linha do Tempo**: Construa uma linha do tempo de eventos em todos os serviços usando rastreamento distribuído

## Análise de Stack Trace

### Interpretando Stack Traces

Extraia o máximo de informações dos stack traces:

**Elementos-chave:**
- **Tipo de erro:** Que tipo de exceção/erro ocorreu?
- **Mensagem de erro:** Informações contextuais sobre a falha.
- **Ponto de origem:** O frame mais profundo onde o erro foi lançado.
- **Cadeia de chamadas:** A sequência de chamadas de função que levou ao erro.
- **Framework vs. Código da aplicação:** Distinga entre o código da biblioteca e o seu código.
- **Limites assíncronos:** Identifique onde as operações assíncronas interrompem o rastreamento.

**Estratégia de análise:**
1. Comece no topo da pilha (origem do erro).
2. Identifique o primeiro frame no código da sua aplicação (não no framework/biblioteca).
3. Examine o contexto desse frame: parâmetros de entrada, variáveis ​​locais, estado.
4. Rastreie o erro retroativamente pelas funções que o chamaram para entender como o estado inválido foi criado.
5. Procure por padrões: isso ocorreu em um loop? Dentro de um callback? Após uma operação assíncrona?

### Enriquecimento do Stack Trace

Ferramentas modernas de rastreamento de erros fornecem stack traces aprimorados:

- **Contexto do Código-Fonte**: Visualize as linhas de código adjacentes a cada frame
- **Valores de Variáveis ​​Locais**: Inspecione o estado das variáveis ​​em cada frame (com o modo de depuração do Sentry)
- **Breadcrumbs**: Veja a sequência de eventos que levaram ao erro
- **Rastreamento de Versões**: Vincule erros a implantações e commits específicos
- **Source Maps**: Para JavaScript minificado, mapeie de volta para o código-fonte original
- **Comentários Inline**: Anote os frames da pilha com informações contextuais

### Padrões Comuns de Stack Trace

**Padrão: Exceção de Ponteiro Nulo em Código de Framework Profundo**
```
NullPointerException

em java.util.HashMap.hash(HashMap.java:339)

em java.util.HashMap.get(HashMap.java:556)
em com.myapp.service.UserService.findUser(UserService.java:45)
```
Causa raiz: O aplicativo passou um valor nulo para o código do framework. Concentre-se em UserService.java:45.

**Padrão: Tempo limite excedido após longa espera**
```
TimeoutException: A operação expirou após 30000 ms
em okhttp3.internal.http2.Http2Stream.waitForIo
em com.myapp.api.PaymentClient.processPayment(PaymentClient.java:89)
```
Causa raiz: Serviço externo lento/sem resposta. Necessário lógica de repetição e disjuntor.

**Padrão: Condição de Corrida em Código Concorrente**
```
ConcurrentModificationException

em java.util.ArrayList$Itr.checkForComodification
em com.myapp.processor.BatchProcessor.process(BatchProcessor.java:112)
```
Causa Raiz: A coleção foi modificada durante a iteração. É necessário utilizar estruturas de dados thread-safe ou sincronização.

## Agregação de Logs e Correspondência de Padrões

### Implementação de Logs Estruturados

Implementar logs estruturados baseados em JSON para logs legíveis por máquina:

**Standard Log Schema:**
```json
{
  "timestamp": "2025-10-11T14:23:45.123Z",
  "level": "ERROR",
  "correlation_id": "req-7f3b2a1c-4d5e-6f7g-8h9i-0j1k2l3m4n5o",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "service": "payment-service",
  "environment": "production",
  "host": "pod-payment-7d4f8b9c-xk2l9",
  "version": "v2.3.1",
  "error": {
    "type": "PaymentProcessingException",
    "message": "Failed to charge card: Insufficient funds",
    "stack_trace": "...",
    "fingerprint": "payment-insufficient-funds"
  },
  "user": {
    "id": "user-12345",
    "ip": "203.0.113.42",
    "session_id": "sess-abc123"
  },
  "request": {
    "method": "POST",
    "path": "/api/v1/payments/charge",
    "duration_ms": 2547,
    "status_code": 402
  },
  "context": {
    "payment_method": "credit_card",
    "amount": 149.99,
    "currency": "USD",
    "merchant_id": "merchant-789"
  }
}
```

**Key Fields to Always Include:**
- `timestamp`: ISO 8601 format in UTC
- `level`: ERROR, WARN, INFO, DEBUG, TRACE
- `correlation_id`: Unique ID for the entire request chain
- `trace_id` and `span_id`: OpenTelemetry identifiers for distributed tracing
- `service`: Which microservice generated this log
- `environment`: dev, staging, production
- `error.fingerprint`: Stable identifier for grouping similar errors

### Correlation ID Pattern

Implement correlation IDs to track requests across distributed systems:

**Node.js/Express Middleware:**
```javascript
const { v4: uuidv4 } = require('uuid');
const asyncLocalStorage = require('async-local-storage');

// Middleware to generate/propagate correlation ID
function correlationIdMiddleware(req, res, next) {
  const correlationId = req.headers['x-correlation-id'] || uuidv4();
  req.correlationId = correlationId;
  res.setHeader('x-correlation-id', correlationId);

  // Store in async context for access in nested calls
  asyncLocalStorage.run(new Map(), () => {
    asyncLocalStorage.set('correlationId', correlationId);
    next();
  });
}

// Propagate to downstream services
function makeApiCall(url, data) {
  const correlationId = asyncLocalStorage.get('correlationId');
  return axios.post(url, data, {
    headers: {
      'x-correlation-id': correlationId,
      'x-source-service': 'api-gateway'
    }
  });
}

// Include in all log statements
function log(level, message, context = {}) {
  const correlationId = asyncLocalStorage.get('correlationId');
  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    level,
    correlation_id: correlationId,
    message,
    ...context
  }));
}
```

**Python/Flask Implementation:**
```python
import uuid
import logging
from flask import request, g
import json

class CorrelationIdFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = g.get('correlation_id', 'N/A')
        return True

@app.before_request
def setup_correlation_id():
    correlation_id = request.headers.get('X-Correlation-ID', str(uuid.uuid4()))
    g.correlation_id = correlation_id

@app.after_request
def add_correlation_header(response):
    response.headers['X-Correlation-ID'] = g.correlation_id
    return response

# Structured logging with correlation ID
logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
logger.addFilter(CorrelationIdFilter())

def log_structured(level, message, **context):
    log_entry = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'level': level,
        'correlation_id': g.correlation_id,
        'service': 'payment-service',
        'message': message,
        **context
    }
    logger.log(getattr(logging, level), json.dumps(log_entry))
```

### Log Aggregation Architecture

**Centralized Logging Pipeline:**
1. **Application**: Outputs structured JSON logs to stdout/stderr
2. **Log Shipper**: Fluentd/Fluent Bit/Vector collects logs from containers
3. **Log Aggregator**: Elasticsearch/Loki/DataDog receives and indexes logs
4. **Visualization**: Kibana/Grafana/DataDog UI for querying and dashboards
5. **Alerting**: Trigger alerts on error patterns and thresholds

**Log Query Examples (Elasticsearch DSL):**
```json
// Find all errors for a specific correlation ID
{
  "query": {
    "bool": {
      "must": [
        { "match": { "correlation_id": "req-7f3b2a1c-4d5e-6f7g" }},
        { "term": { "level": "ERROR" }}
      ]
    }
  },
  "sort": [{ "timestamp": "asc" }]
}

// Find error rate spike in last hour
{
  "query": {
    "bool": {
      "must": [
        { "term": { "level": "ERROR" }},
        { "range": { "timestamp": { "gte": "now-1h" }}}
      ]
    }
  },
  "aggs": {
    "errors_per_minute": {
      "date_histogram": {
        "field": "timestamp",
        "fixed_interval": "1m"
      }
    }
  }
}

// Group errors by fingerprint to find most common issues
{
  "query": {
    "term": { "level": "ERROR" }
  },
  "aggs": {
    "error_types": {
      "terms": {
        "field": "error.fingerprint",
        "size": 10
      },
      "aggs": {
        "affected_users": {
          "cardinality": { "field": "user.id" }
        }
      }
    }
  }
}
```

### Detecção de Padrões e Reconhecimento de Anomalias

Use a análise de logs para identificar padrões:

- **Picos na Taxa de Erros**: Compare a taxa de erros atual com a linha de base histórica (por exemplo, >3 desvios padrão)
- **Novos Tipos de Erro**: Alerte quando surgirem padrões de erro nunca vistos antes
- **Falhas em Cascata**: Detecte quando erros em um serviço desencadeiam erros em serviços dependentes
- **Padrões de Impacto no Usuário**: Identifique quais usuários/segmentos são afetados de forma desproporcional
- **Padrões Geográficos**: Identifique problemas específicos de cada região (por exemplo, problemas com a CDN, interrupções no data center)
- **Padrões Temporais**: Encontre problemas relacionados ao tempo (por exemplo, trabalhos em lote, tarefas agendadas, bugs de fuso horário)

## Fluxo de Trabalho de Depuração

### Depuração Interativa

Para erros determinísticos em desenvolvimento:

**Configuração do Depurador:**
1. Defina um ponto de interrupção antes que o erro ocorra
2. Execute o código linha por linha
3. Inspecione os valores das variáveis e estado do objeto
4. Avalie expressões no console de depuração
5. Observe mudanças de estado inesperadas
6. Modifique variáveis ​​para testar hipóteses

**Ferramentas de Depuração Modernas:**
- **Depurador do VS Code**: Depuração integrada para JavaScript, Python, Go, Java e C++
- **Chrome DevTools**: Depuração de front-end com perfilamento de rede, desempenho e memória
- **pdb/ipdb (Python)**: Depurador interativo com análise pós-mortem
- **dlv (Go)**: Depurador Delve para programas Go
- **lldb (C/C++)**: Depurador de baixo nível com recursos de depuração reversa

### Depuração em Produção

Para erros em ambientes de produção onde depuradores não estão disponíveis:

**Técnicas Seguras de Depuração em Produção:**

1. **Registro Aprimorado**: Adicione instruções de log estratégicas em torno de pontos de falha suspeitos
2. **Sinalizadores de Recursos**: Habilite o registro detalhado para recursos específicos usuários/solicitações
3. **Amostragem**: Registre o contexto detalhado de uma porcentagem das solicitações
4. **Rastreamento de Transações APM**: Use o DataDog APM ou o New Relic para visualizar fluxos de transações detalhados
5. **Rastreamento Distribuído**: Utilize os rastreamentos do OpenTelemetry para entender as interações entre serviços
6. **Perfilamento**: Use profilers contínuos (DataDog Profiler, Pyroscope) para identificar pontos críticos
7. **Despejos de Heap**: Capture snapshots de memória para análise de vazamentos de memória
8. **Espelhamento de Tráfego**: Reproduza o tráfego de produção em um ambiente de teste para investigação segura

**Depuração Remota (Use com Cautela):**
- Anexe o depurador ao processo em execução somente em serviços não críticos
- Use pontos de interrupção somente leitura que não interrompam a execução
- Limite estritamente o tempo das sessões de depuração
- Sempre tenha um plano de reversão pronto

### Depuração de Memória e Desempenho

**Memory Leak Detection:**
```javascript
// Node.js heap snapshot comparison
const v8 = require('v8');
const fs = require('fs');

function takeHeapSnapshot(filename) {
  const snapshot = v8.writeHeapSnapshot(filename);
  console.log(`Heap snapshot written to ${snapshot}`);
}

// Take snapshots at intervals
takeHeapSnapshot('heap-before.heapsnapshot');
// ... run operations that might leak ...
takeHeapSnapshot('heap-after.heapsnapshot');

// Analyze in Chrome DevTools Memory profiler
// Look for objects with increasing retained size
```

**Performance Profiling:**
```python
# Python profiling with cProfile
import cProfile
import pstats
from pstats import SortKey

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()

    # Your code here
    process_large_dataset()

    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(20)  # Top 20 time-consuming functions
```

## Error Prevention Strategies

### Input Validation and Type Safety

**Defensive Programming:**
```typescript
// TypeScript: Leverage type system for compile-time safety
interface PaymentRequest {
  amount: number;
  currency: string;
  customerId: string;
  paymentMethodId: string;
}

function processPayment(request: PaymentRequest): PaymentResult {
  // Runtime validation for external inputs
  if (request.amount <= 0) {
    throw new ValidationError('Amount must be positive');
  }

  if (!['USD', 'EUR', 'GBP'].includes(request.currency)) {
    throw new ValidationError('Unsupported currency');
  }

  // Use Zod or Yup for complex validation
  const schema = z.object({
    amount: z.number().positive().max(1000000),
    currency: z.enum(['USD', 'EUR', 'GBP']),
    customerId: z.string().uuid(),
    paymentMethodId: z.string().min(1)
  });

  const validated = schema.parse(request);

  // Now safe to process
  return chargeCustomer(validated);
}
```

**Python Type Hints and Validation:**
```python
from typing import Optional
from pydantic import BaseModel, validator, Field
from decimal import Decimal

class PaymentRequest(BaseModel):
    amount: Decimal = Field(..., gt=0, le=1000000)
    currency: str
    customer_id: str
    payment_method_id: str

    @validator('currency')
    def validate_currency(cls, v):
        if v not in ['USD', 'EUR', 'GBP']:
            raise ValueError('Unsupported currency')
        return v

    @validator('customer_id', 'payment_method_id')
    def validate_ids(cls, v):
        if not v or len(v) < 1:
            raise ValueError('ID cannot be empty')
        return v

def process_payment(request: PaymentRequest) -> PaymentResult:
    # Pydantic validates automatically on instantiation
    # Type hints provide IDE support and static analysis
    return charge_customer(request)
```

### Error Boundaries and Graceful Degradation

**React Error Boundaries:**
```typescript
import React, { Component, ErrorInfo, ReactNode } from 'react';
import * as Sentry from '@sentry/react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    // Log to error tracking service
    Sentry.captureException(error, {
      contexts: {
        react: {
          componentStack: errorInfo.componentStack
        }
      }
    });

    console.error('Uncaught error:', error, errorInfo);
  }

  public render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div role="alert">
          <h2>Something went wrong</h2>
          <details>
            <summary>Error details</summary>
            <pre>{this.state.error?.message}</pre>
          </details>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
```

**Circuit Breaker Pattern:**
```python
from datetime import datetime, timedelta
from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60, success_threshold=2):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.success_threshold = success_threshold
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerOpenError("Circuit breaker is OPEN")

        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self):
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = CircuitState.CLOSED
                self.success_count = 0

    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

    def _should_attempt_reset(self):
        return (datetime.now() - self.last_failure_time) > timedelta(seconds=self.timeout)

# Usage
payment_circuit = CircuitBreaker(failure_threshold=5, timeout=60)

def process_payment_with_circuit_breaker(payment_data):
    try:
        result = payment_circuit.call(external_payment_api.charge, payment_data)
        return result
    except CircuitBreakerOpenError:
        # Graceful degradation: queue for later processing
        payment_queue.enqueue(payment_data)
        return {"status": "queued", "message": "Payment will be processed shortly"}
```

### Retry Logic with Exponential Backoff

```typescript
// TypeScript retry implementation
interface RetryOptions {
  maxAttempts: number;
  baseDelayMs: number;
  maxDelayMs: number;
  exponentialBase: number;
  retryableErrors?: string[];
}

async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  options: RetryOptions = {
    maxAttempts: 3,
    baseDelayMs: 1000,
    maxDelayMs: 30000,
    exponentialBase: 2
  }
): Promise<T> {
  let lastError: Error;

  for (let attempt = 0; attempt < options.maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;

      // Check if error is retryable
      if (options.retryableErrors &&
          !options.retryableErrors.includes(error.name)) {
        throw error; // Don't retry non-retryable errors
      }

      if (attempt < options.maxAttempts - 1) {
        const delay = Math.min(
          options.baseDelayMs * Math.pow(options.exponentialBase, attempt),
          options.maxDelayMs
        );

        // Add jitter to prevent thundering herd
        const jitter = Math.random() * 0.1 * delay;
        const actualDelay = delay + jitter;

        console.log(`Attempt ${attempt + 1} failed, retrying in ${actualDelay}ms`);
        await new Promise(resolve => setTimeout(resolve, actualDelay));
      }
    }
  }

  throw lastError!;
}

// Usage
const result = await retryWithBackoff(
  () => fetch('https://api.example.com/data'),
  {
    maxAttempts: 3,
    baseDelayMs: 1000,
    maxDelayMs: 10000,
    exponentialBase: 2,
    retryableErrors: ['NetworkError', 'TimeoutError']
  }
);
```

### Pilha de Observabilidade Moderna (2025)

**Arquitetura Recomendada:**
- **Métricas**: Prometheus + Grafana ou DataDog
- **Logs**: Elasticsearch/Loki + Fluentd ou DataDog Logs
- **Rastreamentos**: OpenTelemetry + Jaeger/Tempo ou DataDog APM
- **Erros**: Sentry ou DataDog Error Tracking
- **Frontend**: Sentry Browser SDK ou DataDog RUM
- **Sintéticos**: DataDog Synthetics ou Checkly

### Sentry Integration

**Node.js/Express Setup:**
```javascript
const Sentry = require('@sentry/node');
const { ProfilingIntegration } = require('@sentry/profiling-node');

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  release: process.env.GIT_COMMIT_SHA,

  // Performance monitoring
  tracesSampleRate: 0.1, // 10% of transactions
  profilesSampleRate: 0.1,

  integrations: [
    new ProfilingIntegration(),
    new Sentry.Integrations.Http({ tracing: true }),
    new Sentry.Integrations.Express({ app }),
  ],

  beforeSend(event, hint) {
    // Scrub sensitive data
    if (event.request) {
      delete event.request.cookies;
      delete event.request.headers?.authorization;
    }

    // Add custom context
    event.tags = {
      ...event.tags,
      region: process.env.AWS_REGION,
      instance_id: process.env.INSTANCE_ID
    };

    return event;
  }
});

// Express middleware
app.use(Sentry.Handlers.requestHandler());
app.use(Sentry.Handlers.tracingHandler());

// Routes here...

// Error handler (must be last)
app.use(Sentry.Handlers.errorHandler());

// Manual error capture with context
function processOrder(orderId) {
  try {
    const order = getOrder(orderId);
    chargeCustomer(order);
  } catch (error) {
    Sentry.captureException(error, {
      tags: {
        operation: 'process_order',
        order_id: orderId
      },
      contexts: {
        order: {
          id: orderId,
          status: order?.status,
          amount: order?.amount
        }
      },
      user: {
        id: order?.customerId
      }
    });
    throw error;
  }
}
```

### DataDog APM Integration

**Python/Flask Setup:**
```python
from ddtrace import patch_all, tracer
from ddtrace.contrib.flask import TraceMiddleware
import logging

# Auto-instrument common libraries
patch_all()

app = Flask(__name__)

# Initialize tracing
TraceMiddleware(app, tracer, service='payment-service')

# Custom span for detailed tracing
@app.route('/api/v1/payments/charge', methods=['POST'])
def charge_payment():
    with tracer.trace('payment.charge', service='payment-service') as span:
        payment_data = request.json

        # Add custom tags
        span.set_tag('payment.amount', payment_data['amount'])
        span.set_tag('payment.currency', payment_data['currency'])
        span.set_tag('customer.id', payment_data['customer_id'])

        try:
            result = payment_processor.charge(payment_data)
            span.set_tag('payment.status', 'success')
            return jsonify(result), 200
        except InsufficientFundsError as e:
            span.set_tag('payment.status', 'insufficient_funds')
            span.set_tag('error', True)
            return jsonify({'error': 'Insufficient funds'}), 402
        except Exception as e:
            span.set_tag('payment.status', 'error')
            span.set_tag('error', True)
            span.set_tag('error.message', str(e))
            raise
```

### OpenTelemetry Implementation

**Go Service with OpenTelemetry:**
```go
package main

import (
    "context"
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/sdk/trace"
    sdktrace "go.opentelemetry.io/otel/sdk/trace"
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/codes"
)

func initTracer() (*sdktrace.TracerProvider, error) {
    exporter, err := otlptracegrpc.New(
        context.Background(),
        otlptracegrpc.WithEndpoint("otel-collector:4317"),
        otlptracegrpc.WithInsecure(),
    )
    if err != nil {
        return nil, err
    }

    tp := sdktrace.NewTracerProvider(
        sdktrace.WithBatcher(exporter),
        sdktrace.WithResource(resource.NewWithAttributes(
            semconv.SchemaURL,
            semconv.ServiceNameKey.String("payment-service"),
            semconv.ServiceVersionKey.String("v2.3.1"),
            attribute.String("environment", "production"),
        )),
    )

    otel.SetTracerProvider(tp)
    return tp, nil
}

func processPayment(ctx context.Context, paymentReq PaymentRequest) error {
    tracer := otel.Tracer("payment-service")
    ctx, span := tracer.Start(ctx, "processPayment")
    defer span.End()

    // Add attributes
    span.SetAttributes(
        attribute.Float64("payment.amount", paymentReq.Amount),
        attribute.String("payment.currency", paymentReq.Currency),
        attribute.String("customer.id", paymentReq.CustomerID),
    )

    // Call downstream service
    err := chargeCard(ctx, paymentReq)
    if err != nil {
        span.RecordError(err)
        span.SetStatus(codes.Error, err.Error())
        return err
    }

    span.SetStatus(codes.Ok, "Payment processed successfully")
    return nil
}

func chargeCard(ctx context.Context, paymentReq PaymentRequest) error {
    tracer := otel.Tracer("payment-service")
    ctx, span := tracer.Start(ctx, "chargeCard")
    defer span.End()

    // Simulate external API call
    result, err := paymentGateway.Charge(ctx, paymentReq)
    if err != nil {
        return fmt.Errorf("payment gateway error: %w", err)
    }

    span.SetAttributes(
        attribute.String("transaction.id", result.TransactionID),
        attribute.String("gateway.response_code", result.ResponseCode),
    )

    return nil
}
```

### Alert Configuration

**Intelligent Alerting Strategy:**

```yaml
# DataDog Monitor Configuration
monitors:
  - name: "High Error Rate - Payment Service"
    type: metric
    query: "avg(last_5m):sum:trace.express.request.errors{service:payment-service} / sum:trace.express.request.hits{service:payment-service} > 0.05"
    message: |
      Payment service error rate is {{value}}% (threshold: 5%)

      This may indicate:
      - Payment gateway issues
      - Database connectivity problems
      - Invalid payment data

      Runbook: https://wiki.company.com/runbooks/payment-errors

      @slack-payments-oncall @pagerduty-payments

    tags:
      - service:payment-service
      - severity:high

    options:
      notify_no_data: true
      no_data_timeframe: 10
      escalation_message: "Error rate still elevated after 10 minutes"

  - name: "New Error Type Detected"
    type: log
    query: "logs(\"level:ERROR service:payment-service\").rollup(\"count\").by(\"error.fingerprint\").last(\"5m\") > 0"
    message: |
      New error type detected in payment service: {{error.fingerprint}}

      First occurrence: {{timestamp}}
      Affected users: {{user_count}}

      @slack-engineering

    options:
      enable_logs_sample: true

  - name: "Payment Service - P95 Latency High"
    type: metric
    query: "avg(last_10m):p95:trace.express.request.duration{service:payment-service} > 2000"
    message: |
      Payment service P95 latency is {{value}}ms (threshold: 2000ms)

      Check:
      - Database query performance
      - External API response times
      - Resource constraints (CPU/memory)

      Dashboard: https://app.datadoghq.com/dashboard/payment-service

      @slack-payments-team
```

## Resposta a Incidentes de Produção

### Fluxo de Trabalho de Resposta a Incidentes

**Fase 1: Detecção e Triagem (0-5 minutos)**
1. Confirmar o alerta/incidente
2. Verificar a gravidade do incidente e o impacto no usuário
3. Atribuir o responsável pelo incidente
4. Criar um canal para o incidente (#incident-2025-10-11-payment-errors)
5. Atualizar a página de status, se houver, voltada para o cliente

**Fase 2: Investigação (5-30 minutos)**
1. Coletar dados de observabilidade:

- Taxas de erro do Sentry/DataDog

- Rastreamentos mostrando solicitações com falha

- Logs próximos ao horário de início do incidente

- Métricas mostrando uso de recursos, latência e taxa de transferência
2. Correlacionar com mudanças recentes:

- Implantações recentes (verificar o pipeline de CI/CD)

- Alterações de configuração

- Alterações de infraestrutura

- Status de dependências externas
3. Formular uma hipótese inicial sobre a causa raiz
4. Documentar as descobertas no log de incidentes

**Fase 3: Mitigação (Imediato)**
1. Implementar correção imediata com base na hipótese:

- Reverter a implantação recente
- Aumentar os recursos

- Desativar o recurso problemático (ativar sinalizador de recurso)

- Realizar failover para o sistema de backup

- Aplicar hotfix
2. Verificar se a mitigação funcionou (taxa de erros reduzida)
3. Monitorar por 15 a 30 minutos para garantir a estabilidade

**Fase 4: Recuperação e Validação**

1. Verificar se todos os sistemas estão operacionais
2. Verificar a consistência dos dados
3. Processar solicitações em fila/com falha
4. Atualizar a página de status: incidente resolvido
5. Notificar as partes interessadas

**Fase 5: Análise Pós-Incidente**

1. Agendar análise pós-incidente em até 48 horas
2. Criar uma linha do tempo detalhada dos eventos
3. Identificar a causa raiz (pode ser diferente da hipótese inicial)
4. Documentar os fatores contribuintes
5. Criar itens de ação para:

- Prevenir incidentes semelhantes

- Melhorar o tempo de detecção

- Melhorar o tempo de mitigação

- Melhorar a comunicação

### Ferramentas de Investigação de Incidentes

**Padrões de Consulta para Incidentes Comuns Incidentes:**

```
# Find all errors for a specific time window (Elasticsearch)
GET /logs-*/_search
{
  "query": {
    "bool": {
      "must": [
        { "term": { "level": "ERROR" }},
        { "term": { "service": "payment-service" }},
        { "range": { "timestamp": {
          "gte": "2025-10-11T14:00:00Z",
          "lte": "2025-10-11T14:30:00Z"
        }}}
      ]
    }
  },
  "sort": [{ "timestamp": "asc" }],
  "size": 1000
}

# Encontrar correlação entre erros e implantações (DataDog)
# Usar o rastreamento de implantações para sobrepor marcadores de implantação em gráficos de erros
# Consulta: sum:trace.express.request.errors{service:payment-service} by {version}

# Identificar usuários afetados (Sentry)
# Navegar até a aba Problema → Impacto no Usuário
# Exibe: total de usuários afetados, novos vs. recorrentes, distribuição geográfica

# Rastrear solicitações específicas com falha (OpenTelemetry/Jaeger)
# Pesquisar por trace_id ou correlation_id
# Visualizar o caminho completo da solicitação entre os serviços
# Identificar qual serviço/span falhou
```

### Modelos de Comunicação

**Notificação Inicial de Incidente:**
```
🚨 INCIDENTE: Erros no Processamento de Pagamentos

Gravidade: Alta
Status: Investigando
Iniciado em: 11/10/2025 14:23 UTC
Responsável pelo Incidente: @jane.smith

Sintomas:
- Taxa de erros no processamento de pagamentos: 15% (normal: <1%)
- Usuários afetados: ~500 nos últimos 10 minutos
- Erro: "Tempo limite de conexão com o banco de dados excedido"

Ações tomadas:
- Investigação do pool de conexões do banco de dados
- Verificação de implantações recentes
- Monitoramento da taxa de erros

Atualizações: Forneceremos atualizações a cada 15 minutos
Página de status: https://status.company.com/incident/abc123
```

**Notificação de mitigação:**
```
✅ ATUALIZAÇÃO DO INCIDENTE: Mitigação aplicada

Gravidade: Alta → Média
Status: Mitigado
Duração: 27 minutos

Causa raiz: Pool de conexões do banco de dados esgotado devido a consultas de longa duração
introduzido na implantação da versão 2.3.1 às 14:00 UTC

Mitigação: Revertido para a versão 2.3.0

Status atual:
- Taxa de erros: 0,5% (de volta ao normal) (normal)
- Todos os sistemas operacionais
- Processando o acúmulo de pagamentos em fila

Próximos passos:
- Monitorar por 30 minutos
- Corrigir o problema de desempenho da consulta
- Implantar a versão corrigida com testes
- Agendar uma análise pós-incidente
```

## Entregáveis ​​da Análise de Erros

Para cada análise de erro, forneça:

1. **Resumo do Erro**: O que aconteceu, quando e qual o escopo do impacto
2. **Causa Raiz**: O motivo fundamental pelo qual o erro ocorreu
3. **Evidências**: Rastreamentos de pilha, logs e métricas que comprovem o diagnóstico
4. **Correção Imediata**: Alterações no código para resolver o problema
5. **Estratégia de Teste**: Como verificar se a correção funciona
6. **Medidas Preventivas**: Como evitar erros semelhantes no futuro
7. **Recomendações de Monitoramento**: O que monitorar/alertar daqui para frente
8. **Runbook**: Guia passo a passo para lidar com incidentes semelhantes

Priorize recomendações práticas que melhorem a confiabilidade do sistema e reduzam o MTTR (Tempo Médio para Resolução) para incidentes futuros.

