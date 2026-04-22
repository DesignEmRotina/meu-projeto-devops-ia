--- 
name: design-de-pipeline-de-implantação
description: "Padrões de arquitetura para pipelines de CI/CD de múltiplos estágios com portões de aprovação e estratégias de implantação."
risk: crítico
source: comunidade
date_add: "27/02/2026"
---

# Design de Pipeline de Implantação

Padrões de arquitetura para pipelines de CI/CD de múltiplos estágios com portões de aprovação e estratégias de implantação.

## Não use esta habilidade quando

- A tarefa não estiver relacionada ao design de pipeline de implantação
- Você precisar de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Objetivo

Projetar pipelines de implantação robustos e seguros que equilibrem velocidade e segurança por meio de uma organização adequada dos estágios e fluxos de trabalho de aprovação.

## Use esta habilidade quando:

- Projetar arquitetura de CI/CD
- Implementar pontos de controle de implantação
- Configurar pipelines em múltiplos ambientes
- Estabelecer as melhores práticas de implantação
- Implementar entrega progressiva

## Estágios do Pipeline

### Fluxo Padrão do Pipeline

```
┌─────────┐ ┌──────┐ ┌─────────┐ ┌────────┐ ┌──────────┐
│ Build │ → │ Test │ → │ Preparação │ → │ Aprovação │ → │ Produção │
└─────────┘ └──────┘ └─────────┘ └────────┘ └──────────┘
```

### Detalhamento das Etapas

1. **Código-fonte** - Checkout do código
2. **Build** - Compilar, empacotar e conteinerizar
3. **Teste** - Testes unitários, de integração e de segurança
4. **Implantação em ambiente de teste** - Implantação em ambiente de teste
5. **Testes de integração** - Testes de ponta a ponta e testes de fumaça
6. **Aprovação** - Aprovação manual necessária
7. **Implantação em produção** - Canary, blue-green, rolling
8. **Verificação** - Verificações de integridade e monitoramento
9. **Reversão** - Reversão automática em caso de falha

## Padrões de aprovação

### Padrão 1: Aprovação manual

```yaml
# GitHub Actions
production-deploy:

needs: staging-deploy

environment:

name: production

url: https://app.example.com

runs-on: ubuntu-latest

steps:

- name: Deploy to production

run: |

# Comandos de Implantação
```

### Padrão 2: Aprovação Baseada em Tempo

```yaml
# GitLab CI
deploy:production:

stage: deploy

script:

- deploy.sh production

environment:

name: production

when: delayed

start_in: 30 minutes
only:

- main
```

### Padrão 3: Aprovador Múltiplo

```yaml
# Azure Pipelines
stages:
- stage: Production

dependsOn: Staging
jobs:

- deployment: Deploy

environment:

name: production

resourceType: Kubernetes

strategy:

runOnce:

preDeploy:

steps:

- task: ManualValidation@0
inputs:

notifyUsers: 'team-leads@example.com'

structions: 'Review staging metrics before approving'
```

**Referência:** Consulte `assets/approval-gate-template.yml`

## Estratégias de Implantação

### 1. Implantação Contínua (Rolling Deployment)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:

name: my-app
spec:

replicas: 10

strategy:

type: RollingUpdate

rollingUpdate:

maxSurge: 2

maxUnavailable: 1
```

**Características:**
- Implantação gradual
- Tempo de inatividade zero
- Reversão fácil
- Ideal para a maioria das aplicações

### 2. Implantação Azul-Verde (Blue-Green)

```yaml
# Azul (atual)
kubectl apply -f blue-deployment.yaml
kubectl label service my-app version=blue

# Verde (novo)
kubectl apply -f green-deployment.yaml
# Verde de teste environment
kubectl label service my-app version=green

# Rollback if needed
kubectl label service my-app version=blue
```

**Características:**
- Troca instantânea
- Rollback fácil
- Dobra o custo da infraestrutura temporariamente
- Bom para implantações de alto risco

### 3. Implantação Canary

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:

name: my-app
spec:

replicas: 10

strategy:

canary:

steps:

- setWeight: 10

- pause: {duration: 5m}

- setWeight: 25

- pause: {duration: 5m}

- setWeight: 50

- pause: {duration: 5m}

- setWeight: 100
```

**Características:**
- Mudança gradual de tráfego
- Risco Mitigação
- Testes com usuários reais
- Requer service mesh ou similar

### 4. Feature Flags

```python
from flagsmith import Flagsmith

flagsmith = Flagsmith(environment_key="API_KEY")

if flagsmith.has_feature("new_checkout_flow"):

# Novo caminho de código

process_checkout_v2()
else:

# Caminho de código existente

process_checkout_v1()
```

**Características:**

- Implantação sem lançamento
- Teste A/B
- Reversão instantânea
- Controle granular

## Orquestração de Pipeline

### Exemplo de Pipeline Multiestágio

```yaml

name: Pipeline de Produção

on:

push:

branches: [ main ]

jobs:

build:

runs-on: ubuntu-latest

steps:

- uses: actions/checkout@v4

- name: Build application

run: make construir

- nome: Construir imagem Docker

executar: docker build -t myapp:${{ github.sha }} .
- nome: Enviar para o registro

executar: docker push myapp:${{ github.sha }}

teste:

necessita de: build

executa em: ubuntu-latest

etapas:

- nome: Testes unitários

executar: make test

- nome: Verificação de segurança

executar: trivy image myapp:${{ github.sha }}

implantar em staging:

necessita de: test

executa em: ubuntu-latest

ambiente:

nome: staging

etapas:

- nome: Implantar em staging

executar: kubectl apply -f k8s/staging/

teste de integração:

necessita de: deploy-staging

executa em: ubuntu-latest

etapas:

- nome: Executar testes E2E

executar: npm run test:e2e

implantar em produção:

necessita de: integration-test

executa em: ubuntu-latest

ambiente:

nome: production

etapas:

- nome: Implantação canary

executar: | kubectl apply -f k8s/production/

kubectl argo rollouts promote my-app

verificar:

necessidades: deploy-production
runs-on: ubuntu-latest

etapas:

- nome: Verificação de integridade
executar: curl -f https://app.example.com/health

- nome: Notificar a equipe

executar: |

curl -X POST ${{ secrets.SLACK_WEBHOOK }} \

-d '{"text":"Implantação em produção bem-sucedida!"}'
```

## Melhores Práticas de Pipeline

1. **Falhe rápido** - Execute testes rápidos primeiro
2. **Execução paralela** - Execute jobs independentes simultaneamente
3. **Cache** - Armazene em cache as dependências entre as execuções
4. **Gerenciamento de artefatos** - Armazene os artefatos de build
5. **Paridade de ambientes** - Mantenha os ambientes consistentes
6. **Gerenciamento de segredos** - Use armazenamentos de segredos (Vault, etc.)
7. **Janelas de implantação** - Agende as implantações adequadamente
8. **Integração de monitoramento** - Monitore as métricas de implantação
9. **Automação de rollback** - Rollback automático em caso de falhas
10. **Documentação** - Documente os estágios do pipeline

## Estratégias de Rollback

### Rollback automatizado

```yaml
deploy-and-verify:

steps:

- name: Deploy new version

run: kubectl apply -f k8s/

- name: Wait for rollout

run: kubectl rollout status deployment/my-app

- nome: Verificação de integridade

id: saúde

executar: |

para i em {1..10}; faça

se curl -sf https://app.example.com/health; então

exit 0

fi

sleep 10

done

exit 1

- name: Rollback on failure

if: failure()

run: kubectl rollout undo deployment/my-app
```

### Rollback Manual

```bash

# Listar histórico de revisões
kubectl rollout history deployment/my-app

# Reverter para a versão anterior
kubectl rollout undo deployment/my-app

# Reverter para uma revisão específica
kubectl rollout undo deployment/my-app --to-revision=3
```

## Monitoramento e Métricas

### Principais Métricas do Pipeline

- **Frequência de Implantação** - Com que frequência as implantações ocorrem
- **Tempo de Entrega** - Tempo entre o commit e a produção
- **Taxa de Falha de Alteração** - Percentual de implantações com falha
- **Tempo Médio de Recuperação (MTTR)** - Tempo para recuperação de uma falha
- **Taxa de Sucesso do Pipeline** - Percentual de execuções bem-sucedidas
- **Média do Pipeline** Duração** - Tempo para concluir o pipeline

### Integração com Monitoramento

```yaml
- name: Verificação pós-implantação

run: |

# Aguardar a estabilização das métricas

sleep 60

# Verificar a taxa de erros
ERROR_RATE=$(curl -s "$PROMETHEUS_URL/api/v1/query?query=rate(http_errors_total[5m])" | jq '.data.result[0].value[1]')

if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); então

echo "Taxa de erros muito alta: $ERROR_RATE"

exit 1

fi
```

## Arquivos de Referência

- `references/pipeline-orchestration.md` - Padrões de pipeline complexos
- `assets/approval-gate-template.yml` - Modelos de fluxo de trabalho de aprovação

## Habilidades Relacionadas

- `github-actions-templates` - Para implementação do GitHub Actions
- `gitlab-ci-patterns` - Para implementação do GitLab CI
- `secrets-management` - Para gerenciamento de segredos