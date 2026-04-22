# Guia de Referência de Animações

> Princípios de animação e psicologia do tempo — aprenda a **decidir**, não a copiar.
> **Não há durações fixas para decorar — entenda o que influencia o timing.**

---

## 1. Princípios de Duração

### O que Afeta o Tempo da Animação

```
Fatores que determinam a velocidade da animação:
├── DISTÂNCIA: Quanto maior o deslocamento, maior a duração
├── TAMANHO: Elementos maiores = animações mais lentas
├── COMPLEXIDADE: Quanto mais complexo, mais lento de processar
├── IMPORTÂNCIA: Ações críticas exigem feedback claro
└── CONTEXTO: Urgente = rápido, luxuoso = lento
```

### Faixas de Duração por Objetivo

| Objetivo                  | Faixa     | Por quê                                  |
| ------------------------- | --------- | ---------------------------------------- |
| Feedback instantâneo      | 50–100ms  | Abaixo do limiar de percepção            |
| Microinterações           | 100–200ms | Rápido, mas perceptível                  |
| Transições padrão         | 200–300ms | Ritmo confortável                        |
| Animações complexas       | 300–500ms | Tempo para acompanhar                    |
| Transições de página      | 400–600ms | Transição suave                          |
| **Efeitos Wow / Premium** | 800ms+    | Dramático, orgânico, com molas e camadas |

### Como Escolher a Duração

Pergunte a si mesmo:

1. Quão longe o elemento está se movendo?
2. O quanto é importante que o usuário perceba essa mudança?
3. O usuário está esperando ou isso ocorre em segundo plano?

---

## 2. Princípios de Easing (Curvas de Animação)

### O que o Easing Faz

```
Easing = como a velocidade muda ao longo do tempo
├── Linear: velocidade constante (mecânico, robótico)
├── Ease-out: início rápido, fim lento (entrada natural)
├── Ease-in: início lento, fim rápido (saída natural)
└── Ease-in-out: lento no início e no fim (suave, deliberado)
```

### Quando Usar Cada Um

| Easing               | Melhor Uso         | Sensação              |
| -------------------- | ------------------ | --------------------- |
| **Ease-out**         | Elementos entrando | Chegando, assentando  |
| **Ease-in**          | Elementos saindo   | Partindo, saindo      |
| **Ease-in-out**      | Ênfase, loops      | Suave, intencional    |
| **Linear**           | Movimento contínuo | Mecânico              |
| **Bounce / Elastic** | UI lúdica          | Divertido, energético |

### Padrão de Uso

```css
/* Entrada na tela = ease-out (desacelera) */
.enter {
  animation-timing-function: ease-out;
}

/* Saída da tela = ease-in (acelera) */
.exit {
  animation-timing-function: ease-in;
}

/* Movimento contínuo */
.continuous {
  animation-timing-function: ease-in-out;
}
```

---

## 3. Princípios de Microinterações

### O que Define Boas Microinterações

```
Objetivos das microinterações:
├── FEEDBACK: Confirmar que a ação ocorreu
├── ORIENTAÇÃO: Mostrar o que é possível fazer
├── STATUS: Indicar o estado atual
└── ENCANTO: Pequenos momentos de prazer
```

### Estados de Botões

```
Hover → leve mudança visual (elevação, cor, escala)
Active → sensação de pressionado (reduzir escala, sombra)
Focus → indicador claro (outline, anel)
Loading → indicador de progresso (spinner, skeleton)
Success → confirmação (check, mudança de cor)
```

### Princípios

1. **Responder imediatamente** (abaixo de 100ms)
2. **Combinar com a ação**
   (pressionar = `scale(0.95)`, hover = `translateY(-4px) + brilho`)
3. **Ser marcante, mas suave**
4. **Ser consistente** (mesma ação = mesmo feedback)

---

## 4. Princípios de Estados de Carregamento

### Tipos por Contexto

| Situação                  | Abordagem                      |
| ------------------------- | ------------------------------ |
| Carregamento rápido (<1s) | Nenhum indicador               |
| Médio (1–3s)              | Spinner ou animação simples    |
| Longo (3s+)               | Barra de progresso ou skeleton |
| Duração desconhecida      | Indicador indeterminado        |

### Skeleton Screens

```
Objetivo: Reduzir o tempo percebido
├── Mostrar o layout imediatamente
├── Animar de forma sutil (shimmer, pulso)
├── Substituir pelo conteúdo real
└── Parece mais rápido que spinner
```

### Indicadores de Progresso

```
Quando usar:
├── Ações iniciadas pelo usuário
├── Uploads / downloads
├── Processos em múltiplas etapas
└── Operações longas

Quando NÃO usar:
├── Operações muito rápidas
├── Tarefas em background
└── Carregamento inicial (skeleton é melhor)
```

---

## 5. Princípios de Transição de Página

### Estratégia de Transição

```
Regra simples: saída rápida, entrada mais lenta
├── Conteúdo atual some rapidamente
├── Novo conteúdo entra animado
└── Evita “tudo se mexendo ao mesmo tempo”
```

### Padrões Comuns

| Padrão                     | Quando Usar                   |
| -------------------------- | ----------------------------- |
| **Fade**                   | Seguro, funciona em tudo      |
| **Slide**                  | Navegação sequencial          |
| **Scale**                  | Abertura/fechamento de modais |
| **Elemento compartilhado** | Continuidade visual           |

### Direção Coerente

```
Direção da navegação = direção da animação
├── Avançar → desliza da direita
├── Voltar → desliza da esquerda
├── Aprofundar → escala do centro
├── Retornar → reduz escala
```

---

## 6. Princípios de Animações no Scroll

### Revelação Progressiva

```
Conteúdo aparece conforme o scroll:
├── Reduz carga cognitiva inicial
├── Recompensa exploração
├── Não pode parecer lento
└── Deve poder ser desativado (acessibilidade)
```

### Pontos de Disparo

| Momento              | Efeito               |
| -------------------- | -------------------- |
| Entrando no viewport | Revelação padrão     |
| Centralizado         | Ênfase               |
| Parcialmente visível | Revelação antecipada |
| Totalmente visível   | Disparo tardio       |

### Propriedades Comuns

* Fade-in (opacity)
* Slide-up (transform)
* Scale (transform)
* Combinação das anteriores

### Performance

* Use Intersection Observer
* Anime apenas transform e opacity
* Reduza efeitos no mobile se necessário

---

## 7. Princípios de Efeitos de Hover

### Efeito de Acordo com a Ação

| Elemento      | Efeito                | Intenção            |
| ------------- | --------------------- | ------------------- |
| Card clicável | Elevação + sombra     | “Isso é interativo” |
| Botão         | Mudança de cor/brilho | “Clique aqui”       |
| Imagem        | Zoom / scale          | “Ver mais de perto” |
| Link          | Sublinhado/cor        | “Navegar”           |

### Princípios

1. **Sinalizar interatividade**
2. **Não exagerar**
3. **Combinar com a importância**
4. **Pensar em alternativas para touch**

---

## 8. Princípios de Animações de Feedback

### Estados de Sucesso

```
Celebrar na medida certa:
├── Ação pequena → feedback sutil
├── Ação grande → animação mais visível
├── Conclusão → animação satisfatória
└── Alinhado à personalidade da marca
```

### Estados de Erro

```
Chamar atenção sem causar pânico:
├── Mudança de cor (vermelho semântico)
├── Animação de shake (curta!)
├── Foco no campo com erro
└── Mensagem clara
```

### Timing

* Sucesso: um pouco mais longo
* Erro: rápido
* Loading: contínuo até finalizar

---

## 9. Princípios de Performance

### O que é Barato de Animar

```
Acelerado por GPU (RÁPIDO):
├── transform (translate, scale, rotate)
└── opacity

Custoso (CPU):
├── width, height
├── top, left, right, bottom
├── margin, padding
├── border-radius
└── box-shadow
```

### Estratégias de Otimização

1. Priorize `transform` e `opacity`
2. Evite mudanças de layout
3. Use `will-change` com cautela
4. Teste em dispositivos fracos

### Respeitando Preferências do Usuário

```css
@media (prefers-reduced-motion: reduce) {
  /* Respeite essa preferência */
  /* Apenas animações essenciais */
}
```

---

## 10. Checklist de Decisão de Animação

Antes de adicionar uma animação:

* [ ] **Existe um propósito?** (feedback/orientação/encanto)
* [ ] **O timing está adequado?**
* [ ] **O easing está correto?**
* [ ] **É performático?**
* [ ] **Respeita reduced-motion?**
* [ ] **É consistente com o restante do sistema?**
* [ ] **Não é sempre o mesmo padrão?**
* [ ] **O estilo foi alinhado com o usuário?**

### Anti-Padrões

* ❌ Usar os mesmos tempos em todo projeto
* ❌ Animação sem propósito
* ❌ Ignorar reduced-motion
* ❌ Animar propriedades caras
* ❌ Muitos elementos animando juntos
* ❌ Delays que irritam

---

> **Lembre-se:** animação é comunicação.
> Cada movimento deve ter significado e servir à experiência do usuário.
