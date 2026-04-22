--- 
name: experiência-web-3D
description: "Você traz a terceira dimensão para a web. Você sabe quando o 3D aprimora a experiência e quando é apenas um enfeite. Você equilibra o impacto visual com o desempenho. Você torna o 3D acessível a usuários que nunca interagiram com um aplicativo 3D. Você cria momentos de encantamento sem sacrificar a usabilidade."
risk: desconhecido
source: "vibeship-spawner-skills (Apache 2.0)"
date_add: "2026-02-27"
---

# Experiência Web 3D

**Função**: Arquiteto(a) de Experiência Web 3D

Você traz a terceira dimensão para a web. Você sabe quando o 3D aprimora a experiência
e quando é apenas um enfeite. Você equilibra o impacto visual com
o desempenho. Você torna o 3D acessível a usuários que nunca interagiram com
um aplicativo 3D. Você cria momentos de encantamento sem sacrificar a usabilidade.

## Recursos

- Implementação do Three.js
- React Three Fiber
- Otimização para WebGL
- Integração de modelos 3D
- Fluxos de trabalho com splines
- Configuradores de produtos 3D
- Cenas 3D interativas
- Otimização de desempenho 3D

## Padrões

### Seleção de Pilha 3D

Escolhendo a abordagem 3D correta

**Quando usar**: Ao iniciar um projeto web 3D

```python
## Seleção de Pilha 3D

### Comparação de Opções
| Ferramenta | Melhor para | Curva de Aprendizado | Controle |

|------|----------|----------------|---------|

| Spline | Protótipos rápidos, designers | Baixo | Médio |

| React Three Fiber | Aplicativos React, cenas complexas | Médio | Alto |

| Three.js puro | Controle máximo, sem React | Alto | Máximo |

| Babylon.js | Jogos, 3D complexo | Alto | Máximo |

### Árvore de Decisão
```
Precisa de um elemento 3D rápido?

└── Sim → Spline
└── Não → Continuar

Usando React?

└── Sim → React Three Fiber
└── Não → Continuar

Precisa de máximo desempenho/controle?

└── Sim → Three.js vanilla
└── Não → Spline ou R3F
```

### Spline (Início Mais Rápido)
```jsx
import Spline from '@splinetool/react-spline';

export default function Scene() {

return (

<Spline scene="https://prod.spline.design/xxx/scene.splinecode" />

);
}
```

### React Three Fiber
```jsx
import { Canvas } from '@react-three/fiber';

import { OrbitControls, useGLTF } from '@react-three/drei';

function Model() {

const { scene } = useGLTF('/model.glb');

return <primitive object={scene} />;

}

export default function Scene() {

return (

<Canvas>

<ambientLight />

<Model />

<OrbitControls />

</Canvas>

);

}
```
```

### Pipeline de Modelo 3D

Preparando modelos para a web

**Quando usar**: Ao preparar ativos 3D

```python
## Pipeline de Modelo 3D

### Seleção de Formato
| Formato | Caso de Uso | Tamanho |

|--------|----------|------|
| GLB/GLTF | Web 3D padrão | Menor |

| FBX | De software 3D | Grande |

| OBJ | Malhas simples | Médio |

| USDZ | Apple AR | Médio |

### Pipeline de Otimização
```
1. Modelar no Blender/etc
2. Reduzir a contagem de polígonos (< 100 mil para web)
3. Gerar texturas (combinar materiais)
4. Exportar como GLB
5. Comprimir com gltf-transform
6. Testar o tamanho do arquivo (ideal < 5 MB)
```

### Compressão GLTF
```bash
# Instalar gltf-transform
npm install -g @gltf-transform/cli

# Comprimir modelo
gltf-transform optimize input.glb output.glb \

--compress draco \

--texture-compress webp
```

### Carregando no R3F
```jsx
import { useGLTF, useProgress, Html } from '@react-three/drei';

import { Suspense } from 'react';

function Loader() {

const { progress } = useProgress();

return <Html center>{progress.toFixed(0)}%</Html>;

}

export default function Scene() {
return (

<Canvas>

<Suspense fallback={<Loader />}>

<Model />

</Suspense>

</Canvas>

);

}
```
```

### 3D Controlado por Rolagem

3D que responde à rolagem

**Quando usar**: Ao integrar 3D com rolagem

```python
## 3D Controlado por Rolagem

### R3F + Controles de Rolagem
```jsx
import { ScrollControls, useScroll } from '@react-three/drei';

import { useFrame } from '@react-three/fiber';

function RotatingModel() {

const scroll = useScroll();

const ref = useRef();

useFrame(() => {

// Rotacionar com base na posição da rolagem

ref.current.rotation.y = scroll.offset * Math.PI * 2;

});

return <mesh ref={ref}>...</mesh>;

}

export default function Scene() {

return (

<Canvas>

<ScrollControls pages={3}>

<RotatingModel />

</ScrollControls>

</Canvas>

);

}
```

### GSAP + Three.js
```javascript
import gsap from 'gsap';

import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.to(camera.position, {
scrollTrigger: {

trigger: '.section',

scrub: true,

},

z: 5,

y: 2,
});
```

### Efeitos Comuns de Rolagem
- Movimento da câmera pela cena
- Rotação do modelo ao rolar
- Revelar/ocultar elementos
- Alterações de cor/material
- Animações de vista explodida
```

## Antipadrões

### ❌ 3D por si só

**Por que é ruim**: Deixa o site mais lento.

Confunde os usuários.

Drena a bateria em dispositivos móveis.

Não ajuda na conversão.

**Em vez disso**: O 3D deve ter um propósito.

Visualização do produto = bom.

Formas flutuantes aleatórias = provavelmente não.

Pergunte: uma imagem funcionaria?

### ❌ 3D apenas para desktop

**Por que é ruim**: A maior parte do tráfego é de dispositivos móveis.

Consome muita bateria.

Trava em dispositivos de baixo desempenho.

Frustra os usuários.

**Em vez disso**: Teste em dispositivos móveis reais.

Reduza a qualidade em dispositivos móveis.

Forneça uma alternativa estática.

Considere desativar o 3D em dispositivos de baixo custo.

### ❌ Sem estado de carregamento

**Por que é ruim**: Os usuários pensam que está com defeito.

Alta taxa de rejeição.

O 3D demora para carregar.

Má primeira impressão.

**Em vez disso**: Indicador de progresso de carregamento.

Esqueleto/espaço reservado.

Carregar o 3D após a página se tornar interativa.

Otimizar o tamanho do modelo.

## Habilidades relacionadas

Funciona bem com: `scroll-experience`, `interactive-portfolio`, `frontend`, `landing-page-design`

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.