--- 
name: implementação-cqrs
description: "Implemente a Segregação de Responsabilidades de Comando e Consulta (CQRS) para arquiteturas escaláveis. Use ao separar modelos de leitura e gravação, otimizar o desempenho de consultas ou construir sistemas orientados a eventos."
risk: desconhecido
resource: comunidade
date_add: "27/02/2026"
---

# Implementação de CQRS

Guia completo para implementar padrões CQRS (Segregação de Responsabilidades de Comando e Consulta).

## Use esta habilidade quando:

- Separar as responsabilidades de leitura e gravação
- Escalar as leituras independentemente das gravações
- Construir sistemas orientados a eventos
- Otimizar cenários de consulta complexos
- Diferentes modelos de dados de leitura/gravação forem necessários

- Relatórios de alto desempenho forem necessários

## Não use esta habilidade quando:

- O domínio for simples e o CRUD for suficiente

- Você não puder operar modelos de leitura/gravação separados

- For necessária forte consistência imediata em todos os lugares

## Instruções

- Identifique as cargas de trabalho de leitura/gravação e as necessidades de consistência.

- Defina os modelos de comando e consulta com limites claros.

- Implemente projeções e sincronização do modelo de leitura.

- Valide o desempenho, a recuperação e os modos de falha.

- Se forem necessários padrões detalhados, abra `recursos/manual-de-implementação.md`.

## Recursos

- `recursos/manual-de-implementação.md` para padrões e modelos CQRS detalhados.