--- 
name: gerenciamento-de-segredos
description: "Práticas seguras de gerenciamento de segredos para pipelines de CI/CD usando Vault, AWS Secrets Manager e outras ferramentas."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Gerenciamento de Segredos

Práticas seguras de gerenciamento de segredos para pipelines de CI/CD usando Vault, AWS Secrets Manager e outras ferramentas.

## Objetivo

Implementar o gerenciamento seguro de segredos em pipelines de CI/CD sem codificar informações confidenciais diretamente no código.

## Use esta habilidade quando

- Armazenar chaves de API e credenciais
- Gerenciar senhas de banco de dados
- Lidar com certificados TLS
- Rotacionar segredos automaticamente
- Implementar o princípio do menor privilégio

## Não use esta habilidade quando

- Você planeja codificar segredos diretamente no controle de versão
- Você não consegue proteger o acesso ao backend de segredos
- Você precisa apenas de valores de desenvolvimento local sem compartilhá-los

## Instruções

1. Identifique os tipos de segredos, proprietários e requisitos de rotação. 2. Escolha um backend de segredos e um modelo de acesso.

3. Integre CI/CD ou recuperação em tempo de execução com privilégios mínimos.

4. Valide a rotação e o registro de auditoria.

## Segurança

- Nunca inclua segredos no controle de versão.

- Limite o acesso e registre o uso de segredos para fins de auditoria.

- ## Ferramentas de Gerenciamento de Segredos

### HashiCorp Vault
- Gerenciamento centralizado de segredos
- Geração dinâmica de segredos
- Rotação de segredos
- Registro de auditoria
- Controle de acesso granular

### AWS Secrets Manager
- Solução nativa da AWS
- Rotação automática
- Integração com RDS
- Suporte ao CloudFormation

### Azure Key Vault
- Solução nativa do Azure
- Chaves com suporte a HSM
- Gerenciamento de certificados
- Integração com RBAC

### Google Secret Manager
- Solução nativa do GCP
- Versionamento
- Integração com IAM

## Integração com o HashiCorp Vault

### Configuração do Vault

```bash
# Iniciar o servidor de desenvolvimento do Vault
vault server -dev

# Configurar o ambiente
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

# Habilitar o mecanismo de segredos
vault secrets enable -path=secret kv-v2

# Armazenar segredo
vault kv put secret/database/config username=admin password=secret
```

### GitHub Actions com Vault

```yaml
name: Deploy with Vault Secrets
em: [push]

tarefas:

implantar:

executa em: ubuntu-latest

etapas:

- usa: actions/checkout@v4

- nome: Importar Segredos do Vault

usa: hashicorp/vault-action@v2

com:

url: https://vault.example.com:8200

token: ${{ secrets.VAULT_TOKEN }}

segredos: |

secret/data/database username | DB_USERNAME ;

secret/data/database password | DB_PASSWORD ;

secret/data/api key | API_KEY

- nome: Usar segredos

executar: |
echo "Conectando ao banco de dados como $DB_USERNAME"

# Use $DB_PASSWORD, $API_KEY
```

### GitLab CI com Vault

```yaml
deploy:

image: vault:latest

before_script:

- export VAULT_ADDR=https://vault.example.com:8200

- export VAULT_TOKEN=$VAULT_TOKEN

- apk add curl jq

script:

- |
DB_PASSWORD=$(vault kv get -field=password secret/database/config)

API_KEY=$(vault kv get -field=key secret/api/credentials)

echo "Implantando com segredos..."

# Use $DB_PASSWORD, $API_KEY
```

**Referência:** Consulte `references/vault-setup.md`

## AWS Secrets Manager

### Armazenar Segredo

```bash
aws secretsmanager create-secret \

--name production/database/password \

--secret-string "senha-super-secreta"
```

### Recuperar no GitHub Actions

```yaml

- name: Configurar credenciais da AWS

uses: aws-actions/configure-aws-credentials@v4

with:

aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
aws-region: us-west-2

- name: Obter segredo da AWS

run: |

SECRET=$(aws secretsmanager get-secret-value \

--secret-id production/database/password \

--query SecretString \

--output text)

echo "::add-mask::$SECRET"

echo "DB_PASSWORD=$SECRET" >> $GITHUB_ENV

- name: Usar segredo

run: |

# Usar $DB_PASSWORD

./deploy.sh
```

### Terraform com AWS Secrets Manager

```hcl
data "aws_secretsmanager_secret_version" "db_password" {

secret_id = "production/database/password"
}

resource "aws_db_instance" "main" {

allocated_storage = 100

engine = "postgres"

instance_class = "db.t3.large"

username = "admin"

password = jsondecode(data.aws_secretsmanager_secret_version.db_password.secret_string)["password"]
}
```

## Segredos do GitHub

### Segredos da Organização/Repositório

```yaml
- name: Usar segredo do GitHub

run: | echo "Chave da API: ${{ secrets.API_KEY }}"

echo "URL do banco de dados: ${{ secrets.DATABASE_URL }}"
```

### Segredos do ambiente

```yaml
deploy:

runs-on: ubuntu-latest

environment: production

steps:

- name: Deploy

run: |

echo "Implantando com ${{ secrets.PROD_API_KEY }}"
```

**Referência:** Consulte `references/github-secrets.md`

## Variáveis ​​do GitLab CI/CD

### Variáveis ​​do Projeto

```yaml
deploy:

script:

- echo "Implantando com $API_KEY"

- echo "Banco de dados: $DATABASE_URL"
```

### Variáveis ​​Protegidas e Mascaradas
- Protegidas: Disponíveis apenas em branches protegidas
- Mascaradas: Ocultas nos logs de tarefas
- Tipo de arquivo: Armazenadas como arquivo

## Boas Práticas

1. **Nunca faça commit de segredos** no Git
2. **Use segredos diferentes** por ambiente
3. **Rotacione os segredos regularmente**
4. **Implemente o princípio do menor privilégio**
5. **Habilite o registro de auditoria**
6. **Use verificação de segredos** (GitGuardian, TruffleHog)
7. **Mascare segredos em logs**
8. **Criptografe segredos em repouso**
9. **Use tokens de curta duração** sempre que possível
10. **Documente os requisitos de segredo**

## Rotação de Segredos

### Rotação Automatizada com AWS

```python
import boto3
import json
def lambda_handler(event, context):

client = boto3.client('secretsmanager')

# Obter o segredo atual

response = client.get_secret_value(SecretId='my-secret')

current_secret = json.loads(response['SecretString'])

# Gerar nova senha

new_password = generate_strong_password()

# Atualizar a senha do banco de dados

update_database_password(new_password)

# Atualizar o segredo

client.put_secret_value(
SecretId='my-secret',

SecretString=json.dumps({

'username': current_secret['username'],

'password': new_password
})

)

return {'statusCode': 200}
```

### Processo de Rotação Manual

1. Gerar novo segredo
2. Atualizar o segredo no armazenamento de segredos
3. Atualizar os aplicativos para usar o novo segredo segredo
4. Verificar funcionalidade
5. Revogar segredo antigo

## Operador de Segredos Externos

### Integração com Kubernetes

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:

name: vault-backend

namespace: production
spec:

provider:

vault:

server: "https://vault.example.com:8200"

path: "secret"

version: "v2"

auth:

kubernetes:

mountPath: "kubernetes"

role: "production"

---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:

name: database-credentials

namespace: production
spec:

refreshInterval: 1h
secretStoreRef:

name: vault-backend

kind: SecretStore

target:

name: database-credentials

creationPolicy: Owner

data:
- secretKey: username

remoteRef:

key: database/config

property: username

- secretKey: password

remoteRef:

key: database/config

property: password
```

## Verificação de Segredos

### Hook de Pré-commit

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Verificar segredos com TruffleHog
docker run --rm -v "$(pwd):/repo" \

trufflesecurity/trufflehog:latest \

filesystem --directory=/repo

if [ $? -ne 0 ]; then

echo "❌ Segredo detectado! Commit bloqueado."

exit 1
fi
```

### Verificação de Segredos em CI/CD

```yaml
secret-scan:

stage: security

image: trufflesecurity/trufflehog:latest

script:

- trufflehog filesystem .

allow_failure: false
```

## Arquivos de Referência

- `references/vault-setup.md` - Configuração do HashiCorp Vault
- `references/github-secrets.md` - Melhores práticas para Segredos do GitHub

## Habilidades Relacionadas

- `github-actions-templates` - Para integração com o GitHub Actions
- `gitlab-ci-patterns` - Para integração com o GitLab CI
- `deployment-pipeline-design` - Para arquitetura de pipeline
