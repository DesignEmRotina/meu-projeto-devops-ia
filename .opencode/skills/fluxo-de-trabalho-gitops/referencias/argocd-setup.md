# Configuração e Instalação do ArgoCD

## Métodos de Instalação

### 1. Instalação Padrão
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### 2. Instalação de Alta Disponibilidade
```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/ha/install.yaml
```

### 3. Instalação via Helm
```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm install argocd argo/argo-cd -n argocd --create-namespace
```

## Inicialização Configuração

### Acessar a interface do ArgoCD
```bash
# Encaminhamento de porta
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Obter a senha inicial de administrador
argocd admin initial-password -n argocd
```

### Configurar o Ingress
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:

name: argocd-server-ingress

namespace: argocd

annotations:

cert-manager.io/cluster-issuer: letsencrypt-prod

nginx.ingress.kubernetes.io/ssl-passthrough: "true"

nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
spec:

ingressClassName: nginx

rules:

- host: argocd.example.com

http:

paths:

- path: /

pathType: Prefix

backend:

service:

name: argocd-server

port:

number: 443

tls:

- hosts:

- argocd.example.com

secretName: argocd-secret
```

## Configuração da CLI

### Login
```bash
argocd login argocd.example.com --username admin
```

### Adicionar Repositório
```bash
argocd repo add https://github.com/org/repo --username user --password token
```

### Criar Aplicativo
```bash
argocd app create my-app \
--repo https://github.com/org/repo \

--path apps/my-app \

--dest-server https://kubernetes.default.svc \
--dest-namespace production
```

## Configuração SSO

### GitHub OAuth
```yaml
apiVersion: v1
kind: ConfigMap
metadata:

name: argocd-cm

namespace: argocd
data:

url: https://argocd.example.com

dex.config: |

connectors:

- type: github

id: github

name: GitHub

config:

clientID: $GITHUB_CLIENT_ID

clientSecret: $GITHUB_CLIENT_SECRET

orgs:

- name: my-org
```

## Configuração RBAC
```yaml
apiVersion: v1
kind: ConfigMap
metadata:

name: argocd-rbac-cm

namespace: argocd
data:

policy.default: role:readonly

policy.csv: |

p, role:developers, applications, *, */dev, allow

p, role:operators, applications, *, */*, allow

g, my-org:devs, role:developers

g, my-org:ops, role:operators
```

## Melhores Práticas

1. Habilitar SSO para produção
2. Implementar políticas RBAC
3. Usar projetos separados para equipes
4. Habilitar registro de auditoria
5. Configurar notificações
6. Usar ApplicationSets para vários clusters
7. Implementar hooks de recursos
8. Configurar verificações de integridade
9. Usar janelas de sincronização para manutenção
10. Monitorar com métricas do Prometheus