--- 
name: melhores-práticas-de-React
description: "Guia completo de otimização de desempenho para aplicações React e Next.js, mantido pela Vercel. Use ao escrever novos componentes React ou páginas Next.js, implementar busca de dados (no lado do cliente ou do servidor) ou revisar o código em busca de problemas de desempenho."
risk: seguro
source: comunidade
date_add: "27/02/2026"
---

# Melhores Práticas de React da Vercel

Guia completo de otimização de desempenho para aplicações React e Next.js, mantido pela Vercel. Contém 45 regras em 8 categorias, priorizadas por impacto para orientar a refatoração automatizada e a geração de código.

## Quando usar
Consulte estas diretrizes quando:
- Escrever novos componentes React ou páginas Next.js
- Implementar busca de dados (no lado do cliente ou do servidor)
- Revisar o código em busca de problemas de desempenho
- Refatorar código React/Next.js existente
- Otimizar o tamanho do pacote ou os tempos de carregamento

## Categorias de Regras por Prioridade

| Prioridade | Categoria | Impacto | Prefixo |

|----------|----------|--------|--------|

| 1 | Eliminação de Cascatas | CRÍTICO | `async-` |

| 2 | Otimização do Tamanho do Pacote | CRÍTICO | `bundle-` |

| 3 | Desempenho do Lado do Servidor | ALTO | `server-` |

| 4 | Busca de Dados do Lado do Cliente | MÉDIO-ALTO | `client-` |

| 5 | Otimização de Rerenderização | MÉDIO | `rerender-` |

| 6 | Desempenho de Renderização | MÉDIO | `rendering-` |

| 7 | Desempenho do JavaScript | BAIXO-MÉDIO | `js-` |

| 8 | Padrões Avançados | BAIXO | `advanced-` |

## Referência Rápida

### 1. Eliminando Cascatas (CRÍTICO)

- `async-defer-await` - Mova o `await` para os branches onde ele é realmente usado
- `async-parallel` - Use `Promise.all()` para operações independentes
- `async-dependencies` - Use `better-all` para dependências parciais
- `async-api-routes` - Inicie promises cedo e use `await` mais tarde nas rotas da API
- `async-suspense-boundaries` - Use `Suspense` para transmitir conteúdo

### 2. Otimização do Tamanho do Pacote (CRÍTICO)

- `bundle-barrel-imports` - Importe diretamente, evite arquivos barrel
- `bundle-dynamic-imports` - Use `next`/`dynamic` para componentes pesados
- `bundle-defer-third-party` - Carregue analytics/logging após a hidratação
- `bundle-conditional` - Carregue módulos somente quando o recurso estiver ativado
- `bundle-preload` - Pré-carregue ao passar o mouse/focar para recursos percebidos Velocidade

### 3. Desempenho no Servidor (ALTO)

- `server-cache-react` - Usar React.cache() para deduplicação por requisição
- `server-cache-lru` - Usar cache LRU para cache entre requisições
- `server-serialization` - Minimizar a quantidade de dados passados ​​para os componentes do cliente
- `server-parallel-fetching` - Reestruturar os componentes para paralelizar as buscas
- `server-after-nonblocking` - Usar after() para operações não bloqueantes

### 4. Busca de Dados no Cliente (MÉDIO-ALTO)

- `client-swr-dedup` - Usar SWR para deduplicação automática de requisições
- `client-event-listeners` - Desduplicar listeners de eventos globais

### 5. Otimização de Renderização (MÉDIO)

- `rerender-defer-reads` - Não se inscrever em estados usados ​​apenas em callbacks
- `rerender-memo` - Extrai tarefas complexas para componentes memorizados
- `rerender-dependencies` - Usa dependências primitivas em efeitos
- `rerender-derived-state` - Assina booleanos derivados, não valores brutos
- `rerender-functional-setstate` - Usa setState funcional para callbacks estáveis
- `rerender-lazy-state-init` - Passa uma função para useState para valores complexos
- `rerender-transitions` - Usa startTransition para atualizações não urgentes

### 6. Desempenho de Renderização (MÉDIO)

- `rendering-animate-svg-wrapper` - Anima o elemento div, não o elemento SVG
- `rendering-content-visibility` - Usa content-visibility para listas longas
- `rendering-hoist-jsx` - Extrai JSX estático de fora dos componentes
- `rendering-svg-precision` - Reduz a precisão das coordenadas SVG
- `rendering-hydration-no-flicker` - Use script inline para dados somente do cliente
- `rendering-activity` - Use o componente Activity para mostrar/ocultar
- `rendering-conditional-render` - Use operador ternário, não &&, para condicionais

### 7. Desempenho do JavaScript (BAIXO-MÉDIO)

- `js-batch-dom-css` - Agrupe alterações de CSS por meio de classes ou cssText
- `js-index-maps` - Crie um mapa para consultas repetidas
- `js-cache-property-access` - Armazene em cache as propriedades do objeto em loops
- `js-cache-function-results` - Armazene em cache os resultados da função em um mapa de nível de módulo
- `js-cache-storage` - Armazene em cache as leituras do localStorage/sessionStorage
- `js-combine-iterations` - Combine vários filtros/mapas em um único loop
- `js-length-check-first` - Verifique o comprimento do array antes Comparação dispendiosa
- `js-early-exit` - Retornar antecipadamente de funções
- `js-hoist-regexp` - Elevar a criação de RegExp para fora de loops
- `js-min-max-loop` - Usar loop para min/max em vez de ordenação
- `js-set-map-lookups` - Usar Set/Map para buscas O(1)
- `js-tosorted-immutable` - Usar toSorted() para imutabilidade

### 8. Padrões Avançados (BAIXO)

- `advanced-event-handler-refs` - Armazenar manipuladores de eventos em refs
- `advanced-use-latest` - usar a versão mais recente para refs de callback estáveis

## Como usar

Leia os arquivos de regras individuais para explicações detalhadas e código Exemplos:

```
rules/async-parallel.md
rules/bundle-barrel-imports.md
rules/_sections.md
```

Cada arquivo de regras contém:
- Breve explicação