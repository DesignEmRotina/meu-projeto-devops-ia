--- 
name: interface-de-usuário-básica
description: Valida a duração das animações, impõe a escala tipográfica, verifica a acessibilidade dos componentes e previne antipadrões de layout em projetos Tailwind CSS. Use ao criar componentes de interface do usuário, revisar utilitários CSS, estilizar views React ou garantir consistência de design.
risk: desconhecido
source: comunidade
---

# Baseline UI

Impõe uma linha de base de interface do usuário bem definida para evitar erros de interface gerados por IA.

## Quando usar
- Você está criando ou revisando uma interface do usuário baseada em Tailwind e deseja uma linha de base rigorosa para acessibilidade, movimento, tipografia e layout.

- O objetivo é evitar decisões genéricas ou imprecisas de interface geradas por IA antes que se espalhem pelo código.

- Você precisa de restrições concretas de interface do usuário para aplicar a uma revisão de arquivos ou a uma implementação de frontend em andamento.

## Como usar

- `/baseline-ui`

Aplique essas restrições a qualquer trabalho de interface do usuário nesta conversa.

- `/baseline-ui <arquivo>`

Analise o arquivo em relação a todas as restrições abaixo e apresente:

- violações (cite a linha/trecho exato)

- por que isso é importante (uma frase curta)

- uma solução concreta (sugestão em nível de código)

## Pilha

- DEVE usar os valores padrão do Tailwind CSS, a menos que valores personalizados já existam ou sejam explicitamente solicitados
- DEVE usar `motion/react` (anteriormente `framer-motion`) quando animação em JavaScript for necessária
- DEVE usar `tw-animate-css` para animações de entrada e microanimações no Tailwind CSS
- DEVE usar o utilitário `cn` (`clsx` + `tailwind-merge`) para lógica de classe

## Componentes

- DEVE usar componentes primitivos acessíveis para qualquer coisa com comportamento de teclado ou foco (`Base UI`, `React Aria`, `Radix`)
- DEVE usar os componentes primitivos existentes do projeto primeiro
- NUNCA misture sistemas de componentes primitivos na mesma superfície de interação
- DEVE preferir [`Base UI](https://base-ui.com/react/components) para novos elementos primitivos, se compatíveis com a pilha
- DEVE adicionar um `aria-label` a botões que contenham apenas ícones
- NUNCA reconstrua o comportamento do teclado ou do foco manualmente, a menos que seja explicitamente solicitado

## Interação

- DEVE usar um `AlertDialog` para ações destrutivas ou irreversíveis
- DEVE usar esqueletos estruturais para estados de carregamento
- NUNCA use `h-screen`, use `h-dvh`
- DEVE respeitar `safe-area-inset` para elementos fixos
- DEVE mostrar erros próximos ao local onde a ação ocorre
- NUNCA impeça a colagem em elementos `input` ou `textarea`

## Animação

- NUNCA adicione animação, a menos que seja explicitamente solicitado
- DEVE animar apenas as propriedades do compositor (`transform`, `opacity`)
- NUNCA anime propriedades de layout (`width`, `height`, `top`, `left`, `margin`, `padding`)
- DEVE evitar animar propriedades de pintura (`background`, `color`), exceto para interfaces de usuário pequenas e locais (texto, ícones)
- DEVE usar `ease-out` na entrada
- NUNCA exceda `200ms` para feedback de interação
- DEVE pausar animações em loop quando fora da tela
- DEVE respeitar `prefers-reduced-motion`
- NUNCA introduza curvas de suavização personalizadas, a menos que seja explicitamente solicitado
- DEVE evitar animar imagens grandes ou superfícies em tela cheia

## Tipografia

- DEVE usar `text-balance` para títulos e `text-pretty` para corpo/parágrafos
- DEVE usar `tabular-nums` para dados
- DEVE usar `truncate` ou `line-clamp` para interfaces de usuário densas
- NUNCA modifique o `letter-spacing` (`tracking-*`), a menos que seja explicitamente solicitado

## Layout

- DEVE usar uma escala `z-index` fixa (sem valores arbitrários) `z-*`)
- DEVE-SE usar `size-*` para elementos quadrados em vez de `w-*` + `h-*`

## Desempenho

- NUNCA anime superfícies grandes com `blur()` ou `backdrop-filter`
- NUNCA aplique `will-change` fora de uma animação ativa
- NUNCA use `useEffect` para qualquer coisa que possa ser expressa como lógica de renderização

## Design

- NUNCA use gradientes, a menos que seja explicitamente solicitado
- NUNCA use gradientes roxos ou multicoloridos
- NUNCA use efeitos de brilho como affordances principais
- DEVE-SE usar a escala de sombra padrão do Tailwind CSS, a menos que seja explicitamente solicitado
- DEVE-SE dar aos estados vazios uma próxima ação clara
- DEVE-SE limitar o uso de cores de destaque a uma por visualização
- DEVE-SE usar o tema existente ou os tokens de cor do Tailwind CSS antes de introduzir novos

## Limitações

- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não trate a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente. - Pare e peça esclarecimentos se faltarem informações necessárias, permissões, limites de segurança ou critérios de sucesso.