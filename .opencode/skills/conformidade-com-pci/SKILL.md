---
name: conformidade-com-pci
description: "Conformidade Master PCI DSS (padrão de segurança de dados da indústria de cartões de pagamento) para processamento seguro de pagamentos e manuseio de dados do titular do cartão."
risk: desconhecido
source: comunidade
date_added: "2026/02/27"
---

# Conformidade com PCI

Domine a conformidade com PCI DSS (padrão de segurança de dados da indústria de cartões de pagamento) para processamento seguro de pagamentos e manuseio de dados do titular do cartão.

## Não use esta habilidade quando

- A tarefa não está relacionada à conformidade com PCI
- Você precisa de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça metas, restrições e insumos necessários.
- Aplicar as melhores práticas relevantes e validar os resultados.
- Fornece etapas acionáveis ​​e verificação.
- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Use esta habilidade quando

- Construção de sistemas de processamento de pagamentos
- Tratamento de informações de cartão de crédito
- Implementação de fluxos de pagamento seguros
- Condução de auditorias de conformidade PCI
- Redução do escopo de conformidade com PCI
- Implementação de tokenização e criptografia
- Preparação para avaliações PCI DSS

## Requisitos PCI DSS (12 requisitos principais)

### Construa e mantenha uma rede segura
1. Instale e mantenha a configuração do firewall
2. Não use padrões fornecidos pelo fornecedor para senhas

### Proteja os dados do titular do cartão
3. Proteja os dados armazenados do titular do cartão
4. Criptografar a transmissão de dados do titular do cartão em redes públicas

### Mantenha o gerenciamento de vulnerabilidades
5. Proteja os sistemas contra malware
6. Desenvolva e mantenha sistemas e aplicativos seguros

### Implemente um forte controle de acesso
7. Restringir o acesso aos dados do titular do cartão de acordo com a necessidade comercial
8. Identifique e autentique o acesso aos componentes do sistema
9. Restringir o acesso físico aos dados do titular do cartão

### Monitore e teste redes
10. Rastreie e monitore todos os acessos aos recursos da rede e dados do titular do cartão
11. Teste regularmente sistemas e processos de segurança

### Manter a Política de Segurança da Informação
12. Mantenha uma política que aborde a segurança da informação

## Níveis de conformidade

**Nível 1**: > 6 milhões de transações/ano (ROC anual necessário)
**Nível 2**: 1 a 6 milhões de transações/ano (SAQ anual)
**Nível 3**: 20.000 a 1 milhão de transações de comércio eletrônico/ano
**Nível 4**: < 20.000 comércio eletrônico ou < 1 milhão de transações totais

## Data Minimization (Never Store)

```python
# NEVER STORE THESE
PROHIBITED_DATA = {
    'full_track_data': 'Magnetic stripe data',
    'cvv': 'Card verification code/value',
    'pin': 'PIN or PIN block'
}

# CAN STORE (if encrypted)
ALLOWED_DATA = {
    'pan': 'Primary Account Number (card number)',
    'cardholder_name': 'Name on card',
    'expiration_date': 'Card expiration',
    'service_code': 'Service code'
}

class PaymentData:
    """Safe payment data handling."""

    def __init__(self):
        self.prohibited_fields = ['cvv', 'cvv2', 'cvc', 'pin']

    def sanitize_log(self, data):
        """Remove sensitive data from logs."""
        sanitized = data.copy()

        # Mask PAN
        if 'card_number' in sanitized:
            card = sanitized['card_number']
            sanitized['card_number'] = f"{card[:6]}{'*' * (len(card) - 10)}{card[-4:]}"

        # Remove prohibited data
        for field in self.prohibited_fields:
            sanitized.pop(field, None)

        return sanitized

    def validate_no_prohibited_storage(self, data):
        """Ensure no prohibited data is being stored."""
        for field in self.prohibited_fields:
            if field in data:
                raise SecurityError(f"Attempting to store prohibited field: {field}")
```

## Tokenization

### Using Payment Processor Tokens
```python
import stripe

class TokenizedPayment:
    """Handle payments using tokens (no card data on server)."""

    @staticmethod
    def create_payment_method_token(card_details):
        """Create token from card details (client-side only)."""
        # THIS SHOULD ONLY BE DONE CLIENT-SIDE WITH STRIPE.JS
        # NEVER send card details to your server

        """
        // Frontend JavaScript
        const stripe = Stripe('pk_...');

        const {token, error} = await stripe.createToken({
            card: {
                number: '4242424242424242',
                exp_month: 12,
                exp_year: 2024,
                cvc: '123'
            }
        });

        // Send token.id to server (NOT card details)
        """
        pass

    @staticmethod
    def charge_with_token(token_id, amount):
        """Charge using token (server-side)."""
        # Your server only sees the token, never the card number
        stripe.api_key = "sk_..."

        charge = stripe.Charge.create(
            amount=amount,
            currency="usd",
            source=token_id,  # Token instead of card details
            description="Payment"
        )

        return charge

    @staticmethod
    def store_payment_method(customer_id, payment_method_token):
        """Store payment method as token for future use."""
        stripe.Customer.modify(
            customer_id,
            source=payment_method_token
        )

        # Store only customer_id and payment_method_id in your database
        # NEVER store actual card details
        return {
            'customer_id': customer_id,
            'has_payment_method': True
            # DO NOT store: card number, CVV, etc.
        }
```

### Custom Tokenization (Advanced)
```python
import secrets
from cryptography.fernet import Fernet

class TokenVault:
    """Secure token vault for card data (if you must store it)."""

    def __init__(self, encryption_key):
        self.cipher = Fernet(encryption_key)
        self.vault = {}  # In production: use encrypted database

    def tokenize(self, card_data):
        """Convert card data to token."""
        # Generate secure random token
        token = secrets.token_urlsafe(32)

        # Encrypt card data
        encrypted = self.cipher.encrypt(json.dumps(card_data).encode())

        # Store token -> encrypted data mapping
        self.vault[token] = encrypted

        return token

    def detokenize(self, token):
        """Retrieve card data from token."""
        encrypted = self.vault.get(token)
        if not encrypted:
            raise ValueError("Token not found")

        # Decrypt
        decrypted = self.cipher.decrypt(encrypted)
        return json.loads(decrypted.decode())

    def delete_token(self, token):
        """Remove token from vault."""
        self.vault.pop(token, None)
```

## Encryption

### Data at Rest
```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

class EncryptedStorage:
    """Encrypt data at rest using AES-256-GCM."""

    def __init__(self, encryption_key):
        """Initialize with 256-bit key."""
        self.key = encryption_key  # Must be 32 bytes

    def encrypt(self, plaintext):
        """Encrypt data."""
        # Generate random nonce
        nonce = os.urandom(12)

        # Encrypt
        aesgcm = AESGCM(self.key)
        ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)

        # Return nonce + ciphertext
        return nonce + ciphertext

    def decrypt(self, encrypted_data):
        """Decrypt data."""
        # Extract nonce and ciphertext
        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]

        # Decrypt
        aesgcm = AESGCM(self.key)
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)

        return plaintext.decode()

# Usage
storage = EncryptedStorage(os.urandom(32))
encrypted_pan = storage.encrypt("4242424242424242")
# Store encrypted_pan in database
```

### Data in Transit
```python
# Always use TLS 1.2 or higher
# Flask/Django example
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'

# Enforce HTTPS
from flask_talisman import Talisman
Talisman(app, force_https=True)
```

## Access Control

```python
from functools import wraps
from flask import session

def require_pci_access(f):
    """Decorator to restrict access to cardholder data."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = session.get('user')

        # Check if user has PCI access role
        if not user or 'pci_access' not in user.get('roles', []):
            return {'error': 'Unauthorized access to cardholder data'}, 403

        # Log access attempt
        audit_log(
            user=user['id'],
            action='access_cardholder_data',
            resource=f.__name__
        )

        return f(*args, **kwargs)

    return decorated_function

@app.route('/api/payment-methods')
@require_pci_access
def get_payment_methods():
    """Retrieve payment methods (restricted access)."""
    # Only accessible to users with pci_access role
    pass
```

## Audit Logging

```python
import logging
from datetime import datetime

class PCIAuditLogger:
    """PCI-compliant audit logging."""

    def __init__(self):
        self.logger = logging.getLogger('pci_audit')
        # Configure to write to secure, append-only log

    def log_access(self, user_id, resource, action, result):
        """Log access to cardholder data."""
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'user_id': user_id,
            'resource': resource,
            'action': action,
            'result': result,
            'ip_address': request.remote_addr
        }

        self.logger.info(json.dumps(entry))

    def log_authentication(self, user_id, success, method):
        """Log authentication attempt."""
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'user_id': user_id,
            'event': 'authentication',
            'success': success,
            'method': method,
            'ip_address': request.remote_addr
        }

        self.logger.info(json.dumps(entry))

# Usage
audit = PCIAuditLogger()
audit.log_access(user_id=123, resource='payment_methods', action='read', result='success')
```

## Security Best Practices

### Input Validation
```python
import re

def validate_card_number(card_number):
    """Validate card number format (Luhn algorithm)."""
    # Remove spaces and dashes
    card_number = re.sub(r'[\s-]', '', card_number)

    # Check if all digits
    if not card_number.isdigit():
        return False

    # Luhn algorithm
    def luhn_checksum(card_num):
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_num)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    return luhn_checksum(card_number) == 0

def sanitize_input(user_input):
    """Sanitize user input to prevent injection."""
    # Remove special characters
    # Validate against expected format
    # Escape for database queries
    pass
```

## PCI DSS SAQ (Self-Assessment Questionnaire)

### SAQ A (Least Requirements)
- E-commerce using hosted payment page
- No card data on your systems
- ~20 questions

### SAQ A-EP
- E-commerce with embedded payment form
- Uses JavaScript to handle card data
- ~180 questions

### SAQ D (Most Requirements)
- Store, process, or transmit card data
- Full PCI DSS requirements
- ~300 questions

## Compliance Checklist

```python
PCI_COMPLIANCE_CHECKLIST = {
    'network_security': [
        'Firewall configured and maintained',
        'No vendor default passwords',
        'Network segmentation implemented'
    ],
    'data_protection': [
        'No storage of CVV, track data, or PIN',
        'PAN encrypted when stored',
        'PAN masked when displayed',
        'Encryption keys properly managed'
    ],
    'vulnerability_management': [
        'Anti-virus installed and updated',
        'Secure development practices',
        'Regular security patches',
        'Vulnerability scanning performed'
    ],
    'access_control': [
        'Access restricted by role',
        'Unique IDs for all users',
        'Multi-factor authentication',
        'Physical security measures'
    ],
    'monitoring': [
        'Audit logs enabled',
        'Log review process',
        'File integrity monitoring',
        'Regular security testing'
    ],
    'policy': [
        'Security policy documented',
        'Risk assessment performed',
        'Security awareness training',
        'Incident response plan'
    ]
}
```

## Recursos

- **references/data-minimization.md**: Nunca armazene dados proibidos
- **references/tokenization.md**: Estratégias de tokenização
- **references/encryption.md**: Requisitos de criptografia
- **references/access-control.md**: acesso baseado em função
- **references/audit-logging.md**: registro abrangente
- **assets/pci-compliance-checklist.md**: lista de verificação completa
- **assets/encrypted-storage.py**: utilitários de criptografia
- **scripts/audit-payment-system.sh**: script de auditoria de conformidade

## Violações Comuns

1. **Armazenamento de CVV**: Nunca armazene códigos de verificação de cartão
2. **PAN não criptografado**: os números dos cartões devem ser criptografados em repouso
3. **Criptografia Fraca**: Use AES-256 ou equivalente
4. **Sem controles de acesso**: restrinja quem pode acessar os dados do titular do cartão
5. **Registros de auditoria ausentes**: deve registrar todos os acessos aos dados de pagamento
6. **Transmissão Insegura**: Sempre use TLS 1.2+
7. **Senhas padrão**: altere todas as credenciais padrão
8. **Sem testes de segurança**: testes de penetração regulares são necessários

## Reduzindo o escopo do PCI

1. **Use pagamentos hospedados**: Stripe Checkout, PayPal, etc.
2. **Tokenização**: Substitua os dados do cartão por tokens
3. **Segmentação de rede**: isole o ambiente de dados do titular do cartão
4. **Terceirizar**: Use processadores de pagamento compatíveis com PCI
5. **Sem armazenamento**: Nunca armazene detalhes completos do cartão

Ao minimizar os sistemas que lidam com os dados do cartão, você reduz significativamente a carga de conformidade.