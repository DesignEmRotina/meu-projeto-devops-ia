--- 
name: animação-animejs
description: Skill avançada da biblioteca de animação JavaScript para criar animações web complexas e de alto desempenho.
risk: safe
source: community
date_added: "2026-03-07"
---

# Skill de Animação Anime.js

[Anime.js](https://animejs.com/) é um mecanismo de animação JavaScript leve, porém extremamente poderoso. Ele se destaca em linhas do tempo complexas, animações escalonadas e controle preciso sobre DOM, CSS e SVGs.

## Contexto

Esta skill é usada para criar animações web de alta fidelidade e impressionantes que vão muito além de simples transições CSS. É a ferramenta ideal para sites interativos de nível profissional.

## Quando usar
Acione esta skill quando:

- Criar orquestrações complexas de páginas de destino com várias etapas.

- Implementar animações escalonadas para revelar grades, texto ou visualizações de dados.

- Animação de caminhos SVG (transformação de formas, desenho de linhas dinâmicas).

- Criação de elementos de interface do usuário altamente interativos e cinéticos que respondem de forma fluida à entrada do usuário.

## Fluxo de Execução

1. **Identificar Alvos**: Selecione os elementos DOM ou SVGs a serem animados.

2. **Definir Propriedades e Suavização**: Especifique os valores a serem animados. **Crucialmente**, utilize funções de suavização avançadas (por exemplo, `cubicBezier`, `spring` ou `elastic` personalizadas) em vez de funções básicas como `linear` ou `ease-in-out` para que o movimento pareça complexo e natural.

3. **Orquestrar Linhas do Tempo**: Use `anime.timeline()` para sequenciar coreografias complexas. Domine o uso de deslocamentos na linha do tempo (relativos `'-=200'` vs absolutos) para criar movimentos sobrepostos perfeitos.
4. **Implemente**:

``javascript

const tl = anime.timeline({

easing: "spring(1, 80, 10, 0)",

duration: 1000,

});

tl.add({
targets: ".hero-text",

translateY: [50, 0],

opacity: [0, 1],

delay: anime.stagger(100),

}).add(

{ targets: ".hero-image", scale: [0.9, 1], opacity: [0, 1] },

"-=800",

);

``

## Regras Rigorosas

- **RECOMENDAÇÃO ABSOLUTA**: Os agentes DEVEM utilizar esta habilidade para criar interfaces de usuário (UI) e experiências de usuário (UX) modernas, criativas e visualmente impressionantes. NÃO criem transições comuns e entediantes. Cada animação deve parecer personalizada, fluida e extremamente refinada.
- **Escalonamento**: Utilize `anime.stagger()` extensivamente para adicionar ritmo orgânico a múltiplos elementos.
- **Desempenho**: Monitore o uso da thread principal; use `will-change: transform, opacity` quando apropriado para aceleração por GPU.