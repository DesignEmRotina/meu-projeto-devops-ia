# Manual de Implementação de Resolução Inteligente de Problemas com Orquestração Multiagente

Este arquivo contém padrões detalhados, listas de verificação e exemplos de código referenciados pela habilidade.

# Resolução Inteligente de Problemas com Orquestração Multiagente

[Pensamento ampliado: Este fluxo de trabalho implementa um pipeline sofisticado de depuração e resolução que utiliza ferramentas de depuração assistidas por IA e plataformas de observabilidade para diagnosticar e resolver sistematicamente problemas de produção. A estratégia de depuração inteligente combina análise automatizada da causa raiz com conhecimento humano, utilizando práticas modernas de 2024/2025, incluindo assistentes de código com IA (GitHub Copilot, Claude Code), plataformas de observabilidade (Sentry, DataDog, OpenTelemetry), automação do git bisect para rastreamento de regressão e técnicas de depuração seguras para produção, como rastreamento distribuído e registro estruturado.] O processo segue uma abordagem rigorosa de quatro fases: (1) Fase de Análise de Problemas - agentes de detecção e depuração de erros analisam rastreamentos de erros, logs, etapas de reprodução e dados de observabilidade para entender o contexto completo da falha, incluindo impactos a montante e a jusante; (2) Fase de Investigação da Causa Raiz - agentes de depuração e revisão de código realizam análises profundas de código, busca binária automatizada no Git para identificar o commit que introduziu o problema, verificações de compatibilidade de dependências e inspeção de estado para isolar o mecanismo exato da falha; (3) Fase de Implementação de Correções - agentes específicos do domínio (python-pro, typescript-pro, rust-expert, etc.) implementam correções mínimas com cobertura de testes abrangente, incluindo testes de unidade, integração e casos extremos, seguindo práticas seguras para produção; (4) Fase de Verificação - agentes de automação de testes e engenharia de desempenho executam suítes de regressão, benchmarks de desempenho, varreduras de segurança e verificam se nenhum novo problema foi introduzido. Problemas complexos que abrangem múltiplos sistemas exigem coordenação orquestrada entre agentes especializados (otimizador de banco de dados → engenheiro de desempenho → solucionador de problemas de DevOps) com passagem explícita de contexto e compartilhamento de estado. O fluxo de trabalho enfatiza a compreensão das causas raízes em vez do tratamento dos sintomas, a implementação de melhorias arquitetônicas duradouras, a automatização da detecção por meio de monitoramento e alertas aprimorados e a prevenção de ocorrências futuras por meio de melhorias no sistema de tipos, regras de análise estática e padrões aprimorados de tratamento de erros. O sucesso é medido não apenas pela resolução de problemas, mas também pela redução do tempo médio de recuperação (MTTR), prevenção de problemas semelhantes e melhoria da resiliência do sistema.

## Fase 1: Análise de Problemas - Detecção de Erros e Coleta de Contexto

Use a ferramenta Task com subagent_type="error-debugging::error-detective" seguido por subagent_type="error-debugging::debugger":

**Primeira Fase: Análise de Detecção de Erros**

**Prompt:**

```
Analise os rastreamentos de erros, logs e dados de observabilidade para: $ARGUMENTS

Entregáveis:

1. Análise da assinatura do erro: tipo de exceção, padrões de mensagens, frequência, primeira ocorrência
2. Análise detalhada do rastreamento de pilha: localização da falha, cadeia de chamadas, componentes envolvidos
3. Etapas de reprodução: caso de teste mínimo, requisitos de ambiente, dados necessários
4. Contexto de observabilidade:

- Grupos de erros e tendências do Sentry/DataDog

- Rastreamentos distribuídos mostrando o fluxo de requisições (OpenTelemetry/Jaeger)

- Logs estruturados (Logs JSON com IDs de correlação)

- Métricas de APM: picos de latência, taxas de erro, uso de recursos
5. Avaliação do impacto no usuário: segmentos de usuários afetados, taxa de erro, impacto nas métricas de negócios
6. Análise da linha do tempo: quando começou, correlação com implantações/alterações de configuração
7. Sintomas relacionados: erros semelhantes, falhas em cascata, impactos upstream/downstream

Técnicas modernas de depuração a serem empregadas:
- Análise de logs assistida por IA (detecção de padrões, identificação de anomalias)
- Correlação de rastreamento distribuída entre microsserviços
- Depuração segura para produção (sem alterações de código, uso de dados de observabilidade)
- Impressão digital de erros para desduplicação e rastreamento
```

**Saída esperada:**
```
ASSINATURA_DO_ERRO: {tipo de exceção + padrão da mensagem principal}
FREQUÊNCIA: {contagem, taxa, tendência}
PRIMEIRA_VISÃO: {timestamp ou commit do git}
RASTREAMENTO_DE_PILHA: {rastreamento formatado com quadros-chave destacados}
REPRODUÇÃO: {etapas mínimas + Dados de exemplo}
LINKS_DE_OBSERVABILIDADE: [URL do Sentry, painel do DataDog, IDs de rastreamento]
IMPACTO_NO_USUÁRIO: {usuários afetados, gravidade, impacto nos negócios}
LINHA DO TEMPO: {quando iniciado, correlação com alterações}
PROBLEMAS_RELACIONADOS: [erros semelhantes, falhas em cascata]
```

**Segunda etapa: Identificação da Causa Raiz do Depurador**

**Solicitação:**
```
Realizar investigação da causa raiz usando a saída do Error-Detective:

Contexto do Error-Detective:
- Assinatura do erro: {ERROR_SIGNATURE}
- Rastreamento da pilha: {STACK_TRACE}
- Reprodução: {REPRODUCTION}
- Observabilidade: {OBSERVABILITY_LINKS}

Entregáveis:
1. Hipótese da causa raiz com evidências de suporte
2. Análise em nível de código: estados de variáveis, fluxo de controle, problemas de temporização
3. Análise de binsect do Git: identificar o commit que introduziu o problema (automatizar com `git bisect run`)
4. Análise de dependências: conflitos de versão, alterações na API, desvios de configuração
5. Inspeção de estado: estado do banco de dados, estado do cache, respostas de APIs externas
6. Mecanismo de falha: por que o código falha nessas condições específicas?
7. Opções de estratégia de correção com compensações (correção rápida vs. correção adequada)

Contexto necessário para a próxima fase:
- Caminhos exatos dos arquivos e números de linha que precisam ser alterados
- Estruturas de dados ou contratos de API afetados
- Dependências que podem precisar de atualizações
- Cenários de teste para verificar a correção
- Características de desempenho a serem mantidas

**Saída esperada:**

CAUSA_RAIZ: {explicação técnica com evidências}
COMMIT_INTRODUZIDO: {SHA do Git + resumo, se encontrado via binsect}
ARQUIVOS_AFETADOS: [caminhos dos arquivos com linha específica] [números]
MECANISMO_DE_FALHA: {motivo da falha - condição de corrida, verificação de nulo, incompatibilidade de tipos, etc.}
DEPENDÊNCIAS: [sistemas relacionados, bibliotecas, APIs externas]
ESTRATÉGIA_DE_CORREÇÃO: {abordagem recomendada com justificativa}
OPÇÃO_DE_CORREÇÃO_RÁPIDA: {mitigação temporária, se aplicável}
OPÇÃO_DE_CORREÇÃO_ADEQUADA: {solução a longo prazo}
REQUISITOS_DE_TESTE: [cenários que devem ser cobertos]
```

## Fase 2: Investigação da Causa Raiz - Análise Profunda do Código

Use a ferramenta Task com subagent_type="error-debugging::debugger" e subagent_type="comprehensive-review::code-reviewer" para investigação sistemática:

**Primeiro: Análise de Código do Depurador**

**Solicitação:**
```
Realize análise profunda do código e investigação binária:

Contexto da Fase 1:
- Causa raiz: {CAUSA_RAIZ}
- Arquivos afetados: {ARQUIVOS_AFETADOS}
- Mecanismo de falha: {MECANISMO_DE_FALHA}
- Commit que introduziu a falha: {COMMIT_DE_INTRODUÇÃO}

Entregáveis:
1. Análise do caminho do código: rastrear a execução desde o ponto de entrada até a falha
2. Rastreamento do estado das variáveis: valores em pontos de decisão chave
3. Análise do fluxo de controle: ramificações tomadas, loops, operações assíncronas
4. Automação do Git bisect: criar um script bisect para identificar o commit que causou a falha
```bash

git bisect start HEAD v1.2.3

git bisect run ./test_reproduction.sh

```
5. Matriz de compatibilidade de dependências: combinações de versões que funcionam/falham
6. Análise de configuração: variáveis ​​de ambiente, flags de recursos, configurações de implantação
7. Análise de tempo e condição de corrida: operações assíncronas, ordem de eventos, bloqueios
8. Análise de memória e recursos: vazamentos, esgotamento, contenção

Técnicas modernas de investigação:
- Explicação de código assistida por IA (Claude/Copilot para entender lógica complexa)
- Busca binária automatizada no Git com teste de reprodução
- Análise do grafo de dependências (npm ls, go mod graph, pip show)
- Detecção de desvio de configuração (comparação entre ambientes de teste e produção)
- Depuração com rastreamento de tempo usando os dados de produção
```

**Saída esperada:**
```
CAMINHO_DO_CÓDIGO: {entrada → ... → local da falha com variáveis-chave}
ESTADO_NA_FALHA: {valores de variáveis, estados de objetos, estado do banco de dados}
RESULTADO_DA_BISECT: {commit exato que introduziu o bug + diff}
PROBLEMAS_DE_DEPENDÊNCIA: [conflitos de versão, alterações que quebram a compatibilidade, CVEs]
DERIVA_DE_CONFIGURAÇÃO: {diferenças entre ambientes}
CONDIÇÕES_DE_CORRIDA: {problemas assíncronos, problemas de ordenação de eventos}
VERIFICAÇÃO_DE_ISOLAMENTO: {causa raiz única confirmada versus múltiplos problemas}
```

**Segunda Etapa: Análise Detalhada do Código**

**Proposta:**

```
Revise a lógica do código e identifique problemas de design:

Contexto do Depurador:
- Caminho do código: {CODE_PATH}
- Estado na falha: {STATE_AT_FAILURE}
- Resultado da busca binária: {BISECT_RESULT}

Entregáveis:
1. Análise de falhas lógicas: suposições incorretas, casos extremos não tratados, algoritmos errados
2. Lacunas de segurança de tipos: onde tipos mais robustos poderiam prevenir o problema
3. Revisão do tratamento de erros: ausência de blocos try-catch, promessas não tratadas, cenários de pânico
4. Validação de contrato: lacunas na validação de entrada, garantias de saída não atendidas
5. Problemas arquiteturais: acoplamento forte, ausência de abstrações, violações de camadas
6. Padrões semelhantes: outras localizações de código com a mesma vulnerabilidade
7. Design de correção: alteração mínima vs. refatoração vs. melhoria arquitetural

Lista de verificação da revisão:
- Os valores nulos/indefinidos são tratados corretamente?

- As operações assíncronas são aguardadas/encadeadas corretamente?

- Os casos de erro são tratados explicitamente?

- As asserções de tipo são seguras?

- Os contratos da API são respeitados?

- Os efeitos colaterais são isolados?
```

**Saída esperada:**
```
FALHAS_LÓGICAS: [suposições ou algoritmos incorretos específicos]
LACUNAS_DE_SEGURANÇA_DE_TIPOS: [onde os tipos poderiam prevenir problemas]
LACUNAS_NO_TRATAMENTO_DE_ERROS: [caminhos de erro não tratados]
VULNERABILIDADES_SIMILAR: [outro código com o mesmo padrão]
CORREÇÃO_DE_DESIGN: {abordagem de mudança mínima}
OPORTUNIDADES_DE_REFATORAÇÃO: {se melhorias maiores forem justificadas}
PREOCUPAÇÕES_ARQUITETÔNICAS: {se existirem problemas sistêmicos}
```

## Fase 3: Implementação da correção - Execução do agente específico do domínio

Com base na saída da Fase 2, direcione para o agente de domínio apropriado usando a ferramenta Tarefa:

**Lógica de roteamento:**
- Problemas com Python → subagent_type="python-development::python-pro"
- TypeScript/JavaScript → subagent_type="javascript-typescript::typescript-pro"
- Go → subagent_type="systems-programming::golang-pro"
- Rust → subagent_type="systems-programming::rust-pro"
- SQL/Banco de Dados → subagent_type="database-cloud-optimization::database-optimizer"
- Desempenho → subagent_type="application-performance::performance-engineer"
- Segurança → subagent_type="security-scanning::security-auditor"

**Modelo de Prompt (adapte para o idioma):**
```
Implemente uma correção segura para produção com cobertura de teste abrangente:

Contexto da Fase 2:
- Causa raiz: {ROOT_CAUSE}
- Falhas lógicas: {LOGIC_FLAWS}
- Projeto de correção: {FIX_DESIGN}
- Lacunas de segurança de tipo: {TYPE_SAFETY_GAPS}
- Vulnerabilidades semelhantes: {SIMILAR_VULNERABILITIES}

Entregáveis:
1. Implementação mínima de correção que aborda a causa raiz (não os sintomas)
2. Testes unitários:

- Reprodução de casos de falha específicos

- Casos extremos (valores limite, nulo/vazio, estouro)

- Cobertura do caminho de erro
3. Testes de integração:

- Cenários de ponta a ponta com dependências reais

- Simulação de API externa quando apropriado

- Verificação do estado do banco de dados
4. Testes de regressão:

- Testes para vulnerabilidades semelhantes

- Testes que abrangem caminhos de código relacionados
5. Validação de desempenho:

- Benchmarks que mostram nenhuma degradação

- Testes de carga, se aplicável
6. Práticas seguras para produção:

- Sinalizadores de recursos para implantação gradual

- Degradação controlada se a correção falhar

- Mecanismos de monitoramento para verificação da correção

- Registro estruturado para depuração

Técnicas modernas de implementação (2024/2025):
- Programação em pares com IA (GitHub Copilot, Código Claude) para geração de testes
- Desenvolvimento orientado a tipos (utilizando TypeScript, mypy, clippy)
- APIs com foco em contratos (OpenAPI, esquemas gRPC)
- Foco em observabilidade (logs estruturados, métricas, rastreamentos)
- Programação defensiva (tratamento explícito de erros, validação)

Requisitos de implementação:
- Seguir os padrões e convenções de código existentes
- Adicionar registro de depuração estratégico (logs estruturados em JSON)
- Incluir anotações de tipo abrangentes
- Atualizar as mensagens de erro para que sejam acionáveis ​​(incluir contexto, sugestões)
- Manter a compatibilidade com versões anteriores (verificar APIs se houver quebra de versão)
- Adicionar spans OpenTelemetry para rastreamento distribuído
- Incluir contadores de métricas para monitoramento (taxas de sucesso/falha)
```

**Saída esperada:**

``` FIX_SUMMARY: {o que mudou e por quê - causa raiz vs sintoma}
CHANGED_FILES: [
{path: "...", changes: "...", reasoning: "..."}
] NOVOS_ARQUIVOS: [{caminho: "...", propósito: "..."}]
COBERTURA_DE_TESTES: {
unidade: "X cenários",

integração: "Y cenários",

casos_limite: "Z cenários",

regressão: "W cenários"
}
RESULTADOS_DE_TESTES: {todos_aprovados: true/false, detalhes: "..."}
ALTERAÇÕES_QUEBRAM_A_COMPLETA: {nenhuma | alterações na API com o caminho de migração}
ADIÇÕES_DE_OBSERVABILIDADE: [
{tipo: "log", localização: "...", propósito: "..."},

{tipo: "métrica", nome: "...", propósito: "..."},

{tipo: "rastreamento", intervalo: "...", propósito: "..."}
]
FLAGS_DE_RECURSOS: [{flag: "...", estratégia_de_implementação: "..."}]
COMPATIBILIDADE_COM VERSÕES ANTERIORES: {mantida | quebrando com mitigação}
```

## Fase 4: Verificação - Testes Automatizados e Validação de Desempenho

Use a ferramenta Task com subagent_type="unit-testing::test-automator" e subagent_type="application-performance::performance-engineer":

**Primeiro: Conjunto de Testes de Regressão do Test-Automator**

**Solicitação:**

```
Execute testes de regressão abrangentes e verifique a qualidade da correção:

Contexto da Fase 3:
- Resumo da correção: {FIX_SUMMARY}
- Arquivos alterados: {CHANGED_FILES}
- Cobertura de testes: {TEST_COVERAGE}
- Resultados dos testes: {TEST_RESULTS}

Entregáveis:

1. Execução completa do conjunto de testes:

- Testes unitários (todos os existentes + novos)

- Testes de integração

- Testes de ponta a ponta

- Testes de contrato (se microsserviços)
2. Detecção de regressão:

- Comparar os resultados dos testes antes e depois da correção

- Identificar quaisquer novas falhas

- Verificar se todos os casos extremos foram cobertos
3. Avaliação da qualidade dos testes:
- Métricas de cobertura de código (linha, ramificação, condição)

- Teste de mutação, se aplicável

- Determinismo de teste (execução múltipla)
4. Testes em diferentes ambientes:

- Testes em ambientes de homologação/QA

- Testes com volumes de dados semelhantes aos de produção

- Testes com condições de rede realistas
5. Testes de segurança:

- Verificações de autenticação/autorização

- Testes de validação de entrada

- Prevenção de injeção de SQL e XSS

- Varredura de vulnerabilidades de dependências
6. Geração automatizada de testes de regressão:

- Uso de IA para gerar testes adicionais de casos extremos

- Testes baseados em propriedades para lógica complexa

- Fuzzing para validação de entrada

Práticas modernas de teste (2024/2025):
- Casos de teste gerados por IA (GitHub Copilot, Claude Code)
- Testes de snapshot para contratos de UI/API
- Testes de regressão visual para frontend
- Engenharia do caos para testes de resiliência
- Reprodução de tráfego de produção para testes de carga

**Saída esperada:**

RESULTADOS_DE_TESTE: {

total: N,
Aprovado: X,

Reprovado: Y,

Ignorado: Z,

Novas_falhas: [listar se houver],

Testes_instáveis: [listar se houver]
}
COBERTURA_DE_CÓDIGO: {
linha: "X%",

branch: "Y%",

função: "Z%",

delta: "+/-W%"
}
REGRESSÃO_DETECTADA: {sim/não + detalhes se sim}
RESULTADOS_DE_AMBIENTES_CROSS: {staging: "...", qa: "..."}
VERIFICAÇÃO_DE_SEGURANÇA: {
vulnerabilidades: [listar ou "nenhuma"],

análise_estática: "...",

auditoria_de_dependência: "..."
}
QUALIDADE_DO_TESTE: {determinístico: verdadeiro/falso, cobertura_adequada: verdadeiro/falso}
```

**Segundo: Validação do Engenheiro de Desempenho**

**Prompt:**
```
Medir o impacto no desempenho e validar não Regressões:

Contexto do Test-Automator:
- Resultados dos testes: {TEST_RESULTS}
- Cobertura de código: {CODE_COVERAGE}
- Resumo das correções: {FIX_SUMMARY}

Entregáveis:
1. Benchmarks de desempenho:

- Tempo de resposta (p50, p95, p99)

- Taxa de transferência (requisições/segundo)

- Utilização de recursos (CPU, memória, E/S)

- Desempenho de consultas ao banco de dados
2. Comparação com a linha de base:

- Métricas antes/depois

- Limiares de degradação aceitáveis

- Oportunidades de melhoria de desempenho
3. Teste de carga:

- Teste de estresse sob carga máxima

- Teste de resistência para vazamentos de memória

- Teste de pico para tratamento de rajadas
4. Análise de APM:

- Análise de rastreamento distribuído

- Detecção de consultas lentas

- Padrões de consulta N+1
5. Perfil de recursos:

- Gráficos de chama da CPU

- Rastreamento de alocação de memória

- Vazamentos de goroutines/threads
6. Prontidão para produção:

- Impacto no planejamento de capacidade

- Características de escalabilidade

- Implicações de custo (nuvem) Recursos)

Práticas modernas de desempenho:
- Instrumentação OpenTelemetry
- Perfilamento contínuo (Pyroscope, pprof)
- Monitoramento de Usuário Real (RUM)
- Monitoramento sintético
```

**Saída esperada:**
```
DESEMPENHO_BASELINE: {

response_time_p95: "Xms",

throughput: "Y req/s",

cpu_usage: "Z%",

memory_usage: "W MB"
}
DESEMPENHO_APÓS_A CORREÇÃO: {
response_time_p95: "Xms (delta)",

throughput: "Y req/s (delta)",

cpu_usage: "Z% (delta)",

memory_usage: "W MB (delta)"
}
IMPACTO_NO_DESEMPENHO: {
veredicto: "melhorado|neutro|degradado",

aceitável: verdadeiro/falso,

raciocínio: "..."
}
RESULTADOS_DO_TESTE_DE_CARGA: {

max_throughput: "...",

breakpoint: "...",

memory_leaks: "nenhum|detectado"
}
INSIGHTS_APM: [consultas lentas, [Padrões N+1, gargalos]
PRONTO_PARA_PRODUÇÃO: {sim/não + bloqueadores se não}
```

**Terceira etapa: Aprovação final do revisor de código**

**Solicitação:**
```
Realizar revisão final do código e aprovar para implantação:

Contexto dos testes:
- Resultados dos testes: {RESULTADOS_DE_TESTES}
- Regressão detectada: {REGRESSÃO_DETECTADA}
- Impacto no desempenho: {IMPACTO_NO_DESEMPENHO}
- Análise de segurança: {ANÁLISE_DE_SEGURANÇA}

Entregáveis:

1. Revisão da qualidade do código:

- Segue as convenções do projeto

- Sem problemas de código ou antipadrões

- Tratamento de erros adequado

- Registro e observabilidade adequados
2. Revisão da arquitetura:

- Mantém os limites do sistema

- Sem acoplamento forte introduzido

- Considerações de escalabilidade
3. Revisão de segurança:

- Sem vulnerabilidades de segurança

- Validação de entrada adequada

- Autenticação/autorização correta
4. Documentação Revisão:

- Comentários no código onde necessário

- Documentação da API atualizada

- Manual de procedimentos atualizado, se houver impacto operacional
5. Preparação para implantação:

- Plano de reversão documentado

- Estratégia de flags de recursos definida

- Monitoramento/alertas configurados
6. Avaliação de riscos:

- Estimativa do raio de impacto
- Recomendação de estratégia de implantação

- Métricas de sucesso definidas

Lista de verificação da revisão:
- Todos os testes aprovados
- Sem regressões de desempenho
- Vulnerabilidades de segurança corrigidas
- Alterações que causam quebra de compatibilidade documentadas
- Compatibilidade com versões anteriores mantida
- Observabilidade adequada
- Plano de implantação claro
```

**Saída esperada:**
```
STATUS_DA_REVISÃO: {APROVADO|NECESSITA_DE_REVISÃO|BLOQUEADO}
QUALIDADE_DO_CÓDIGO: {pontuação/avaliação}
PREOCUPAÇÕES_DE_ARQUITETURA: [listar ou "nenhuma"]
PREOCUPAÇÕES_DE_SEGURANÇA: [listar ou "nenhuma"]
RISCO_DE_IMPLANTAÇÃO: {baixo|médio|alto}
PLANO_DE_ROLLBACK: {

etapas: ["..."],

tempo_estimado: "X minutos",

recuperação_de_dados: "..."
}
ESTRATÉGIA_DE_IMPLIFICAÇÃO: {
abordagem: "canário|azul-verde|contínuo|big-bang",

fases: ["..."],

métricas_de_sucesso: ["..."],

critérios_de_aborto: ["..."]
}
REQUISITOS_DE_MONITORAMENTO: [
{métrica: "...", limite: "...", ação: "..."}

VEREDITO_FINAL: {

aprovado: verdadeiro/falso,

bloqueadores: [listar se não aprovado],

recomendações: ["..."]
}
```

## Fase 5: Documentação e Prevenção - Resiliência a Longo Prazo

Use a ferramenta Task com subagent_type="comprehensive-review::code-reviewer" para estratégias de prevenção:

**Prompt:**

```
Documente a correção e Implementar estratégias de prevenção para evitar recorrências:

Contexto da Fase 4:
- Veredito final: {FINAL_VERDICT}
- Status da revisão: {REVIEW_STATUS}
- Causa raiz: {ROOT_CAUSE}
- Plano de reversão: {ROLLBACK_PLAN}
- Requisitos de monitoramento: {MONITORING_REQUIREMENTS}

Entregáveis:
1. Documentação do código:

- Comentários embutidos para lógica não óbvia (mínimo)

- Atualizações na documentação de funções/classes

- Documentação do contrato da API
2. Documentação operacional:

- Entrada no CHANGELOG com descrição e versão da correção

- Notas de versão para as partes interessadas

- Entrada no runbook para engenheiros de plantão

- Documento pós-incidente (se o incidente for de alta gravidade)
3. Prevenção por meio de análise estática:

- Adicionar regras de linting (eslint, ruff, golangci-lint)

- Configurar configurações mais rigorosas de compilador/verificador de tipos

- Adicionar regras de linting personalizadas para padrões específicos do domínio

- Atualizar o pre-commit 4. Melhorias no sistema de tipos:

- Adicionar verificação de exaustividade
- Usar tipos de união/soma discriminados
- Adicionar modificadores const/readonly

- Aproveitar tipos de marca para validação
5. Monitoramento e alertas:

- Criar alertas de taxa de erros (Sentry, DataDog)

- Adicionar métricas personalizadas para a lógica de negócios

- Configurar monitores sintéticos (Pingdom, Checkly)

- Configurar painéis de SLO/SLI
6. Melhorias arquitetônicas:

- Identificar padrões de vulnerabilidade semelhantes

- Propor refatoração para melhor isolamento

- Documentar decisões de design

- Atualizar diagramas de arquitetura, se necessário
7. Melhorias nos testes:

- Adicionar testes baseados em propriedades

- Expandir cenários de teste de integração

- Adicionar testes de engenharia do caos

- Documentar lacunas na estratégia de testes

Práticas modernas de prevenção (2024/2025):
- Regras de revisão de código assistidas por IA (GitHub Copilot, Claude Code)
- Varredura contínua de segurança (Snyk, Dependabot)
- Validação de Infraestrutura como Código (Terraform validate, CloudFormation) Linter)
- Teste de contratos para APIs (Pact, validação OpenAPI)
- Desenvolvimento orientado à observabilidade (instrumentação antes da implantação)
```

**Saída esperada:**
```
ATUALIZAÇÕES_DE_DOCUMENTAÇÃO: [
{arquivo: "CHANGELOG.md", resumo: "..."},

{arquivo: "docs/runbook.md", resumo: "..."},

{arquivo: "docs/architecture.md", resumo: "..."}
]
MEDIDAS_DE_PREVENÇÃO: {

análise_estática: [
{ferramenta: "eslint", regra: "...", motivo: "..."},

{ferramenta: "ruff", regra: "...", motivo: "..."}

],

sistema_de_tipos: [
{aprimoramento: "...", localização: "...", benefício: "..."}

],

ganchos_pré_commit: [
{gancho: "...", propósito: "..."}

]
}
MONITORAMENTO_ADICIONADO: {

alertas: [
{nome: "...", limite: "...", canal: "..."}

],

painéis: [
{nome: "...", métricas: [...], url: "..."}

],

slos: [
{service: "...", sli: "...", target: "...", window: "..."}

]
}
MELHORIAS_ARQUITETÔNICAS: [
{improvement: "...", reasoning: "...", effort: "small|medium|large"}

VULNERABILIDADES_SIMILAR: {
found: N,

locations: [...],

remediation_plan: "..."
}
TAREFAS_DE_ACOMPANHAMENTO: [
{task: "...", priority: "high|medium|low", owner: "..."}

] ANÁLISE PÓS-INCIDÊNCIA: {
created: true/false,

location: "...",

incident_severity: "SEV1|SEV2|SEV3|SEV4"
}
ATUALIZAÇÕES_DA_BASE_DE_CONHECIMENTO: [
{article: "...", summary: "..."}
]
```

## Coordenação Multidomínio para Problemas Complexos

Para problemas que abrangem múltiplos domínios, orquestre agentes especializados sequencialmente com passagem de contexto explícita:

**Exemplo 1: Problema de desempenho do banco de dados causando timeouts da aplicação**

**Sequência:**
1. **Fase 1-2**: detecção de erros + depurador identificam consultas lentas ao banco de dados
2. **Fase 3a**: Task(subagent_type="database-cloud-optimization::database-optimizer")

- Otimizar consulta com índices adequados
- Contexto: "Execução da consulta levando 5s, índice ausente na coluna user_id, padrão de consulta N+1 detectado"
3. **Fase 3b**: Task(subagent_type="application-performance::performance-engineer")

- Adicionar camada de cache para dados acessados ​​frequentemente
- Contexto: "Consulta ao banco de dados otimizada de 5s para 50ms com a adição de um índice na coluna user_id. A aplicação ainda apresenta tempos de resposta de 2s devido ao carregamento do padrão de consulta N+1" Mais de 100 registros de usuários por solicitação. Adicione cache Redis com TTL de 5 minutos para perfis de usuário.
4. **Fase 3c**: Task(subagent_type="incident-response::devops-troubleshooter")
- Configure o monitoramento de desempenho de consultas e taxas de acerto de cache
- Contexto: "Camada de cache adicionada com Redis. Necessário monitoramento para: latência p95 da consulta (limite: 100ms), taxa de acerto de cache (limite: >80%), uso de memória cache (alerta em 80%)."

**Exemplo 2: Erro de JavaScript no Frontend em Produção**

**Sequência:**
1. **Fase 1**: o detector de erros analisa os relatórios de erro do Sentry
- Contexto: "TypeError: Não é possível ler a propriedade 'map' de undefined, mais de 500 ocorrências na última hora, afetando usuários do Safari no iOS 14"
2. **Fase 2**: o depurador e o revisor de código investigam
- Contexto: "A resposta da API às vezes retorna null em vez de um array vazio quando não há resultados. O frontend assume um array."

3. **Fase 3a**: Task(subagent_type="javascript-typescript::typescript-pro")

- Corrigir o frontend com verificações de nulo adequadas
- Adicionar verificações de tipo
- Contexto: "O endpoint /api/users da API do backend retorna null em vez de [] quando não há resultados. Corrigir o frontend para lidar com ambos. Adicionar verificações de nulo estritas do TypeScript."

4. **Fase 3b**: Task(subagent_type="backend-development::backend-architect")
- Corrigir o backend para sempre retornar um array
- Atualizar o contrato da API
- Contexto: "O frontend agora lida com valores nulos, mas a API deve seguir o contrato e retornar [] em vez de nulo. Atualizar a especificação OpenAPI para documentar isso."
5. **Fase 4**: o automatizador de testes executa testes entre navegadores
6. **Fase 5**: o revisor de código documenta as alterações no contrato da API

**Exemplo 3: Vulnerabilidade de segurança na autenticação**

**Sequência:**
1. **Fase 1**: o detector de erros revisa o relatório de varredura de segurança
- Contexto: "Vulnerabilidade de injeção de SQL no endpoint de login, gravidade Snyk: ALTA"
2. **Fase 2**: o depurador e o auditor de segurança investigam
- Contexto: "Entrada do usuário não sanitizada na cláusula WHERE do SQL, permite bypass de autenticação"
3. **Fase 3**: Task(subagent_type="security-scanning::security-auditor")

- Implementar consultas parametrizadas

- Adicionar validação de entrada

- Adicionar limitação de taxa

- Contexto: "Substituir concatenação de strings por instruções preparadas. Adicionar validação de entrada para formato de e-mail. Implementar limitação de taxa (5 tentativas a cada 15 minutos)." 4. **Fase 4a**: o automatizador de testes adiciona testes de segurança

- Tentativas de injeção de SQL

- Cenários de força bruta
5. **Fase 4b**: o auditor de segurança realiza testes de penetração
6. **Fase 5**: o revisor de código documenta as melhorias de segurança e cria um relatório pós-mortem

**Modelo de Passagem de Contexto:**

```
Contexto para {next_agent}:

Concluído por {previous_agent}:
- {summary_of_work}
- {key_findings}
- {changes_made}

Trabalho restante:
- {specific_tasks_for_next_agent}
- {files_to_modify}
- {constraints_to_follow}

Dependências:
- {systems_or_components_affected}
- {data_needed}
- {integration_points}

Critérios de sucesso:
- {resultados_mensuráveis}
- {etapas_de_verificação}
```

## Opções de Configuração

Personalize o comportamento do fluxo de trabalho definindo prioridades na invocação:

**NÍVEL_DE_VERIFICAÇÃO**: Controla a profundidade dos testes e da validação
- **mínimo**: Correção rápida com testes básicos, ignorando benchmarks de desempenho

- Use para: Bugs de baixo risco, problemas estéticos, correções de documentação

- Fases: 1-2-3 (ignora a Fase 4 detalhada)

- Duração: ~30 minutos
- **padrão**: Cobertura completa de testes + revisão de código (padrão)

- Use para: A maioria dos bugs de produção, problemas de funcionalidades, bugs de dados

- Fases: 1-2-3-4 (todas as verificações)

- Duração: ~2-4 horas
- **abrangente**: Padrão + auditoria de segurança + benchmarks de desempenho + testes de caos

- Use para: Problemas de segurança, problemas de desempenho, corrupção de dados, sistemas de alto tráfego

- Fases: 1-2-3-4-5 (incluindo prevenção a longo prazo)

- Duração: ~1-2 dias

**FOCO_NA_PREVENÇÃO**: Controla o investimento no futuro Prevenção
- **nenhuma**: Apenas correção, sem trabalho de prevenção
- Use para: Problemas pontuais, código legado sendo descontinuado, bugs em bibliotecas externas
- Saída: Correção de código + apenas testes
- **imediata**: Adiciona testes e linting básico (padrão)

- Use para: Bugs comuns, padrões recorrentes, código-fonte da equipe
- Saída: Correção + testes + regras de linting + monitoramento mínimo
- **abrangente**: Conjunto completo de prevenção com monitoramento e melhorias na arquitetura

- Use para: Incidentes de alta gravidade, problemas sistêmicos, problemas de arquitetura

- Saída: Correção + testes + linting + monitoramento + documentação da arquitetura + análise pós-incidente

**ESTRATÉGIA_DE_IMPLANTAÇÃO**: Controla a abordagem de implantação
- **imediata**: Implantação direta em produção (para correções rápidas, alterações de baixo risco)
- **canário**: Implantação gradual para um subconjunto do tráfego (padrão para risco médio)
- **azul-verde**: Troca completa de ambiente com capacidade de reversão instantânea
- **flag de recurso**: Implantação de código, mas controle a ativação via sinalizadores de recursos (alterações de alto risco)

**NÍVEL_DE_OBSERVABILIDADE**: Controla a profundidade da instrumentação
- **mínimo**: Registro básico de erros apenas
- **padrão**: Logs estruturados + métricas principais (padrão)
- **abrangente**: Rastreamento distribuído completo + painéis personalizados + SLOs

**Exemplo de Invocação:**
```
Problema: Usuários enfrentando erros de tempo limite na página de finalização da compra (mais de 500 erros/hora)

Configuração:
- NÍVEL_DE_VERIFICAÇÃO: abrangente (afeta a receita)
- FOCO_NA_PREVENÇÃO: abrangente (alto impacto nos negócios)
- ESTRATÉGIA_DE_IMPLANTAÇÃO: canário (testar primeiro com 5% do tráfego)
- NÍVEL_DE_OBSERVABILIDADE: abrangente (necessita de monitoramento detalhado)
```

## Integração com Ferramentas Modernas de Depuração

Este fluxo de trabalho utiliza ferramentas modernas de 2024/2025:

**Plataformas de Observabilidade:**
- Sentry (rastreamento de erros, lançamento) **Rastreamento, monitoramento de desempenho)
- DataDog (APM, logs, rastreamentos, monitoramento de infraestrutura)
- OpenTelemetry (rastreamento distribuído independente de fornecedor)
- Honeycomb (observabilidade para sistemas distribuídos complexos)
- New Relic (APM, monitoramento sintético)

**Depuração assistida por IA:**
- GitHub Copilot (sugestões de código, geração de testes, reconhecimento de padrões de bugs)
- Claude Code (análise de código abrangente, revisão de arquitetura)
- Sourcegraph Cody (busca e compreensão da base de código)
- Tabnine (preenchimento automático de código com prevenção de bugs)

**Git e controle de versão:**
- Busca binária automatizada com scripts de reprodução
- GitHub Actions para testes automatizados em commits de busca binária
- Análise de git blame para identificar a propriedade do código
- Análise de mensagens de commit para entender as alterações

**Frameworks de teste:**
- Jest/Vitest (testes de unidade/integração em JavaScript/TypeScript)
- pytest (testes em Python com fixtures e parametrização)
- Testes em Go + testify **Testes unitários e orientados a tabelas em Go:**
- Playwright/Cypress (testes de navegador de ponta a ponta)
- k6/Locust (testes de carga e desempenho)

**Análise Estática:**
- ESLint/Prettier (linting e formatação de JavaScript/TypeScript)
- Ruff/mypy (linting e verificação de tipos em Python)
- golangci-lint (linting abrangente em Go)
- Clippy (linting e melhores práticas em Rust)
- SonarQube (qualidade e segurança de código corporativo)

**Perfilamento de Desempenho:**
- Chrome DevTools (desempenho do frontend)
- pprof (perfilamento em Go)
- py-spy (perfilamento em Python)
- Pyroscope (perfilamento contínuo)
- Flame graphs para análise de CPU/memória

**Verificação de Segurança:**
- Snyk (verificação de vulnerabilidades em dependências)
- Dependabot (atualizações automáticas de dependências)
- OWASP ZAP (teste de segurança)
- Semgrep (regras de segurança personalizadas)
- npm audit / pip-audit / cargo audit

## Critérios de Sucesso

Uma correção é considerada completa quando TODOS os seguintes critérios forem atendidos:

**Compreensão da Causa Raiz:**
- A causa raiz é identificada com evidências que a comprovam
- O mecanismo de falha é claramente documentado
- O commit que introduziu a falha é identificado (se aplicável, via git bisect)
- Vulnerabilidades semelhantes são catalogadas

**Qualidade da Correção:**
- A correção aborda a causa raiz, não apenas os sintomas
- Alterações mínimas no código (evitar engenharia excessiva)
- Segue as convenções e padrões do projeto
- Nenhum "code smell" ou antipadrão foi introduzido
- Compatibilidade com versões anteriores é mantida (ou alterações que quebram a compatibilidade são documentadas)

**Verificação por Teste:**
- Todos os testes existentes são aprovados (zero regressões)
- Novos testes cobrem a reprodução específica do bug
- Casos extremos e caminhos de erro são testados
- Testes de integração verificam o comportamento de ponta a ponta
- Cobertura de testes aumentada (ou mantida em alto nível)

**Desempenho e Segurança:**
- Sem degradação de desempenho (latência p95 dentro de 5% da linha de base)
- Sem **Vulnerabilidades de segurança introduzidas:**
- Uso de recursos aceitável (memória, CPU, E/S)
- Teste de carga aprovado para alterações de alto tráfego

**Preparação para Implantação:**
- Revisão de código aprovada por especialista da área
- Plano de reversão documentado e testado
- Flags de recursos configuradas (se aplicável)
- Monitoramento e alertas configurados
- Manual de procedimentos atualizado com etapas de solução de problemas

**Medidas de Prevenção:**
- Regras de análise estática adicionadas (se aplicável)
- Melhorias no sistema de tipos implementadas (se aplicável)
- Documentação atualizada (código, API, manual de procedimentos)
- Relatório pós-incidente criado (se incidente de alta gravidade)
- Artigo na base de conhecimento criado (se problema novo)

**Métricas:**
- Tempo Médio de Recuperação (MTTR): < 4 horas para SEV2+
- Taxa de recorrência de bugs: 0% (a mesma causa raiz não deve ocorrer novamente)
- Cobertura de testes: Sem redução, idealmente aumento
- Taxa de sucesso de implantação: > 95% (taxa de reversão < 5%)

Problema a ser resolvido: $ARGUMENTOS