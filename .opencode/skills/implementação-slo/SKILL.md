--- 
name: implementação-slo
description: "Estrutura para definir e implementar Indicadores de Nível de Serviço (SLIs), Objetivos de Nível de Serviço (SLOs) e orçamentos de erros."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Implementação de SLO

Estrutura para definir e implementar Indicadores de Nível de Serviço (SLIs), Objetivos de Nível de Serviço (SLOs) e orçamentos de erros.

## Não utilize esta habilidade quando:

- A tarefa não estiver relacionada à implementação de SLOs.
- Você precisar de um domínio ou ferramenta diferente, fora deste escopo.

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra o arquivo `resources/implementation-playbook.md`.

## Objetivo

Implementar metas de confiabilidade mensuráveis ​​usando SLIs, SLOs e orçamentos de erros para equilibrar a confiabilidade com a velocidade de inovação.

## Use esta habilidade quando

- Definir metas de confiabilidade do serviço
- Medir a confiabilidade percebida pelo usuário
- Implementar orçamentos de erros
- Criar alertas baseados em SLOs
- Monitorar metas de confiabilidade

## Hierarquia SLI/SLO/SLA

``` SLA (Acordo de Nível de Serviço)

↓ Contrato com clientes
SLO (Objetivo de Nível de Serviço)

↓ Meta de confiabilidade interna
SLI (Indicador de Nível de Serviço)

↓ Medição real
```

## Definindo SLIs

### Tipos comuns de SLI

#### 1. SLI de Disponibilidade
```promql
# Requisições bem-sucedidas / Total de requisições
sum(rate(http_requests_total{status!~"5.."}[28d]))
/
sum(rate(http_requests_total[28d]))
```

#### 2. SLI de Latência
```promql
# Requisições abaixo da latência Limite / Total de solicitações
soma(taxa(http_request_duration_seconds_bucket{le="0.5"}[28d]))
/
soma(taxa(http_request_duration_seconds_count[28d]))
```

#### 3. SLO de Durabilidade
```
# Gravações bem-sucedidas / Total de gravações
soma(storage_writes_successful_total)
/
soma(storage_writes_total)
```

**Referência:** Consulte `references/slo-definitions.md`

## Definindo Metas de SLO

### Exemplos de SLO de Disponibilidade

| SLO % | Tempo de inatividade/mês | Tempo de inatividade/ano |

|-------|----------------|---------------|

| 99% | 7,2 horas | 3,65 dias |

| 99,9% | 43,2 minutos | 8,76 horas |

| 99,95% | 21,6 minutos | 4,38 horas |

| 99,99% | 4,32 minutos | 52,56 minutos |

### Escolha SLOs apropriados

**Considere:**
- Expectativas do usuário
- Requisitos de negócio
- Desempenho atual
- Custo da confiabilidade
- Benchmarks da concorrência

**Exemplos de SLOs:**
```yaml
slos:

- name: api_availability

target: 99.9

window: 28d

sli: |

sum(rate(http_requests_total{status!~"5.."}[28d]))

/
sum(rate(http_requests_total[28d]))

- name: api_latency_p95

target: 99

window: 28d

sli: |
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))

/
sum(rate(http_request_duration_seconds_count[28d]))
```

## Cálculo do Orçamento de Erros

### Fórmula do Orçamento de Erros

``` Orçamento de Erros = 1 - Meta de SLO
```

**Exemplo:**
- SLO: 99,9% de disponibilidade
- Orçamento de Erros: 0,1% = 43,2 minutos/mês
- Erro Atual: 0,05% = 21,6 minutos/mês
- Orçamento Restante: 50%

### Política de Orçamento de Erros

```yaml
error_budget_policy:

- remaining_budget: 100%

action: Velocidade de desenvolvimento normal

- remaining_budget: 50%

action: Considerar o adiamento de mudanças arriscadas

- remaining_budget: 10%

action: Congelar mudanças não críticas

- remaining_budget: 0%

action: Congelamento de funcionalidades, foco na confiabilidade
```

**Referência:** Consulte `references/error-budget.md`

## Implementação de SLO

### Gravação do Prometheus Regras

```yaml
# Regras de gravação SLI
grupos:

- nome: sli_rules

intervalo: 30s

regras:

# SLI de disponibilidade

- registro: sli:http_availability:ratio

expr: |

sum(rate(http_requests_total{status!~"5.."}[28d]))

/
sum(rate(http_requests_total[28d]))

# SLI de latência (requisições < 500ms)

- registro: sli:http_latency:ratio

expr: |
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))

/
sum(rate(http_request_duration_seconds_count[28d]))

- name: slo_rules

interval: 5m

rules:

# Conformidade com o SLO (1 = atendendo ao SLO, 0 = violando)

- record: slo:http_availability:compliance

expr: sli:http_availability:ratio >= bool 0.999

- record: slo:http_latency:compliance

expr: sli:http_latency:ratio >= bool 0.99

# Orçamento de erros restante (percentual)

- record: slo:http_availability:error_budget_remaining
expr: | (sli:http_availability:ratio - 0.999) / (1 - 0.999) * 100

# Taxa de consumo do orçamento de erros

- record: slo:http_availability:burn_rate_5m

expr: |

(1 - (
sum(rate(http_requests_total{status!~"5.."}[5m]))

/
sum(rate(http_requests_total[5m]))

)) / (1 - 0.999)
```

### Regras de alerta de SLO

```yaml
groups:

- name: slo_alerts

interval: 1m

rules:

# Consumo rápido: taxa de 14,4x, janela de 1 hora

# Consome 2% do orçamento de erros em 1 hora

- alert: SLOErrorBudgetBurnFast
expr: |
slo:http_availability:burn_rate_1h > 14.4

e

slo:http_availability:burn_rate_5m > 14.4

para: 2m

rótulos:

gravidade: crítica

anotações:

resumo: "Detectado consumo rápido do orçamento de erros"

descrição: "Consumo do orçamento de erros a uma taxa de {{ $value }}x"

# Consumo lento: taxa 6x, janela de 6 horas

# Consome 5% do orçamento de erros em 6 horas

- alerta: SLOErrorBudgetBurnSlow
expr: |

slo:http_availability:burn_rate_6h > 6

e

slo:http_availability:burn_rate_30m > 6

para: 15m

rótulos:

gravidade: aviso

anotações:

resumo: "Detectado consumo lento do orçamento de erros"

descrição: "Consumo do orçamento de erros a uma taxa de {{ $value }}x"

# Orçamento de erros esgotado

- alerta: SLOErrorBudgetExhausted

expr: slo:http_availability:error_budget_remaining < 0

para: 5m

rótulos:

gravidade: crítica

anotações:

resumo: "Orçamento de erros SLO esgotado"

descrição: "Orçamento de erros restante: {{ $value }}%"
```

Painel de SLO

**Estrutura do Painel do Grafana:**

```
┌─────────────────────────────────────┐
│ Conformidade com o SLO (Atual)      │
│ ✓ 99,95% (Meta: 99,9%)              │
├─────────────────────────────────────┤
│ Orçamento Restante: 65%             │
│ ████████░░ 65%                      │
├─────────────────────────────────────┤
│ Tendência SLI (28 dias)             │
│ [Gráfico de série temporal]         │
├─────────────────────────────────────┤
│ Análise da Taxa de Queima           │
│ [Taxa de queima por janela de tempo] │
└──────────────────────────────────────┘
```

**Exemplos de Consultas:**

```promql
# Conformidade atual com o SLO
sli:http_availability:ratio * 100

# Orçamento de erros restante
slo:http_availability:error_budget_remaining

# Dias até o orçamento de erros se esgotar (na taxa de consumo atual)
(slo:http_availability:error_budget_remaining / 100)
*
28
/ sli:http_availability:ratio) * (1 - 0,999)
```

## Alertas de Taxa de Queima em Múltiplas Janelas

```yaml
# A combinação de janelas curtas e longas reduz falsos positivos
regras:

- alert: SLOBurnRateHigh

expr: |

(
slo:http_availability:burn_rate_1h > 14.4

e

slo:http_availability:burn_rate_5m > 14.4

)

ou

(
slo:http_availability:burn_rate_6h > 6

e

slo:http_availability:burn_rate_30m > 6

)

rótulos:

gravidade: crítica
```

## Processo de Revisão de SLO

### Revisão Semanal
- Conformidade atual com o SLO
- Status do orçamento de erros
- Análise de tendências
- Impacto do incidente

### Revisão Mensal
- Cumprimento do SLO
- Uso do orçamento de erros
- Análises pós-incidente
- Ajustes de SLO

### Revisão Trimestral
- Relevância do SLO
- Ajustes de metas
- Melhorias de processo
- Aprimoramentos de ferramentas

## Melhores Práticas

1. **Comece com os serviços voltados para o usuário**
2. **Use vários SLIs** (disponibilidade, latência, etc.)
3. **Defina SLOs alcançáveis** (não busque 100%)
4. **Implemente alertas em várias janelas** para reduzir o ruído
5. **Monitore o orçamento de erros** de forma consistente
6. **Revise os SLOs regularmente**
7. **Documente as decisões sobre SLOs**
8. **Alinhe-as com os objetivos de negócios**
9. **Automatize os relatórios de SLOs**
10. **Use os SLOs para priorização**

## Arquivos de Referência

- `assets/slo-template.md` - Modelo de definição de SLO
- `references/slo-definitions.md` - Padrões de definição de SLO
- `references/error-budget.md` - Cálculos de orçamento de erros

## Habilidades Relacionadas

- `prometheus-configuration` - Para coleta de métricas
- `grafana-dashboards` - Para visualização de SLO