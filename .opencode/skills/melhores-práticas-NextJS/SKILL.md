--- 
name: melhores-práticas-NextJS
description: "Princípios do Next.js App Router. Componentes do servidor, busca de dados, padrões de roteamento."
risk: desconhecido
source: comunidade
date_add: "2026-02-27"
---

# Melhores Práticas do Next.js

> Princípios para o desenvolvimento do Next.js App Router.

---

## 1. Componentes do Servidor vs. Componentes do Cliente

### Árvore de Decisão

```
Precisa de...?

│
├── useState, useEffect, manipuladores de eventos
│ └── Componente do Cliente ('use client')
│
├── Busca direta de dados, sem interatividade
│ └── Componente do Servidor (padrão)
│
└── Ambos? └── Divisão: Servidor pai + Cliente filho
```

### Por padrão

| Tipo | Uso |

|------|-----|

| **Servidor** | Busca de dados, layout, conteúdo estático |

| **Cliente** | Formulários, botões, interface interativa |


---

## 2. Padrões de Busca de Dados

### Estratégia de Busca

| Padrão | Uso |

|---------|-----|

| **Padrão** | Estático (em cache na compilação) |

| **Revalidar** | ISR (atualização baseada em tempo) |

| **Sem armazenamento** | Dinâmico (a cada requisição) |

### Fluxo de Dados

| Origem | Padrão |

|--------|---------|

| Banco de dados | Busca por componente do servidor |

| API | Busca com cache |

| Entrada do usuário | Estado do cliente + ação do servidor |

---

## 3. Princípios de Roteamento

### Convenções de Arquivos

| Arquivo | Finalidade |

|------|---------|

| `page.tsx` | Interface de Rota |

| `layout.tsx` | Layout compartilhado |

| `loading.tsx` | Estado de carregamento |

| `error.tsx` | Limite de erro |

| `not-found.tsx` | Página 404 |

### Organização de Rotas

| Padrão | Uso |

|---------|-----|

| Grupos de rotas `(nome)` | Organizar sem URL |

| Rotas paralelas `@slot` | Múltiplas páginas do mesmo nível |

| Interceptação `(.)` | Sobreposições modais |

---

## 4. Rotas de API

### Manipuladores de Rotas

| Método | Uso |

|--------|-----|

| GET | Ler dados | | POST | Criar dados |

| PUT/PATCH | Atualizar dados |

| DELETE | Remover dados |

### Boas Práticas

- Validar a entrada com Zod
- Retornar códigos de status apropriados
- Tratar erros de forma adequada
- Usar o runtime do Edge sempre que possível

---

## 5. Princípios de Desempenho

### Otimização de Imagens

- Usar o componente next/image
- Definir prioridade para a imagem acima da dobra
- Fornecer um placeholder de desfoque
- Usar tamanhos responsivos

### Otimização de Pacotes

- Importações dinâmicas para componentes pesados
- Divisão de código baseada em rotas (automática)
- Analisar com o analisador de pacotes

---

## 6. Metadados

### Estático vs. Dinâmico

| Tipo | Uso |

|------|-----|

| Exportação estática | Metadados fixos |

| generateMetadata | Metadados dinâmicos por rota |

### Tags Essenciais

- título (50-60 caracteres)
- descrição (150-160 caracteres)
- imagens Open Graph
- URL canônica

---

## 7. Estratégia de Cache

### Camadas de Cache

| Camada | Controle |

|-------|---------|

| Requisição | opções de busca |

| Dados | revalidar/tags |

| Rota completa | configuração de rota |

### Revalidação

| Método | Uso |

|--------|-----|

| Baseado em tempo | `revalidar: 60` |

| Sob demanda | `revalidarCaminho/Tag` |

| Sem cache | `sem armazenamento` |

---

## 8. Ações do Servidor

### Casos de Uso

- Envio de formulários
- Modificações de dados
- Acionadores de revalidação

### Boas Práticas

- Marcar com 'use server'
- Validar todas as entradas
- Retornar respostas tipadas
- Tratar erros

---

## 9. Antipadrões

| ❌ Não | ✅ Faça |

|----------|-------|

| 'use client' em todos os lugares | Servidor por padrão |

| Buscar em componentes do cliente | Buscar no servidor |

| Ignorar estados de carregamento | Usar loading.tsx |

| Ignorar limites de erro | Usar error.tsx |

| Pacotes de cliente grandes | Importações dinâmicas |

---

## 10. Estrutura do Projeto

```
app/
├── (marketing)/ # Grupo de rotas
│ └── page.tsx
├── (dashboard)/
│ ├── layout.tsx # Layout do painel
│ └── page.tsx
├── api/
│ └── [resource]/
│ └── route.ts
└── components/

└── ui/
```

---

> **Lembre-se:** Os componentes do servidor são os padrões por um motivo. Comece por eles e adicione os componentes do cliente somente quando necessário.

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.