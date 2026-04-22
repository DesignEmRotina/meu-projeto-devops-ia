# Políticas de Sincronização do GitOps

## Políticas de Sincronização do ArgoCD

### Sincronização Automatizada
```yaml
syncPolicy:

automatized:

prune: true # Excluir recursos removidos do Git

selfHeal: true # Reconciliar alterações manuais

allowEmpty: false # Impedir sincronização vazia
```

### Sincronização Manual
```yaml
syncPolicy:

syncOptions:

- PrunePropagationPolicy=foreground

- CreateNamespace=true
```

### Janelas de Sincronização
```yaml
syncWindows:
- kind: allow

schedule: "0 8 * * *"

duration: 1h

applications:

- my-app
- kind: deny

schedule: "0 22 * ​​* *"

duration: 8h

applications:

- '*'
```

### Política de Repetição
```yaml
syncPolicy:

retry:

limit: 5

Recuo:

Duração: 5s

Fator: 2

Duração máxima: 3m
```

## Políticas de Sincronização do Flux

### Sincronização do Kustomization
```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:

name: my-app
spec:

intervalo: 5m
pune: true

wait: true

timeout: 5m
retryInterval: 1m

force: false
```

### Intervalo de Sincronização da Fonte
```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:

name: my-app
spec:

intervalo: 1m

timeout: 60s
```

## Avaliação de Saúde

### Verificações de Saúde Personalizadas
```yaml
# ArgoCD
apiVersion: v1
tipo: ConfigMap
metadados:

nome: argocd-cm
namespace: argocd
dados:

resource.customizations.health.MyCustomResource: |

hs = {}

if obj.status ~= nil then

if obj.status.conditions ~= nil then

for i, condition in ipairs(obj.status.conditions) do

if condition.type == "Ready" and condition.status == "False" then

hs.status = "Degraded"

hs.message = condition.message

return hs

end

if condition.type == "Ready" and condition.status == "True" then

hs.status = "Healthy"

hs.message = condition.message

return hs

end

end

end

hs.status = "Progressing"

hs.message = "Waiting for status"

return hs
```

## Opções de Sincronização

### Opções de Sincronização Comuns
- `PrunePropagationPolicy=foreground` - Aguardar recursos podados Para ser excluído
- `CreateNamespace=true` - Criar namespace automaticamente
- `Validate=false` - Ignorar validação do kubectl
- `PruneLast=true` - Remover recursos após a sincronização
- `RespectIgnoreDifferences=true` - Respeitar diferenças ignoradas
- `ApplyOutOfSyncOnly=true` - Aplicar somente recursos dessincronizados

## Melhores Práticas

1. Use sincronização automatizada para ambientes de não produção
2. Exija aprovação manual para produção
3. Configure janelas de sincronização para manutenção
4. Implemente verificações de integridade para recursos personalizados
5. Use sincronização seletiva para aplicações grandes
6. Configure políticas de repetição apropriadas
7. Monitore falhas de sincronização com alertas
8. Use a remoção de recursos com cautela em produção
9. Teste as políticas de sincronização em ambiente de teste
10. Documente o comportamento da sincronização para as equipes