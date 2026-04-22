--- 
name: redação-de-post-mortem
description: "Guia completo para escrever relatórios pós-incidente eficazes e sem culpabilização, que impulsionam o aprendizado organizacional e previnem a recorrência de incidentes."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Redação de Post-mortem

Guia completo para escrever relatórios pós-incidente eficazes e sem culpabilização, que impulsionam o aprendizado organizacional e previnem a recorrência de incidentes.

## Não use esta habilidade quando

- A tarefa não estiver relacionada à redação de post-mortem
- Você precisar de um domínio ou ferramenta diferente, fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Utilize esta habilidade quando:

- Realizar análises pós-incidente
- Redigir documentos de análise pós-incidente
- Facilitar reuniões de análise pós-incidente sem atribuição de culpa
- Identificar causas raízes e fatores contribuintes
- Criar itens de acompanhamento acionáveis
- Construir uma cultura de aprendizagem organizacional

## Conceitos Essenciais

### 1. Cultura sem Atribuição de Culpa

| Focada na Culpa | Sem Atribuição de Culpa |

|---------------|-----------|

| "Quem causou isso?" | "Quais condições permitiram isso?" |

| "Alguém cometeu um erro" | "O sistema permitiu esse erro" |

| Punir indivíduos | Melhorar sistemas |

| Ocultar informações | Compartilhar aprendizados |

| Medo de se manifestar | Segurança psicológica |

### 2. Gatilhos para Análise Pós-Incidente

- Incidentes SEV1 ou SEV2
- Interrupções que afetam o cliente com duração superior a 15 minutos
- Perda de dados ou incidentes de segurança
- Quase acidentes que poderiam ter sido graves
- Modos de falha inéditos
- Incidentes que exigem intervenção incomum

## Início Rápido

### Cronograma da Análise Pós-Incidente
```
Dia 0: Ocorrência do incidente
Dias 1-2: Elaboração do rascunho do documento de análise pós-incidente
Dias 3-5: Reunião de análise pós-incidente
Dias 5-7: Finalização do documento, criação de chamados
Semana 2+: Conclusão dos itens de ação
Trimestralmente: Revisão de padrões entre os incidentes
```

## Modelos

### Modelo 1: Análise Pós-Incidente Padrão

```markdown
# Análise Pós-Incidente: [Título do Incidente]

**Data**: 15/01/2024
**Autores**: @alice, @bob
**Status**: Rascunho | Em Revisão | Classificação Final do Incidente: SEV2

Duração do Incidente: 47 minutos

## Resumo Executivo

Em 15 de janeiro de 2024, o serviço de processamento de pagamentos sofreu uma interrupção de 47 minutos, afetando aproximadamente 12.000 clientes. A causa raiz foi o esgotamento do pool de conexões do banco de dados, desencadeado por uma alteração de configuração na implantação v2.3.4. O incidente foi resolvido com o retorno à versão v2.3.3 e o aumento dos limites do pool de conexões.

**Impacto**:
- 12.000 clientes impossibilitados de concluir compras
- Perda estimada de receita: US$ 45.000
- 847 chamados de suporte criados
- Sem perda de dados ou implicações de segurança

## Linha do Tempo (Todos os horários em UTC)

| Hora | Evento |

|------|-------|

| 14:23 | Implantação v2.3.4 concluída em produção |

| 14:31 | Primeiro alerta: `payment_error_rate > 5%` | | 14:33 | A engenheira de plantão @alice reconhece o alerta |
| 14:35 | Início da investigação inicial, taxa de erros em 23% |
| 14:41 | Incidente declarado SEV2, @bob entra na equipe |
| 14:45 | Identificada exaustão de conexões com o banco de dados |
| 14:52 | Decisão de reverter a implantação |
| 14:58 | Reversão para a versão 2.3.3 iniciada |
| 15:10 | Reversão concluída, taxa de erros diminuindo |
| 15:18 | Serviço totalmente recuperado, incidente resolvido |

## Análise da Causa Raiz

### O que aconteceu

A implementação da versão 2.3.4 incluiu uma alteração no padrão de consulta ao banco de dados que, inadvertidamente, removeu o pool de conexões para um endpoint frequentemente acessado. Cada requisição abria uma nova conexão com o banco de dados em vez de reutilizar as conexões do pool.

### Por que aconteceu

1. **Causa Imediata**: A alteração no código em `PaymentRepository.java` substituiu o pool de `DataSource` por chamadas diretas a `DriverManager.getConnection()`.

2. **Fatores Contribuintes**:

- A revisão de código não detectou a alteração no tratamento de conexões

- Ausência de testes de integração específicos para o comportamento do pool de conexões

- O ambiente de staging possui tráfego reduzido, mascarando o problema

- O limite de alerta das métricas de conexão do banco de dados estava muito alto (90%)

3. **Análise dos 5 Porquês**:

- Por que o serviço falhou? → Conexões com o banco de dados esgotadas
- Por que as conexões foram esgotadas? → Cada requisição abria uma nova conexão

- Por que cada requisição abria uma nova conexão? → O código ignorou o pool de conexões
- Por que o código ignorou o pool de conexões? → Desenvolvedor não familiarizado com padrões de código
- Por que o desenvolvedor não estava familiarizado? → Sem documentação sobre padrões de gerenciamento de conexões

### Diagrama do Sistema

```
[Cliente] → [Balanceador de Carga] → [Serviço de Pagamento] → [Banco de Dados]

↓

Pool de Conexões (com problemas)

↓

Conexões diretas (causa)
```

## Detecção

### O que funcionou
- Alerta de taxa de erros disparado em até 8 minutos após a implantação
- O painel do Grafana mostrou claramente o pico de conexões
- Resposta rápida do suporte (reconhecimento em 2 minutos)

### O que não funcionou
- Limiar de alerta da métrica de conexão do banco de dados muito alto
- Sem alertas correlacionados à implantação
- Uma implantação canary teria detectado o problema mais cedo

### Lacuna na Detecção
A implantação foi concluída às 14h23, mas o primeiro alerta só foi disparado às 14h31 (8 minutos). Um alerta que reconhecesse a implantação poderia ter detectado o problema mais rapidamente.

## Resposta

### O que funcionou
- O engenheiro de plantão identificou rapidamente o banco de dados como o problema
- A decisão de reverter o problema foi tomada de forma decisiva
- Comunicação clara no canal de incidentes

### O que poderia ser melhorado
- Levou 10 minutos para correlacionar o problema com a implantação recente
- Foi necessário verificar manualmente o histórico de implantações
- A reversão levou 12 minutos (poderia ser mais rápida)

## Impacto

### Impacto no cliente
- 12.000 clientes únicos afetados
- Duração média do impacto: 35 minutos
- 847 chamados de suporte (23% dos usuários afetados)
- A pontuação de satisfação do cliente caiu 12 pontos

### Impacto nos negócios
- Perda de receita estimada: US$ 45.000
- Custo do suporte: ~US$ 2.500 (tempo do agente)
- Tempo de engenharia: ~8 horas-homem

### Impacto técnico
- O banco de dados primário apresentou carga elevada
- Algum atraso na réplica durante o incidente
- Nenhum dano permanente aos sistemas

## Lições aprendidas

### O que deu errado Bem-estar
1. O sistema de alertas detectou o problema antes que o cliente o reportasse
2. A equipe colaborou de forma eficaz sob pressão
3. O procedimento de reversão funcionou sem problemas
4. A comunicação foi clara e oportuna

### O que deu errado
1. A revisão de código não detectou uma alteração crítica
2. Lacuna na cobertura de testes para o pool de conexões
3. O ambiente de homologação não reflete o tráfego de produção
4. Os limites de alerta não foram ajustados corretamente

### Onde tivemos sorte
1. O incidente ocorreu durante o horário comercial com toda a equipe disponível
2. O banco de dados suportou a carga sem falhar completamente
3. Nenhum outro incidente ocorreu simultaneamente

## Itens de ação

| Prioridade | Ação | Responsável | Data de vencimento | Ticket |

|----------|--------|-------|----------|--------|

| P0 | Adicionar teste de integração para o comportamento do pool de conexões | @alice | 22/01/2024 | ENG-1234 |

| P0 | Reduzir o limite de alerta de conexão do banco de dados para 70% | @bob | 17/01/2024 | OPS-567 |
| P1 | Documentar padrões de gerenciamento de conexão | @alice | 29/01/2024 | DOC-89 |
| P1 | Implementar alertas correlacionados à implantação | @bob | 05/02/2024 | OPS-568 |
| P2 | Avaliar estratégia de implantação canary | @charlie | 15/02/2024 | ENG-1235 |

| P2 | Testar a carga do ambiente de teste com tráfego semelhante ao de produção | @dave | 28/02/2024 | QA-123 |

## Apêndice

### Dados de Suporte

#### Gráfico da Taxa de Erros
[Link para captura de tela do painel do Grafana]

#### Gráfico de Conexões com o Banco de Dados
[Link para métricas]

### Incidentes Relacionados
- 02/11/2023: Problema de conexão semelhante no Serviço de Usuário (POSTMORTEM-42)

### Referências
- Melhores Práticas para Pool de Conexões
- Manual de Implantação
```

### Modelo 2: Análise dos 5 Porquês

```markdown
# Análise dos 5 Porquês: [Incidente]

## Declaração do Problema
O serviço de pagamento sofreu uma interrupção de 47 minutos devido ao esgotamento das conexões com o banco de dados.

## Análise

### Porquê nº 1: Por que o serviço falhou?

**Resposta**: As conexões com o banco de dados foram esgotadas, causando a falha de todas as novas solicitações.

**Evidência**: As métricas mostraram uma contagem de conexões de 100/100 (máxima), com mais de 500 solicitações pendentes.

---

### Por que #2: Por que as conexões com o banco de dados foram esgotadas?

**Resposta**: Cada requisição recebida abria uma nova conexão com o banco de dados em vez de usar o pool de conexões.

**Evidência**: A comparação de código mostra o uso direto de `DriverManager.getConnection()` em vez de `DataSource` do pool.

---

### Por que #3: Por que o código ignorou o pool de conexões?

**Resposta**: Um desenvolvedor refatorou a classe do repositório e inadvertidamente alterou o método de aquisição de conexão.

**Evidência**: O PR #1234 mostra a alteração, feita ao corrigir um bug diferente.

---

### Por que #4: Por que isso não foi detectado na revisão de código?

**Resposta**: O revisor focou na alteração funcional (a correção do bug) e não percebeu a alteração na infraestrutura.

**Evidência**: Os comentários da revisão discutem apenas a lógica de negócios.

---

### Por que #5: Por que não existe uma rede de segurança para esse tipo de alteração? **Resposta**: Não temos testes automatizados que verifiquem o comportamento do pool de conexões e não temos documentação sobre nossos padrões de conexão.

**Evidência**: O conjunto de testes não possui testes para o tratamento de conexões; a wiki não possui artigo sobre conexões de banco de dados.

## Causas Raiz Identificadas

1. **Primária**: Ausência de testes automatizados para o comportamento da infraestrutura
2. **Secundária**: Documentação insuficiente dos padrões arquitetônicos
3. **Terciária**: A lista de verificação da revisão de código não inclui considerações sobre a infraestrutura

## Melhorias Sistêmicas

| Causa Raiz | Melhoria | Tipo |

|------------|-------------|------|

| Testes ausentes | Adicionar testes de comportamento da infraestrutura | Prevenção |

| Documentação ausente | Documentar padrões de conexão | Prevenção |

| Lacunas na revisão | Atualizar a lista de verificação da revisão | Detecção |

| Sem canary | Implementar implantações canary | Mitigação | ```

### Modelo 3: Análise Pós-Incidente Rápida (Incidentes Menores)

```markdown
# Análise Pós-Incidente Rápida: [Título Breve]

**Data**: 15/01/2024 | **Duração**: 12 min | **Gravidade**: SEV3

## O que aconteceu
A latência da API atingiu um pico de 5 segundos devido a uma tempestade de falhas de cache após a limpeza do cache.

## Cronologia
- 10:00 - Limpeza do cache iniciada para atualização de configuração
- 10:02 - Alertas de latência disparados
- 10:05 - Identificada como tempestade de falhas de cache
- 10:08 - Aquecimento de cache ativado
- 10:12 - Latência normalizada

## Causa raiz
A limpeza completa do cache para uma pequena atualização de configuração causou um pico de latência.

## Correção
- Imediata: Ativar o aquecimento de cache
- Longo prazo: Implementar a invalidação parcial de cache (ENG-999)

## Lições aprendidas
Não limpe completamente o cache em produção; use a invalidação direcionada.

```

## Guia de Facilitação

### Conduzindo uma Reunião Pós-Incidente

```markdown
## Estrutura da Reunião (60 minutos)

### 1. Abertura (5 min)
- Relembrar a todos a cultura de não culpabilização
- "Estamos aqui para aprender, não para culpar"
- Revisar as normas da reunião

### 2. Revisão da Linha do Tempo (15 min)
- Percorrer os eventos cronologicamente
- Fazer perguntas para esclarecimento
- Identificar lacunas na linha do tempo

### 3. Discussão da Análise (20 min)
- O que falhou?

- Por que falhou?

- Quais condições permitiram isso?

- O que teria evitado?

### 4. Itens de Ação (15 min)
- Brainstorm de melhorias
- Priorizar por impacto e esforço
- Atribuir responsáveis ​​e prazos

### 5. Encerramento (5 min)
- Resumir os principais aprendizados
- Confirmar os responsáveis ​​pelos itens de ação
- Agendar acompanhamento, se necessário

## Dicas de Facilitação
- Manter a discussão focada
- Direcionar a culpa para os sistemas
- Incentivar a participação de pessoas mais quietas
- Documentar opiniões divergentes
- Limitar o tempo para digressões
```

## Antipadrões a Evitar

| Antipadrão | Problema | Melhor Abordagem |

|--------------|---------|-----------------|

| **Jogo de culpa** | Impede o aprendizado | Foco nos sistemas |

| **Análise superficial** | Não previne recorrências | Perguntar "por quê?" 5 vezes |

| **Sem itens de ação** | Perda de tempo | Sempre tenha próximos passos concretos |

| **Ações irrealistas** | Nunca concluído | Escopo para tarefas realizáveis ​​|

| **Sem acompanhamento** | Ações esquecidas | Rastreamento em sistema de tickets |

## Melhores Práticas

### O que fazer
- **Comece imediatamente** - A memória falha rapidamente
- **Seja específico** - Horários exatos, erros exatos
- **Inclua gráficos** - Evidências visuais
- **Atribua responsáveis** - Sem itens de ação órfãos
- **Compartilhe amplamente** - Aprendizado organizacional

### O que não fazer
- **Não explique publicamente** - Nunca
- **Não ignore pequenos incidentes** - Eles revelam padrões
- **Não transforme em um documento de busca de culpados** - Isso impede o aprendizado
- **Não crie tarefas improdutivas** - As ações devem ser significativas
- **Não ignore o acompanhamento** - Verifique se as ações foram concluídas

## Recursos

- [Google SRE - Cultura de Análise Pós-Incidente](https://sre.google/sre-book/postmortem-culture/)
- [Etsy's Blameless](https://sre.google/sre-book/postmortem-culture/) [Análises pós-mortem](https://codeascraft.com/2012/05/22/blameless-postmortems/)
- [Guia de Análises Pós-Mortem do PagerDuty](https://postmortems.pagerduty.com/)
