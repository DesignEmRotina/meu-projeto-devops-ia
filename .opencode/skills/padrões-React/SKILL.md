--- 
name: padrões-React
description: "Padrões e princípios modernos do React. Hooks, composição, desempenho, melhores práticas do TypeScript."
risk: seguro
source: comunidade
date_add: "2026-02-27"
---

# React Patterns

> Princípios para construir aplicações React prontas para produção.

---

## 1. Princípios de Design de Componentes

### Tipos de Componentes

| Tipo | Uso | Estado |

|------|-----|-------|

| **Servidor** | Busca de dados, estático | Nenhum |

| **Cliente** | Interatividade | useState, efeitos |

| **Apresentação** | Exibição da interface do usuário | Somente props |

| **Contêiner** | Lógica/estado | Estado complexo |

### Regras de Design

- Uma responsabilidade por componente
- Props de cima para baixo, eventos de baixo para cima
- Composição em vez de herança
- Prefira componentes pequenos e focados

---

## 2. Padrões de Hooks

### Quando Extrair Hooks

| Padrão | Extrair Quando |

|---------|-------------|

| **useLocalStorage** | Mesma lógica de armazenamento necessária |

| **useDebounce** | Múltiplos valores com debounce |

| **useFetch** | Padrões de busca repetidos |

| **useForm** | Estado de formulário complexo |

### Regras de Hooks

- Hooks apenas no nível superior
- Mesma ordem em todas as renderizações
- Hooks personalizados começam com "use"
- Limpar os efeitos ao desmontar

---

## 3. Seleção de Gerenciamento de Estado

| Complexidade | Solução |

|------------|----------|

| Simples | useState, useReducer |

| Local compartilhado | Contexto |

| Estado do servidor | React Query, SWR |

| Global complexo | Zustand, Redux Toolkit |

### Posicionamento do Estado

| Escopo | Onde |

|-------|-------|

| Componente único | useState |

| Pai-filho | Elevar estado |

| Subárvore | Contexto |

| Aplicativo inteiro | Armazenamento global |

---

## 4. Padrões do React 19

### Novos Hooks

| Hook | Propósito |

|------|---------|

| **useActionState** | Estado de submissão de formulário |

| **useOptimistic** | Atualizações de UI otimistas |

| **use** | Ler recursos na renderização |

### Benefícios do Compilador

- Memorização automática
- Menos uso manual de useMemo/useCallback
- Foco em componentes puros

---

## 5. Padrões de Composição

### Componentes Compostos

- O componente pai fornece o contexto
- Os componentes filhos consomem o contexto
- Composição flexível baseada em slots
- Exemplo: Abas, Acordeão, Menu suspenso

### Render Props vs Hooks

| Caso de Uso | Preferência |

|----------|--------|

| Lógica reutilizável | Hook personalizado |

| Flexibilidade de renderização | Render props |

| Transversal | Componente de ordem superior |

---

## 6. Princípios de Desempenho

### Quando Otimizar

| Sinal | Ação |

|--------|--------|

| Renderizações lentas | Analise o desempenho primeiro |

| Listas grandes | Virtualize |

| Cálculo custoso | useMemo |

| Callbacks estáveis ​​| useCallback |

### Ordem de Otimização

1. Verificar se o problema é realmente a lentidão
2. Criar um perfil com as Ferramentas de Desenvolvedor
3. Identificar o gargalo
4. Aplicar a correção direcionada

---

## 7. Tratamento de Erros

### Uso de Limites de Erro

| Escopo | Localização |

|-------|-----------|

| Em todo o aplicativo | Nível raiz |

| Funcionalidade | Nível de rota/funcionalidade |

| Componente | Ao redor do componente de risco |

### Recuperação de Erros

- Exibir interface de usuário alternativa
- Registrar o erro
- Oferecer opção de nova tentativa
- Preservar os dados do usuário

---

## 8. Padrões do TypeScript

### Tipagem de Props

| Padrão | Uso |

|---------|-----|

| Interface | Props de componente |

| Tipo | Uniões, complexas |

| Genérico | Componentes reutilizáveis ​​|

### Tipos Comuns

| Necessidade | Tipo |

|------|------| | Filhos | ReactNode |

| Manipulador de eventos | MouseEventHandler |

| Ref | RefObject<Element> |


---

## 9. Princípios de Teste

| Nível | Foco |

|-------|-------|

| Unidade | Funções puras, hooks |

| Integração | Comportamento do componente |

| E2E | Fluxos de usuário |

### Prioridades de teste

- Comportamento visível ao usuário
- Casos extremos
- Estados de erro
- Acessibilidade

---

## 10. Antipadrões

| ❌ Não faça | ✅ Faça |

|----------|-------|

| Exploração profunda de props | Usar contexto |

| Componentes gigantes | Dividir em componentes menores |

| useEffect para tudo | Componentes de servidor |

| Otimização prematura | Primeiro o perfil |

| Índice como chave | ID único e estável |

---

> **Lembre-se:** React é sobre composição. Construa em pequena escala, combine com cuidado.

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.