--- 
name: correção-acessibilidade
description: Audite e corrija problemas de acessibilidade HTML, incluindo rótulos ARIA, navegação por teclado, gerenciamento de foco, contraste de cores e erros de formulário. Use ao adicionar controles interativos, formulários, diálogos ou ao revisar a conformidade com as WCAG.
risk: desconhecido
source: comunidade
---

# fixing-accessibility

Corrija problemas de acessibilidade.

## como usar

- `/fixing-accessibility`

Aplique estas restrições a qualquer trabalho de interface do usuário nesta conversa.

- `/fixing-accessibility <arquivo>`

Analise o arquivo em relação a todas as regras abaixo e relate:

- violações (cite a linha ou trecho exato)

- por que isso é importante (uma frase curta)

- uma correção concreta (sugestão em nível de código)

Não reescreva grandes partes da interface do usuário. Prefira correções mínimas e direcionadas.

## Quando usar
Consulte estas diretrizes ao:
- adicionar ou alterar botões, links, entradas, menus, diálogos, guias e listas suspensas
- criar formulários, validações, estados de erro e textos auxiliares
- implementar atalhos de teclado ou interações personalizadas
- trabalhar com estados de foco, captura de foco ou comportamento modal
- renderizar controles somente com ícones
- adicionar interações que só aparecem ao passar o mouse ou conteúdo oculto

## Categorias de regras por prioridade

| prioridade | categoria | impacto |

|----------|----------|--------|

| 1 | nomes acessíveis | crítica |

| 2 | acesso por teclado | crítica |

| 3 | foco e diálogos | crítica |

| 4 | semântica | alta |

| 5 | formulários e erros | alta |

| 6 | anúncios | média-alta |

| 7 | contraste e estados | média |

| 8 | mídia e movimento | baixa-média |

| 9 | limites de ferramentas | crítica |

## Referência rápida

### 1. Nomes acessíveis (crítico)

- Todo controle interativo deve ter um nome acessível
- Botões com apenas ícones devem ter aria-label ou aria-labelledby
- Todos os inputs, selects e textareas devem ter um rótulo
- Links devem ter um texto significativo (sem “clique aqui”)
- Ícones decorativos devem ter aria-hidden

### 2. Acesso por teclado (crítico)

- Não use divs ou spans como botões sem suporte completo ao teclado
- Todos os elementos interativos devem ser acessíveis pela tecla Tab
- O foco deve ser visível para usuários que utilizam o teclado
- Não use tabindex maior que 0
- A tecla Escape deve fechar diálogos ou sobreposições quando aplicável

### 3. Foco e diálogos (crítico)

- Modais devem reter o foco enquanto abertos
- Restaure o foco ao elemento que o acionou ao fechar
- Defina o foco inicial dentro dos diálogos
- Abrir um diálogo não deve rolar a página inesperadamente

### 4. Semântica (alta)

- Prefira elementos nativos (button, a, Entrada) em vez de soluções alternativas baseadas em funções
- Se uma função for usada, os atributos ARIA obrigatórios devem estar presentes
- Listas devem usar `ul` ou `ol` com `li`
- Não ignore níveis de cabeçalho
- Tabelas devem usar `th` para cabeçalhos quando aplicável

### 5. Formulários e erros (alta prioridade)

- Os erros devem ser vinculados aos campos usando `aria-describedby`
- Campos obrigatórios devem ser anunciados
- Campos inválidos devem ter `aria-invalid` definido
- Textos auxiliares devem ser associados às entradas
- Ações de envio desabilitadas devem explicar o motivo

### 6. Anúncios (média-alta prioridade)

- Erros críticos em formulários devem usar `aria-live`
- Estados de carregamento devem usar `aria-busy` ou texto de status
- Notificações (toasts) não devem ser a única maneira de transmitir informações críticas
- Controles expansíveis devem usar `aria-expanded` e `aria-controls`

### 7. Contraste e estados (média prioridade)

- Garanta contraste suficiente para texto e ícones
- Interações que ocorrem apenas ao passar o mouse devem ter equivalentes no teclado
- Estados desabilitados não devem depender apenas da cor
- Não remova os contornos de foco sem uma substituição visível

### 8. Mídia e movimento (baixa a média)

- As imagens devem ter texto alternativo correto (significativo ou vazio)
- Vídeos com fala devem fornecer legendas quando relevantes
- Respeite a preferência por movimento reduzido para movimentos não essenciais
- Evite reproduzir automaticamente mídias com som

### 9. Limites de ferramentas (crítico)

- Prefira alterações mínimas, não refatore código não relacionado
- Não adicione aria quando a semântica nativa já resolver o problema
- Não migre bibliotecas de interface do usuário, a menos que seja solicitado

## Correções comuns

```html
<!-- botão somente com ícone: adicione aria-label -->
<!-- antes --> <button><svg>...</svg></button>
<!-- depois --> <button aria-label="Fechar"><svg aria-hidden="true">...</svg></button>

<!-- div como botão: use elemento nativo -->
<!-- antes --> <div onclick="save()">Salvar</div>
<!-- depois --> <button onclick="save()">Salvar</button>

<!-- erro de formulário: link com aria-describedby -->
<!-- antes --> <input id="email" /> <span>Email inválido</span>
<!-- depois --> <input id="email" aria-describedby="email-err" aria-invalid="true" /> <span id="email-err">Email inválido</span>
```

## orientações de revisão

- Corrija primeiro os problemas críticos (nomes, teclado, foco, limites de ferramentas)
- Prefira HTML nativo antes de adicionar aria
- Cite o trecho exato, descreva a falha e proponha uma pequena correção
- Para widgets complexos (menu, diálogo, caixa de combinação), prefira primitivas acessíveis estabelecidas em vez de comportamento personalizado