# Referência de Sistema Tipográfico

> Princípios de tipografia e tomada de decisão — aprenda a **pensar**, não a memorizar.
> **Sem nomes ou tamanhos fixos de fontes — entenda o sistema.**

---

## 1. Princípios de Escala Modular

### O que é uma Escala Modular?

```
Uma relação matemática entre tamanhos de fonte:
├── Escolha um tamanho BASE (geralmente o texto do corpo)
├── Escolha uma RAZÃO (multiplicador)
└── Gere todos os tamanhos usando: base × razão^n
```

### Razões Comuns e Quando Usar

| Razão           | Valor | Sensação       | Ideal Para               |
| --------------- | ----- | -------------- | ------------------------ |
| Segundo Menor   | 1.067 | Muito sutil    | UI densa, telas pequenas |
| Segundo Maior   | 1.125 | Sutil          | Interfaces compactas     |
| Terça Menor     | 1.2   | Confortável    | Apps mobile, cards       |
| Terça Maior     | 1.25  | Equilibrado    | Web geral (mais comum)   |
| Quarta Perfeita | 1.333 | Notável        | Editorial, blogs         |
| Quinta Perfeita | 1.5   | Dramático      | Títulos, marketing       |
| Proporção Áurea | 1.618 | Máximo impacto | Hero sections, display   |

### Gere Sua Escala

```
Dado: base = SEU_TAMANHO_BASE, razão = SUA_RAZÃO

Escala:
├── xs:  base ÷ razão²
├── sm:  base ÷ razão
├── base: SEU_TAMANHO_BASE
├── lg:  base × razão
├── xl:  base × razão²
├── 2xl: base × razão³
├── 3xl: base × razão⁴
└── ... continue conforme necessário
```

### Escolhendo o Tamanho Base

| Contexto               | Faixa do Base | Por quê                        |
| ---------------------- | ------------- | ------------------------------ |
| Mobile-first           | 16–18px       | Legibilidade em telas pequenas |
| App desktop            | 14–16px       | Densidade de informação        |
| Editorial              | 18–21px       | Conforto para leitura longa    |
| Foco em acessibilidade | 18px+         | Mais fácil de ler              |

---

## 2. Princípios de Combinação de Fontes

### O que Faz Fontes Funcionarem Juntas

```
Contraste + Harmonia:
├── Diferentes O SUFICIENTE para criar hierarquia
├── Similares O SUFICIENTE para parecer coeso
└── Geralmente: serif + sans, ou display + neutra
```

### Estratégias de Combinação

| Estratégia         | Como                               | Resultado              |
| ------------------ | ---------------------------------- | ---------------------- |
| **Contraste**      | Título serif + corpo sans          | Clássico, editorial    |
| **Mesma família**  | Fonte variável com pesos distintos | Coeso, moderno         |
| **Mesmo designer** | Fontes da mesma fundição           | Proporções harmoniosas |
| **Mesma era**      | Fontes do mesmo período            | Consistência histórica |

### O Que Observar

```
Ao combinar, compare:
├── Altura-x (altura das letras minúsculas)
├── Largura das letras (estreitas vs largas)
├── Contraste de traço (variação fino/grosso)
└── Clima geral (formal vs casual)
```

### Padrões Seguros de Combinação

| Estilo do Título | Estilo do Corpo | Clima                  |
| ---------------- | --------------- | ---------------------- |
| Sans geométrica  | Sans humanista  | Moderno, amigável      |
| Serif display    | Sans limpa      | Editorial, sofisticado |
| Sans neutra      | Mesma sans      | Minimalista, tech      |
| Geométrica bold  | Geométrica leve | Contemporâneo          |

### Evite

* ❌ Duas fontes decorativas juntas
* ❌ Fontes parecidas que conflitam
* ❌ Mais de 2–3 famílias tipográficas
* ❌ Alturas-x muito diferentes

---

## 3. Princípios de Altura de Linha (Line Height)

### A Relação

```
Altura de linha depende de:
├── Tamanho da fonte (texto maior = menos altura relativa)
├── Comprimento da linha (linhas longas = mais altura)
├── Design da fonte (algumas precisam de mais espaço)
└── Tipo de conteúdo (título vs corpo)
```

### Diretrizes por Contexto

| Tipo de Conteúdo    | Altura de Linha | Por quê                      |
| ------------------- | --------------- | ---------------------------- |
| **Títulos**         | 1.1 – 1.3       | Linhas curtas, mais compacto |
| **Texto do corpo**  | 1.4 – 1.6       | Leitura confortável          |
| **Texto longo**     | 1.6 – 1.8       | Máxima legibilidade          |
| **Elementos de UI** | 1.2 – 1.4       | Eficiência de espaço         |

### Fatores de Ajuste

* **Linhas mais longas** → aumente a altura
* **Fontes maiores** → reduza a proporção
* **Texto em CAIXA ALTA** → pode precisar de mais espaço
* **Tracking apertado** → pode exigir mais altura

---

## 4. Princípios de Comprimento de Linha

### Largura Ideal de Leitura

```
Zona ideal: 45–75 caracteres por linha
├── < 45: Quebra o fluxo
├── 45–75: Leitura confortável
├── > 75: Esforço visual
```

### Como Medir

```css
/* Baseado em caracteres (recomendado) */
max-width: 65ch; /* ch = largura do caractere "0" */
```

### Ajustes por Contexto

| Contexto         | Faixa                 |
| ---------------- | --------------------- |
| Artigo desktop   | 60–75 caracteres      |
| Mobile           | 35–50 caracteres      |
| Sidebar          | 30–45 caracteres      |
| Monitores largos | Ainda limitar a ~75ch |

---

## 5. Princípios de Tipografia Responsiva

### O Problema

```
Tamanhos fixos não escalam bem:
├── Desktop grande demais no mobile
├── Mobile pequeno demais no desktop
└── Saltos bruscos entre breakpoints
```

### Tipografia Fluida (clamp)

```css
/* Sintaxe: clamp(MÍN, IDEAL, MÁX) */
font-size: clamp(
  TAMANHO_MÍNIMO,
  CÁLCULO_FLUIDO,
  TAMANHO_MÁXIMO
);
```

### Estratégia de Escala

| Elemento       | Comportamento         |
| -------------- | --------------------- |
| Texto do corpo | Escala leve           |
| Subtítulos     | Escala moderada       |
| Títulos        | Escala mais dramática |
| Display        | Escala máxima         |

---

## 6. Princípios de Peso e Ênfase

### Uso Semântico de Pesos

| Peso    | Nome         | Uso                |
| ------- | ------------ | ------------------ |
| 300–400 | Light/Normal | Texto do corpo     |
| 500     | Medium       | Ênfase sutil       |
| 600     | Semibold     | Subtítulos, labels |
| 700     | Bold         | Títulos            |
| 800–900 | Heavy/Black  | Display, hero      |

### Criando Contraste

```
Bom contraste = pular pelo menos 2 níveis
├── 400 corpo + 700 título = bom
├── 400 corpo + 500 ênfase = sutil
├── 600 título + 700 subtítulo = fraco
```

### Evite

* ❌ Muitos pesos (máx. 3–4 por página)
* ❌ Pesos adjacentes para hierarquia
* ❌ Pesos pesados em textos longos

---

## 7. Espaçamento entre Letras (Tracking)

### Princípios

```
Texto grande: tracking mais apertado
Texto pequeno: tracking normal ou levemente maior
CAIXA ALTA: sempre tracking maior
```

### Diretrizes

| Contexto      | Ajuste     |
| ------------- | ---------- |
| Display/Hero  | -2% a -4%  |
| Títulos       | -1% a -2%  |
| Corpo         | 0%         |
| Texto pequeno | +1% a +2%  |
| CAIXA ALTA    | +5% a +10% |

---

## 8. Princípios de Hierarquia

### Como Criar Hierarquia Visual

```
├── TAMANHO
├── PESO
├── COR
├── ESPAÇAMENTO
└── POSIÇÃO
```

### Hierarquia Típica

| Nível           | Características    |
| --------------- | ------------------ |
| Primário (H1)   | Maior, mais forte  |
| Secundário (H2) | Menor, ainda forte |
| Terciário (H3)  | Médio              |
| Corpo           | Padrão             |
| Legenda         | Menor, cor suave   |

**Teste:** Dá para entender a importância só de bater o olho?

---

## 9. Psicologia da Leitura

### Padrão de Leitura em F

Usuários escaneiam:

* Topo
* Lado esquerdo
* Subtítulos

**Implicação:** informações-chave à esquerda e nos títulos.

### Chunking Cognitivo

* Parágrafos curtos
* Subtítulos claros
* Listas
* Espaço em branco

---

## 10. Checklist de Seleção Tipográfica

Antes de finalizar:

* [ ] Perguntou preferências do usuário?
* [ ] Considerou marca e contexto?
* [ ] Escolheu razão adequada?
* [ ] Limitou a 2–3 famílias?
* [ ] Testou legibilidade?
* [ ] Conferiu comprimento da linha?
* [ ] Verificou contraste (acessibilidade)?
* [ ] Diferente do último projeto?

### Anti-Patterns

* ❌ Mesmas fontes sempre
* ❌ Fontes demais
* ❌ Estilo acima da legibilidade
* ❌ Tamanhos fixos
* ❌ Fontes decorativas no corpo

---

> **Lembre-se:** Tipografia é comunicação clara. Escolha com base no conteúdo e no público — não em gosto pessoal.
