--- 
name: memória-de-conversação
description: Sistemas de memória persistente para conversas LLM, incluindo memória de curto prazo, de longo prazo e baseada em entidades
risk: desconhecido
source: vibeship-spawner-skills (Apache 2.0)
date_add: 27/02/2026
---

# Memória de Conversação

Sistemas de memória persistente para conversas LLM, incluindo memória de curto prazo, de longo prazo e baseada em entidades

## Recursos

- memória de curto prazo
- memória de longo prazo
- memória de entidades
- persistência de memória
- recuperação de memória
- consolidação de memória

## Pré-requisitos

- Conhecimento: Padrões de conversação LLM, Noções básicas de banco de dados, Armazenamento chave-valor
- Habilidades_recomendadas: gerenciamento de janelas de contexto, implementação de rag

## Escopo

- Não abrange: Construção de grafos de conhecimento, Semântica Implementação de busca, Administração de banco de dados
- Limites: O foco está nos padrões de memória para LLMs, abrangendo estratégias de armazenamento e recuperação

## Ecossistema

### Ferramentas principais

- Mem0 - Camada de memória para aplicações de IA
- Memória LangChain - Utilitários de memória no LangChain
- Redis - Armazenamento de dados em memória para a sessão

## Padrões

### Sistema de memória em camadas

Diferentes camadas de memória para diferentes finalidades

**Quando usar**: Para construir qualquer IA conversacional
interface MemorySystem {
    // Buffer: Current conversation (in context)
    buffer: ConversationBuffer;

    // Short-term: Recent interactions (session)
    shortTerm: ShortTermMemory;

    // Long-term: Persistent across sessions
    longTerm: LongTermMemory;

    // Entity: Facts about people, places, things
    entity: EntityMemory;
}

class TieredMemory implements MemorySystem {
    async addMessage(message: Message): Promise<void> {
        // Always add to buffer
        this.buffer.add(message);

        // Extract entities
        const entities = await extractEntities(message);
        for (const entity of entities) {
            await this.entity.upsert(entity);
        }

        // Check for memorable content
        if (await isMemoryWorthy(message)) {
            await this.shortTerm.add({
                content: message.content,
                timestamp: Date.now(),
                importance: await scoreImportance(message)
            });
        }
    }

    async consolidate(): Promise<void> {
        // Move important short-term to long-term
        const memories = await this.shortTerm.getOld(24 * 60 * 60 * 1000);
        for (const memory of memories) {
            if (memory.importance > 0.7 || memory.referenced > 2) {
                await this.longTerm.add(memory);
            }
            await this.shortTerm.remove(memory.id);
        }
    }

    async buildContext(query: string): Promise<string> {
        const parts: string[] = [];

        // Relevant long-term memories
        const longTermRelevant = await this.longTerm.search(query, 3);
        if (longTermRelevant.length) {
            parts.push('## Relevant Memories\n' +
                longTermRelevant.map(m => `- ${m.content}`).join('\n'));
        }

        // Relevant entities
        const entities = await this.entity.getRelevant(query);
        if (entities.length) {
            parts.push('## Known Entities\n' +
                entities.map(e => `- ${e.name}: ${e.facts.join(', ')}`).join('\n'));
        }

        // Recent conversation
        const recent = this.buffer.getRecent(10);
        parts.push('## Recent Conversation\n' + formatMessages(recent));

        return parts.join('\n\n');
    }
}

### Memória de Entidades

Armazena e atualiza informações sobre entidades

**Quando usar**: Necessidade de lembrar detalhes sobre pessoas, lugares e coisas

interface Entity {

id: string;

name: string;

type: 'person' | 'place' | 'thing' | 'concept';

facts: Fact[];

lastMentioned: number;

mentionCount: number;

}

interface Fact {
content: string;

confidence: number;

source: string; // De qual mensagem isso veio

timestamp: number;

}

class EntityMemory {

async extractAndStore(message: Message): Promise<void> {

// Use LLM para extrair entidades e fatos

const extraction = await llm.complete(`

Extrai entidades e fatos desta mensagem.

Retorna JSON: { "entities": [

{ "name": "...", "type": "...", "facts": ["..."] }

]}

Mensagem: "${message.content}"

`);

const { entities } = JSON.parse(extraction);

for (const entity of entities) {

await this.upsert(entity, message.id);

}

}

async upsert(entity: ExtractedEntity, sourceId: string): Promise<void> {

const existing = await this.store.get(entity.name.toLowerCase());

if (existing) {

// Mesclar fatos, evitando duplicados

for (const fact of entity.facts) {

if (!this.hasSimilarFact(existing.facts, fact)) {
existing.facts.push({

content: fact,

confidence: 0.9,

source: sourceId,

timestamp: Date.now()
});

}

existing.lastMentioned = Date.now();

existing.mentionCount++;

await this.store.set(existing.id, existing);

} else {

// Criar nova entidade

await this.store.set(entity.name.toLowerCase(), {

id: generateId(),

name: entity.name,

type: entity.type,

facts: entity.facts.map(f => ({

content: f,

confidence: 0.9,

source: sourceId,

timestamp: Date.now()
})),

lastMentioned: Date.now(),

mentionCount: 1

});

}
}
}

### Solicitação com reconhecimento de memória

Incluir memórias relevantes nas solicitações

**Quando usar**: Fazendo chamadas LLM com contexto de memória

async function promptWithMemory(
query: string,

memory: MemorySystem,

systemPrompt: string
): Promise<string> {

// Recuperar memórias relevantes

const relevantMemories = await memory.longTerm.search(query, 5);

const entities = await memory.entity.getRelevant(query);

const recentContext = memory.buffer.getRecent(5);

// Construir solicitação com reconhecimento de memória

const prompt = `
${systemPrompt}

## Contexto do usuário
${entities.length ? `Informações conhecidas sobre o usuário:\n${entities.map(e =>
`- ${e.name}: ${e.facts.map(f => f.content).join('; ')}`
).join('\n')}` : ''}

${relevantMemories.length ? `Interações relevantes anteriores:\n${relevantMemories.map(m =>

`- [${formatDate(m.timestamp)}] ${m.content}`

).join('\n')}` : ''}

## Conversa recente
${formatMessages(recentContext)}

## Consulta atual
${query}

`.trim();

const response = await llm.complete(prompt);

// Extrai quaisquer novas memórias da resposta

await memory.addMessage({ role: 'assistant', content: response });

return response;

}

## Problemas Críticos

### Armazenamento em memória cresce indefinidamente, sistema fica lento

Gravidade: ALTA

Situação: O sistema fica mais lento com o tempo, os custos aumentam

Sintomas:
- Recuperação lenta da memória
- Altos custos de armazenamento
- Latência crescente ao longo do tempo

Por que isso causa problemas:
Cada mensagem é armazenada na memória.

Sem limpeza ou consolidação.

Recuperação de milhões de itens.

Correção recomendada:

// Implementar gerenciamento do ciclo de vida da memória

class ManagedMemory {

// Limites

private readonly SHORT_TERM_MAX = 100;

private readonly LONG_TERM_MAX = 10000;

private readonly CONSOLIDATION_INTERVAL = 24 * 60 * 60 * 1000;

async add(memory: Memory): Promise<void> {

// Atribui uma pontuação de importância antes de armazenar

const score = await this.scoreImportance(memory);

if (score < 0.3) return; // Não armazena itens de baixa importância

memory.importance = score;

await this.shortTerm.add(memory);

// Verifica os limites

await this.enforceShortTermLimit();

}

async enforceShortTermLimit(): Promise<void> {

const count = await this.shortTerm.count();

if (count > this.SHORT_TERM_MAX) {

// Consolida: move itens importantes para o longo prazo e exclui o restante

const memories = await this.shortTerm.getAll();

memories.sort((a, b) => b.importance - a.importance);

const toKeep = memories.slice(0, this.SHORT_TERM_MAX * 0.7);
const toConsolidate = memories.slice(this.SHORT_TERM_MAX * 0.7);

for (const m of toConsolidate) {
if (m.importance > 0.7) {

await this.longTerm.add(m);

}

await this.shortTerm.remove(m.id);

}

}

async scoreImportance(memory: Memory): Promise<number> {

const factors = {
hasUserPreference: /prefer|like|don't like|hate|love/i.test(memory.content) ? 0.3 : 0,

hasDecision: /decided|chose|will do|won't do/i.test(memory.content) ? 0.3 : 0,
hasFactAboutUser: /my|Eu sou|Eu tenho|Eu trabalho/i.test(memory.content) ? 0.2 : 0,

length: memory.content.length > 100 ? 0.1 : 0,

userMessage: memory.role === 'user' ? 0.1 : 0,
};

return Object.values(factors).reduce((a, b) => a + b, 0);

}
}

### Memórias recuperadas irrelevantes para a consulta atual

Gravidade: ALTA

Situação: Memórias incluídas no contexto, mas não úteis

Sintomas:
- Memórias no contexto parecem aleatórias
- O usuário pergunta sobre coisas que já estão na memória
- Confusão devido ao contexto irrelevante

Motivo da falha:

Correspondência simples de palavras-chave.

Sem pontuação de relevância.

Inclusão de todas as memórias recuperadas.

Correção recomendada:

// Recuperação inteligente de memória

async function retrieveRelevant(

query: string,

memorys: MemoryStore,

maxResults: number = 5
): Promise<Memory[]> {

// 1. Busca semântica

const candidates = await memories.semanticSearch(query, maxResults * 3);

// 2. Avaliar a relevância com o contexto

const scored = await Promise.all(candidates.map(async (m) => {

const relevanceScore = await llm.complete(`

Avalie de 0 a 1 a relevância desta memória para a consulta.

Consulta: "${query}"

Memória: "${m.content}"

Retorne apenas o número.

`);

return { ...m, relevance: parseFloat(relevanceScore) };

}));

// 3. Filtrar baixa relevância

const relevant = scored.filter(m => m.relevance > 0.5);

// 4. Ordenar e limitar

return relevant

.sort((a, b) => b.relevance - a.relevance)

.slice(0, maxResults);
}

### Memórias de um usuário acessíveis a outro

Gravidade: CRÍTICA

Situação: O usuário vê informações das sessões de outro usuário

Sintomas:
- O usuário vê informações de outro usuário
- Reclamações de privacidade
- Violações de conformidade

Motivo da falha:

Ausência de isolamento de usuário no armazenamento de memória.

Espaço de nomes de memória compartilhado.

Recuperação entre usuários.

Correção recomendada:

// Isolamento estrito de usuário na memória

class IsolatedMemory {

private getKey(userId: string, memoryId: string): string {

// Namespace de todas as chaves por usuário

return `user:${userId}:memory:${memoryId}`;

}

async add(userId: string, memory: Memory): Promise<void> {

// Valida se o userId está autenticado

if (!isValidUserId(userId)) {

throw new Error('ID de usuário inválido');

}

const key = this.getKey(userId, memory.id);

memory.userId = userId; // Marca com o usuário

await this.store.set(key, memory);

}

async search(userId: string, query: string): Promise<Memory[]> {

// CRÍTICO: Filtra por usuário na consulta

return await this.store.search({
query,

filter: { userId: userId }, // Filtro obrigatório

limit: 10
});

}

async delete(userId: string, memoryId: string): Promise<void> {

const memory = await this.get(userId, memoryId);

// Verificar a propriedade antes de excluir

if (memory.userId !== userId) {

throw new Error('Acesso negado');

}
await this.store.delete(this.getKey(userId, memoryId));

}

// Exportação de dados do usuário (conformidade com o GDPR)

async exportUserData(userId: string): Promise<Memory[]> {
return await this.store.getAll({ userId });

}

// Exclusão de dados do usuário (conformidade com o GDPR)

async deleteUserData(userId: string): Promise<void> {
const memories = await this.exportUserData(userId);
for (const m of memories) {
await this.store.delete(this.getKey(userId, m.id));

}
}
}

## Verificações de Validação

### Ausência de Isolamento de Usuário na Memória

Gravidade: CRÍTICA

Mensagem: Operações de memória sem isolamento de usuário. Vulnerabilidade de privacidade.

Ação corretiva: Adicionar userId a todas as operações de memória, filtrar por usuário na recuperação.

### Ausência de Filtragem por Importância

Gravidade: AVISO

Mensagem: Armazenamento de memórias sem filtragem por importância. Pode causar explosão de memória.

Ação corretiva: Atribuir pontuação de importância antes de armazenar, filtrar conteúdo de baixa importância.

### Armazenamento de Memória sem Recuperação

Gravidade: AVISO

Mensagem: Armazenamento de memórias sem lógica de recuperação. As memórias não serão utilizadas.

Ação corretiva: Implementar recuperação de memória e incluir nos prompts.

### Ausência de Limpeza de Memória

Gravidade: INFORMAÇÃO

Mensagem: Ausência de mecanismo de limpeza de memória. O armazenamento crescerá indefinidamente.

Ação corretiva: Implementar consolidação e limpeza com base na idade/importância

## Colaboração

### Gatilhos de Delegação

- janela de contexto|token -> gerenciamento de janela de contexto (Necessita de otimização de contexto)
- rag|recuperação|vetor -> implementação de rag (Necessita de sistema de recuperação)
- cache|caching -> cache de prompts (Necessita de estratégias de cache)

### Sistema de Memória Completo

Habilidades: memória de conversa, gerenciamento de janela de contexto, implementação de rag

Fluxo de trabalho:

```
1. Projetar camadas de memória
2. Implementar armazenamento e recuperação
3. Integrar com o gerenciamento de contexto
4. Adicionar consolidação e limpeza
```

## Habilidades Relacionadas

Funciona bem com: `gerenciamento de janela de contexto`, `implementação de rag`, `caching de prompts`, `llm-npc-dialogue`

## Quando usar

- Usuário Menciona ou implica: memória de conversa
- O usuário menciona ou implica: lembrar
- O usuário menciona ou implica: persistência da memória
- O usuário menciona ou implica: memória de longo prazo
- O usuário menciona ou implica: histórico do chat

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.

