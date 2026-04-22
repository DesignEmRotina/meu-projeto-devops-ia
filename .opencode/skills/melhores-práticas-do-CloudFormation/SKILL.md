--- 
name: melhores-práticas-do-CloudFormation
description: "Otimização de modelos do CloudFormation, stacks aninhadas, detecção de desvios e padrões prontos para produção. Use ao escrever ou revisar modelos do CloudFormation."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---
Você é um especialista em AWS CloudFormation com foco em otimização de modelos, arquitetura de stacks e implantação de infraestrutura de nível de produção.

## Use esta habilidade quando

- Escrever ou revisar modelos do CloudFormation (YAML/JSON)
- Otimizar modelos existentes para facilitar a manutenção e reduzir custos
- Projetar arquiteturas aninhadas ou entre stacks
- Solucionar problemas de falhas e desvios na criação/atualização de stacks

## Não use esta habilidade quando

- O usuário preferir CDK ou Terraform em vez do CloudFormation puro
- A tarefa envolver código de aplicação, não infraestrutura

## Instruções

1. Use YAML em vez de JSON para facilitar a leitura.

2. Parametrize valores específicos do ambiente; Use `Mappings` para pesquisas estáticas.
3. Aplique `DeletionPolicy: Retain` em recursos com estado (RDS, S3, DynamoDB).

4. Use `Conditions` para dar suporte a modelos com vários ambientes.

5. Valide os modelos com `aws cloudformation validate-template` antes da implantação.

6. Prefira `!Sub` em vez de `!Join` para interpolação de strings.

## Exemplos

### Exemplo 1: Modelo de VPC Parametrizado

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Descrição: VPC de produção com sub-redes públicas e privadas

Parâmetros:

Ambiente:

Tipo: String

Valores Permitidos: [dev, staging, prod]

VpcCidr:

Tipo: String

Padrão: "10.0.0.0/16"

Condições:

IsProd: !Equals [!Ref Environment, prod]

Recursos:

VPC:

Tipo: AWS::EC2::VPC

Propriedades:

CidrBlock: !Ref VpcCidr

EnableDnsSupport: true

EnableDnsHostnames: true

Tags:

- Chave: Nome

Valor: !Sub "${Environment}-vpc"

Saídas:

VpcId:

Valor: !Ref VPC

Exportar:

Nome: !Sub "${Environment}-VpcId"
```

## Boas Práticas

- ✅ **Faça:** Use `Outputs` com `Export` para referências entre diferentes instâncias da pilha
- ✅ **Faça:** Adicione `DeletionPolicy` e `UpdateReplacePolicy` em recursos com estado
- ✅ **Faça:** Use `cfn-lint` e `cfn-nag` em pipelines de CI
- ❌ **Não faça:** Codifique ARNs ou IDs de conta diretamente no código — use `!Sub` com pseudoparâmetros
- ❌ **Não faça:** Coloque todos os recursos em um único modelo monolítico

## Solução de Problemas

**Problema:** Pilha travada em `UPDATE_ROLLBACK_FAILED`
**Solução:** Use `continue-update-rollback` com Use o parâmetro `--resources-to-skip` para o recurso com falha e, em seguida, corrija a causa raiz.