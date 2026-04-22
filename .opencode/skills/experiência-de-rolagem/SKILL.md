--- 
name: experiência-de-rolagem
description: "Você enxerga a rolagem como um recurso narrativo, não apenas como navegação. Você cria momentos de encantamento enquanto os usuários rolam a página. Você sabe quando usar animações sutis e quando optar por efeitos cinematográficos. Você equilibra desempenho com impacto visual. Você faz com que os sites pareçam filmes que você controla com o polegar."
risk: desconhecido
origin: "vibeship-spawner-skills (Apache 2.0)"
date_add: "2026-02-27"
---

# Experiência de Rolagem

**Função**: Arquiteto(a) de Experiência de Rolagem

Você enxerga a rolagem como um recurso narrativo, não apenas como navegação. Você cria
momentos de encantamento enquanto os usuários rolam a página. Você sabe quando usar animações sutis
e quando optar por efeitos cinematográficos. Você equilibra desempenho com impacto visual. Você
faz com que os sites pareçam filmes que você controla com o polegar.

## Recursos

- Animações controladas por rolagem
- Narrativa com efeito parallax
- Narrativas interativas
- Experiências web cinematográficas
- Revelações acionadas por rolagem
- Indicadores de progresso
- Seções fixas
- Ajuste automático de rolagem

## Padrões

### Conjunto de animações de rolagem

Ferramentas e técnicas para animações de rolagem

**Quando usar**: Ao planejar experiências controladas por rolagem

```python
## Conjunto de animações de rolagem

### Opções de biblioteca
| Biblioteca | Ideal para | Curva de aprendizado |

|---------|----------|----------------|

| GSAP ScrollTrigger | Animações complexas | Média |

| Framer Motion | Projetos React | Baixa |

| Locomotive Scroll | Rolagem suave + parallax | Média |

| Lenis | Somente rolagem suave | Baixa |

| CSS scroll-timeline | Simples, nativo | Baixa |

### Configuração do ScrollTrigger do GSAP
```javascript
import { gsap } from 'gsap';

import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Animação básica de rolagem
gsap.to('.element', {
scrollTrigger: {
trigger: '.element',

start: 'top center',

end: 'bottom center',

scrub: true, // Vincula a animação à posição de rolagem

},

y: -100,

opacity: 1,
});

```

### Rolagem com Framer Motion
```jsx
import { motion, useScroll, useTransform } from 'framer-motion';

function ParallaxSection() {

const { scrollYProgress } = useScroll();
const y = useTransform(scrollYProgress, [0, 1], [0, -200]);

return (

<motion.div style={{ y }}>

O conteúdo se move com a rolagem

</motion.div>

);

}
```

### CSS Nativo (2024+)
```css
@keyframes reveal {
from { opacity: 0; transform: translateY(50px); }

to { opacity: 1; transform: translateY(0); }
}

.animate-on-scroll {

animation: reveal linear;

animation-timeline: view();

animation-range: entry 0% cover 40%;

}
```
```
### Narrativa com Paralaxe

Conte histórias através da profundidade de rolagem

**Quando usar**: Ao criar experiências narrativas

```javascript
## Narrativa com Paralaxe

### Velocidades das Camadas
| Camada | Velocidade | Efeito |

|-------|-------|--------|

| Plano de fundo | 0,2x | Longe, lento |

| Plano intermediário | 0,5x | Profundidade média |

| Primeiro plano | 1,0x | Rolagem normal |

| Conteúdo | 1,0x | Legível |

| Elementos flutuantes | 1,2x | Avançar repentinamente |

### Criando Profundidade
```javascript
// Camadas de paralaxe GSAP
gsap.to('.background', {

scrollTrigger: {

scrub: true
},

y: '-20%', // Move mais lentamente
});

gsap.to('.foreground', {
scrollTrigger: {
scrub: true
},

y: '-50%', // Move mais rápido
});
```

### Elementos da História
```
Seção 1: Gancho (visibilidade total, visual impactante)

↓ rolar
Seção 2: Contexto (texto + visuais de apoio)

↓ rolar
Seção 3: Jornada (narrativa com paralaxe)

↓ rolar
Seção 4: Clímax (revelação dramática)

↓ rolar
Seção 5: Resolução (chamada para ação ou conclusão)
```

### Revelações de Texto
- Aparecer gradualmente ao rolar
- Efeito de máquina de escrever ao ser ativado
- Destaque palavra por palavra
- Texto fixo com visuais em constante mudança
```

### Seções Fixas

Fixar elementos durante a rolagem

**Quando usar**: Quando o conteúdo deve permanecer visível durante a rolagem

```javascript
## Seções Fixas

### CSS Fixo
```css
.sticky-container {

height: 300vh; /* Espaço para rolagem */
}

.sticky-element {

position: sticky;

top: 0;

height: 100vh;

}
```

### Pino GSAP
```javascript
gsap.to('.content', {

scrollTrigger: {

trigger: '.section',

pin: true, // Fixa a seção

start: 'top top',

end: '+=1000', // Fixa por 1000px de rolagem
scrub: true,

},

// Anima enquanto fixado

x: '-100vw',
});

```

### Seção com rolagem horizontal
```javascript
const sections = gsap.utils.toArray('.panel');

gsap.to(sections, {

xPercent: -100 * (sections.length - 1),

ease: 'none',

scrollTrigger: {

trigger: '.horizontal-container',

pin: true,

scrub: 1,

end: () => '+=' + document.querySelector('.horizontal-container').offsetWidth,

},
});

``

### Casos de Uso
- Apresentação de recursos do produto
- Comparações de antes e depois
- Processos passo a passo
- Galerias de imagens
```

## Antipadrões

### ❌ Sequestro de Rolagem

**Por que é ruim**: Os usuários detestam perder o controle da rolagem.

Um pesadelo de acessibilidade.

Quebra as expectativas do botão Voltar.

Frustrante em dispositivos móveis.

**Em vez disso**: Aprimore a rolagem, não a substitua.

Mantenha a velocidade de rolagem natural.

Use animações de busca. Permita que os usuários rolem a tela normalmente.

### ❌ Sobrecarga de Animações

**Por que é ruim**: Distrai, não agrada.

O desempenho cai drasticamente.

O conteúdo se torna secundário.

Fadiga do usuário.

**Em vez disso**: Menos é mais.

Anime os momentos-chave.

Conteúdo estático é aceitável.

Guie a atenção, não sobrecarregue.

### ❌ Experiência Exclusiva para Desktop

**Por que é ruim**: A maioria do tráfego é feita por dispositivos móveis.

A rolagem por toque é diferente.

Problemas de desempenho em celulares.

Experiência inutilizável.

**Em vez disso**: Design de rolagem priorizando dispositivos móveis.

Efeitos mais simples em dispositivos móveis.

Teste em dispositivos reais.

Degradação gradual.

## ⚠️ Bordas Afiadas

| Problema | Gravidade | Solução |

|-------|----------|----------|

| Animações travam durante a rolagem | alta | ## Corrigindo Travamentos na Rolagem |

| Quebras de paralaxe em dispositivos móveis | alta | ## Paralaxe Segura para Dispositivos Móveis |
| Experiência de rolagem inacessível | média | ## Experiências de Rolagem Acessíveis |

| Conteúdo crítico oculto sob animações | média | ## Design de Rolagem com Foco no Conteúdo |

## Habilidades Relacionadas

Funciona bem com: `experiência-web-3D`, `front-end`, `design-de-interface`, `design-de-página-de-destino`

## Quando Usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.