--- 
name: implantação-azd
description: "Implantar aplicativos de front-end e back-end em contêineres no Azure Container Apps com builds remotos, identidade gerenciada e infraestrutura idempotente."
risk: crítico
source: comunidade
date_add: "27/02/2026"
---

# Implantação de aplicativos de contêiner com a CLI do desenvolvedor do Azure (azd)

Implantar aplicativos de front-end e back-end em contêineres no Azure Container Apps com builds remotos, identidade gerenciada e infraestrutura idempotente.

## Início Rápido

```bash
# Inicializar e implantar
azd auth login
azd init # Cria o arquivo azure.yaml e a pasta .azure/
azd env new <nome-do-ambiente> # Cria o ambiente (desenvolvimento, teste, produção)
azd up # Provisiona a infraestrutura, compila e implanta
```

## Estrutura de Arquivos Principal

```
project/
├── azure.yaml # Definições de serviço azd + hooks
├── infraestrutura/
│ ├── main.bicep # Módulo raiz da infraestrutura
│ ├── main.parameters.json # Injeção de parâmetros a partir de variáveis ​​de ambiente
│ └── modules/
│ ├── container-apps-environment.bicep
│ └── container-app.bicep
├── .azure/
│ ├── config.json # Ponteiro para o ambiente padrão
│ └── <nome-do-ambiente>/
│ ├── .env # Valores específicos do ambiente (gerenciado pelo azd)
│ └── config.json # Metadados do ambiente
└── src/
	├── frontend/Dockerfile
	└── backend/Dockerfile
```

## Configuração do azure.yaml

### Configuração mínima

```yaml
name: azd-deployment
services:

backend:

project: ./src/backend

language: python

host: containerapp

docker:

path: ./Dockerfile

remoteBuild: true
```

### Configuração Completa com Hooks

```yaml

name: azd-deployment
metadata:

template: my-project@1.0.0

infra:

provider: bicep

path: ./infra

azure:

location: eastus2

services:

frontend:

project: ./src/frontend

language: ts

host: containerapp

docker:

path: ./Dockerfile

context: .

remoteBuild: true

backend:

project: ./src/backend

language: python

host: containerapp

docker:

path: ./Dockerfile

context: .

remoteBuild: true

hooks:

preprovision:

shell: sh

run: |

echo "Antes do provisionamento..."

postprovision:

shell: sh

run: |
echo "Após o provisionamento - configure o RBAC, etc."

postdeploy:

shell: sh

run: |

echo "Frontend: ${SERVICE_FRONTEND_URI}"

echo "Backend: ${SERVICE_BACKEND_URI}"
```

### Opções principais do azure.yaml

| Opção | Descrição |

|--------|-------------|

| `remoteBuild: true` | Criar imagens no Registro de Contêineres do Azure (recomendado) |

| `context: .` | Contexto de construção do Docker relativo ao caminho do projeto |

| `host: containerapp` | Implantar no Azure Container Apps |

| `infra.provider: bicep` | Usar o Bicep para infraestrutura |

## Fluxo de Variáveis ​​de Ambiente

### Configuração em Três Níveis

1. **`.env` local** - Somente para desenvolvimento local
2. **`.azure/<env>/.env`** - Gerenciado pelo azd, preenchido automaticamente a partir das saídas do Bicep
3. **`main.parameters.json`** - Mapeia variáveis ​​de ambiente para parâmetros do Bicep

### Padrão de Injeção de Parâmetros

```json
// infra/main.parameters.json
{

"parameters": {

"environmentName": { "value": "${AZURE_ENV_NAME}" },

"location": { "value": "${AZURE_LOCATION=eastus2}" },

"azureOpenAiEndpoint": { "value": "${AZURE_OPENAI_ENDPOINT}" }

}
}
```

Sintaxe: `${VAR_NAME}` ou `${VAR_NAME=default_value}`

### Definindo Variáveis ​​de Ambiente

```bash
# Definir para o ambiente atual
azd env set AZURE_OPENAI_ENDPOINT "https://my-openai.openai.azure.com"
azd env set AZURE_SEARCH_ENDPOINT "https://my-search.search.windows.net"

# Definir durante a inicialização
azd env new prod
azd env set AZURE_OPENAI_ENDPOINT "..."
```

### Saída do Bicep → Variável de Ambiente

```bicep
// Em main.bicep - as saídas são preenchidas automaticamente com .azure/<env>/.env
output SERVICE_FRONTEND_URI string = frontend.outputs.uri
output SERVICE_BACKEND_URI string = backend.outputs.uri
output BACKEND_PRINCIPAL_ID string = backend.outputs.principalId
```

## Implantações Idempotentes

### Por que o comando `azd up` é Idempotente?

1. **O Bicep é declarativo** - Os recursos são reconciliados para o estado desejado.
2. **As compilações remotas possuem tags exclusivas** - As tags de imagem incluem o carimbo de data/hora da implantação.
3. **O ACR reutiliza camadas** - Somente as camadas alteradas são carregadas.

### Preservando Alterações Manuais

Domínios personalizados adicionados via Portal podem ser perdidos na reimplementação. Preserve-os com hooks:
```yaml
hooks:

preprovision:

shell: sh

run: |

# Salvar domínios personalizados antes do provisionamento

if az containerapp show --name "$FRONTEND_NAME" -g "$RG" &>/dev/null; then

az containerapp show --name "$FRONTEND_NAME" -g "$RG" \

--query "properties.configuration.ingress.customDomains" \

-o json > /tmp/domains.json

fi

postprovision:

shell: sh

run: |

# Verificar/restaurar domínios personalizados

if [ -f /tmp/domains.json ]; então

echo "Domínios salvos: $(cat /tmp/domains.json)"

fi
```

### Lidando com Recursos Existentes

```bicep
// Referenciar ACR existente (não recriar)
resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-07-01' existing = {

name: containerRegistryName
}

// Definir customDomains como nulo para preservar os domínios adicionados pelo Portal
customDomains: empty(customDomainsParam) ? null : customDomainsParam
```

## Descoberta de Serviços de Aplicativos em Contêineres

Roteamento HTTP interno entre Aplicativos em Contêineres no mesmo ambiente:

```bicep
// Referência do backend nas variáveis ​​de ambiente do frontend
env: [

{

name: 'BACKEND_URL'

value: 'http://ca-backend-${resourceToken}' // DNS interno
}

```

Proxies nginx do frontend para URL interna:
```nginx
location /api {

proxy_pass $BACKEND_URL;
}
```

## Identidade Gerenciada e RBAC

### Habilitar Identidade Atribuída pelo Sistema

```bicep
resource containerApp 'Microsoft.App/containerApps@2024-03-01' = {

identity: {

type: 'SystemAssigned'

}
}

output principalId string = containerApp.identity.principalId
```

### Atribuição de RBAC Pós-Provisionamento

```yaml
hooks:

postprovision:

shell: sh

run: |

ID_PRINCIPAL="${BACKEND_PRINCIPAL_ID}"

# Acesso ao Azure OpenAI

az role assignment create \

--assignee-object-id "$PRINCIPAL_ID" \

--assignee-principal-type ServicePrincipal \

--role "Usuário do OpenAI dos Serviços Cognitivos" \

--scope "$OPENAI_RESOURCE_ID" 2>/dev/null || true

# Acesso à Pesquisa de IA do Azure

az role assignment create \

--assignee-object-id "$PRINCIPAL_ID" \

--role "Leitor de Dados do Índice de Pesquisa" \

--scope "$SEARCH_RESOURCE_ID" 2>/dev/null || true
```

## Comandos Comuns

```bash
# Gerenciamento de Ambientes
azd env list # Listar ambientes
azd env select <nome> # Alternar entre ambientes
azd env get-values ​​# Exibir todas as variáveis ​​de ambiente
azd env set KEY value # Definir variável

# Implantação
azd up # Provisionamento completo + implantação
azd provision # Somente infraestrutura
azd deploy # Implantação somente de código
azd deploy --service backend # Implantar um único serviço

# Depuração
azd show # Exibir o status do projeto
az containerapp logs show -n <app> -g <rg> --follow # Exibir logs
```

## Arquivos de Referência

- **Padrões Bicep**: Consulte references/bicep-patterns.md para módulos de Aplicativos de Contêiner
- **Solução de Problemas**: Consulte references/troubleshooting.md para problemas comuns
- **Esquema azure.yaml**: Consulte references/azure-yaml-schema.md para opções completas

## Crítico Lembretes

1. **Sempre use `remoteBuild: true`** - As compilações locais falham em Macs M1/ARM ao implantar em AMD64
2. **As saídas do Bicep preenchem automaticamente .azure/<env>/.env** - Não edite manualmente
3. **Use `azd env set` para segredos** - Não use os padrões de main.parameters.json
4. **Tags de serviço (`azd-service-name`)** - Necessárias para que o azd encontre aplicativos de contêiner
5. **`|| true` em hooks** - Impede que erros de RBAC "já existe" impeçam a implantação

## Quando usar
Esta skill é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.

## Limitações
- Use esta skill somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente. - Pare e peça esclarecimentos se faltarem informações necessárias, permissões, limites de segurança ou critérios de sucesso.
