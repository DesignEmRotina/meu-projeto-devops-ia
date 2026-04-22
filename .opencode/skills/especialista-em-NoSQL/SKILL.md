--- 
name: especialista-em-NoSQL
description: "Orientação especializada para bancos de dados NoSQL distribuídos (Cassandra, DynamoDB). Foca em modelos mentais, modelagem orientada a consultas, design de tabela única e como evitar partições críticas em sistemas de alta escala."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Padrões de Especialista em NoSQL (Cassandra e DynamoDB)

## Visão Geral

Esta habilidade fornece modelos mentais profissionais e padrões de design para **bancos de dados distribuídos com colunas largas e chave-valor** (especificamente Apache Cassandra e Amazon DynamoDB).

Ao contrário do SQL (onde você modela entidades de dados) ou de bancos de dados de documentos (como o MongoDB), esses sistemas distribuídos exigem que você **modele suas consultas primeiro**.

## Quando usar
- **Projetando para Escala**: Indo além de bancos de dados simples de nó único para clusters distribuídos.

- **Seleção de Tecnologia**: Avaliar ou utilizar **Cassandra**, **ScyllaDB** ou **DynamoDB**.

- **Otimização de Desempenho**: Solucionar problemas de "partições quentes" ou alta latência em sistemas NoSQL existentes.

- **Microsserviços**: Implementar padrões de "banco de dados por serviço" onde leituras altamente otimizadas são necessárias.

## A Mudança de Mentalidade: SQL vs. NoSQL Distribuído

| Recurso | SQL (Relacional) | NoSQL Distribuído (Cassandra/DynamoDB) |

| :--- | :--- | :--- |

| **Modelagem de Dados** | Modelar Entidades + Relacionamentos | Modelar **Consultas** (Padrões de Acesso) |

| **Joins** | Uso intensivo de CPU no momento da leitura | **Pré-computados** (Desnormalizados) no momento da gravação |

| **Custo de Armazenamento** | Caro (minimizar duplicação) | Baixo custo (duplicação de dados para velocidade de leitura) |
| **Consistência** | ACID (Forte) | **BASE (Eventual)** / Ajustável |

| **Escalabilidade** | Vertical (Máquina maior) | **Horizontal** (Mais nós/fragmentos) |

> **A Regra de Ouro:** Em SQL, você projeta o modelo de dados para responder a *qualquer* consulta. Em NoSQL, você projeta o modelo de dados para responder a consultas *específicas* de forma eficiente.

## Padrões de Projeto Essenciais

### 1. Modelagem Orientada a Consultas (Padrões de Acesso)

Normalmente, você não pode "adicionar uma consulta posteriormente" sem migração ou criação de uma nova tabela/índice.

**Processo:**
1. **Liste todas as Entidades** (Usuário, Pedido, Produto).

2. **Liste todos os Padrões de Acesso** ("Obter Usuário por E-mail", "Obter Pedidos por Usuário classificados por Data").

3. **Projete a(s) Tabela(s)** especificamente para atender a esses padrões com uma única consulta.

### 2. A Chave de Partição é Fundamental

Os dados são distribuídos entre os nós físicos com base na **Chave de Partição (PK)**.

- **Objetivo:** Distribuição uniforme de dados e tráfego.

- **Anticorrealismo:** Usar uma PK de baixa cardinalidade (por exemplo, `status="active"` ou `gender="m"`) cria **Partições Quentes**, limitando a taxa de transferência à capacidade de um único nó.

- **Melhor Prática:** Use chaves de alta cardinalidade (IDs de Usuário, IDs de Dispositivo, Chaves Compostas).

### 3. Chaves de Agrupamento/Classificação

Dentro de uma partição, os dados são classificados em disco pela **Chave de Agrupamento (Cassandra)** ou **Chave de Classificação (DynamoDB)**.

- Isso permite **Consultas de Intervalo** eficientes (por exemplo, `WHERE user_id=X AND date > Y`).

- Ele pré-classifica seus dados de forma eficaz para requisitos específicos de recuperação.

### 4. Design de Tabela Única (Listas de Adjacência)

*Uso principal: DynamoDB (mas os conceitos se aplicam a outros lugares)*

Armazenar vários tipos de entidade em uma única tabela para permitir leituras pré-convergentes.

| PK (Partição) | SK (Classificação) | Campos de Dados... |

| :--- | :--- | :--- |

| `USUÁRIO#123` | `PERFIL` | `{ nome: "Ian", email: "..." }` |

| `USUÁRIO#123` | `PEDIDO#998` | `{ total: 50,00, status: "enviado" }` |

| `USUÁRIO#123` | `PEDIDO#999` | `{ total: 12,00, status: "pendente" }` |

- **Consulta:** `PK="USER#123"`
- **Resultado:** Busca o perfil do usuário E todos os pedidos em **uma única requisição de rede**.

### 5. Desnormalização e Duplicação

Não tenha receio de armazenar os mesmos dados em várias tabelas para atender a diferentes padrões de consulta.

- **Tabela A:** `users_by_id` (PK: uuid)
- **Tabela B:** `users_by_email` (PK: email)

*Desvantagem: Você deve gerenciar a consistência dos dados entre as tabelas (geralmente usando consistência eventual ou gravações em lote).*

## Orientações Específicas

### Apache Cassandra / ScyllaDB

- **Estrutura da Chave Primária:** `((Chave de Partição), Colunas de Agrupamento)`
- **Sem Junções, Sem Agregações:** Não tente usar `JOIN` ou `GROUP BY`. Pré-calcule as agregações em uma tabela de contadores separada.
- **Evite `ALLOW FILTERING`:** Se você vir isso em produção, seu modelo de dados está incorreto. Isso implica em uma varredura completa do cluster.
- **Gravações são baratas:** Inserções e atualizações são apenas acréscimos à árvore LSM. Não se preocupe tanto com o volume de gravação quanto com a eficiência de leitura.

- **Marcadores de exclusão:** Exclusões são marcadores caros. Evite padrões de exclusão de alta velocidade (como filas) em tabelas padrão.

### AWS DynamoDB

- **GSI (Índice Secundário Global):** Use GSIs para criar visualizações alternativas dos seus dados (por exemplo, "Pesquisar Pedidos por Data" em vez de por Usuário).

- *Observação:* Os GSIs são eventualmente consistentes.

- **LSI (Índice Secundário Local):** Classifica os dados de forma diferente *dentro* da mesma partição. Deve ser criado no momento da criação da tabela.

- **WCU / RCU:** Compreenda os modos de capacidade. O design de tabela única ajuda a otimizar as unidades de capacidade consumidas.

- **TTL:** Use atributos de Tempo de Vida (TTL) para expirar automaticamente dados antigos (exclusão gratuita) sem criar marcadores de exclusão (tombstones).

## Lista de Verificação para Especialistas

Antes de finalizar seu esquema NoSQL:

- [ ] **Cobertura de Padrões de Acesso:** Cada padrão de consulta mapeia para uma tabela ou índice específico?

- [ ] **Verificação de Cardinalidade:** A chave de partição possui valores únicos suficientes para distribuir o tráfego uniformemente? - [ ] **Risco de Partição Dividida:** Para qualquer partição individual (por exemplo, os pedidos de um único usuário), ela crescerá indefinidamente? (Se > 10 GB, você precisa "fragmentar" a partição, por exemplo, `USUÁRIO#123#2024-01`).
- [ ] **Requisito de Consistência:** O aplicativo pode tolerar consistência eventual para este padrão de leitura?

## Antipadrões Comuns

❌ **Dispersão-Coleta:** Consultar *todas* as partições para encontrar um item (Scan).

❌ **Teclas de Atalho:** Colocar todos os dados de "segunda-feira" em uma única partição.

❌ **Modelagem Relacional:** Criar tabelas `Autor` e `Livro` e tentar uni-las no código. (Em vez disso, incorpore resumos de livros em Autor ou duplique as informações de Autor em Livros).