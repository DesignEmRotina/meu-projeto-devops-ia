--- 
name: kpi-dashboard-design
description: "Padrões abrangentes para projetar painéis de Indicadores-Chave de Desempenho (KPIs) eficazes que orientam as decisões de negócios."
risk: desconhecido
source: comunidade
date_added: "27/02/2026"
---

# Design de Painel de KPIs

Padrões abrangentes para projetar painéis de Indicadores-Chave de Desempenho (KPIs) eficazes que orientam as decisões de negócios.

## Não use esta habilidade quando

- A tarefa não estiver relacionada ao design de painéis de KPIs
- Você precisar de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Utilize esta habilidade quando:

- Estiver projetando dashboards executivos
- Estiver selecionando KPIs relevantes
- Estudar visualizações de monitoramento em tempo real
- Estudar visualizações de métricas específicas para cada departamento
- Estudar layouts de dashboards existentes
- Estudar a governança de métricas

## Conceitos Essenciais

### 1. Estrutura de KPIs

| Nível | Foco | Frequência de Atualização | Público-alvo |

| --------------- | ---------------- | ----------------- | ---------- |

| **Estratégico** | Metas de longo prazo | Mensal/Trimestral | Executivos |

| **Tático** | Metas departamentais | Semanal/Mensal | Gerentes |

| **Operacional** | Dia a dia | Em tempo real/Diário | Equipes |

### 2. KPIs SMART

``` Específicos: Definição clara
Mensuráveis: Quantificáveis
Atingíveis: Metas realistas
Relevantes: Alinhados aos objetivos
Temporais: Período definido
```

### 3. Hierarquia do Painel

```
├── Resumo Executivo (1 página)
│ ├── 4 a 6 KPIs principais
│ ├── Indicadores de tendência
│ └── Alertas importantes
├── Visões por Departamento
│ ├── Painel de Vendas
│ ├── Painel de Marketing
│ ├── Painel de Operações
│ └── Painel Financeiro
└── Detalhamento
Métricas individuais

Análise da causa raiz

## KPIs comuns por departamento

### KPIs de vendas

Métricas de receita:

- Receita recorrente mensal (MRR)

- Receita recorrente anual (ARR)

- Receita média por usuário (ARPU)

- Taxa de crescimento da receita

Métricas do pipeline:

- Valor do pipeline de vendas

- Taxa de conversão

- Tamanho médio do negócio

- Duração do ciclo de vendas

Métricas de atividade:

- Ligações/e-mails por representante

- Demonstrações agendadas

- Propostas enviadas

- Taxa de fechamento

### KPIs de marketing

Aquisição:

- Custo por aquisição (CPA)

- Custo de aquisição de clientes (CAC)

- Volume de leads

- Leads qualificados para marketing (MQL)

Engajamento:

- Tráfego do site

- Taxa de conversão

- Abertura/Clique de e-mail Taxa

- Engajamento Social

ROI:

- ROI de Marketing

- Desempenho da Campanha

- Atribuição de Canal

- Período de Retorno do CAC

```

### KPIs de Produto

```yaml

Uso:

- Usuários Ativos Diários/Mensais (DAU/MAU)

- Duração da Sessão

- Taxa de Adoção de Recursos

- Fidelização (DAU/MAU)

Qualidade:

- Net Promoter Score (NPS)

- Satisfação do Cliente (CSAT)

- Número de Bugs/Problemas

- Tempo de Resolução

Crescimento:

- Taxa de Crescimento de Usuários

- Taxa de Ativação

- Taxa de Retenção

- Taxa de Cancelamento
```

### KPIs Financeiros

```yaml

Lucratividade:

- Margem Bruta

- Margem de Lucro Líquido

- EBITDA

- Margem Operacional

Liquidez:

- Índice de Liquidez Corrente

- Índice de Liquidez Seca

- Fluxo de Caixa

- Capital de Giro

Eficiência:

- Receita por Funcionário

- Índice de Despesas Operacionais

- Prazo Médio de Recebimento de Vendas

- Giro de Estoque
```

## Padrões de Layout do Painel

### Padrão 1: Resumo Executivo

```
┌───────────────────────────────────────────────────────────────┐
│ PAINEL EXECUTIVO [Intervalo de Datas ▼] │
├─────────────┬─────────────┬─────────────┬────────────────┤
│ RECEITA │ LUCRO │ CLIENTES │ PONTUAÇÃO NPS │
│ US$ 2,4 milhões │ US$ 450 mil │ 12.450 │ 72 │
│ ▲ 12% │ ▲ 8% │ ▲ 15% │ ▲ 5 pontos │
├─────────────┴─────────────┴─────────────┴─────────────────┤
│ │
│ Tendência de Receita │ Receita por Produto │
│ ┌───────────────────────┐ │ ┌──────────────────┐ │
│ │ /\ /\ │ │ │ ████████ 45% │ │
│ │ / \ / \ /\ │ │ │ ██████ 32% │ │
│ │ / \/ \ / \ │ │ │ ████ 18% │ │
│ │ / \/ \ │ │ │ ██ 5% │ │
│ └───────────────────────┘ │ └──────────────────┘ │
│ │
├─────────────────────────────────────────────────────────────────┤
│ 🔴 Alerta: Taxa de cancelamento acima do limite (>5%) │
│ 🟡 Aviso: Volume de chamados de suporte 20% acima da média │
└──────────────────────────────────────────────────────────────────┘
```

### Padrão 2: Métricas de SaaS Painel de Controle

```
┌───────────────────────────────────────────────────────────────┐
│ Métricas SaaS Jan 2024 [Mensal ▼] │
├───────────────────────┬──────────────────────────────────────┤
│ ┌────────────────┐ │ CRESCIMENTO DA RECEITA MÍNIMA REQUERIDA (MRR) │
│ │ MRR │ │ ┌─────────────────────────────────┐ │
│ │ US$ 125.000 │ │ │ /── │ │
│ │ ▲ 8% │ │ │ /────/ │ │
│ └────────────────┘ │ │ /────/ │ │
│ ┌────────────────┐ │ │ /────/ │ │
│ │ ARR │ │ │ /────/ │ │
│ │ $1.500.000 │ │ └─────────────────────────────────┘ │
│ │ ▲ 15% │ │ J F M A M J J A S O N D │
│ └────────────────┘ │ │
├───────────────────────┼────────────────────────────────────────┤
│ ECONOMIA UNITÁRIA │ RETENÇÃO DE COORTE │
│ │ │
│ CAC: $450 │ Mês 1: ████████████████████ 100% │
│ LTV: $2.700 │ Mês 3: █████████████████ 85% │
│ LTV/CAC: 6,0x │ Mês 6: ████████████████ 80% │
│ │ Mês 12: ██████████████ 72% │
│ Retorno do investimento: 4 meses │ │
├───────────────────────┴───────────────────────────────────────┤
│ ANÁLISE DE ROTATIVIDADE │
│ ┌──────────┬──────────┬──────────┬──────────────────────┐ │
│ │ Bruto │ Líquido │ Logotipo │ Expansão │ │
│ │ 4,2% │ 1,8% │ 3,1% │ 2,4% │ │
│ └──────────┴──────────┴──────────┴───────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Padrão 3: Tempo real Operações

```
┌────────────────────────────────────────────────────────────────┐
│ CENTRAL DE OPERAÇÕES Ao vivo ● Última atualização: 10:42:15 │
├─────────────────────────────┬─────────────────────────────────┤
│ SAÚDE DO SISTEMA │ STATUS DO SERVIÇO │
│ ┌──────────────────────┐ │ │
│ │ CPU MEM DISCO │ │ ● Gateway de API Saudável │
│ │ 45% 72% 58% │ │ ● Serviço de Usuário Saudável │
│ │ ███ ████ ███ │ │ ● Serviço de Pagamento Degradado │
│ │ ███ ████ ███ │ │ ● Banco de dados íntegro │
│ │ ███ ████ ███ │ │ ● Cache íntegro │
│ └──────────────────────┘ │ │
├─────────────────────────────┼────────────────────────────────┤
│ TAXA DE TRANSFERÊNCIA DE SOLICITAÇÕES │ TAXA DE ERROS │
│ ┌──────────────────────┐ │ ┌──────────────────────────┐ │
│ │ ▂▃▄▅▆▇█▇▆▅▄▃▂ ▂▃▄▅ │ │ │ ▂ │ │
│ └───────────────────────┘ │ └───────────────────────────┘ │
│ Atual: 12.450 requisições/s │ Atual: 0,02% │
│ Pico: 18.200 requisições/s │ Limiar: 1,0% │
├─────────────────────────────┴─────────────────────────────────┤
│ ALERTAS RECENTES │
│ 10:40 🟡 Alta latência no serviço de pagamento (p99 > 500 ms) │
│ 10:35 🟢 Resolvido: Pool de conexões do banco de dados recuperado │
│ 10:22 🔴 Disjuntor do serviço de pagamento acionado │
└────────────────────────────────────────────────────────────────┘
```

## Padrões de Implementação

### SQL para Cálculos de KPIs

```sql
-- Receita Recorrente Mensal (MRR)
WITH mrr_calculation AS (

SELECT
DATE_TRUNC('month', billing_date) AS month,

SUM(
CASE subscription_interval
WHEN 'monthly' THEN amount

WHEN 'yearly' THEN amount / 12

WHEN 'quarterly' THEN amount / 3

END

AS mrr

FROM subscriptions
WHERE status = 'active'

GROUP BY DATE_TRUNC('month', billing_date)
)
SELECT

month,

mrr,

LAG(mrr) OVER (ORDER BY month) AS prev_mrr,

(mrr - LAG(mrr) OVER (ORDER BY month)) / LAG(mrr) OVER (ORDER BY month) * 100 AS growth_pct
FROM mrr_calculation;

-- Retenção de Coortes
COM coortes AS (

SELECT
user_id,

DATE_TRUNC('month', created_at) AS cohort_month
FROM users
),
activity AS (
SELECT

user_id,

DATE_TRUNC('month', event_date) AS activity_month
FROM user_events
WHERE event_type = 'active_session'
)
SELECT

c.cohort_month,

EXTRACT(MONTH FROM age(a.activity_month, c.cohort_month)) AS months_since_signup,

COUNT(DISTINCT a.user_id) AS active_users,

COUNT(DISTINCT a.user_id)::FLOAT / COUNT(DISTINCT c.user_id) * 100 AS retention_rate
FROM cohorts c
LEFT JOIN activity a ON c.user_id = a.user_id
AND a.activity_month >= c.cohort_month
GROUP BY c.cohort_month, EXTRACT(MONTH FROM age(a.activity_month, c.cohort_month))
ORDER BY c.cohort_month, months_since_signup;

-- Custo de Aquisição de Clientes (CAC)
SELECT

DATE_TRUNC('month', acquired_date) AS month,

SUM(marketing_spend) / NULLIF(COUNT(new_customers), 0) AS cac,

SUM(marketing_spend) AS total_spend,

COUNT(new_customers) AS customers_acquired
FROM (

SELECT

DATE_TRUNC('month', u.created_at) AS acquired_date,

u.id AS new_customers,

m.spend AS marketing_spend

FROM users u

JOIN marketing_spend m ON DATE_TRUNC('month', u.created_at) = m.month
WHERE u.source = 'marketing'
) acquisition
GROUP BY DATE_TRUNC('month', acquired_date);
```

### Código do Painel de Controle em Python (Streamlit)

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Painel de Controle de KPIs", layout="wide")

# Cabeçalho com filtro de data
col1, col2 = st.columns([3, 1])
with col1:

st.title("Painel de Controle Executivo")
with col2:

date_range = st.selectbox(

"Período",

["Últimos 7 dias", "Últimos 30 dias", "Último trimestre", "Acumulado do ano"]

)

# Cartões de KPIs
def metric_card(label, value, delta, prefix="", suffix=""):

delta_color = "green" if delta >= 0 else "red"

delta_arrow = "▲" if delta >= 0 senão "▼"

st.metric(

label=label,

value=f"{prefix}{value:,.0f}{suffix}",

delta=f"{delta_arrow} {abs(delta):.1f}%"

)

col1, col2, col3, col4 = st.columns(4)
with col1:

metric_card("Receita", 2400000, 12.5, prefix="$")
with col2:

metric_card("Clientes", 12450, 15.2)
with col3:

metric_card("Pontuação NPS", 72, 5.0)
with col4:

metric_card("Taxa de Cancelamento", 4.2, -0.8, suffix="%")

# Gráficos
col1, col2 = st.columns(2)

with col1:

st.subheader("Receita" Tendência")
data_receita = pd.DataFrame({
'Mês': pd.date_range('2024-01-01', periods=12, freq='M'),
'Receita': [180000, 195000, 210000, 225000, 240000, 255000,

270000, 285000, 300000, 315000, 330000, 345000]

})
fig = px.line(dados_receita, x='Mês', y='Receita',
line_shape='spline', markers=True)

fig.update_layout(height=300)

st.plotly_chart(fig, use_container_width=True)

with col2:

st.subheader("Receita por Produto")

product_data = pd.DataFrame({

'Produto': ['Enterprise', 'Professional', 'Starter', 'Other'],

'Receita': [45, 32, 18, 5]

})

fig = px.pie(product_data, values='Receita', names='Produto',

hole=0.4)

fig.update_layout(height=300)

st.plotly_chart(fig, use_container_width=True)

# Mapa de Calor da Coorte
st.subheader("Retenção da Coorte")
cohort_data = pd.DataFrame({
'Coorte': ['Jan', 'Fev', 'Mar', 'Abr', 'Maio'],

'M0': [100, 100, 100, 100, 100],

'M1': [85, 87, 84, 86, 88],

'M2': [78, 80, 76, 79, Nenhum],

'M3': [72, 74, 70, Nenhum, Nenhum],

'M4': [68, 70, Nenhum, Nenhum, Nenhum],
})
fig = go.Figure(data=go.Heatmap(
z=cohort_data.iloc[:, 1:].values,

x=['M0', 'M1', 'M2', 'M3', 'M4'],

y=cohort_data['Cohort'],

colorscale='Blues',

text=cohort_data.iloc[:, 1:].values,
texttemplate='%{text}%',

textfont={"size": 12},
))
fig.update_layout(height=250)
st.plotly_chart(fig, use_container_width=True)

# Seção de Alertas
st.subheader("Alertas")
alerts = [
{"level": "error", "message": "Taxa de cancelamento excedeu o limite (>5%)"},

{"level": "warning", "message": "Volume de chamados de suporte 20% acima da média"},
]
for alert in alerts:

if alert["level"] == "error":

st.error(f"🔴 {alert['message']}")

elif alert["level"] == "warning":

## Melhores Práticas

### Recomendações

- **Limite a 5-7 KPIs** - Foque no que importa
- **Mostre o contexto** - Comparações, tendências, metas
- **Use cores consistentes** - Vermelho = ruim, verde = bom
- **Permita detalhamento** - Do resumo ao detalhe
- **Atualize adequadamente** - Mantenha a frequência das métricas

### Recomendações

- **Não mostre métricas supérfluas** - Foque em dados acionáveis
- **Não sobrecarregue o painel** - Espaço em branco facilita a compreensão
- **Não use gráficos 3D** - Eles distorcem a percepção
- **Não oculte a metodologia** - Documente os cálculos
- **Não ignore dispositivos móveis** - Garanta um design responsivo

## Recursos

- [Design de Dashboards de Stephen Few](https://www.perceptualedge.com/articles/visual_business_intelligence/rules_for_using_color.pdf)
- [De Edward Tufte](https://www.perceptualedge.com/articles/visual_business_intelligence/rules_for_using_color) Princípios](https://www.edwardtufte.com/tufte/)
- [Galeria do Google Data Studio](https://datastudio.google.com/gallery)