# Guia de Implementação de Padrões de Microsserviços

Este arquivo contém padrões detalhados, listas de verificação e exemplos de código referenciados pela habilidade.

# Padrões de Microsserviços

Domine os padrões de arquitetura de microsserviços, incluindo limites de serviço, comunicação entre serviços, gerenciamento de dados e padrões de resiliência para a construção de sistemas distribuídos.

## Use esta habilidade quando:

- Decompor monolitos em microsserviços
- Projetar limites e contratos de serviço
- Implementar comunicação entre serviços
- Gerenciar dados e transações distribuídas
- Construir sistemas distribuídos resilientes
- Implementar descoberta de serviços e balanceamento de carga
- Projetar arquiteturas orientadas a eventos

## Não use esta habilidade quando:

- O sistema for pequeno o suficiente para um monolito modular
- Você precisar de um protótipo rápido sem a complexidade da distribuição
- Não houver suporte operacional para sistemas distribuídos

## Instruções

1. Identifique os limites de domínio e a propriedade de cada serviço.

2. Defina contratos, propriedade de dados e padrões de comunicação.

3. Planeje a resiliência, a observabilidade e a estratégia de implantação.

4. Forneça etapas de migração e diretrizes operacionais.

## Conceitos Essenciais

### 1. Estratégias de Decomposição de Serviços

**Por Capacidade de Negócio**

- Organizar os serviços em torno das funções de negócio
- Cada serviço possui seu próprio domínio
- Exemplo: OrderService, PaymentService, InventoryService

**Por Subdomínio (DDD)**

- Domínio principal, com subdomínios de suporte
- Contextos delimitados mapeados para os serviços
- Propriedade e responsabilidade claras

**Padrão Strangler Fig**

- Extrair gradualmente do monolito
- Novas funcionalidades como microsserviços
- Rotas proxy para sistemas antigos/novos

### 2. Padrões de Comunicação

**Síncrono (Requisição/Resposta)**

- APIs REST
- gRPC
- GraphQL

**Assíncrono (Eventos/Mensagens)**

- Streaming de eventos (Kafka)
- Filas de mensagens (RabbitMQ, SQS)
- Padrões Pub/Sub

### 3. Gerenciamento de Dados

**Banco de Dados Per Serviço**

- Cada serviço possui seus próprios dados
- Sem bancos de dados compartilhados
- Baixo acoplamento

**Padrão Saga**

- Transações distribuídas
- Ações compensatórias
- Consistência eventual

### 4. Padrões de Resiliência

**Disjuntor**

- Falha rápida em erros repetidos
- Prevenção de falhas em cascata

**Repetição com Backoff**

- Tratamento de falhas transitórias
- Backoff exponencial

**Bulkhead**

- Isolamento de recursos
- Limitação do impacto de falhas

## Padrões de Decomposição de Serviços

### Padrão 1: Por Capacidade de Negócio

```python
# Exemplo de e-commerce

# Serviço de Pedidos
class OrderService:

""Lida com o ciclo de vida do pedido."""

async def create_order(self, order_data: dict) -> Order:

order = Order.create(order_data)

# Publica o evento para outros serviços

await self.event_bus.publish(
OrderCreatedEvent(
order_id=order.id,

customer_id=order.customer_id,

items=order.items,

total=order.total
)

)

return order

# Serviço de Pagamento (serviço separado)
class PaymentService:

""Lida com o processamento de pagamentos."""

async def process_payment(self, payment_request: PaymentRequest) -> PaymentResult:

# Processa o pagamento

result = await self.payment_gateway.charge(
amount=payment_request.amount,

customer=payment_request.customer_id
)

if result.success:

await self.event_bus.publish(
PaymentCompletedEvent(
order_id=payment_request.order_id,

transaction_id=result.transaction_id
)

)

return result
# Serviço de Inventário (serviço separado)
class InventoryService:

""Gerencia o inventário."""

async def reserve_items(self, order_id: str, items: List[OrderItem]) -> ReservationResult:

# Verificar disponibilidade

for item in items:

available = await self.inventory_repo.get_available(item.product_id)

if available < item.quantity:

return ReservationResult(

success=False,

error=f"Insufficient stock for {item.product_id}"

)

# Reservar itens

reservation = await self.create_reservation(order_id, items)

await self.event_bus.publish(
EventoDeReservaDeInventário(
order_id=order_id,

reservation_id=reservation.id

)

)

return ReservationResult(success=True, reservation=reservation)
```

### Padrão 2: Gateway de API

```python
from fastapi import FastAPI, HTTPException, Depends
import httpx
from circuitbreaker import circuit

app = FastAPI()

class APIGateway:

""Ponto de entrada central para todas as solicitações do cliente."""

def __init__(self):

self.order_service_url = "http://order-service:8000"

self.payment_service_url = "http://payment-service:8001"

self.inventory_service_url = "http://inventory-service:8002"

self.http_client = httpx.AsyncClient(timeout=5.0)

@circuit(failure_threshold=5, recovery_timeout=30)

async def call_order_service(self, path: str, method: str = "GET", **kwargs):

""Chama o serviço de pedidos com disjuntor."""

response = await self.http_client.request(

method,

f"{self.order_service_url}{path}",

**kwargs

)
response.raise_for_status()

return response.json()

async def create_order_aggregate(self, order_id: str) -> dict:

""Agrega dados de múltiplos serviços."""

# Requisições paralelas
order, payment, inventory = await asyncio.gather(

self.call_order_service(f"/orders/{order_id}"),

self.call_payment_service(f"/payments/order/{order_id}"),
self.call_inventory_service(f"/reservations/order/{order_id}"),

return_exceptions=True



# Lidar com falhas parciais

result = {"order": order}

if not isinstance(payment, Exception):

result["payment"] = payment

if not isinstance(inventory, Exception):

result["inventory"] = inventory

return result

@app.post("/api/orders")
async def create_order(

order_data: dict,

gateway: APIGateway = Depends()

""Endpoint do API Gateway."""

try:

# Rota para o serviço de pedidos

order = await gateway.call_order_service(

"/orders",

method="POST",

json=order_data

)

return {"order": order}

except httpx.HTTPError as e:

raise HTTPException(status_code=503, detail="Serviço de pedidos" indisponível")
```

## Padrões de Comunicação

### Padrão 1: Comunicação REST Síncrona

```python
# Serviço A chama o Serviço B
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

class ServiceClient:

""Cliente HTTP com tentativas e tempo limite."""

def __init__(self, base_url: str):

self.base_url = base_url

self.client = httpx.AsyncClient(
timeout=httpx.Timeout(5.0, connect=2.0),

limits=httpx.Limits(max_keepalive_connections=20)

)

@retry(
stop=stop_after_attempt(3),

wait=wait_exponential(multiplier=1, min=2, max=10)

)

async def get(self, path: str, **kwargs):

""GET com novas tentativas automáticas."""

response = await self.client.get(f"{self.base_url}{path}", **kwargs)

response.raise_for_status()

return response.json()

async def post(self, path: str, **kwargs):

""Requisição POST."""

response = await self.client.post(f"{self.base_url}{path}", **kwargs)

response.raise_for_status()

return response.json()

# Uso
payment_client = ServiceClient("http://payment-service:8001")
result = await payment_client.post("/payments", json=payment_data)
```

arquiteto sênior, padrões de arquitetura, padrões de microsserviços, arquiteto de event sourcing, implementação de CQRS, orquestração de sagas, padrões de projeção, design orientado a domínio

# Serviço de Inventário (serviço separado)
class InventoryService:

""Gerencia o inventário."""

async def reserve_items(self, order_id: str, items: List[OrderItem]) -> ReservationResult:

# Verificar disponibilidade

for item in items:

available = await self.inventory_repo.get_available(item.product_id)

if available < item.quantity:

return ReservationResult(

success=False,

error=f"Insufficient stock for {item.product_id}"

)

# Reservar itens

reservation = await self.create_reservation(order_id, items)

await self.event_bus.publish(
EventoDeReservaDeInventário(
order_id=order_id,

reservation_id=reservation.id

)

)

return ReservationResult(success=True, reservation=reservation)
```

### Padrão 2: Gateway de API

```python
from fastapi import FastAPI, HTTPException, Depends
import httpx
from circuitbreaker import circuit

app = FastAPI()

class APIGateway:

""Ponto de entrada central para todas as solicitações do cliente."""

def __init__(self):

self.order_service_url = "http://order-service:8000"

self.payment_service_url = "http://payment-service:8001"

self.inventory_service_url = "http://inventory-service:8002"

self.http_client = httpx.AsyncClient(timeout=5.0)

@circuit(failure_threshold=5, recovery_timeout=30)

async def call_order_service(self, path: str, method: str = "GET", **kwargs):

""Chama o serviço de pedidos com disjuntor."""

response = await self.http_client.request(

method,

f"{self.order_service_url}{path}",

**kwargs

)
response.raise_for_status()

return response.json()

async def create_order_aggregate(self, order_id: str) -> dict:

""Agrega dados de múltiplos serviços."""

# Requisições paralelas
order, payment, inventory = await asyncio.gather(

self.call_order_service(f"/orders/{order_id}"),

self.call_payment_service(f"/payments/order/{order_id}"),
self.call_inventory_service(f"/reservations/order/{order_id}"),

return_exceptions=True



# Lidar com falhas parciais

result = {"order": order}

if not isinstance(payment, Exception):

result["payment"] = payment

if not isinstance(inventory, Exception):

result["inventory"] = inventory

return result

@app.post("/api/orders")
async def create_order(

order_data: dict,

gateway: APIGateway = Depends()

""Endpoint do API Gateway."""

try:

# Rota para o serviço de pedidos

order = await gateway.call_order_service(

"/orders",

method="POST",

json=order_data

)

return {"order": order}

except httpx.HTTPError as e:

raise HTTPException(status_code=503, detail="Serviço de pedidos" indisponível")
```

## Padrões de Comunicação

### Padrão 1: Comunicação REST Síncrona

```python
# Serviço A chama o Serviço B
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

class ServiceClient:

""Cliente HTTP com tentativas e tempo limite."""

def __init__(self, base_url: str):

self.base_url = base_url

self.client = httpx.AsyncClient(
timeout=httpx.Timeout(5.0, connect=2.0),

limits=httpx.Limits(max_keepalive_connections=20)

)

@retry(
stop=stop_after_attempt(3),

wait=wait_exponential(multiplier=1, min=2, max=10)

)

async def get(self, path: str, **kwargs):

""GET com novas tentativas automáticas."""

response = await self.client.get(f"{self.base_url}{path}", **kwargs)

response.raise_for_status()

return response.json()

async def post(self, path: str, **kwargs):

""Requisição POST."""

response = await self.client.post(f"{self.base_url}{path}", **kwargs)

response.raise_for_status()

return response.json()

# Uso
payment_client = ServiceClient("http://payment-service:8001")
result = await payment_client.post("/payments", json=payment_data)
```

### Padrão 2: Assíncrono Orientado a Eventos

```python
# Comunicação orientada a eventos com Kafka
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class DomainEvent:

event_id: str

event_type: str

aggregate_id: str

occurrence_at: datetime

data: dict

class EventBus:

""Publicação e assinatura de eventos."""

def __init__(self, bootstrap_servers: List[str]):

self.bootstrap_servers = bootstrap_servers

self.producer = None

async def start(self):

self.producer = AIOKafkaProducer(
bootstrap_servers=self.bootstrap_servers,

value_serializer=lambda v: json.dumps(v).encode()

)

await self.producer.start()


async def publish(self, event: DomainEvent):

""Publicar evento no tópico do Kafka."""

topic = event.event_type

await self.producer.send_and_wait(
topic,

value=asdict(event),

key=event.aggregate_id.encode()
)

async def subscribe(self, topic: str, handler: callable):

""Inscrever-se em eventos."""
consumer = AIOKafkaConsumer(
topic,

bootstrap_servers=self.bootstrap_servers,

value_deserializer=lambda v: json.loads(v.decode()),

group_id="my-service"

)

await consumer.start()

try:

async for message in consumer:

event_data = message.value

await handler(event_data)

finalmente:

await consumer.stop()

# O Serviço de Pedidos publica o evento
async def create_order(order_data: dict):

order = await save_order(order_data)

event = DomainEvent(
event_id=str(uuid.uuid4()),

event_type="OrderCreated",

aggregate_id=order.id,

occurred_at=datetime.now(),

data={

"order_id": order.id,

"customer_id": order.customer_id,

"total": order.total

}

)

await event_bus.publish(event)

# O Serviço de Estoque escuta o evento OrderCreated
async def handle_order_created(event_data: dict):

""Reage à criação do pedido."""
order_id = event_data["data"]["order_id"]

items = event_data["data"]["items"]

# Reservar estoque

await reserve_inventory(order_id, items)
```

### Padrão 3: Padrão Saga (Transações Distribuídas)

```python
# Orquestração de saga para atendimento de pedidos
from enum import Enum
from typing import List, Callable

class SagaStep:

""Etapa única na saga."""

def __init__(

self,

name: str,

action: Callable,

compensation: Callable

):

self.name = name

self.action = action

self.compensation = compensation

class SagaStatus(Enum):

PENDING = "pending"

COMPLETED = "completed"

COMPENSATING = "compensating"

FAILED = "failed"

class OrderFulfillmentSaga:

""Saga orquestrada para atendimento de pedidos."""

def __init__(self):

self.steps: List[SagaStep] = [

SagaStep(
"create_order",

action=self.create_order,

compensation=self.cancel_order

),

SagaStep(

"reserve_inventory",

action=self.reserve_inventory,

compensation=self.release_inventory

),

SagaStep(

"process_payment",

action=self.process_payment,

compensation=self.refund_payment

),

SagaStep(

"confirm_order",

action=self.confirm_order,

compensation=self.cancel_order_confirmation

)

]

async def execute(self, order_data: dict) -> SagaResult:

""Executar etapas da saga."""

completed_steps = []

context = {"order_data": order_data}

try:

for step in self.steps:

# Executar etapa
resultado = await passo.ação(contexto)

if not resultado.success:

# Compensar

await self.compensar(passos_concluídos, contexto)

retornar SagaResult(
status=SagaStatus.FAILED,

erro=resultado.error

)

passos_concluídos.append(passo)

contexto.update(resultado.data)

retornar SagaResult(status=SagaStatus.COMPLETED, data=contexto)

except Exception as e:

# Compensar em caso de erro

await self.compensar(passos_concluídos, contexto)

retornar SagaResult(status=SagaStatus.FAILED, erro=str(e))

async def compensar(self, passos_concluídos: List[SagaStep], contexto: dict):

""Executar ações compensatórias na revisão

## Padrões de Resiliência

### Padrão Circuit Breaker

```python
from enum import Enum
from datetime import datetime, timedelta
from typing import Callable, Any

class CircuitState(Enum):

CLOSED = "closed" # Operação normal

OPEN = "open" # Falha, rejeita solicitações

HALF_OPEN = "half_open" # Testando se recuperado

class CircuitBreaker:

""Disjuntor para chamadas de serviço."""

def __init__(

self,

failure_threshold: int = 5,

recovery_timeout: int = 30,

success_threshold: int = 2

):

self.failure_threshold = failure_threshold

self.recovery_timeout = recovery_timeout

self.success_threshold = success_threshold

self.failure_count = 0
self.success_count = 0

self.state = CircuitState.CLOSED

self.opened_at = None

async def call(self, func: Callable, *args, **kwargs) -> Any:

""Executa a função com o disjuntor."""

if self.state == CircuitState.OPEN:

if self._should_attempt_reset():

self.state = CircuitState.HALF_OPEN

else:

raise CircuitBreakerOpenError("Disjuntor aberto")

try:

result = await func(*args, **kwargs)

self._on_success()

return result

except Exception as e:

self._on_failure()

raise

def _on_success(self):

""Lida com a chamada bem-sucedida."""

self.failure_count = 0

if self.state == CircuitState.HALF_OPEN:

self.success_count += 1

if self.success_count >= self.success_threshold:

self.state = CircuitState.CLOSED

self.success_count = 0

def _on_failure(self):

""Lida com a chamada com falha."""

self.failure_count += 1

if self.failure_count >= self.failure_threshold:

self.state = CircuitState.OPEN

self.opened_at = datetime.now()

if self.state == CircuitState.HALF_OPEN:

self.state = CircuitState.OPEN

self.opened_at = datetime.now()

def _should_attempt_reset(self) -> bool:

""Verifica se passou tempo suficiente para tentar novamente."""

return (
datetime.now() - self.opened_at

> timedelta(seconds=self.recovery_timeout)

)

# Uso
breaker = CircuitBreaker(failure_threshold=5, recovery_timeout=30)

async def call_payment_service(payment_data: dict):

return await breaker.call(
payment_client.process_payment,

payment_data
)
```

## Recursos

- **references/service-decomposition-guide.md**: Desmembrando monolitos
- **references/communication-patterns.md**: Padrões síncronos vs. assíncronos
- **references/saga-implementation.md**: Transações distribuídas
- **assets/circuit-breaker.py**: Circuit Breaker de produção
- **assets/event-bus-template.py**: Implementação do barramento de eventos Kafka
- **assets/api-gateway-template.py**: Gateway de API completo

## Melhores Práticas

1. **Limites de Serviço**: Alinhar com as capacidades de negócio
2. **Banco de Dados por Serviço**: Sem bancos de dados compartilhados
3. **Contratos de API**: Versionados e retrocompatíveis
4. **Assíncrono Sempre que Possível**: Eventos em vez de chamadas diretas
5. **Disjuntores**: Falha rápida em caso de falhas de serviço
6. **Rastreamento Distribuído**: Rastrear requisições entre serviços
7. **Registro de Serviços**: Descoberta dinâmica de serviços
8. **Verificações de Saúde**: Sondagens de disponibilidade e prontidão

## Armadilhas Comuns

- **Monólito Distribuído**: Serviços fortemente acoplados
- **Serviços Verborrágicos**: Muitas chamadas entre serviços
- **Bancos de Dados Compartilhados**: Acoplamento forte por meio de dados
- **Sem Disjuntores**: Falhas em cascata
- **Tudo Síncrono**: Acoplamento forte, baixa resiliência
- **Microsserviços Prematuros**: Começar com microsserviços
- **Ignorar Falhas de Rede**: Assumir rede confiável
- **Sem lógica de compensação**: Não é possível desfazer transações com falha.