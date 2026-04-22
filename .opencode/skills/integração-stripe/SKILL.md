--- 
name: integração-stripe
description: "Integração de processamento de pagamentos com o Stripe para fluxos de pagamento robustos e em conformidade com o PCI, incluindo finalização de compra, assinaturas, webhooks e reembolsos."
risk: desconhecido
source: comunidade
date_added: "27/02/2026"
---

# Integração com o Stripe

Integração de processamento de pagamentos com o Stripe para fluxos de pagamento robustos e em conformidade com o PCI, incluindo finalização de compra, assinaturas, webhooks e reembolsos.

## Não use esta habilidade quando

- A tarefa não estiver relacionada à integração com o Stripe
- Você precisar de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Use esta habilidade quando:

- Implementar processamento de pagamentos em aplicativos web/mobile
- Configurar sistemas de cobrança por assinatura
- Lidar com pagamentos únicos e cobranças recorrentes
- Processar reembolsos e contestações
- Gerenciar métodos de pagamento de clientes
- Implementar SCA (Autenticação Forte do Cliente) para pagamentos europeus
- Criar fluxos de pagamento para marketplaces com o Stripe Connect

## Conceitos Essenciais

### 1. Fluxos de Pagamento
**Sessão de Checkout (Hospedada)**
- Página de pagamento hospedada pelo Stripe
- Carga mínima de conformidade com PCI
- Implementação mais rápida
- Suporta pagamentos únicos e recorrentes

**Intenções de Pagamento (Interface Personalizada)**
- Controle total sobre a interface de pagamento
- Requer Stripe.js para conformidade com PCI
- Implementação mais complexa
- Melhores opções de personalização

**Intenções de Configuração (Salvar Métodos de Pagamento)**
- Coletar método de pagamento sem cobrar
- Usado para assinaturas e pagamentos futuros
- Requer confirmação do cliente

### 2. Webhooks
**Eventos Críticos:**
- `payment_intent.succeeded`: Pagamento concluído
- `payment_intent.payment_failed`: Pagamento falhou
- `customer.subscription.updated`: Assinatura alterada
- `customer.subscription.deleted`: Assinatura cancelada
- `charge.refunded`: Reembolso processado
- `invoice.payment_succeeded`: Pagamento da assinatura realizado com sucesso

### 3. Assinaturas
**Componentes:**
- **Produto**: O que você está vendendo
- **Preço**: Quanto custa e com que frequência
- **Assinatura**: Pagamento recorrente do cliente
- **Fatura**: Gerada a cada ciclo de faturamento

### 4. Gerenciamento de Clientes
- Criar e gerenciar registros de clientes
- Armazenar múltiplos métodos de pagamento
- Rastrear metadados do cliente
- Gerenciar detalhes de faturamento

## Início Rápido

```python
import stripe

stripe.api_key = "sk_test_..."

# Criar uma sessão de checkout
session = stripe.checkout.Session.create(
payment_method_types=['card'],

line_items=[{

'price_data': {

'currency': 'usd',

'product_data': {

'name': 'Assinatura Premium',

},

'unit_amount': 2000, # $20.00

'recurring': {

'interval': 'month',

},

},

'quantity': 1,

}],

mode='subscription',

success_url='https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID}',

cancel_url='https://yourdomain.com/cancel',

)

# Redirecionar o usuário para session.url
print(session.url)
```

## Padrões de Implementação de Pagamento

### Padrão 1: Pagamento Único (Checkout Hospedado)
```python
def create_checkout_session(amount, currency='usd'):

""Cria uma sessão de checkout para pagamento único."""

try:

session = stripe.checkout.Session.create(
payment_method_types=['card'],

line_items=[{

'price_data': {

'currency': currency,

'product_data': {

'name': 'Compra',

'images': ['https://example.com/product.jpg'],

},

'unit_amount': amount, # Valor em centavos

},

'quantity': 1,

}],

mode='payment',
success_url='https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID}',

cancel_url='https://yourdomain.com/cancel',

metadata={

'order_id': 'order_123',

'user_id': 'user_456'

}

)

return session

except stripe.error.StripeError as e:

# Tratar erro

print(f"Erro do Stripe: {e.user_message}")

raise
```
### Padrão 2: Fluxo de Intenção de Pagamento Personalizado
```python
def create_payment_intent(amount, currency='usd', customer_id=None):

""Cria uma intenção de pagamento para a interface de checkout personalizada."""

intent = stripe.PaymentIntent.create(

amount=amount,

currency=currency,

customer=customer_id,

automatic_payment_methods={

'enabled': True,

},

metadata={

'integration_check': 'accept_a_payment'

}

)

return intent.client_secret # Enviar para o frontend

# Frontend (JavaScript)
"""
const stripe = Stripe('pk_test_...');
const elements = stripe.elements();
const cardElement = elements.create('card');
cardElement.mount('#card-element');

const {error, paymentIntent} = await stripe.confirmCardPayment(
clientSecret,

{
payment_method: {

card: cardElement,

billing_details: {

name: 'Nome do Cliente'

}
}

}
);

if (error) {
// Tratar erro
} else if (paymentIntent.status === 'succeeded') {
// Pagamento bem-sucedido
}
"""
```

### Padrão 3: Criação de Assinatura
```python
def create_subscription(customer_id, price_id):

"""Cria uma assinatura para um cliente."""

try:

subscription = stripe.Subscription.create(
customer=customer_id,

items=[{'price': price_id}],

payment_behavior='default_incomplete',

payment_settings={'save_default_payment_method': 'on_subscription'},

expand=['latest_invoice.payment_intent'],

)

return {

'subscription_id': subscription.id,

'client_secret': subscription.latest_invoice.payment_intent.client_secret

}

except stripe.error.StripeError as e:

print(f"Falha na criação da assinatura: {e}")

raise
```

### Padrão 4: Portal do Cliente
```python
def create_customer_portal_session(customer_id):

"""Cria uma sessão no portal para que os clientes gerenciem suas assinaturas."""
session = stripe.billing_portal.Session.create(

customer=customer_id,

return_url='https://yourdomain.com/account',

)

return session.url # Redireciona o cliente para cá
```

## Tratamento de Webhook

### Webhook Seguro Endpoint
```python
from flask import Flask, request
import stripe

app = Flask(__name__)

endpoint_secret = 'whsec_...'

@app.route('/webhook', methods=['POST'])
def webhook():

payload = request.data

sig_header = request.headers.get('Stripe-Signature')

try:

event = stripe.Webhook.construct_event(

payload, sig_header, endpoint_secret

)

except ValueError:

# Payload inválido
return 'Payload inválido', 400

except stripe.error.SignatureVerificationError:

# Assinatura inválida
return 'Assinatura inválida', 400

# Tratar o evento

if event['type'] == 'payment_intent.succeeded':

payment_intent = event['data']['object']

handle_successful_payment(payment_intent)

elif event['type'] == 'payment_intent.payment_failed':
payment_intent = event['data']['object']

handle_failed_payment(payment_intent)

elif event['type'] == 'customer.subscription.deleted':
subscription = event['data']['object']

handle_subscription_canceled(subscription)

return 'Success', 200

def handle_successful_payment(payment_intent):

""Processar pagamento bem-sucedido."""
customer_id = payment_intent.get('customer')

amount = payment_intent['amount']

metadata = payment_intent.get('metadata', {})

# Atualizar o banco de dados

# Enviar e-mail de confirmação
# Concluir pedido

print(f"Pagamento efetuado com sucesso: {payment_intent['id']}")

def handle_failed_payment(payment_intent):

""Lidar com falha no pagamento."""

error = payment_intent.get('last_payment_error', {})

print(f"Pagamento falhou: {error.get('message')}")

# Notificar o cliente

# Atualizar o status do pedido

def handle_subscription_canceled(subscription):

""Lidar com o cancelamento da assinatura."""

customer_id = subscription['customer']

# Atualizar o acesso do usuário

# Enviar e-mail de cancelamento

print(f"Assinatura cancelada: {subscription['id']}")
```

### Melhores Práticas de Webhook
```python
import hashlib
import hmac

def verify_webhook_signature(payload, signature, secret):

""Verificar o webhook manualmente assinatura."""

assinatura_esperada = hmac.new(

secret.encode('utf-8'),

payload,

hashlib.sha256

).hexdigest()

return hmac.compare_digest(assinatura, assinatura_esperada)

def handle_webhook_idempotently(event_id, handler):

"""Garantir que o webhook seja processado exatamente uma vez."""

# Verificar se o evento já foi processado
if is_event_processed(event_id):

return

# Processar evento

try:

handler()

mark_event_processed(event_id)

except Exception as e:

log_error(e)

# O Stripe tentará novamente os webhooks com falha

raise


## Customer Management

```python
def create_customer(email, name, payment_method_id=None):
    """Create a Stripe customer."""
    customer = stripe.Customer.create(
        email=email,
        name=name,
        payment_method=payment_method_id,
        invoice_settings={
            'default_payment_method': payment_method_id
        } if payment_method_id else None,
        metadata={
            'user_id': '12345'
        }
    )
    return customer

def attach_payment_method(customer_id, payment_method_id):
    """Attach a payment method to a customer."""
    stripe.PaymentMethod.attach(
        payment_method_id,
        customer=customer_id
    )

    # Set as default
    stripe.Customer.modify(
        customer_id,
        invoice_settings={
            'default_payment_method': payment_method_id
        }
    )

def list_customer_payment_methods(customer_id):
    """List all payment methods for a customer."""
    payment_methods = stripe.PaymentMethod.list(
        customer=customer_id,
        type='card'
    )
    return payment_methods.data
```

## Refund Handling

```python
def create_refund(payment_intent_id, amount=None, reason=None):
    """Create a refund."""
    refund_params = {
        'payment_intent': payment_intent_id
    }

    if amount:
        refund_params['amount'] = amount  # Partial refund

    if reason:
        refund_params['reason'] = reason  # 'duplicate', 'fraudulent', 'requested_by_customer'

    refund = stripe.Refund.create(**refund_params)
    return refund

def handle_dispute(charge_id, evidence):
    """Update dispute with evidence."""
    stripe.Dispute.modify(
        charge_id,
        evidence={
            'customer_name': evidence.get('customer_name'),
            'customer_email_address': evidence.get('customer_email'),
            'shipping_documentation': evidence.get('shipping_proof'),
            'customer_communication': evidence.get('communication'),
        }
    )
```

## Testing

```python
# Use test mode keys
stripe.api_key = "sk_test_..."

# Test card numbers
TEST_CARDS = {
    'success': '4242424242424242',
    'declined': '4000000000000002',
    '3d_secure': '4000002500003155',
    'insufficient_funds': '4000000000009995'
}

def test_payment_flow():
    """Test complete payment flow."""
    # Create test customer
    customer = stripe.Customer.create(
        email="test@example.com"
    )

    # Create payment intent
    intent = stripe.PaymentIntent.create(
        amount=1000,
        currency='usd',
        customer=customer.id,
        payment_method_types=['card']
    )

    # Confirm with test card
    confirmed = stripe.PaymentIntent.confirm(
        intent.id,
        payment_method='pm_card_visa'  # Test payment method
    )

    assert confirmed.status == 'succeeded'
```

## Resources

- **references/checkout-flows.md**: Detailed checkout implementation
- **references/webhook-handling.md**: Webhook security and processing
- **references/subscription-management.md**: Subscription lifecycle
- **references/customer-management.md**: Customer and payment method handling
- **references/invoice-generation.md**: Invoicing and billing
- **assets/stripe-client.py**: Production-ready Stripe client wrapper
- **assets/webhook-handler.py**: Complete webhook processor
- **assets/checkout-config.json**: Checkout configuration templates

## Best Practices

1. **Always Use Webhooks**: Don't rely solely on client-side confirmation
2. **Idempotency**: Handle webhook events idempotently
3. **Error Handling**: Gracefully handle all Stripe errors
4. **Test Mode**: Thoroughly test with test keys before production
5. **Metadata**: Use metadata to link Stripe objects to your database
6. **Monitoring**: Track payment success rates and errors
7. **PCI Compliance**: Never handle raw card data on your server
8. **SCA Ready**: Implement 3D Secure for European payments

## Common Pitfalls

- **Not Verifying Webhooks**: Always verify webhook signatures
- **Missing Webhook Events**: Handle all relevant webhook events
- **Hardcoded Amounts**: Use cents/smallest currency unit
- **No Retry Logic**: Implement retries for API calls
- **Ignoring Test Mode**: Test all edge cases with test cards