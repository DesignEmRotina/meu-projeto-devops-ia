--- 
name: fluxo-de-trabalho-gitops
description: "Guia completo para implementar fluxos de trabalho GitOps com ArgoCD e Flux para implantações automatizadas do Kubernetes."
risk: desconhecido
source: comunidade
date_added: "27/02/2026"
---

# Fluxo de Trabalho GitOps

Guia completo para implementar fluxos de trabalho GitOps com ArgoCD e Flux para implantações automatizadas do Kubernetes.

## Objetivo

Implementar entrega contínua declarativa baseada em Git para Kubernetes usando ArgoCD ou Flux CD, seguindo os princípios do OpenGitOps.

## Use esta habilidade quando

- Configurar GitOps para clusters Kubernetes
- Automatizar implantações de aplicativos a partir do Git
- Implementar estratégias de entrega progressiva
- Gerenciar implantações em múltiplos clusters
- Configurar políticas de sincronização automatizadas
- Configurar o gerenciamento de segredos no GitOps

## Não use esta habilidade quando

- Você precisar de uma implantação manual pontual
- Você não puder gerenciar o acesso ao cluster ou as permissões do repositório
- Você não estiver implantando no Kubernetes

## Instruções

1. Defina o layout do repositório e as convenções de estado desejado.

2. Instale o ArgoCD ou Flux e conecte os clusters.

3. Configure as políticas de sincronização, os ambientes e o fluxo de promoção.

4. Valide os rollbacks e o tratamento de segredos.

## Segurança

- Evite a sincronização automática com a produção sem aprovações.

- Mantenha os segredos fora do Git e use gerenciadores de segredos externos ou selados.

## Princípios do OpenGitOps

1. **Declarativo** - Todo o sistema é descrito declarativamente
2. **Versionado e Imutável** - O estado desejado é armazenado no Git
3. **Pull Automático** - Os agentes de software baixam o estado desejado
4. **Conciliação Contínua** - Os agentes conciliam o estado atual com o estado desejado

## Configuração do ArgoCD

### 1. Instalação

```bash
# Criar namespace
kubectl create namespace argocd

# Instalar o ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Obter senha de administrador
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

**Referência:** Consulte `referencias/argocd-setup.md` para obter detalhes da configuração

### 2. Estrutura do Repositório

```
gitops-repo/
├── apps/
│ ├── production/
│ │ ├── app1/
│ │ │ ├── kustomization.yaml
│ │ │ └── deployment.yaml
│ │ └── app2/
│ └── staging/
├── infrastructure/
│ ├── ingress-nginx/
│ ├── cert-manager/
│ └── monitoring/
└── argocd/

├── applications/

└── projects/
```

### 3. Criar Aplicativo

```yaml
# argocd/applications/my-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:

name: my-app

namespace: argocd
spec:

project: default

source:

repoURL: https://github.com/org/gitops-repo

targetRevision: main

path: apps/production/my-app

destination:

server: https://kubernetes.default.svc

namespace: production

syncPolicy:

automated:

prune: true

selfHeal: true
syncOptions:

- CreateNamespace=true
```

### 4. Padrão App of Apps

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:

name: applications

namespace: argocd
spec:

project: default

source:

repoURL: https://github.com/org/gitops-repo

targetRevision: main

path: argocd/applications

destination:

server: https://kubernetes.default.svc

namespace: argocd

syncPolicy:

automated: {}
```

## Configuração do Flux CD

### 1. Instalação

```bash
# Instalar a CLI do Flux
curl -s https://fluxcd.io/install.sh | sudo bash

# Inicializar o Flux
flux bootstrap github \

--owner=org \

--repository=gitops-repo \

--branch=main \

--path=clusters/production \

--personal
```

### 2. Criar repositório Git

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:

name: my-app

namespace: flux-system
spec:

interval: 1m

url: https://github.com/org/my-app

ref:

branch: main
```

### 3. Criar Kustomização

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:

name: my-app

namespace: flux-system
spec:

interval: 5m
caminho: ./deploy

pune: true

sourceRef:

kind: GitRepository

name: my-app
```

## Políticas de Sincronização

### Configuração de Sincronização Automática

**ArgoCD:**
```yaml
syncPolicy:

automated:

prune: true # Excluir recursos não presentes no Git

selfHeal: true # Conciliar alterações manuais

allowEmpty: false

retry:

limit: 5

backoff:

duration: 5s
factor: 2

maxDuration: 3m
```

**Flux:**
```yaml
spec:

intervalo: 1m

prun: true

espera: true

tempo limite: 5m
```

**Referência:** Consulte `referencias/políticas-de-sincronização.md`

## Entrega Progressiva

### Implantação Canary com Rollouts do ArgoCD

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:

name: my-app
spec:

replicas: 5

strategy:

canary:

steps:

- setWeight: 20

- pause: {duration: 1m}

- setWeight: 50

- pause: {duration: 2m}

- setWeight: 100
```

### Implantação Azul-Verde

```yaml
strategy:

blueGreen:

activeService: my-app

previewService: my-app-preview
autoPromotionEnabled: false
```

## Gerenciamento de Segredos

### Operador de Segredos Externos

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:

name: db-credentials
spec:

refreshInterval: 1h

secretStoreRef:

name: aws-secrets-manager

kind: SecretStore

target:

name: db-credentials

data:

- secretKey: password

remoteRef:

key: prod/db/password
```

### Segredos Selados

```bash
# Criptografar segredo
kubeseal --format yaml < secret.yaml > sealed-secret.yaml

# Enviar sealed-secret.yaml para o Git
```

## Boas Práticas

1. **Use repositórios ou branches separados** para diferentes ambientes
2. **Implemente RBAC** para Git Repositórios
3. **Habilite notificações** para falhas de sincronização
4. **Use verificações de integridade** para recursos personalizados
5. **Implemente controles de aprovação** para produção
6. **Mantenha segredos fora do Git** (use Segredos Externos)
7. **Use o padrão Aplicativo de Aplicativos** para organização
8. **Marque versões** para facilitar o rollback
9. **Monitore o status de sincronização** com alertas
10. **Teste as alterações** primeiro em um ambiente de staging

## Solução de Problemas

**Falhas de sincronização:**
```bash
argocd app get my-app
argocd app sync my-app --prune
```

**Status fora de sincronização:**
```bash
argocd app diff my-app
argocd app sync my-app --force
```

## Habilidades Relacionadas

- `k8s-manifest-generator` - Para criar manifestos
- `helm-chart-scaffolding` - Para aplicações de embalagem