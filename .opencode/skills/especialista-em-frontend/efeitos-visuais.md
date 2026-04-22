# Referência de Efeitos Visuais

> Princípios e técnicas modernas de efeitos em CSS — aprenda os **conceitos**, crie variações.
> **Sem valores fixos para copiar — entenda os padrões.**

---

## 1. Princípios de Glassmorphism

### O Que Faz o Glassmorphism Funcionar

```
Propriedades-chave:
├── Fundo semitransparente (não sólido)
├── Desfoque do fundo (efeito de vidro fosco)
├── Borda sutil (para definição)
└── Geralmente: sombra leve para profundidade
```

### O Padrão (Personalize os Valores)

```css
.glass {
  /* Transparência: ajuste a opacidade conforme a legibilidade do conteúdo */
  background: rgba(R, G, B, OPACITY);
  /* OPACITY: 0.1–0.3 para fundo escuro, 0.5–0.8 para fundo claro */
  
  /* Blur: quanto maior, mais fosco */
  backdrop-filter: blur(AMOUNT);
  /* AMOUNT: 8–12px sutil, 16–24px forte */
  
  /* Borda: define os limites */
  border: 1px solid rgba(255, 255, 255, OPACITY);
  /* OPACITY: normalmente 0.1–0.3 */
  
  /* Raio: deve seguir seu design system */
  border-radius: YOUR_RADIUS;
}
```

### Quando Usar Glassmorphism

* ✅ Sobre fundos coloridos ou com imagens
* ✅ Modais, overlays, cards
* ✅ Barras de navegação com conteúdo rolando por trás
* ❌ Conteúdo com muito texto (problemas de legibilidade)
* ❌ Fundos sólidos simples (sem propósito)

### Quando **NÃO** Usar

* Situações de baixo contraste
* Conteúdo crítico para acessibilidade
* Dispositivos com limitações de performance

---

## 2. Princípios de Neomorphism

### O Que Faz o Neomorphism Funcionar

```
Conceito-chave: Elementos suaves e “extrudados” usando SOMBRAS DUPLAS
├── Sombra clara (direção da luz)
├── Sombra escura (direção oposta)
└── Fundo igual ao ambiente (mesma cor)
```

### O Padrão

```css
.neo-raised {
  /* O fundo DEVE ser igual ao do elemento pai */
  background: SAME_AS_PARENT;
  
  /* Duas sombras: clara + escura */
  box-shadow: 
    OFFSET OFFSET BLUR rgba(light-color),
    -OFFSET -OFFSET BLUR rgba(dark-color);
  
  /* OFFSET: normalmente 6–12px */
  /* BLUR: normalmente 12–20px */
}

.neo-pressed {
  /* inset cria o efeito “pressionado” */
  box-shadow: 
    inset OFFSET OFFSET BLUR rgba(dark-color),
    inset -OFFSET -OFFSET BLUR rgba(light-color);
}
```

### Alerta de Acessibilidade

⚠️ **Baixo contraste** — use com moderação e garanta limites visuais claros.

### Quando Usar

* Elementos decorativos
* Estados sutis de interação
* Interfaces minimalistas com cores planas

---

## 3. Princípios de Hierarquia de Sombras

### Conceito: Sombras Indicam Elevação

```
Maior elevação = sombra maior
├── Nível 0: Sem sombra (plano)
├── Nível 1: Sombra sutil (levemente elevado)
├── Nível 2: Sombra média (cards, botões)
├── Nível 3: Sombra grande (modais, dropdowns)
└── Nível 4: Sombra profunda (elementos flutuantes)
```

### Propriedades de Sombra para Ajustar

```css
box-shadow: OFFSET-X OFFSET-Y BLUR SPREAD COLOR;

/* Offset: direção da sombra */
/* Blur: suavidade (maior = mais suave) */
/* Spread: expansão do tamanho */
/* Cor: normalmente preto com baixa opacidade */
```

### Princípios para Sombras Naturais

1. **Offset em Y maior que em X** (luz vem de cima)
2. **Baixa opacidade** (5–15% sutil, 15–25% mais forte)
3. **Múltiplas camadas** para realismo (ambiente + direta)
4. **Blur escala com o offset** (offset maior = blur maior)

### Sombras em Dark Mode

* Menos visíveis em fundos escuros
* Pode ser necessário aumentar a opacidade
* Ou usar brilho/highlight no lugar

---

## 4. Princípios de Gradientes

### Tipos e Quando Usar

| Tipo       | Padrão                     | Uso                         |
| ---------- | -------------------------- | --------------------------- |
| **Linear** | Cor A → Cor B em uma linha | Fundos, botões, headers     |
| **Radial** | Centro → exterior          | Destaques, pontos focais    |
| **Cônico** | Ao redor do centro         | Gráficos, efeitos criativos |

### Criando Gradientes Harmoniosos

```
Regras de bons gradientes:
├── Use cores ADJACENTES no círculo cromático
├── Ou mesma matiz com luminosidade diferente
├── Evite complementares (podem ficar agressivos)
└── Adicione paradas intermediárias para suavizar
```

### Padrão de Sintaxe

```css
.gradient {
  background: linear-gradient(
    DIRECTION,           /* ângulo ou palavra-chave */
    COLOR-STOP-1,        /* cor + posição opcional */
    COLOR-STOP-2
    /* ... mais paradas */
  );
}

/* Exemplos de DIRECTION */
/* 90deg, 135deg, to right, to bottom right */
```

### Mesh Gradients

```
Vários gradientes radiais sobrepostos:
├── Cada um em uma posição diferente
├── Com transição para transparente
├── **Essencial para efeito “WOW” em Hero sections**
└── Efeito orgânico e colorido (pesquise: "Aurora Gradient CSS")
```

---

## 5. Princípios de Efeitos de Borda

### Bordas com Gradiente

```
Técnica: Pseudo-elemento com fundo em gradiente
├── Elemento tem padding = largura da borda
├── Pseudo-elemento preenche com gradiente
└── Mask ou clip cria o efeito de borda
```

### Bordas Animadas

```
Técnica: Gradiente rotativo ou varredura cônica
├── Pseudo-elemento maior que o conteúdo
├── Animação gira o gradiente
└── Overflow hidden recorta no formato
```

### Bordas com Glow

```css
/* Múltiplos box-shadows criam o brilho */
box-shadow:
  0 0 SMALL-BLUR COLOR,
  0 0 MEDIUM-BLUR COLOR,
  0 0 LARGE-BLUR COLOR;

/* Cada camada intensifica o glow */
```

---

## 6. Princípios de Glow (Brilho)

### Glow em Texto

```css
text-shadow: 
  0 0 BLUR-1 COLOR,
  0 0 BLUR-2 COLOR,
  0 0 BLUR-3 COLOR;

/* Múltiplas camadas = brilho mais forte */
/* Blur maior = espalhamento mais suave */
```

### Glow em Elementos

```css
box-shadow:
  0 0 BLUR-1 COLOR,
  0 0 BLUR-2 COLOR;

/* Use cor próxima ao elemento */
/* Opacidade baixa = sutil, alta = neon */
```

### Animação de Glow Pulsante

```css
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 SMALL-BLUR COLOR; }
  50% { box-shadow: 0 0 LARGE-BLUR COLOR; }
}

/* Easing e duração mudam a sensação */
```

---

## 7. Técnicas de Overlay

### Overlay em Gradiente sobre Imagens

```
Objetivo: Melhorar legibilidade do texto
Padrão: Gradiente de transparente para opaco
Posição: Onde o texto aparece
```

```css
.overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    DIRECTION,
    transparent PERCENTAGE,
    rgba(0,0,0,OPACITY) 100%
  );
}
```

### Overlay Colorido

```css
/* Modo blend ou camadas */
background:
  linear-gradient(YOUR-COLOR-WITH-OPACITY),
  url('image.jpg');
```

---

## 8. Técnicas Modernas de CSS

### Container Queries (Conceito)

```
Em vez de breakpoints da viewport:
├── O componente reage ao SEU container
├── Componentes realmente modulares
└── Sintaxe: @container (condição) { }
```

### Seletor :has() (Conceito)

```
Estilizar o pai com base nos filhos:
├── “Pai que TEM um filho X”
├── Habilita padrões antes impossíveis
└── Use como progressive enhancement
```

### Animações Guiadas por Scroll (Conceito)

```
Progresso da animação ligado ao scroll:
├── Animações de entrada/saída
├── Efeito parallax
├── Indicadores de progresso
└── Timeline baseada em scroll ou viewport
```

---

## 9. Princípios de Performance

### Propriedades Aceleradas por GPU

```
BARATAS de animar (GPU):
├── transform (translate, scale, rotate)
└── opacity

CARAS de animar (CPU):
├── width, height
├── top, left, right, bottom
├── margin, padding
└── box-shadow (recalcula)
```

### Uso de will-change

```css
/* Use com cautela, apenas em animações pesadas */
.heavy-animation {
  will-change: transform;
}

/* Remova após a animação, se possível */
```

### Movimento Reduzido

```css
@media (prefers-reduced-motion: reduce) {
  /* Desative ou reduza animações */
  /* Respeite a preferência do usuário */
}
```

---

## 10. Checklist de Seleção de Efeitos

Antes de aplicar qualquer efeito:

* [ ] **Serve a um propósito?** (não é só decoração)
* [ ] **É adequado ao contexto?** (marca, público)
* [ ] **Evita repetição de projetos anteriores?**
* [ ] **É acessível?** (contraste, sensibilidade a movimento)
* [ ] **É performático?** (especialmente no mobile)
* [ ] **Considerou a preferência do usuário?**

### Anti-Patterns

* ❌ Glassmorphism em tudo (kitsch)
* ❌ Dark + neon como padrão (visual preguiçoso de IA)
* ❌ **Design estático/flat sem profundidade (REPROVADO)**
* ❌ Efeitos que prejudicam a leitura
* ❌ Animações sem propósito

---

> **Lembre-se:** Efeitos reforçam significado. Escolha com base em propósito e contexto — não só porque “fica bonito”.
