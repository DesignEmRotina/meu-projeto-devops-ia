--- 
name: padrões-de-transferência-de-plantão
description: "Padrões eficazes para transições de plantão, garantindo continuidade, transferência de contexto e resposta confiável a incidentes entre turnos."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Padrões de Transição de Plantão

Padrões eficazes para transições de plantão, garantindo continuidade, transferência de contexto e resposta confiável a incidentes entre turnos.

## Não use esta habilidade quando

- A tarefa não estiver relacionada a padrões de transição de plantão
- Você precisar de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Utilize esta habilidade quando:

- Transicionar responsabilidades de plantão
- Redigir resumos de passagem de turno
- Documentar investigações em andamento
- Estabelecer procedimentos de rodízio de plantão
- Melhorar a qualidade da passagem de plantão
- Integrar novos engenheiros de plantão

## Conceitos Essenciais

### 1. Componentes da Passagem de Plantão

| Componente | Finalidade |

|-----------|---------|

| **Incidentes Ativos** | Problemas atuais |

| **Investigações em Andamento** | Problemas sendo depurados |

| **Alterações Recentes** | Implantações, configurações |

| **Problemas Conhecidos** | Soluções alternativas implementadas |

| **Próximos Eventos** | Manutenções, lançamentos |

### 2. Cronograma de Transição de Turno

``` Recomendado: 30 minutos de sobreposição entre os turnos

Saída:
├── 15 min: Redigir o documento de transição de turno
└── 15 min: Sincronizar a chamada com a chamada recebida

Recepção:
├── 15 min: Revisar o documento de transição de turno
├── 15 min: Sincronizar a chamada com a chamada de saída
└── 5 min: Verificar a configuração de alertas
```

## Modelos

### Modelo 1: Documento de Transição de Turno

```markdown
# Transição de Plantão: Equipe de Plataforma

**Saída**: @alice (15/01/2024 a 22/01/2024)
**Recepção**: @bob (22/01/2024 a 29/01/2024)
**Horário de transferência**: 22/01/2024 09:00 UTC

---

## 🔴 Incidentes ativos

### Nenhum incidente ativo no momento da transferência.

Nenhum incidente ativo no momento da transferência.

---

## 🟡 Investigações em Andamento

### 1. Tempos limite intermitentes da API (ENG-1234)
**Status**: Investigando
**Iniciado**: 20/01/2024
**Impacto**: ~0,1% das requisições com tempo limite excedido

**Contexto**:
- Os tempos limite estão correlacionados com a janela de backup do banco de dados (02:00-03:00 UTC)
- Suspeita-se que o processo de backup esteja causando contenção de bloqueio
- Adicionado registro adicional no PR #567 (implantado em 21/01)

**Próximos Passos**:
- [ ] Analisar os novos registros após o backup de hoje
- [ ] Considerar a alteração da janela de backup, se confirmado

**Recursos**:
- Painel: [Latência da API](https://grafana/d/api-latency)
- Tópico: #platform-eng (20/01, 14:32)

---

### 2. Crescimento de memória no serviço de autenticação (ENG-1235)
**Status**: Monitoramento
**Iniciado**: 18/01/2024
**Impacto**: Nenhum ainda (proativo)

**Contexto**:
- Uso de memória crescendo ~5% ao dia
- Nenhum vazamento de memória encontrado no perfilamento
- Suspeita-se que o pool de conexões não esteja sendo liberado corretamente

**Próximos passos**:
- [ ] Revisar o dump de heap de 21/01
- [ ] Considerar reinicialização se o uso for > 80%

**Recursos**:
- Painel: [Memória do Serviço de Autenticação](https://grafana/d/auth-memory)
- Documento de análise: [Investigação de Memória](https://docs/eng-1235)

---

## 🟢 Resolvido neste turno

### Interrupção do Serviço de Pagamento (19/01/2024)
- **Duração**: 23 minutos
- **Root **Causa**: Esgotamento de conexões com o banco de dados
- **Resolução**: Reversão para a versão 2.3.4, aumento do tamanho do pool
- **Análise pós-incidente**: [POSTMORTEM-89](https://docs/postmortem-89)
- **Tickets de acompanhamento**: ENG-1230, ENG-1231

---

## 📋 Alterações recentes

### Implantações
| Serviço | Versão | Hora | Observações |

|---------|---------|------|-------|

| api-gateway | v3.2.1 | 21/01 14:00 | Correção de bug na análise de cabeçalho |
| user-service | v2.8.0 | 20/01 10:00 | Novos recursos de perfil |

| auth-service | v4.1.2 | 19/01 16:00 | Patch de segurança |

### Alterações de Configuração
- 21/01: Aumentado o limite de taxa da API de 1000 para 1500 RPS
- 20/01: Atualizado o número máximo de conexões do pool de banco de dados de 50 para 75

### Infraestrutura
- 20/01: Adicionados 2 nós ao cluster Kubernetes
- 19/01: Atualizado o Redis da versão 6.2 para a 7.0

---

## ⚠️ Problemas Conhecidos e Soluções Alternativas

### 1. Carregamento Lento do Painel
**Problema**: Painéis do Grafana lentos nas manhãs de segunda-feira
**Solução Alternativa**: Aguarde 5 minutos após as 08:00 UTC para o aquecimento do cache
**Ticket**: OPS-456 (P3)

### 2. Teste de Integração Instável
**Problema**: `test_payment_flow` falha intermitentemente na CI
**Solução Alternativa**: Execute novamente o job com falha (geralmente é aprovado) (na tentativa)
**Ticket**: ENG-1200 (P2)

---

## 📅 Próximos Eventos

| Data | Evento | Impacto | Contato |

|------|-------|--------|---------|

| 23/01 02:00 | Manutenção do banco de dados | 5 min somente leitura | @dba-team |

| 24/01 14:00 | Lançamento da versão 5.0 | Monitorar atentamente | @release-team |

| 25/01 | Campanha de marketing | Tráfego 2x maior esperado | @platform |


---

## 📞 Lembretes de Escalonamento

| Tipo de Problema | Primeiro Escalonamento | Segundo Escalonamento |

|------------|------------------|-------------------|

| Problemas com pagamentos | @payments-oncall | @payments-manager |

| Problemas com autenticação | @auth-oncall | @security-team |

| Problemas no banco de dados | @dba-team | @infra-manager |

| Desconhecido/grave | @engineering-manager | @vp-engineering |

---

## 🔧 Referência Rápida

### Comandos Comuns
```bash
# Verificar a integridade do serviço
kubectl get pods -A | grep -v Running

# Implantações recentes
kubectl get events --sort-by='.lastTimestamp' | tail -20

# Conexões com o banco de dados
psql -c "SELECT count(*) FROM pg_stat_activity;"

# Limpar cache (somente em caso de emergência)
redis-cli FLUSHDB
```

### Links importantes
- [Runbooks](https://wiki/runbooks)
- [Catálogo de serviços](https://wiki/services)
- [Slack de incidentes](https://slack.com/incidents)
- [PagerDuty](https://pagerduty.com/schedules)

---

## Lista de verificação para transferência de responsabilidade

### Engenheiro de saída
- [x] Documentar incidentes ativos
- [x] Documentar investigações em andamento
- [x] Listar alterações recentes
- [x] Anotar problemas conhecidos
- [x] Adicionar eventos futuros
- [x] Sincronizar com o engenheiro de entrada

### Engenheiro de entrada
- [ ] Ler este documento
- [ ] Participar da chamada de sincronização
- [ ] Verificar se o PagerDuty está roteando para você
- [ ] Verificar se as notificações do Slack estão funcionando
- [ ] Verificar se a VPN/acesso está funcionando
- [ ] Revisar Painéis críticos
```

### Modelo 2: Transferência Rápida (Assíncrona)

```markdown
# Transferência Rápida: @alice → @bob

## Resumo
- Nenhum incidente ativo
- 1 investigação em andamento (timeouts da API, veja ENG-1234)
- Lançamento principal amanhã (24/01) - esteja preparado para problemas

## Lista de Observação
1. Latência da API por volta das 02:00-03:00 UTC (janela de backup)
2. Memória do serviço de autenticação (reinicie se > 80%)

## Recente
- Implantação do api-gateway v3.2.1 ontem (estável)
- Aumento dos limites de taxa para 1500 RPS

## Próximos Eventos
- 23/01 02:00 - Manutenção do banco de dados (5 min somente leitura)
- 24/01 14:00 - Lançamento da v5.0

## Perguntas?
Estarei disponível no Slack até às 17h de hoje.
```

### Modelo 3: Transferência de Incidente (Meio do Incidente)

```markdown
# TRANSFERÊNCIA DE INCIDENTE: Degradação do Serviço de Pagamento

**Início do Incidente**: 22/01/2024 08:15 UTC
**Status Atual**: Mitigando
**Gravidade**: SEV2

---

## Estado Atual
- Taxa de erros: 15% (reduzida de 40%)
- Mitigação em andamento: aumentando o número de pods
- Previsão de resolução: ~30 min

## O que sabemos
1. Causa raiz: Pressão de memória nos pods do serviço de pagamento
2. Acionado por: Pico de tráfego incomum (3x o normal)
3. Contribuinte: Consulta ineficiente no fluxo de finalização da compra

## O que fizemos
- Aumentamos o número de pods do serviço de pagamento de 5 para 15
- Habilitamos a limitação de taxa no endpoint de finalização da compra
- Desabilitamos Funcionalidades não críticas

## O que precisa acontecer
1. Monitorar a taxa de erros - deve atingir <1% em ~15 minutos
2. Se não houver melhora, escalar para @payments-manager
3. Assim que estabilizar, iniciar a investigação da causa raiz

## Pessoas-chave
- Coordenador do incidente: @alice (passando o caso)
- Líder de comunicação: @charlie
- Líder técnico: @bob (chegando)

## Comunicação
- Página de status: Atualizada às 08:45
- Suporte ao cliente: Notificado
- Equipe executiva: Ciente

## Recursos
- Canal do incidente: #inc-20240122-payment
- Painel: [Serviço de Pagamento](https://grafana/d/payments)
- Manual de procedimentos: [Degradação de Pagamento](https://wiki/runbooks/payments)

---

**Chegando para o plantão (@bob) - Por favor, confirme se você:**
- [ ] Entrou #inc-20240122-pagamento
- [ ] Acesso aos painéis
- [ ] Compreender o estado atual
- [ ] Conhecer o caminho de escalonamento
```

## Reunião de Transição de Responsabilidade

### Agenda (15 minutos)

```markdown
## Transição de Responsabilidade: @alice → @bob

1. **Problemas Ativos** (5 min)

- Analisar quaisquer incidentes em andamento

- Discutir o status da investigação

- Transferir contexto e teorias

2. **Alterações Recentes** (3 min)

- Implantações a serem monitoradas

- Alterações de configuração

- Regressões conhecidas

3. **Próximos Eventos** (3 min)

- Janelas de manutenção

- Alterações de tráfego esperadas

- Lançamentos planejados

4. **Perguntas** (4 min)

- Esclarecer qualquer dúvida
- Confirmar acesso e alertas

- Trocar informações de contato
```

## Melhores Práticas para Plantão

### Antes do Seu Turno

```markdown
## Lista de Verificação Pré-Turno

### Verificação de Acesso
- [ ] VPN funcionando
- [ ] Acesso kubectl a todos os clusters
- [ ] Acesso de leitura ao banco de dados
- [ ] Acesso ao agregador de logs (Splunk/Datadog)
- [ ] Aplicativo PagerDuty instalado e conectado

### Configuração de Alertas
- [ ] Agenda do PagerDuty mostra você como principal
- [ ] Notificações no celular ativadas
- [ ] Notificações do Slack para canais de incidentes
- [ ] Alerta de teste recebido e confirmado

### Atualização de Conhecimento
- [ ] Revisar incidentes recentes (últimas 2 semanas)
- [ ] Verificar o changelog do serviço
- [ ] Ler rapidamente os runbooks críticos
- [ ] Conhecer os contatos de escalonamento

### Ambiente Pronto
- [ ] Laptop carregado e acessível
- [ ] Celular carregado
- [ ] Espaço silencioso disponível para chamadas
- [ ] Contato secundário identificado (se estiver viajando)
```

### Durante o seu turno

```markdown
## Rotina diária de plantão

### Manhã (início do dia)
- [ ] Verificar alertas noturnos
- [ ] Revisar painéis em busca de anomalias
- [ ] Verificar se algum ticket P0/P1 foi criado
- [ ] Analisar rapidamente os canais de incidentes para obter contexto

### Ao longo do dia
- [ ] Responder a alertas dentro do SLA
- [ ] Documentar o progresso da investigação
- [ ] Atualizar a equipe sobre problemas significativos
- [ ] Triar mensagens recebidas

### Fim do dia
- [ ] Passar quaisquer problemas ativos para a equipe
- [ ] Atualizar a documentação da investigação
- [ ] Anotar qualquer coisa para o próximo turno
```

### Após o seu turno

```markdown
## Lista de verificação pós-turno

- [ ] Preencher o documento de transferência de responsabilidade
- [ ] Sincronizar com o plantonista que entrará
- [ ] Verificar se o roteamento do PagerDuty foi alterado
- [ ] Fechar/atualizar chamados de investigação
- [ ] Registrar relatórios pós-incidente para quaisquer incidentes
- [ ] Tirar folga se o turno foi estressante
```

## Diretrizes de Escalonamento

### Quando Escalonar

```markdown
## Gatilhos para Escalonamento

### Escalonamento Imediato
- Incidente SEV1 declarado
- Suspeita de violação de dados
- Não foi possível diagnosticar em 30 minutos
- Escalonamento recebido de cliente ou do departamento jurídico

### Considerar Escalonamento
- Problema envolve várias equipes
- Requer conhecimento especializado que você não possui
- Impacto nos negócios excede o limite
- Você não tem certeza sobre os próximos passos

### Como Escalonar
1. Acione o canal de escalonamento apropriado
2. Forneça um breve contexto no Slack
3. Mantenha-se engajado até que o escalonamento seja confirmado
4. Transfira a responsabilidade de forma clara, não desapareça
```

## Melhores Práticas

### Recomendações
- **Documente tudo** - Você agradecerá no futuro
- **Escalone o mais cedo possível** - Melhor Melhor prevenir do que remediar
- **Faça pausas** - A fadiga de alertas é real
- **Mantenha as transições síncronas** - Assíncronas perdem o contexto
- **Teste sua configuração** - Antes dos incidentes, não durante

### O que NÃO fazer
- **Não pule transições** - A perda de contexto causa incidentes
- **Não seja herói** - Acione a escalação quando necessário
- **Não ignore alertas** - Mesmo que pareçam insignificantes
- **Não trabalhe doente** - Troque de turno
- **Não desapareça** - Mantenha-se acessível durante o turno

## Recursos

- [Google SRE - Being On-Call](https://sre.google/sre-book/being-on-call/)
- [PagerDuty On-Call Guide](https://www.pagerduty.com/resources/learn/on-call-management/)
- [Increment On-Call](https://www.pagerduty.com/resources/learn/on-call-management/) Problema](https://increment.com/on-call/)

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.
