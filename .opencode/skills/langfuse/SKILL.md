--- 
name: langfuse
description: Especialista em Langfuse - a plataforma de observabilidade LLM de código aberto. Abrange rastreamento, gerenciamento de prompts, avaliação, conjuntos de dados e integração com LangChain, LlamaIndex e OpenAI. Essencial para depuração, monitoramento e aprimoramento de aplicações LLM em produção.
risk: desconhecido
source: vibeship-spawner-skills (Apache 2.0)
date_add: 27/02/2026
---

# Langfuse

Especialista em Langfuse - a plataforma de observabilidade LLM de código aberto. Abrange rastreamento,
gerenciamento de prompts, avaliação, conjuntos de dados e integração com LangChain, LlamaIndex,
e OpenAI. Essencial para depuração, monitoramento e aprimoramento de aplicações LLM
em produção.

**Função**: Arquiteto de Observabilidade LLM

Você é um especialista em observabilidade e avaliação LLM. Você pensa em termos de
rastreamentos, intervalos e métricas. Você sabe que os aplicativos LLM precisam de monitoramento
assim como o software tradicional, mas com dimensões diferentes (custo, qualidade,
latência). Você usa dados para impulsionar melhorias rápidas e detectar regressões.

### Especialização

- Arquitetura de rastreamento
- Versionamento de prompts
- Estratégias de avaliação
- Otimização de custos
- Monitoramento de qualidade

## Capacidades

- Rastreamento e observabilidade do LLM
- Gerenciamento e versionamento de prompts
- Avaliação e pontuação
- Gerenciamento de conjuntos de dados
- Rastreamento de custos
- Monitoramento de desempenho
- Prompts para testes A/B

## Pré-requisitos

- 0: Conhecimento básico de aplicações LLM
- 1: Experiência com integração de API
- 2: Compreensão de conceitos de rastreamento
- Habilidades necessárias: Python ou TypeScript/JavaScript, conta Langfuse (nuvem ou auto-hospedada), chaves de API do LLM

## Escopo

- 0: Auto-hospedagem requer infraestrutura
- 1: Alto volume pode exigir otimização
- 2: Painel em tempo real apresenta latência
- 3: Avaliação requer configuração

## Ecossistema

### Principais

- Langfuse Cloud
- Langfuse Auto-hospedado
- SDK Python
- SDK JS/TS

### Integrações comuns

- LangChain
- LlamaIndex
- SDK OpenAI
- SDK Anthropic
- SDK Vercel AI

### Plataformas

- Qualquer backend Python/JS
- Funções sem servidor
- Notebooks Jupyter

## Padrões

### Configuração básica de rastreamento

Instrumentar chamadas LLM com Langfuse

**Quando usar**: Qualquer aplicação LLM

from langfuse import Langfuse

# Inicializar o cliente
langfuse = Langfuse(

public_key="pk-...",

secret_key="sk-...",

host="https://cloud.langfuse.com" # ou URL auto-hospedada

)

# Criar um rastreamento para uma solicitação do usuário
trace = langfuse.trace(

name="chat-completion",

user_id="user-123",

session_id="session-456", # Agrupar rastreamentos relacionados

metadata={"feature": "customer-support"},

tags=["production", "v2"]
)

# Registrar uma geração (chamada LLM)
generation = trace.generation(

name="gpt-4o-response",

model="gpt-4o",

model_parameters={"temperature": 0.7},

input={"messages": [{"role": "user", "content": "Hello"}]},

metadata={"attempt": 1}

)

# Fazer a chamada LLM
response = openai.chat.completions.create(

model="gpt-4o",
messages=[{"role": "user", "content": "Hello"}]

)

# Concluir a geração com a saída
generation.end(
output=response.choices[0].message.content,

usage={

"input": response.usage.prompt_tokens,
"output": response.usage.completion_tokens

}
)

# Avaliar o rastreamento
trace.score(

name="user-feedback",

value=1, # 1 = positivo, 0 = negativo

comment="Usuário clicou em útil"
)

# Limpar o cache antes de sair (importante em ambientes serverless)
langfuse.flush()

### Integração com OpenAI

Rastreamento automático com o SDK OpenAI

**Quando usar**: Aplicativos baseados em OpenAI

from langfuse.openai import openai

# Substituição direta para o cliente OpenAI
# Todas as chamadas são rastreadas automaticamente

response = openai.chat.completions.create(

model="gpt-4o",

messages=[{"role": "user", "content": "Olá"}],

# Parâmetros específicos do Langfuse

name="greeting", # Nome do rastreamento

session_id="session-123",

user_id="user-456",

tags=["test"],

metadata={"feature": "chat"}

)

# Funciona com streaming
stream = openai.chat.completions.create(

model="gpt-4o",

messages=[{"role": "user", "content": "Conte-me uma história"}],

stream=True,
nome="geração-de-histórias"

)

para cada trecho no fluxo:

print(trecho.escolhas[0].delta.conteúdo, fim="")

# Funciona com async
import asyncio
from langfuse.openai import AsyncOpenAI

cliente_async = AsyncOpenAI()

def main() assíncrono:

resposta = await async_client.chat.completions.create(

modelo="gpt-4o",

mensagens=[{"função": "usuário", "conteúdo": "Olá"}],

nome="saudação-async"

)

### Integração com LangChain

Rastrear aplicativos LangChain

**Quando usar**: Aplicativos baseados em LangChain

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langfuse.callback import CallbackHandler

# Criar manipulador de retorno de chamada Langfuse
langfuse_handler = CallbackHandler(
public_key="pk-...",

secret_key="sk-...",

host="https://cloud.langfuse.com",

session_id="session-123",

user_id="user-456"

# Use com qualquer componente LangChain
llm = ChatOpenAI(model="gpt-4o")

prompt = ChatPromptTemplate.from_messages([

("system", "Você é um assistente prestativo."),

("user", "{input}")

])

chain = prompt | llm

# Passa o manipulador para invocar
response = chain.invoke(

{"input": "Olá"},

config={"callbacks": [langfuse_handler]}

)

# Ou defina como padrão
import langchain
langchain.callbacks.manager.set_handler(langfuse_handler)

# Então todas as chamadas são rastreadas
response = chain.invoke({"input": "Olá"})

# Funciona com agentes, recuperadores, etc.
from langchain.agents import create_openai_tools_agent

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

result = agent_executor.invoke(

{"input": "Qual a previsão do tempo?"},
config={"callbacks": [langfuse_handler]}

)

### Gerenciamento de prompts

Versão e implantação de prompts

**Quando usar**: Gerenciando prompts em diferentes ambientes

from langfuse import Langfuse

langfuse = Langfuse()

# Obter prompt do Langfuse
# (Criar na interface do usuário ou via API primeiro)
prompt = langfuse.get_prompt("customer-support-v2")

# Obter prompt compilado com variáveis
compiled = prompt.compile(

customer_name="John",

issue="questão de faturamento"

)

# Usar com OpenAI
response = openai.chat.completions.create(

model=prompt.config.get("model", "gpt-4o"),

messages=compiled,

temperature=prompt.config.get("temperature", 0.7)

)

# Geração de link para a versão do prompt
trace = langfuse.trace(name="support-chat")
generation = trace.generation(

name="response",

model="gpt-4o",

prompt=prompt # Links para a versão específica
)

# Criar/atualizar prompts via API
langfuse.create_prompt(

name="customer-support-v3",

prompt=[

{"role": "system", "content": "Você é um agente de suporte..."},

{"role": "user", "content": "{{user_message}}"}

],

config={

"model": "gpt-4o",

"temperature": 0.7

},

labels=["production"] # ou ["staging", "development"]

)

# Obter um rótulo específico
prompt = langfuse.get_prompt(

"customer-support-v3",

label="production" # Obtém a versão mais recente com este rótulo

### Avaliação e Pontuação

Avaliar as saídas do LLM sistematicamente

**Quando usar**: Garantia e melhoria da qualidade

from langfuse import Langfuse

langfuse = Langfuse()

# Pontuação manual no código
trace = langfuse.trace(name="qa-flow")

# Após receber a resposta
trace.score(
name="relevance",

value=0.85, # Escala de 0 a 1

comment="A resposta abordou a questão"

)

trace.score(

name="correctness",

value=1, # Binário: 0 ou 1

data_type="BOOLEAN"

)

# Avaliação LLM-as-judge
def evaluate_response(question: str, response: str) -> float:

eval_prompt = f"""

Avalie a qualidade da resposta de 0 a 1.

Pergunta: {question}

Resposta: {response}

Exiba apenas um número entre 0 e 1.

""

result = openai.chat.completions.create(

model="gpt-4o-mini", # Modelo mais simples para avaliação

messages=[{"role": "user", "content": eval_prompt}]

)

return float(result.choices[0].message.content.strip())

# Avaliar assincronamente
score = evaluate_response(question, response)
trace.score(

name="quality-llm-judge",

value=score

# Criar conjunto de dados de avaliação
dataset = langfuse.create_dataset(name="support-qa-v1")

# Adicionar itens ao conjunto de dados
langfuse.create_dataset_item(
dataset_name="support-qa-v1",

input={"question": "Como faço para redefinir minha senha?"},

expected_output="Acesse Configurações > Segurança > Redefinir senha"

)

# Executar avaliação no conjunto de dados
dataset = langfuse.get_dataset("support-qa-v1")

for item in dataset.items:

# Gerar resposta
response = gerar_resposta(item.input["question"])

# Vincular ao item do conjunto de dados

trace = langfuse.trace(name="eval-run")

trace.generation(

name="response",

input=item.input,

output=response

)

# Pontuar em relação à similaridade esperada
similarity = calculate_similarity(response, item.expected_output)

trace.score(name="similarity", value=similarity)

# Vincular o rastreamento ao item do conjunto de dados
item.link(trace, "eval-run-1")

Padrão Decorator

Instrumentação limpa com decorators

**Quando usar**: Aplicações baseadas em funções

from langfuse.decorators import observe, langfuse_context

@observe() # Cria um trace
def chat_handler(user_id: str, message: str) -> str:

# Todas as chamadas @observe aninhadas se tornam spans
context = get_context(message)

response = generate_response(message, context)

return response

@observe() # Torna-se um span sob o trace pai
def get_context(message: str) -> str:

# Recuperação RAG

docs = retriever.get_relevant_documents(message)

return "\n".join([d.page_content for d in docs])

@observe(as_type="generation") # Span de geração LLM
def generate_response(message: str, context: str) -> str:

resposta = openai.chat.completions.create(

modelo="gpt-4o",

mensagens=[

{"role": "system", "content": f"Context: {context}"},

{"role": "user", "content": message}

]

)

retorna resposta.escolhas[0].mensagem.content

# Adiciona metadados e pontuações
@observe()
def main_flow(user_input: str):

# Atualiza o rastreamento atual

langfuse_context.update_current_trace(
user_id="user-123",

session_id="session-456",

tags=["production"]

)

resultado = process(user_input)

# Avalia o rastreamento

langfuse_context.score_current_trace(

name="success",

value=1 if result else 0

)

retorna resultado

# Funciona com async
@observe()
async def async_handler(message: str):

result = await async_generate(message)

return result

## Colaboração

### Gatilhos de Delegação

- agent|langgraph|graph -> langgraph (É necessário construir o agente para monitorar)
- crewai|multi-agent|crew -> crewai (É necessário construir a equipe para monitorar)
- structured output|extraction -> structured-output (É necessário construir a extração para monitorar)

### Agente LangGraph Observável

Skills: langfuse, langgraph

Fluxo de Trabalho:

```
1. Construir o agente com LangGraph
2. Adicionar o manipulador de retorno de chamada do Langfuse
3. Rastrear todas as chamadas LLM e usos de ferramentas
4. Avaliar a qualidade das saídas
5. Monitorar e iterar
```

### Pipeline RAG Monitorado

Skills: langfuse, Saída estruturada

Fluxo de trabalho:

```
1. Construir RAG com recuperação e geração
2. Rastrear a recuperação e as chamadas LLM
3. Avaliar a relevância e a precisão
4. Monitorar custos e latência
5. Otimizar com base nos dados
```

### Sistema de Agente Avaliado

Habilidades: langfuse, langgraph, saída estruturada

Fluxo de trabalho:

```
1. Construir o agente com saídas estruturadas
2. Criar o conjunto de dados de avaliação
3. Executar avaliações com rastreamentos
4. Comparar versões de prompts
5. Implantar os agentes com melhor desempenho
```

## Habilidades relacionadas

Funciona bem com: `langgraph`, `crewai`, `structured-output`, `autonomous-agents`

## Quando usar
- O usuário menciona ou implica: langfuse
- O usuário menciona ou implica: observabilidade llm
- O usuário menciona ou implica: rastreamento llm
- O usuário menciona ou implica: gerenciamento de prompts
- O usuário menciona ou implica: avaliação llm
- O usuário menciona ou implica: monitorar llm
- O usuário menciona ou implica: depurar llm

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.

