--- 
name: automação-de-fluxo-de-trabalho
description: A automação de fluxo de trabalho é a infraestrutura que torna os agentes de IA confiáveis. Sem uma execução robusta, uma falha na rede durante um fluxo de pagamento de 10 etapas significa perda de dinheiro e clientes insatisfeitos. Com ela, os fluxos de trabalho são retomados exatamente de onde pararam.
risk: crítico
source: vibeship-spawner-skills (Apache 2.0)
date_add: 27/02/2026
---

# Automação de Fluxo de Trabalho

A automação de fluxo de trabalho é a infraestrutura que torna os agentes de IA confiáveis.

Sem uma execução robusta, uma falha na rede durante um fluxo de pagamento de 10 etapas
significa perda de dinheiro e clientes insatisfeitos. Com ela, os fluxos de trabalho são retomados
exatamente de onde pararam.

Esta habilidade abrange as plataformas (n8n, Temporal, Inngest) e os padrões
(sequencial, paralelo, orquestrador-trabalhador) que transformam scripts frágeis
em automação de nível de produção.

Principal insight: As plataformas fazem diferentes concessões. O n8n prioriza a acessibilidade, o Temporal a correção e o Inngest a experiência do desenvolvedor.

Escolha com base nas suas necessidades reais, não na propaganda.

## Princípios

- Execução durável é imprescindível para fluxos de trabalho críticos, sejam eles financeiros ou de estado.
- Eventos são a linguagem universal dos gatilhos de fluxo de trabalho.
- Etapas são pontos de verificação – cada uma deve ser repetível independentemente.
- Comece com o básico e adicione complexidade somente quando a confiabilidade exigir.
- Observabilidade não é opcional – você precisa ver onde os fluxos de trabalho falham.
- Fluxos de trabalho e agentes coevoluem – projete para ambos.

## Recursos

- Automação de fluxo de trabalho
- Orquestração de fluxo de trabalho
- Execução durável
- Fluxos de trabalho orientados a eventos
- Step Functions
- Filas de tarefas
- Tarefas em segundo plano
- Tarefas agendadas

## Escopo

- Coordenação multiagente → Orquestração multiagente
- Pipelines de CI/CD → DevOps
- Pipelines de dados → Engenharia de dados
- Design de API → Design de API

## Ferramentas

### Plataformas

- n8n - Quando: Automação com pouco código, prototipagem rápida, usuários não técnicos. Observação: Hospedagem própria, mais de 400 integrações, ótimo para fluxos de trabalho visuais.
- Temporal - Quando: Fluxos de trabalho de missão crítica, transações financeiras, microsserviços. Observação: Garantias de durabilidade mais robustas, curva de aprendizado mais acentuada.
- Inngest - Quando: Serverless orientado a eventos, bases de código TypeScript, fluxos de trabalho de IA. Observação: Melhor experiência para desenvolvedores, funciona com qualquer hospedagem.
- AWS Step Functions - Quando: Stacks nativas da AWS, funções Lambda existentes. Observação: Integração estreita com a AWS, definição de fluxo de trabalho baseada em JSON.
- Azure Durable Functions - Quando: Stacks do Azure, .NET ou TypeScript. Observação: Bom suporte a agentes de IA, checkpoint e replay.

## Padrões

### Padrão de Fluxo de Trabalho Sequencial

As etapas são executadas em ordem, cada saída se torna a próxima entrada.

**Quando usar**: Pipelines de conteúdo, processamento de dados, operações ordenadas.

# FLUXO DE TRABALHO SEQUENCIAL:

"""
Etapa 1 → Etapa 2 → Etapa 3 → Saída
↓ ↓ ↓
(ponto de verificação em cada etapa)
"""

## Exemplo de Ingestão (TypeScript)
"""
import { inngest } from "./client";

export const processOrder = inngest.createFunction(

{ id: "process-order" },

{ event: "order/created" },

async ({ event, step }) => {

// Etapa 1: Validar pedido

const validated = await step.run("validate-order", async () => {

return validateOrder(event.data.order);

});

// Etapa 2: Processar pagamento (durável - sobrevive a falhas)

const payment = await step.run("process-payment", async () => {

return chargeCard(validated.paymentMethod, validated.total);

});

// Etapa 3: Criar remessa

const shipment = await step.run("create-shipment", async () => {

return createShipment(validated.items, validated.address);

});

// Etapa 4: Enviar confirmação

await step.run("send-confirmation", async () => {

return sendEmail(validated.email, { payment, shipment });

});

return { success: true, orderId: event.data.orderId };

}
);

"""

## Exemplo Temporal (TypeScript)
"""
import { proxyActivities } from '@temporalio/workflow';

import type * as activities from './activities';

const { validateOrder, chargeCard, createShipment, sendEmail } =

proxyActivities<typeof activities>({
startToCloseTimeout: '30 segundos',

retry: {
maximumAttempts: 3,

backoffCoefficient: 2,

}
});

export async function processOrderWorkflow(order: Order): Promise<void> {
const validated = await validateOrder(order);

const payment = await chargeCard(validated.paymentMethod, validated.total);

const shipment = await createShipment(validated.items, validated.address);

await sendEmail(validated.email, { payment, shipment });

}
"""

## Padrão n8n
"""
[Webhook: order.created]

↓
[Requisição HTTP: Validar Pedido]

↓
[Requisição HTTP: Processar Pagamento]

↓
[Requisição HTTP: Criar Envio]

↓
[Enviar Email: Confirmação]

Configure cada nó com nova tentativa em caso de falha.
Use o gatilho de erro para tratamento de e-mails não entregues.
"""

### Padrão de Fluxo de Trabalho Paralelo

Etapas independentes executadas simultaneamente, agregando os resultados

**Quando usar**: Múltiplas análises independentes, dados de múltiplas fontes

# FLUXO DE TRABALHO PARALELO:

"""

┌→ Etapa A ─┐
Entrada ──┼→ Etapa B ─┼→ Agregar → Saída

└→ Etapa C ─┘
"""

## Ingestão Exemplo
"""
export const analyzeDocument = inngest.createFunction(

{ id: "analyze-document" },

{ event: "document/uploaded" },

async ({ event, step }) => {

// Executar análises em paralelo

const [security, performance, compliance] = await Promise.all([

step.run("security-analysis", () =>

analyzeForSecurityIssues(event.data.document)

),

step.run("performance-analysis", () =>

analyzeForPerformance(event.data.document)

),

step.run("compliance-analysis", () =>

analyzeForCompliance(event.data.document)

),

]);

// Agregar resultados

const report = await step.run("generate-report", () =>

generateReport({ security, performance, compliance })

);

retornar relatório;

}
);

"""

## AWS Step Functions (Amazon States Language)
"""
{

"Type": "Parallel",

"Branches": [

{
"StartAt": "SecurityAnalysis",

"States": {
"SecurityAnalysis": {

"Type": "Task",

"Resource": "arn:aws:lambda:...:security-analyzer",

"End": true

}

}
},

{
"StartAt": "PerformanceAnalysis",

"States": {

"PerformanceAnalysis": {

"Type": "Task",

"Resource": "arn:aws:lambda:...:performance-analyzer",

"End": true

}

}

}
],

"Next": "ResultadosAgregados"

}
"""

### Padrão Orquestrador-Trabalhador

Um coordenador central distribui o trabalho para trabalhadores especializados

**Quando usar**: Tarefas complexas que exigem diferentes especializações, criação dinâmica de subtarefas

# PADRÃO ORQUESTRADOR-TRABALHADOR:

"""
┌──────────────────────────────────────┐
│ ORQUESTRADOR │
│ - Analisa a tarefa │
│ - Cria subtarefas │
│ - Distribui para os trabalhadores │
│ - Resultados agregados │
└───────────────────────────────────────┘
│
┌───────────┼───────────┐

▼ ▼ ▼
┌───────┐    ┌───────┐      ┌───────┐
│Trabalhador1│ │Trabalhador2│ │Trabalhador3│
│Criar  │    │Modificar     │ │Excluir │
└───────┘    └───────┘      └───────┘
"""

## Temporal Exemplo
""" export async function orchestratorWorkflow(task: ComplexTask) {

// O Orchestrator decide qual trabalho precisa ser feito

const plan = await analyzeTask(task);

// Encaminha para fluxos de trabalho especializados

const results = await Promise.all(
plan.subtasks.map(subtask => {

switch (subtask.type) {

case 'create':

return executeChild(createWorkerWorkflow, { args: [subtask] });

case 'modify':

return executeChild(modifyWorkerWorkflow, { args: [subtask] });

case 'delete':

return executeChild(deleteWorkerWorkflow, { args: [subtask] });

}

})

);

// Agrega os resultados
return aggregateResults(results);
}
"""

## Ingestão com Orquestração de IA
"""
export const aiOrchestrator = inngest.createFunction(

{ id: "ai-orchestrator" },

{ event: "task/complex" },

async ({ event, step }) => {

// A IA decide o que precisa ser feito

const plan = await step.run("create-plan", async () => {

return await llm.chat({

messages: [
{ role: "system", content: "Divida esta tarefa em subtarefas..." },

{ role: "user", content: event.data.task }

]

});

});

// Execute cada subtarefa como uma etapa persistente
const results = [];

for (const subtask of plan.subtasks) {

const result = await step.run(`execute-${subtask.id}`, async () => {

return executeSubtask(subtask);

});

results.push(result);

}

// Síntese final

return await step.run("synthesize", async () => {

return synthesizeResults(results);

});

}
);

"""

### Padrão de Gatilho Orientado a Eventos

Fluxos de trabalho acionados por eventos, não por agendamentos

**Quando usar**: Sistemas reativos, ações do usuário, integrações de webhook

# GATILHOS ORIENTADOS A EVENTOS:

## Ingestão Baseada em Eventos
"""
// Define eventos com tipos TypeScript
type Events = {

"user/signed.up": {

data: { userId: string; email: string };

};

"order/completed": {

data: { orderId: string; total: number };

};

};

// Função acionada por evento
export const onboardUser = inngest.createFunction(

{ id: "onboard-user" },

{ event: "user/signed.up" }, // Acionar este evento

async ({ event, step }) => {

// Aguardar 1 hora e enviar e-mail de boas-vindas

await step.sleep("wait-for-exploration", "1 hour");

await step.run("send-welcome", async () => {

return sendWelcomeEmail(event.data.email);

});

// Aguardar 3 dias para verificação de engajamento

await step.sleep("wait-for-engagement", "3 days");

const engaged = await step.run("check-engagement", async () => {

return checkUserEngagement(event.data.userId);

});

if (!engaged) {

await step.run("send-nudge", async () => {
return sendNudgeEmail(event.data.email);

});

}
}
);

// Enviar eventos de qualquer lugar
await inngest.send({

name: "user/signed.up",

data: { userId: "123", email: "user@example.com" }
});

"""

## Gatilho Webhook n8n
"""
[Webhook: POST /api/webhooks/order]

↓
[Switch: event.type]

↓ order.created
[Processar Subfluxo de Trabalho de Novo Pedido]

↓ order.cancelled
[Lidar com Subfluxo de Trabalho de Cancelamento]
"""

### Padrão de Repetição e Recuperação

Repetição automática com backoff, tratamento de mensagens não entregues

**Quando usar**: Qualquer fluxo de trabalho com dependências externas

# RETIRADA E RECUPERAÇÃO:

## Configuração Temporal de Repetição
"""
const activities = proxyActivities<typeof activitiesType>({
startToCloseTimeout: '30 segundos',

retry: {
initialInterval: '1 segundo',

backoffCoefficient: 2,

maximumInterval: '1 minuto',

maximumAttempts: 5,

nonRetryableErrorTypes: [
'ValidationError', // Não tentar novamente em caso de falha na validação

'InsufficientFunds', // Não tentar novamente em caso de falha no pagamento

]
}
});

"""

## Configuração de Repetição do Inngest
"""
export const processPayment = inngest.createFunction(

{
id: "process-payment",

retries: 5, // Tentar até 5 vezes

},

{ event: "payment/initiated" },

async ({ event, step, attempt }) => {

// attempt é a contagem de tentativas indexada a partir de 0

const result = await step.run("charge-card", async () => {

try {
return await stripe.charges.create({...});

} catch (error) {

if (error.code === 'card_declined') {

// Não tente novamente em caso de recusa do cartão

throw new NonRetriableError("Cartão recusado");

}

throw error; // Tente novamente em caso de outros erros

}
});

return result;

}
);

""

## Tratamento de Mensagens Não Entregues
"""
// n8n: Usar o nó de Gatilho de Erro
[Gatilho de Erro]

↓
[Registrar no Banco de Dados de Erros]

↓
[Enviar Alerta para o Slack]

↓
[Criar Ticket no Jira]

// Inngest: Tratar em onFailure
export const myFunction = inngest.createFunction(

{
id: "my-function",

onFailure: async ({ error, event, step }) => {

await step.run("alert-team", async () => {

await slack.postMessage({

channel: "#errors",

text: `Função falhou: ${error.message}`

});

});

}

},

{ event: "..." },

async ({ step }) => { ... }
);
"""

### Padrão de Fluxo de Trabalho Agendado

Gatilhos baseados em tempo para tarefas recorrentes

**Quando usar**: Relatórios diários, sincronização periódica, processamento em lote

# FLUXOS DE TRABALHO AGENDADOS:

## Inngest Cron
"""
export const dailyReport = inngest.createFunction(

{ id: "daily-report" },

{ cron: "0 9 * * *" }, // Todos os dias às 9h

async ({ step }) => {

const data = await step.run("gather-metrics", async () => {

return gatherDailyMetrics();

});

await step.run("generate-report", async () => {

return generateAndSendReport(data);

});

}
);

export const syncInventory = inngest.createFunction(

{ id: "sync-inventory" },

{ cron: "*/15 * * * *" }, // A cada 15 minutos

async ({ step }) => {

await step.run("sync", async () => {

return syncWithSupplier();

});

}
);

""

## Fluxo de Trabalho Temporal Cron
"""
// Agendar fluxo de trabalho para ser executado no cron
const handle = await client.workflow.start(dailyReportWorkflow, {
taskQueue: 'reports',

workflowId: 'daily-report',

cronSchedule: '0 9 * * *', // 9h diariamente
});

""

## Gatilho de Agendamento n8n
"""
[Gatilho de Agendamento: Todos os dias às 9h]

↓
[Requisição HTTP: Obter Métricas]

↓
[Nó de Código: Gerar Relatório]

↓
[Enviar Email: [Relatório]

"""

## Problemas Críticos

### Etapas Não Idempotentes em Fluxos de Trabalho Duráveis

Gravidade: CRÍTICA

Situação: Criação de etapas de fluxo de trabalho que modificam o estado externo

Sintomas:
Cliente cobrado duas vezes. E-mail enviado três vezes. Registro de banco de dados
criado várias vezes. As novas tentativas do fluxo de trabalho causam efeitos colaterais duplicados.

Por que isso causa problemas:
A execução durável reproduz os fluxos de trabalho desde o início na reinicialização.
Se a etapa 3 falhar e o fluxo de trabalho for retomado, as etapas 1 e 2 serão executadas novamente.
Sem chaves de idempotência, os serviços externos não sabem que se tratam de novas tentativas.

Correção recomendada:

# SEMPRE use chaves de idempotência para chamadas externas:

## Exemplo com Stripe:
await stripe.paymentIntents.create({

amount: 1000,

currency: 'usd',

idempotency_key: `order-${orderId}-payment` # Crítico!
});

## Exemplo com e-mail:
await step.run("send-confirmation", async () => {

const alreadySent = await checkEmailSent(orderId);

if (alreadySent) return { skipped: true };

return sendEmail(customer, orderId);
});

## Exemplo com banco de dados:
await db.query(`

INSERT INTO orders (id, ...) VALUES ($1, ...)

ON CONFLICT (id) DO NOTHING
`, [orderId]);

# Gerar chave de idempotência a partir de entradas estáveis, não de valores aleatórios

### Fluxo de trabalho executado por horas/dias sem pontos de verificação

Gravidade: ALTA

Situação: Fluxos de trabalho de longa duração com etapas pouco frequentes

Sintomas:
Consumo de memória crescente. Tempo limite de processos. Perda de progresso após
falhas. Erros de "Fluxo de trabalho excedeu a duração máxima".

Por que isso causa problemas:
Fluxos de trabalho mantêm o estado na memória até que um ponto de verificação seja criado. Um fluxo de trabalho que
é executado por 24 horas com uma etapa por hora acumula estado por 24 horas.

Processos têm limites de memória. Funções têm limites de tempo de execução.

Correção recomendada:

# Divida fluxos de trabalho longos em etapas com pontos de verificação:

## INCORRETO - uma única etapa longa:
await step.run("process-all", async () => {

for (const item of thousandItems) {

await processItem(item); // Horas de trabalho, um ponto de verificação
}
});

## CORRETO - várias etapas pequenas:
for (const item of thousandItems) {

await step.run(`process-${item.id}`, async () => {

return processItem(item); // Ponto de verificação após cada etapa
});

}

## Para esperas muito longas, use sleep:
await step.sleep("wait-for-trial", "14 days");
// Não consome recursos durante a espera

## Considere fluxos de trabalho filhos para processos longos:
await step.invoke("process-batch", {

function: batchProcessor,

data: { items: batch }
});

### Atividades sem configuração de tempo limite

Gravidade: ALTA

Situação: Chamando serviços externos a partir de atividades de fluxo de trabalho

Sintomas:
Fluxos de trabalho travam indefinidamente. Pool de workers esgotado. Fluxos de trabalho inativos
que nunca são concluídos ou falham. Intervenção manual necessária para encerrar fluxos de trabalho travados.

Por que isso causa problemas:
APIs externas podem travar indefinidamente. Sem um tempo limite, seu fluxo de trabalho espera indefinidamente. Ao contrário dos clientes HTTP, as atividades de fluxo de trabalho não possuem tempos limite padrão na maioria das plataformas.

Correção recomendada:

# SEMPRE defina tempos limite para as atividades:

## Temporal:
const activities = proxyActivities<typeof activitiesType>({
startToCloseTimeout: '30 segundos', # Obrigatório!

scheduleToCloseTimeout: '5 minutos',

heartbeatTimeout: '10 segundos', # Para atividades longas
retry: {
maximumAttempts: 3,
initialInterval: '1 segundo',

}
});

## Ingestão:
await step.run("call-api", { timeout: "30s" }, async () => {

return fetch(url, { signal: AbortSignal.timeout(25000) });
});

## AWS Step Functions:
{

"Type": "Task",

"TimeoutSeconds": 30,

"HeartbeatSeconds": 10,

"Resource": "arn:aws:lambda:..."
}

# Regra: Tempo limite da atividade < Tempo limite do fluxo de trabalho

### Efeitos colaterais fora dos limites da etapa/atividade

Gravidade: CRÍTICA

Situação: Escrita de código que é executado durante a reprodução do fluxo de trabalho

Sintomas:
Falhas aleatórias na reprodução. Erros de "Fluxo de trabalho corrompido". Comportamento diferente na reprodução em comparação com a execução inicial.
Erros de não determinismo.

Por que isso causa problemas:
O código do fluxo de trabalho é executado em TODAS as reproduções. Se você gerar um ID aleatório no código do fluxo de trabalho,
você obterá um ID diferente a cada reprodução. Se você ler a
hora atual, obterá uma hora diferente. Isso quebra o determinismo.

Correção recomendada:

# INCORRETO - efeitos colaterais no código do fluxo de trabalho:
export async function orderWorkflow(order) {

const orderId = uuid(); // Diferente a cada repetição!

const now = new Date(); // Diferente a cada repetição!

await activities.process(orderId, now);

}

# CORRETO - efeitos colaterais nas atividades:
export async function orderWorkflow(order) {
const orderId = await activities.generateOrderId(); # Registrado

const now = await activities.getCurrentTime(); # Registrado

await activities.process(orderId, now);

}

# Também CORRETO - workflow.now() e sideEffect do Temporal:
import { sideEffect } from '@temporalio/workflow';

const orderId = await sideEffect(() => uuid());

const now = workflow.now(); # Tempo determinístico seguro para repetição

# Efeitos colaterais seguros no código do fluxo de trabalho:
# - Leitura de argumentos de função
# - Cálculos simples (sem aleatoriedade)
# - Registro de logs (geralmente)

### Configuração de repetição sem backoff exponencial

Gravidade: MÉDIA

Situação: Configuração do comportamento de repetição para etapas com falha

Sintomas:
Sobrecarga de serviços com falhas. Limitação de taxa. Falhas em cascata.

Tempestades de repetição causando interrupções. Bloqueio por APIs externas.

Por que isso causa problemas:
Quando um serviço está com dificuldades, as repetições imediatas pioram a situação.

100 fluxos de trabalho com repetição instantânea = 100 solicitações atingindo um serviço
que já está com falhas. O backoff dá ao serviço tempo para se recuperar.

Correção recomendada:

# SEMPRE use backoff exponencial:
## Temporal:
const activities = proxyActivities({

retry: {
initialInterval: '1 segundo',

backoffCoefficient: 2, # 1s, 2s, 4s, 8s, 16s...

maximumInterval: '1 minuto', # Limita o backoff
maximumAttempts: 5,

}
});

## Ingestão (backoff integrado):
{

id: "my-function",

retries: 5, # Usa backoff exponencial por padrão
}

## Backoff manual:
const backoff = (attempt) => {

const base = 1000;

const max = 60000;

const delay = Math.min(base * Math.pow(2, attempt), max);

const jitter = delay * 0.1 * Math.random();

return delay + jitter;

};

# Adicionando jitter para evitar sobrecarga de dados

### Armazenando Grandes Volumes de Dados no Estado do Fluxo de Trabalho

Gravidade: ALTA

Situação: Passagem de grandes volumes de dados entre etapas do fluxo de trabalho

Sintomas:
Execução lenta do fluxo de trabalho. Erros de memória. Erros de "volume de dados muito grande".

Custos de armazenamento elevados. Reproduções lentas.

Por que isso causa problemas:
O estado do fluxo de trabalho é persistido e reproduzido. Um volume de dados de 10 MB é armazenado,
serializado e desserializado em cada etapa. Isso adiciona latência e
custo. Algumas plataformas têm limites rígidos (por exemplo, Step Functions 256 KB).

Correção recomendada:

# INCORRETO - grandes volumes de dados no fluxo de trabalho:
await step.run("fetch-data", async () => {

const largeDataset = await fetchAllRecords(); // 100 MB!

return largeDataset; // Armazenado no estado do fluxo de trabalho
});

# CORRETO - armazenar a referência, não os dados:
await step.run("fetch-data", async () => {

const largeDataset = await fetchAllRecords();

const s3Key = await uploadToS3(largeDataset);

return { s3Key }; // Apenas a referência
});

const processed = await step.run("process-data", async () => {
const data = await downloadFromS3(fetchResult.s3Key);

return processData(data);
});

# Para Step Functions, use o S3 para payloads grandes:
{

"Type": "Task",

"Resource": "arn:aws:states:::s3:putObject",

"Parameters": {

"Bucket": "my-bucket",

"Key.$": "$.outputKey",

"Body.$": "$.largeData"

}
}

### Ausência de Fila de Mensagens Não Entregues ou Tratamento de Falhas

Gravidade: ALTA

Situação: Fluxos de trabalho que esgotam todas as tentativas

Sintomas:
Fluxos de trabalho com falha desaparecem silenciosamente. Nenhum alerta quando algo dá errado.

Problemas do cliente descobertos dias depois. Recuperação manual impossível.

Por que isso causa problemas:
Mesmo com novas tentativas, alguns fluxos de trabalho falharão permanentemente. Sem o tratamento de mensagens não entregues, você não sabe que eles falharam. O cliente espera indefinidamente, você não fica sabendo e não há dados para depurar.

Correção recomendada:

# Manipulador onFailure do Inngest:
export const myFunction = inngest.createFunction(

{

id: "process-order",

onFailure: async ({ error, event, step }) => {

// Registrar no sistema de rastreamento de erros

await step.run("log-error", () =>

sentry.captureException(error, { extra: { event } })

);

// Alertar a equipe

await step.run("alert", () =>

slack.postMessage({

channel: "#alerts",

text: `Pedido ${event.data.orderId} falhou: ${error.message}`

})

);

// Enfileirar para revisão manual

await step.run("queue-review", () =>

db.insert(failedOrders, { orderId, error, event })

);

}
},
{ evento: "pedido/criado" },

async ({ evento, passo }) => { ... }
);

# Gatilho de Erro n8n:
[Gatilho de Erro] → [Registrar no Banco de Dados] → [Alerta no Slack] → [Criar Ticket]

# Temporal: Use workflow.failed ou sinais de fluxo de trabalho

### Fluxo de Trabalho n8n Sem Gatilho de Erro

Gravidade: MÉDIA

Situação: Criação de fluxos de trabalho n8n em produção

Sintomas:
O fluxo de trabalho falha silenciosamente. Os erros são visíveis apenas nos logs de execução.

Sem alertas, sem recuperação, sem visibilidade até que alguém perceba.

Por que isso causa problemas:
O n8n não notifica falhas por padrão. Sem um nó de Gatilho de Erro conectado ao sistema de alertas, as falhas são visíveis apenas na interface do usuário.

Falhas em produção passam despercebidas.

Correção recomendada:

# Todo fluxo de trabalho n8n em produção precisa de:

1. Nó de Gatilho de Erro

- Captura qualquer falha de nó no fluxo de trabalho

- Fornece detalhes e contexto do erro

2. Tratamento de erros conectado:

[Gatilho de Erro]

↓

[Configurar: Extrair Detalhes do Erro]

↓

[HTTP: Registrar no Serviço de Erros]

↓

[Slack/E-mail: Alertar a Equipe]

3. Considerar o padrão de mensagens não entregues:

[Gatilho de Erro]

↓

[Redis/Postgres: Armazenar Tarefa com Falha]

↓

[Fluxo de Trabalho de Recuperação Separado]

# Use também:
- Tentar novamente em caso de falhas de nó (integrado)
- Configurações de tempo limite do nó
- Tempo limite do fluxo de trabalho

### Atividades Temporais de Longa Duração Sem Pulsação

Gravidade: MÉDIA

Situação: Atividades que são executadas por mais de alguns segundos

Sintomas:
Tempo limite da atividade expira mesmo quando o trabalho está em andamento Em andamento. Perda de trabalho quando
os workers reiniciam. Não é possível cancelar atividades de longa duração.

Por que isso causa problemas:
O Temporal detecta atividades travadas por meio de heartbeats. Sem o heartbeat,
o Temporal não consegue determinar se a atividade está em execução ou travada. Atividades longas
parecem travadas, podem expirar e não podem ser canceladas corretamente.

Correção recomendada:

# Para qualquer atividade com duração superior a 10 segundos, adicione o heartbeat:

import { heartbeat, activityInfo } from '@temporalio/activity';

export async function processLargeFile(fileUrl: string): Promise<void> {

const chunks = await downloadChunks(fileUrl);

for (let i = 0; i < chunks.length; i++) {

// Verifica se houve cancelamento

const { cancelled } = activityInfo();

if (cancelled) {

throw new CancelledFailure('Atividade cancelada');
}

await processChunk(chunks[i]);

// Reportar progresso

heartbeat({ progress: (i + 1) / chunks.length });

}
}

# Configurar tempo limite de heartbeat:
const activities = proxyActivities({

startToCloseTimeout: '10 minutos',

heartbeatTimeout: '30 segundos', # Deve enviar um heartbeat a cada 30 segundos
});

# Se não houver heartbeat por 30 segundos, a atividade é considerada travada

## Verificações de Validação

### Chamadas Externas Sem Chave de Idempotência

Severidade: ERRO

As chamadas Stripe/payment devem usar chaves de idempotência

Mensagem: Chamada de pagamento sem chave de idempotência. Adicione uma chave de idempotência para evitar cobranças duplicadas em novas tentativas.

### Envio de e-mail sem deduplicação

Gravidade: AVISO

O envio de e-mails em fluxos de trabalho deve verificar se já foram enviados.

Mensagem: E-mail enviado no fluxo de trabalho sem verificação de deduplicação. Novas tentativas podem enviar e-mails duplicados.

### Atividades Temporais sem Tempo Limite

Gravidade: ERRO

Todas as atividades temporais precisam de configuração de tempo limite.

Mensagem: Atividades proxy sem tempo limite. Adicione `startToCloseTimeout` para evitar travamentos indefinidos.

### Etapas de Ingestão Chamando APIs Externas sem Tempo Limite

Gravidade: AVISO

As chamadas de API externa devem ter tempos limite.

Mensagem: Chamada de API externa na etapa sem tempo limite. Adicione um tempo limite para evitar travamentos do fluxo de trabalho.

### Valores Aleatórios no Código do Fluxo de Trabalho

Gravidade: ERRO

Valores aleatórios quebram o determinismo na reprodução.

Mensagem: Valor aleatório no código do fluxo de trabalho. Mova para a atividade/etapa ou use um efeito colateral.

### Date.now() no código do fluxo de trabalho

Gravidade: ERRO

A hora atual quebra o determinismo na reprodução.

Mensagem: Hora atual no código do fluxo de trabalho. Use workflow.now() ou mova para a atividade/etapa.

### Função de ingestão sem tratamento de falha

Gravidade: AVISO

As funções de produção devem ter tratamento de falhas.

Mensagem: Função de ingestão sem tratamento de falha. Adicione tratamento de falhas para garantir a confiabilidade em produção.

### Etapa sem tratamento de erros

Gravidade: AVISO

As etapas devem tratar os erros de forma adequada.

Mensagem: Etapa sem bloco try/catch. Considere tratar casos de erro específicos.

### Dados potencialmente grandes retornados da etapa

Gravidade: INFORMAÇÃO

Dados grandes no estado do fluxo de trabalho tornam a execução mais lenta.

Mensagem: Dados potencialmente grandes retornados da etapa. Considere armazená-los no S3/Banco de Dados e retornar uma referência.

### Tentativa de Reinicialização Sem Configuração de Backoff

Gravidade: AVISO

As tentativas de reinicialização devem usar backoff exponencial.

Mensagem: Tentativa de reinicialização configurada sem backoff. Adicione backoffCoefficient e initialInterval.

## Colaboração

### Gatilhos de Delegação

- O usuário precisa de coordenação multiagente -> orquestração multiagente (O fluxo de trabalho fornece a infraestrutura, a orquestração fornece os padrões)
- O usuário precisa de criação de ferramentas para fluxos de trabalho -> criador de ferramentas para agentes (Ferramentas que os fluxos de trabalho podem invocar)
- O usuário precisa de integração com Zapier/Make -> padrões Zapier/Make (Plataformas de automação sem código)
- O usuário precisa de automação de navegador no fluxo de trabalho -> automação de navegador (Atividades de Playwright/Puppeteer)
- O usuário precisa de controle de computador no fluxo de trabalho -> agentes de uso de computador (Atividades de automação de desktop)
- O usuário precisa de integração com LLM no fluxo de trabalho -> arquiteto LLM (Etapas de fluxo de trabalho com IA)

## Habilidades Relacionadas

Funciona bem com: `orquestração multiagente`, `criador de ferramentas para agentes`, `backend`, `devops`

## Quando Usar

- O usuário menciona ou implica: fluxo de trabalho
- O usuário menciona ou implica: automação
- O usuário menciona ou implica: n8n
- O usuário menciona ou implica: temporal
- O usuário menciona ou implica: ingestão
- O usuário menciona ou implica: função passo a passo
- O usuário menciona ou implica: tarefa em segundo plano
- O usuário menciona ou implica: execução durável
- O usuário menciona ou implica: orientado a eventos
- O usuário menciona ou implica: tarefa agendada
- O usuário menciona ou implica: fila de tarefas
- O usuário menciona ou implica: cron
- O usuário menciona ou implica: gatilho
-