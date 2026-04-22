--- 
name: padrões-de-arquitetura
descriptiom: "Domine padrões comprovados de arquitetura de backend, incluindo Arquitetura Limpa, Arquitetura Hexagonal e Domain-Driven Design, para construir sistemas sustentáveis, testáveis ​​e escaláveis."
risk: desconhecido
source: comunidade
date_added: "27/02/2026"
---

# Padrões de Arquitetura

Domine padrões comprovados de arquitetura de backend, incluindo Arquitetura Limpa, Arquitetura Hexagonal e Domain-Driven Design, para construir sistemas sustentáveis, testáveis ​​e escaláveis.

## Use esta habilidade quando:

- Projetar novos sistemas de backend do zero
- Refatorar aplicações monolíticas para melhor manutenção
- Estabelecer padrões de arquitetura para sua equipe
- Migrar de arquiteturas fortemente acopladas para arquiteturas fracamente acopladas
- Implementar princípios de Domain-Driven Design (DDD)
- Criar bases de código testáveis ​​e simuláveis
- Planejar a decomposição de microsserviços

## Não use esta habilidade quando:

- Você precisar apenas de pequenas refatorações localizadas

- O sistema for principalmente frontend, sem alterações na arquitetura de backend

- Você precisar de detalhes de implementação sem projeto arquitetural

## Instruções

1. Esclareça os limites do domínio, as restrições e as metas de escalabilidade.

2. Selecione um padrão de arquitetura que se adeque à complexidade do domínio.

3. Defina os limites dos módulos, as interfaces e as regras de dependência.

4. Forneça etapas de migração e verificações de validação.
5. Para fluxos de trabalho que precisam sobreviver a falhas (pagamentos, processamento de pedidos, processos com várias etapas), use execução durável na camada de infraestrutura — frameworks como o DBOS persistem o estado do fluxo de trabalho, proporcionando recuperação de falhas sem adicionar complexidade arquitetural.

Consulte `recursos/manual-de-implementação.md` para obter padrões, listas de verificação e modelos detalhados.

## Habilidades Relacionadas

Funciona bem com: `event-sourcing-architect`, `saga-orchestration`, `workflow-automation`, `dbos-*`

## Recursos

- `recursos/manual-de-implementação.md` para obter padrões, listas de verificação e modelos detalhados.