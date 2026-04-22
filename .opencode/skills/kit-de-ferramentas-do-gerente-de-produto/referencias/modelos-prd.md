# Modelos de Documento de Requisitos do Produto (PRD)

## Modelo Padrão de PRD

### 1. Resumo Executivo
**Objetivo**: Visão geral em uma página para executivos e stakeholders

#### Componentes:
- **Declaração do Problema** (2 a 3 frases)
- **Solução Proposta** (2 a 3 frases)
- **Impacto nos Negócios** (3 tópicos)
- **Cronograma** (Marcos importantes)
- **Recursos Necessários** (Tamanho da equipe e orçamento)
- **Métricas de Sucesso** (3 a 5 KPIs)

### 2. Definição do Problema

#### 2.1 Problema do Cliente
- **Quem**: Persona(s) do usuário-alvo
- **O quê**: Problema ou necessidade específica
- **Quando**: Contexto e frequência
- **Onde**: Ambiente e pontos de contato
- **Por quê**: Análise da causa raiz
- **Impacto**: Custo de não solucionar o problema

#### 2.2 Oportunidade de Mercado
- **Tamanho do Mercado**: TAM, SAM, SOM
- **Taxa de Crescimento**: Percentual de crescimento anual
- **Concorrência**: Soluções atuais e lacunas
- **Momento Oportuno**: Por que agora?

#### 2.3 Análise de Viabilidade
- **Potencial de Receita**: Impacto projetado
- **Redução de Custos**: Ganhos de eficiência
- **Valor Estratégico**: Alinhamento com os objetivos da empresa
- **Análise de Riscos**: E se não fizermos isso?

### 3. Visão Geral da Solução

#### 3.1 Solução Proposta
- **Descrição Geral**: O que estamos construindo
- **Principais Funcionalidades**: Funcionalidades essenciais
- **Jornada do Usuário**: Fluxo completo (de ponta a ponta)
- **Diferenciação**: Proposta de valor única

#### 3.2 Dentro do Escopo
- Funcionalidade 1: Descrição e prioridade
- Funcionalidade 2: Descrição e prioridade
- Funcionalidade 3: Descrição e prioridade

#### 3.3 Fora do Escopo
- O que NÃO estamos fazendo explicitamente
- Considerações futuras
- Dependências de outras equipes

#### 3.4 Definição do MVP
- **Funcionalidades Essenciais**: Conjunto mínimo de funcionalidades viáveis
- **Critérios de Sucesso**: Definição de "funcionamento"
- **Cronograma**: Data de entrega do MVP
- **Objetivos de Aprendizagem**: O que queremos validar

### 4. Histórias de Usuário e Requisitos

#### 4.1 Histórias de Usuário
``` [persona]
Eu quero [ação]
Para que [resultado/benefício]

Critérios de Aceitação:
- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3
```

#### 4.2 Requisitos Funcionais
| ID | Requisito | Prioridade | Observações |

|----|------------|----------|-------|

| FR1 | O usuário pode... | P0 | Crítico para o MVP |

| FR2 | O sistema deve... | P1 | Importante |

| FR3 | O recurso deve... | P2 | Desejável |

#### 4.3 Requisitos Não Funcionais
- **Desempenho**: Tempos de resposta, taxa de transferência
- **Escalabilidade**: Metas de crescimento de usuários/dados
- **Segurança**: Autenticação, autorização, proteção de dados
- **Confiabilidade**: Metas de tempo de atividade, taxas de erro
- **Usabilidade**: Padrões de acessibilidade, suporte a dispositivos
- **Conformidade**: Requisitos regulatórios

### 5. Design e Experiência do Usuário

#### 5.1 Princípios de Design
- Princípio 1: Descrição
- Princípio 2: Descrição
- Princípio 3: Descrição

#### 5.2 Wireframes/Mockups
- Link para arquivos Figma/Sketch
- Telas e fluxos principais
- Padrões de interação

#### 5.3 Arquitetura da Informação
- Estrutura de navegação
- Organização de dados
- Hierarquia de conteúdo

### 6. Especificações Técnicas

#### 6.1 Visão Geral da Arquitetura
- Diagrama da arquitetura do sistema
- Pilha de tecnologias
- Pontos de integração
- Dados Fluxo

#### 6.2 Design da API
- Endpoints e métodos
- Formatos de requisição/resposta
- Abordagem de autenticação
- Limitação de taxa

#### 6.3 Design do Banco de Dados
- Modelo de dados
- Entidades e relacionamentos principais
- Estratégia de migração

#### 6.4 Considerações de Segurança
- Método de autenticação
- Modelo de autorização
- Criptografia de dados
- Tratamento de informações pessoais identificáveis ​​(PII)

### 7. Estratégia de Entrada no Mercado

#### 7.1 Plano de Lançamento
- **Lançamento Inicial**: Usuários beta, cronograma
- **Lançamento Completo**: Todos os usuários, cronograma
- **Marketing**: Campanhas e canais
- **Suporte**: Documentação e treinamento

#### 7.2 Estratégia de Preços
- Modelo de preços
- Análise da concorrência
- Proposta de valor

#### 7.3 Métricas de Sucesso
| Métrica | Meta | Método de Medição |

|--------|--------|-------------------|
| Taxa de Adoção | X% | Usuários Ativos Diários |

| Satisfação do Usuário | X/10 | Pontuação NPS |

| Impacto na Receita | $X | Receita Recorrente Mensal |

| Desempenho | <Xms | Tempo de Resposta P95 |

### 8. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Estratégia de Mitigação |

|------|------------|--------|-------------------|

| Dívida técnica | Média | Alta | Alocar 20% para refatoração |

| Adoção do usuário | Baixa | Alta | Programa beta com ciclos de feedback |

| Escopo crescente | Alto | Médio | Revisões semanais com as partes interessadas |

### 9. Cronograma e Marcos

| Marco | Data | Entregáveis ​​| Critérios de Sucesso |

|-----------|------|--------------|-----------------|

| Design concluído | Semana 2 | Mockups, Arquitetura da Informação | Aprovação das partes interessadas |

| Desenvolvimento do MVP | Semana 6 | Funcionalidades principais | Todos os P0s concluídos |

| Lançamento Beta | Semana 8 | Lançamento limitado | 100 usuários beta |

| Lançamento completo | Semana 12 | Disponibilidade geral | Taxa de erro <1% |

### 10. Equipe e Recursos

#### 10.1 Estrutura da Equipe
- **Gerente de Produto**: [Nome]
- **Líder de Engenharia**: [Nome]
- **Líder de Design**: [Nome]
- **Engenheiros**: X FTEs
- **QA**: X FTEs

#### 10.2 Orçamento
- Desenvolvimento: $X
- Infraestrutura: $X
- Marketing: $X
- Total: $X

### 11. Anexo
- Dados da Pesquisa de Usuários
- Análise Competitiva
- Diagramas Técnicos
- Documentos Legais/de Conformidade

---

## Modelo de Épico Ágil

### Épico: [Nome do Épico]

#### Visão Geral
**ID do Épico**: EPIC-XXX
**Tema**: [Tema do Produto]
**Trimestre**: QX 20XX
**Status**: Descoberta | Em Andamento | Completo

#### Declaração do Problema
[2-3 frases descrevendo o problema]

#### Metas e Objetivos
1. Objetivo 1
2. Objetivo 2
3. Objetivo 3

#### Métricas de Sucesso
- Métrica 1: Meta
- Métrica 2: Meta
- Métrica 3: Meta

#### Histórias de Usuário
| ID da História | Título | Prioridade | Pontos | Status |

|----------|-------|----------|--------|--------|

| US-001 | Como um... | P0 | 5 | A Fazer |

| US-002 | Como um... | P1 | 3 | A Fazer |

#### Dependências
- Dependência 1: Equipe/Sistema
- Dependência 2: Equipe/Sistema

#### Critérios de Aceitação
- [ ] Todas as histórias P0 concluídas
- [ ] Metas de desempenho atingidas
- [ ] Revisão de segurança aprovada
- [ ] Documentação atualizada

---

## Modelo de PRD de uma página

### [Nome do Recurso] - PRD de uma página

**Data**: [Data]
**Autor**: [Nome do Gerente de Produto]
**Status**: Rascunho | Em Revisão | Aprovado

#### Problema
*Qual problema estamos resolvendo? Para quem?*
[2-3 frases]

#### Solução
*O que estamos construindo?*
[2-3 frases]

#### Por que agora?

*O que justifica a urgência?*
- Motivo 1
- Motivo 2
- Motivo 3

#### Métricas de Sucesso
| Métrica | Atual | Meta |

|--------|---------|--------|
| KPI 1 | X | Y |

| KPI 2 | X | Y |

#### Escopo
**Entrada**: Funcionalidade 1, Funcionalidade 2, Funcionalidade 3
**Saída**: Funcionalidade A, Funcionalidade B

#### Fluxo do Usuário
```
Etapa 1 → Etapa 2 → Etapa 3 → Sucesso!

```

#### Riscos
1. Risco 1 → Mitigação
2. Risco 2 → Mitigação

#### Cronograma
- Design: Semanas 1-2
- Desenvolvimento: Semanas 3-6
- Testes: Semana 7
- Lançamento: Semana 8

#### Recursos
- Engenharia: X desenvolvedores
- Design: X designer
- QA: X testador

#### Perguntas em Aberto
1. Pergunta 1?

2. Pergunta 2?

---

## Modelo de Briefing de Funcionalidade (Leve)

### Funcionalidade: [Nome]

#### Contexto
*Por que estamos considerando isso?*

#### Hipótese
*Acreditamos que [desenvolver esta funcionalidade]
Para [estes usuários]
[alcançará este resultado]
Saberemos que estamos certos quando [vermos esta métrica]*

#### Solução Proposta
*Abordagem geral*

#### Estimativa de Esforço
- **Tamanho**: PP | P | M | G | GG
- **Confiança**: Alta | Média | Baixa

#### Próximos Passos
1. [ ] Pesquisa com usuários
2. [ ] Exploração de design
3. [ ] Teste técnico preliminar
4. [ ] Revisão com as partes interessadas