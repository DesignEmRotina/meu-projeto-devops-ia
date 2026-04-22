---
name: desempenho-de-aplicação-otimização
description: "Otimize o desempenho de ponta a ponta da aplicação com criação de perfis, observabilidade e ajustes de backend/frontend. Use ao coordenar a otimização de desempenho em toda a pilha."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

Otimize o desempenho da aplicação de ponta a ponta usando agentes especializados de desempenho e otimização:

[Pensamento ampliado: Este fluxo de trabalho orquestra um processo abrangente de otimização de desempenho em toda a pilha da aplicação. Começando com a criação de perfis detalhados e o estabelecimento da linha de base, o fluxo de trabalho avança por meio de otimizações direcionadas em cada camada do sistema, valida as melhorias por meio de testes de carga e estabelece o monitoramento contínuo para um desempenho sustentado. Cada fase se baseia em insights das fases anteriores, criando uma estratégia de otimização orientada por dados que aborda gargalos reais em vez de melhorias teóricas.] O fluxo de trabalho enfatiza práticas modernas de observabilidade, métricas de desempenho centradas no usuário e estratégias de otimização com boa relação custo-benefício.

## Use esta habilidade quando:

- Coordenar a otimização de desempenho em backend, frontend e infraestrutura
- Estabelecer linhas de base e criar perfis para identificar gargalos
- Projetar testes de carga, orçamentos de desempenho ou planos de capacidade

- Criar observabilidade para metas de desempenho e confiabilidade

## Não use esta habilidade quando:

- A tarefa for uma pequena correção localizada sem objetivos de desempenho mais amplos
- Não houver acesso a métricas, rastreamento ou dados de perfil
- A solicitação não estiver relacionada a desempenho ou escalabilidade

## Instruções

1. Confirme as metas de desempenho, restrições e métricas-alvo.

2. Estabeleça linhas de base com perfil, rastreamento e dados de usuários reais.

3. Execute otimizações faseadas em toda a pilha com impacto mensurável.

4. Valide as melhorias e defina salvaguardas para evitar regressões.

## Segurança

- Evite testes de carga em produção sem aprovações e medidas de segurança. - Implemente as alterações de desempenho gradualmente, com planos de reversão.

## Fase 1: Criação de Perfil de Desempenho e Linha de Base

### 1. Criação de Perfil de Desempenho Abrangente

- Use a ferramenta Task com o subagent_type="performance-engineer"
- Prompt: "Crie um perfil de desempenho abrangente para o aplicativo: $ARGUMENTS. Gere flame graphs para uso da CPU, heap dumps para análise de memória, rastreie operações de E/S e identifique os caminhos críticos. Use ferramentas de APM como DataDog ou New Relic, se disponíveis. Inclua a criação de perfil de consultas ao banco de dados, tempos de resposta da API e métricas de renderização do frontend. Estabeleça linhas de base de desempenho para todas as jornadas críticas do usuário."

- Contexto: Investigação inicial de desempenho
- Saída: Perfil de desempenho detalhado com flame graphs, análise de memória, identificação de gargalos e métricas de referência

### 2. Avaliação da Pilha de Observabilidade

- Use a ferramenta Task com subagent_type="observability-engineer"
- Prompt: "Avalie a configuração atual de observabilidade para: $ARGUMENTS. Analise o monitoramento existente, o rastreamento distribuído com OpenTelemetry, a agregação de logs e a coleta de métricas. Identifique lacunas de visibilidade, métricas ausentes e áreas que necessitam de melhor instrumentação. Recomende a integração de ferramentas APM e métricas personalizadas para operações críticas de negócios."

- Contexto: Perfil de desempenho da etapa 1
- Saída: Relatório de avaliação de observabilidade, lacunas de instrumentação, recomendações de monitoramento

### 3. Análise da Experiência do Usuário

- Use a ferramenta Tarefa com o subagente "performance-engineer"
- Instrução: "Analise as métricas de experiência do usuário para: $ARGUMENTS. Meça os Core Web Vitals (LCP, FID, CLS), tempos de carregamento de página, tempo de interação e desempenho percebido. Use dados de Monitoramento de Usuário Real (RUM), se disponíveis. Identifique as jornadas do usuário com baixo desempenho e seu impacto nos negócios."

- Contexto: Linhas de base de desempenho da etapa 1
- Saída: Relatório de desempenho da experiência do usuário, análise de Core Web Vitals, avaliação de impacto no usuário

## Fase 2: Otimização de Banco de Dados e Backend

### 4. Otimização de Desempenho do Banco de Dados

- Use a ferramenta Task com subagent_type="database-cloud-optimization::database-optimizer"
- Prompt: "Otimize o desempenho do banco de dados para: $ARGUMENTS com base nos dados de perfil: {context_from_phase_1}. Analise os logs de consultas lentas, crie índices ausentes, otimize os planos de execução, implemente o cache de resultados de consultas com Redis/Memcached. Revise o pool de conexões, instruções preparadas e oportunidades de processamento em lote. Considere réplicas de leitura e particionamento de banco de dados, se necessário."

- Contexto: Gargalos de desempenho da fase 1
- Saída: Consultas otimizadas, novos índices, estratégia de cache, configuração do pool de conexões

### 5. Otimização de Código de Backend e API

- Use a ferramenta Task com subagent_type="backend-development::backend-architect"
- Prompt: "Otimize os serviços de backend para: $ARGUMENTS, visando os gargalos: {context_from_phase_1}. Implemente algoritmos eficientes, adicione cache em nível de aplicação, otimize consultas N+1, use padrões async/await de forma eficaz. Implemente paginação, compressão de resposta, otimização de consultas GraphQL e operações de API em lote. Adicione disjuntores e bulkheads para resiliência."

### 6. Microsserviços e Otimização de Sistemas Distribuídos

- Use a ferramenta Task com o subagent_type="performance-engineer"
- Prompt: "Otimize o desempenho do sistema distribuído para: $ARGUMENTS. Analise a comunicação entre serviços, implemente otimizações na malha de serviços, otimize o desempenho da fila de mensagens (Kafka/RabbitMQ), reduza os saltos na rede. Implemente estratégias de cache distribuído e otimize a serialização/desserialização."

- Contexto: Otimizações de backend da etapa 5
- Saída: Melhorias na comunicação do serviço, otimização da fila de mensagens, configuração de cache distribuído

## Fase 3: Otimização de Frontend e CDN

### 7. Otimização de Pacotes e Carregamento do Frontend

- Use a ferramenta Task com subagent_type="frontend-developer"
- Prompt: "Otimize o desempenho do frontend para: $ARGUMENTS visando os Core Web Vitals: {context_from_phase_1}. Implemente divisão de código, tree shaking, carregamento lento e importações dinâmicas. Otimize os tamanhos dos pacotes com análise webpack/rollup. Implemente dicas de recursos (prefetch, preconnect, preload). Otimize o caminho de renderização crítico e elimine recursos que bloqueiam a renderização."
- Contexto: Análise de UX da fase 1, otimizações de backend da fase 2
- Saída: Pacotes otimizados, implementação de carregamento lento (lazy loading), melhorias nas Core Web Vitals

### 8. Otimização de CDN e Edge

- Use a ferramenta Task com subagent_type="cloud-infrastructure::cloud-architect"
- Prompt: "Otimize o desempenho da CDN e da edge para: $ARGUMENTS. Configure o CloudFlare/CloudFront para cache ideal, implemente funções de edge para conteúdo dinâmico, configure a otimização de imagens com imagens responsivas e formatos WebP/AVIF. Configure HTTP/2 e HTTP/3, implemente a compressão Brotli. Configure a distribuição geográfica para usuários globais."

- Contexto: Otimizações de front-end da etapa 7
- Saída: Configuração de CDN, regras de cache de borda, configuração de compressão, otimização geográfica

### 9. Otimização de Aplicativos Móveis e Progressive Web Apps

- Use a ferramenta Task com subagent_type="frontend-mobile-development::mobile-developer"
- Prompt: "Otimize a experiência móvel para: $ARGUMENTS. Implemente service workers para funcionalidade offline, otimize para redes lentas com carregamento adaptativo. Reduza o tempo de execução do JavaScript para CPUs móveis. Implemente rolagem virtual para listas longas. Otimize a responsividade ao toque e animações suaves. Considere otimizações específicas para React Native/Flutter, se aplicável."

- Contexto: Otimizações de front-end das etapas 7-8
- Saída: Código otimizado para dispositivos móveis, implementação de PWA, funcionalidade offline

## Fase 4: Teste de Carga e Validação

### 10. Teste de Carga Abrangente

- Use a ferramenta Task com subagent_type="performance-engineer"
- Instrução: "Realize testes de carga abrangentes para: $ARGUMENTS usando k6/Gatling/Artillery. Projete cenários de carga realistas com base em padrões de tráfego de produção. Teste cenários de carga normal, carga de pico e estresse. Inclua testes de API, testes baseados em navegador e testes de WebSocket, se aplicável. Meça os tempos de resposta, a taxa de transferência, as taxas de erro e a utilização de recursos em vários níveis de carga."

- Contexto: Todas as otimizações das fases 1 a 3
- Saída: Resultados do teste de carga, desempenho sob carga, pontos de ruptura, análise de escalabilidade

### 11. Teste de Regressão de Desempenho

- Use a ferramenta Task com o subagent_type="performance-testing-review::test-automator"
- Prompt: "Crie testes automatizados de regressão de desempenho para: $ARGUMENTS. Configure orçamentos de desempenho para as principais métricas, integre com o pipeline de CI/CD usando o GitHub Actions ou similar. Crie testes Lighthouse CI para o frontend, testes de desempenho da API com o Artillery e benchmarks de desempenho do banco de dados. Implemente gatilhos de rollback automáticos para regressões de desempenho."

- Contexto: Resultados do teste de carga da etapa 10, métricas de referência da fase 1
- Saída: Conjunto de testes de desempenho, integração CI/CD, sistema de prevenção de regressão

## Fase 5: Monitoramento e Otimização Contínua

### 12. Configuração do Monitoramento de Produção

- Use a ferramenta Task com subagent_type="observability-engineer"
- Prompt: "Implemente o monitoramento de desempenho de produção para: $ARGUMENTS. Configure o APM com DataDog/New Relic/Dynatrace, configure o rastreamento distribuído com OpenTelemetry, implemente métricas de negócios personalizadas. Crie painéis do Grafana para as principais métricas, configure alertas do PagerDuty para degradação de desempenho. Defina SLIs/SLOs para serviços críticos com orçamentos de erro."

- Contexto: Melhorias de desempenho de todas as fases anteriores
- Saída: Painéis de monitoramento, regras de alerta, definições de SLI/SLO, manuais de operação

### 11. Testes de Regressão de Desempenho

- Use a ferramenta Task com o subagent_type="performance-testing-review::test-automator"
- Prompt: "Crie testes automatizados de regressão de desempenho para: $ARGUMENTS. Configure orçamentos de desempenho para as principais métricas, integre com o pipeline de CI/CD usando o GitHub Actions ou similar. Crie testes Lighthouse CI para o frontend, testes de desempenho da API com o Artillery e benchmarks de desempenho do banco de dados. Implemente gatilhos de rollback automáticos para regressões de desempenho."

- Contexto: Resultados do teste de carga da etapa 10, métricas de referência da fase 1
- Saída: Conjunto de testes de desempenho, integração CI/CD, sistema de prevenção de regressão

## Fase 5: Monitoramento e Otimização Contínua

### 12. Configuração do Monitoramento de Produção

- Use a ferramenta Task com subagent_type="observability-engineer"
- Prompt: "Implemente o monitoramento de desempenho de produção para: $ARGUMENTS. Configure o APM com DataDog/New Relic/Dynatrace, configure o rastreamento distribuído com OpenTelemetry, implemente métricas de negócios personalizadas. Crie painéis do Grafana para as principais métricas, configure alertas do PagerDuty para degradação de desempenho. Defina SLIs/SLOs para serviços críticos com orçamentos de erro."

- Contexto: Melhorias de desempenho de todas as fases anteriores
- Saída: Painéis de monitoramento, regras de alerta, definições de SLI/SLO, manuais de operação

### 13. Otimização Contínua de Desempenho

- Use a ferramenta Tarefa com o subagente `subagent_type="performance-engineer"`
- Prompt: "Estabeleça um processo de otimização contínua para: $ARGUMENTS. Crie um controle do orçamento de desempenho, implemente testes A/B para alterações de desempenho, configure o perfilamento contínuo em produção. Documente o backlog de oportunidades de otimização, crie modelos de planejamento de capacidade e estabeleça ciclos regulares de revisão de desempenho."

- Contexto: Configuração de monitoramento da etapa 12, todo o trabalho de otimização anterior
- Saída: Controle do orçamento de desempenho, backlog de otimização, planejamento de capacidade, processo de revisão

## Opções de Configuração

- **performance_focus**: "latency" | "throughput" | "cost" | "balanced" (padrão: "balanced")
- **optimization_depth**: "quick-wins" | "comprehensive" | "enterprise" (padrão: "comprehensive")
- **tools_available**: ["datadog", "newrelic", "prometheus", "grafana", "k6", "gatling"]
- **budget_constraints**: Define os custos máximos aceitáveis ​​para alterações na infraestrutura
- **user_impact_tolerance**: "zero-downtime" | "maintenance-window" | Implementação gradual

## Critérios de sucesso

- **Tempo de resposta**: P50 < 200 ms, P95 < 1 s, P99 < 2 s para endpoints críticos
- **Indicadores vitais da Web**: LCP < 2,5 s, FID < 100 ms, CLS < 0,1
- **Taxa de transferência**: Suportar o dobro da carga máxima atual com taxa de erro < 1%
- **Desempenho do banco de dados**: Consulta P95 < 100 ms, nenhuma consulta > 1 s
- **Utilização de recursos**: CPU < 70%, Memória < 80% sob carga normal
- **Eficiência de custo**: Desempenho por dólar melhorado em no mínimo 30%
- **Cobertura de monitoramento**: 100% dos caminhos críticos instrumentados com alertas

Meta de otimização de desempenho: $ARGUMENTS