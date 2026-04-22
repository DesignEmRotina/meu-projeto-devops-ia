# Referência de Motion Graphics

> Técnicas avançadas de animação para experiências web premium — Lottie, GSAP, SVG, 3D, Partículas.
> **Aprenda os princípios, crie efeitos WOW.**

---

## 1. Animações Lottie

### O que é Lottie?

```
Animações vetoriais baseadas em JSON:
├── Exportadas do After Effects via Bodymovin
├── Leves (menores que GIF/vídeo)
├── Escaláveis (vetoriais, sem pixelização)
├── Interativas (controle de playback e segmentos)
└── Multiplataforma (web, iOS, Android, React Native)
```

### Quando Usar Lottie

| Caso de Uso                       | Por que Lottie?                         |
| --------------------------------- | --------------------------------------- |
| **Animações de loading**          | Personalizadas, suaves e leves          |
| **Estados vazios (empty states)** | Ilustrações envolventes                 |
| **Fluxos de onboarding**          | Animações complexas em múltiplas etapas |
| **Feedback de sucesso/erro**      | Microinterações agradáveis              |
| **Ícones animados**               | Consistência entre plataformas          |

### Princípios

* Mantenha o tamanho do arquivo abaixo de **100KB** para performance
* Use loop com moderação (evite distrações)
* Ofereça fallback estático para `prefers-reduced-motion`
* Faça lazy load dos arquivos de animação sempre que possível

### Fontes

* **LottieFiles.com** (biblioteca gratuita)
* **After Effects + Bodymovin** (animações customizadas)
* **Plugins do Figma** (exportação direta do design)

---

## 2. GSAP (GreenSock)

### O que Torna o GSAP Diferente

```
Animação profissional baseada em timelines:
├── Controle preciso de sequências
├── ScrollTrigger para animações baseadas em scroll
├── MorphSVG para transições de formas
├── Easing com física realista
└── Funciona com qualquer elemento do DOM
```

### Conceitos Fundamentais

| Conceito          | Finalidade                             |
| ----------------- | -------------------------------------- |
| **Tween**         | Animação simples de A → B              |
| **Timeline**      | Sequência ou sobreposição de animações |
| **ScrollTrigger** | Scroll controla a execução             |
| **Stagger**       | Efeito em cascata entre elementos      |

### Quando Usar GSAP

* ✅ Animações complexas e sequenciais
* ✅ Animações acionadas por scroll
* ✅ Necessidade de controle preciso de timing
* ✅ Efeitos de morph em SVG
* ❌ Hover/focus simples (prefira CSS)
* ❌ Mobile crítico em performance (biblioteca mais pesada)

### Princípios

* Use **timeline** para orquestração (não tweens isolados)
* Delay de stagger: **0.05–0.15s** entre itens
* ScrollTrigger: iniciar entre **70–80%** da entrada no viewport
* Finalize animações no unmount (evita memory leaks)

---

## 3. Animações SVG

### Tipos de Animação SVG

| Tipo                 | Técnica                  | Caso de Uso         |
| -------------------- | ------------------------ | ------------------- |
| **Desenho de linha** | stroke-dashoffset        | Logos, assinaturas  |
| **Morph**            | Interpolação de paths    | Transição de ícones |
| **Transformação**    | rotate, scale, translate | Ícones interativos  |
| **Cor**              | Transição de fill/stroke | Mudança de estado   |

### Princípio do Line Drawing

```
Como funciona o stroke-dashoffset:
├── Definir dasharray com o tamanho do path
├── Definir dashoffset igual ao dasharray (oculto)
├── Animar dashoffset até 0 (revela)
└── Cria efeito de "desenho"
```

### Quando Usar Animações SVG

* ✅ Revelação de logos e momentos de marca
* ✅ Transições de estado (hamburger ↔ X)
* ✅ Infográficos e visualização de dados
* ✅ Ilustrações interativas
* ❌ Conteúdo fotorrealista (use vídeo)
* ❌ Cenas muito complexas (performance)

### Princípios

* Calcule o tamanho do path dinamicamente
* Duração: **1–3s** para desenhos completos
* Easing: **ease-out** para sensação natural
* Fills simples complementam, não competem

---

## 4. Transformações 3D com CSS

### Propriedades Essenciais

```
Espaço 3D no CSS:
├── perspective: profundidade do campo 3D (500–1500px)
├── transform-style: preserve-3d
├── rotateX/Y/Z: rotação por eixo
├── translateZ: aproxima/afasta do observador
└── backface-visibility: exibir ou ocultar verso
```

### Padrões Comuns

| Padrão                  | Caso de Uso            |
| ----------------------- | ---------------------- |
| **Flip de card**        | Revelações, flashcards |
| **Inclinação no hover** | Cards interativos      |
| **Camadas parallax**    | Hero sections          |
| **Carrossel 3D**        | Galerias e sliders     |

### Princípios

* Perspectiva: **800–1200px** (sutil), **400–600px** (dramático)
* Mantenha transformações simples
* Use `backface-visibility: hidden`
* Teste no Safari (renderização diferente)

---

## 5. Efeitos de Partículas

### Tipos de Sistemas de Partículas

| Tipo             | Sensação    | Uso              |
| ---------------- | ----------- | ---------------- |
| **Geométrico**   | Tech        | SaaS, tecnologia |
| **Confete**      | Celebração  | Sucesso          |
| **Neve/Chuva**   | Atmosfera   | Sazonal          |
| **Poeira/Bokeh** | Sofisticado | Luxo             |
| **Vagalumes**    | Mágico      | Jogos, fantasia  |

### Bibliotecas

| Biblioteca       | Melhor Para             |
| ---------------- | ----------------------- |
| **tsParticles**  | Configurável e leve     |
| **particles.js** | Fundos simples          |
| **Canvas API**   | Total controle          |
| **Three.js**     | Partículas 3D complexas |

### Princípios

* Padrão: **30–50 partículas**
* Movimento lento e orgânico (velocidade 0.5–2)
* Opacidade: **0.3–0.6**
* Conexões sutis para efeito de rede
* ⚠️ Reduza ou desative em mobile

### Quando Usar

* ✅ Fundos atmosféricos
* ✅ Celebrações de sucesso
* ✅ Visualizações tecnológicas
* ❌ Páginas com muito conteúdo
* ❌ Dispositivos fracos (bateria)

---

## 6. Animações Baseadas em Scroll

### CSS Nativo (Moderno)

```
Scroll Timelines no CSS:
├── animation-timeline: scroll()
├── animation-timeline: view()
├── animation-range: pontos de entrada/saída
└── Sem JavaScript
```

### Princípios

| Ponto de Disparo | Uso               |
| ---------------- | ----------------- |
| **Entry 0%**     | Começo da entrada |
| **Entry 50%**    | Metade visível    |
| **Cover 50%**    | Centralizado      |
| **Exit 100%**    | Totalmente fora   |

### Boas Práticas

* Revelações: iniciar em ~25% de entrada
* Parallax: progresso contínuo
* Elementos sticky: usar cover range
* Testar performance de scroll

---

## 7. Princípios de Performance

### GPU vs CPU

```
BARATO (GPU):
├── transform
├── opacity
└── filter (com cuidado)

CARO (reflow):
├── width, height
├── top, left, right, bottom
├── padding, margin
└── box-shadow complexo
```

### Checklist de Otimização

* [ ] Animar apenas transform/opacity
* [ ] Usar `will-change` temporariamente
* [ ] Testar em dispositivos fracos
* [ ] Implementar `prefers-reduced-motion`
* [ ] Lazy load de bibliotecas
* [ ] Throttle em cálculos de scroll

---

## 8. Árvore de Decisão de Motion Graphics

```
Qual animação você precisa?
│
├── Animação complexa de marca?
│   └── Lottie
│
├── Sequência com scroll?
│   └── GSAP + ScrollTrigger
│
├── Logo ou ícone?
│   └── SVG
│
├── Efeito 3D interativo?
│   └── CSS 3D ou Three.js
│
├── Fundo atmosférico?
│   └── tsParticles ou Canvas
│
└── Entrada/hover simples?
    └── CSS ou Framer Motion
```

---

## 9. Anti-Padrões

| ❌ Evite                               | ✅ Prefira         |
| ------------------------------------- | ----------------- |
| Animar tudo ao mesmo tempo            | Sequenciar        |
| Biblioteca pesada para efeito simples | CSS primeiro      |
| Ignorar reduced-motion                | Sempre fallback   |
| Bloquear a main thread                | 60fps             |
| Mesmo efeito em todo projeto          | Alinhar à marca   |
| Efeitos complexos em mobile           | Feature detection |

---

## 10. Referência Rápida

| Efeito            | Ferramenta    | Performance |
| ----------------- | ------------- | ----------- |
| Loading           | CSS / Lottie  | Leve        |
| Reveal em cascata | GSAP / Framer | Média       |
| SVG draw          | CSS stroke    | Leve        |
| Flip 3D           | CSS           | Leve        |
| Partículas        | tsParticles   | Pesada      |
| Parallax          | GSAP          | Média       |
| Morph             | GSAP          | Média       |

---

> **Lembre-se**: motion graphics devem **amplificar**, não distrair.
> Toda animação precisa ter um **PROPÓSITO** — feedback, orientação, deleite ou storytelling.
