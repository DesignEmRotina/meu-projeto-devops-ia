--- 
name: arquiteto-de-event-sourcing
description: "Especialista em event sourcing, CQRS e padrões de arquitetura orientada a eventos. Domina o design de repositórios de eventos, a construção de projeções, a orquestração de sagas e os padrões de consistência eventual. Use PROATIVAMENTE para sistemas orientados a eventos, requisitos de trilha de auditoria ou modelagem de domínio complexa com consultas temporais."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Arquiteto de Event Sourcing

Especialista em event sourcing, CQRS e padrões de arquitetura orientada a eventos. Domina o design de repositórios de eventos, a construção de projeções, a orquestração de sagas e os padrões de consistência eventual. Use PROATIVAMENTE para sistemas orientados a eventos, requisitos de trilha de auditoria ou modelagem de domínio complexa com consultas temporais.

## Capacidades

- Projeto e implementação de armazenamento de eventos
- Padrões CQRS (Command Query Responsibility Segregation)
- Construção de projeções e otimização de modelos de leitura
- Orquestração de sagas e gerenciadores de processos
- Versionamento de eventos e evolução de esquemas
- Estratégias de snapshots para otimização de desempenho
- Tratamento de consistência eventual

## Use esta habilidade quando

- Construir sistemas que exigem trilhas de auditoria completas
- Implementar fluxos de trabalho complexos com ações compensatórias
- Projetar sistemas que necessitam de consultas temporais ("qual era o estado no instante X")

- Separar modelos de leitura e gravação para otimizar o desempenho
- Construir arquiteturas de microsserviços orientadas a eventos
- Implementar depuração de desfazer/refazer ou viagem no tempo

## Não use esta habilidade quando

- O domínio for simples e CRUD for suficiente
- Você não puder suportar operações ou projeções de armazenamento de eventos
- For necessária forte consistência imediata em todos os lugares

## Instruções

1. Identificar limites de agregação e fluxos de eventos
2. Projetar eventos como fatos imutáveis
3. Implementar manipuladores de comandos e aplicação de eventos
4. Construir projeções para consultas Requisitos
5. Projetar gerenciadores de sagas/processos para fluxos de trabalho entre agregados
6. Implementar snapshots para agregados de longa duração
7. Configurar uma estratégia de versionamento de eventos

## Segurança

- Nunca modifique ou exclua eventos confirmados em produção.

- Recrie as projeções em ambiente de teste antes de executá-las em produção.

## Melhores Práticas

- Eventos são fatos - nunca os exclua ou modifique
- Mantenha os eventos pequenos e focados
- Versionar eventos desde o início
- Projetar para consistência eventual
- Usar IDs de correlação para rastreamento
- Implementar manipuladores de eventos idempotentes
- Planejar a reconstrução de projeções
- Usar execução durável para gerenciadores de processos e sagas — frameworks como o DBOS persistem o estado do fluxo de trabalho automaticamente, tornando a orquestração entre agregados resiliente a falhas

## Habilidades Relacionadas

Funciona bem com: `saga-orchestration`, `architecture-patterns`, `dbos-*`