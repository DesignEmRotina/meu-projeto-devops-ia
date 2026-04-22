# Referência de Sistema de Cores

> Princípios de teoria das cores, processo de seleção e diretrizes de tomada de decisão.
> **Nada de decorar códigos hex — aprenda a PENSAR sobre cores.**

---

## 1. Fundamentos da Teoria das Cores

### O Círculo Cromático

```
                    AMARELO
                      │
           Amarelo-    │    Amarelo-
           Verde       │    Laranja
              ╲       │       ╱
               ╲      │      ╱
    VERDE ─────────── ● ─────────── LARANJA
               ╱      │      ╲
              ╱       │       ╲
           Azul-       │    Vermelho-
           Verde       │    Laranja
                      │
                   VERMELHO
                      │
                   ROXO
                  ╱       ╲
             Azul-         Vermelho-
             Roxo          Roxo
                  ╲       ╱
                    AZUL
```

### Relações de Cores

| Esquema                   | Como Criar                                            | Quando Usar                              |
| ------------------------- | ----------------------------------------------------- | ---------------------------------------- |
| **Monocromático**         | Escolha UM matiz, varie apenas luminosidade/saturação | Minimalista, profissional, coeso         |
| **Análogo**               | Escolha 2–3 matizes ADJACENTES no círculo             | Harmonioso, calmo, inspirado na natureza |
| **Complementar**          | Escolha matizes OPOSTOS no círculo                    | Alto contraste, vibrante, chama atenção  |
| **Complementar Dividido** | Cor base + 2 cores adjacentes à complementar          | Dinâmico, porém equilibrado              |
| **Triádico**              | 3 matizes EQUIDISTANTES no círculo                    | Vibrante, lúdico, criativo               |

### Como Escolher um Esquema

1. **Qual é o clima do projeto?** Calmo → Análogo. Ousado → Complementar.
2. **Quantas cores são necessárias?** Minimalista → Monocromático. Complexo → Triádico.
3. **Quem é o público?** Conservador → Monocromático. Jovem → Triádico.

---

## 2. Regra 60-30-10

### Princípio de Distribuição

```
┌─────────────────────────────────────────────────┐
│                                                 │
│     60% PRIMÁRIA (Fundo, áreas grandes)          │
│     → Deve ser neutra ou relaxante               │
│     → Define o tom geral                         │
│                                                 │
├────────────────────────────────────┬────────────┤
│                                    │            │
│   30% SECUNDÁRIA                   │ 10% DESTAQUE│
│   (Cards, seções, headers)         │ (CTAs,      │
│   → Apoia sem dominar              │ destaques)  │
│                                    │ → Chama     │
│                                    │   atenção   │
└────────────────────────────────────┴────────────┘
```

### Padrão de Implementação

```css
:root {
  /* 60% - Baseado em light/dark mode e clima */
  --color-bg: /* neutro: branco, off-white ou cinza escuro */
  --color-surface: /* levemente diferente do bg */
  
  /* 30% - Baseado na marca ou contexto */
  --color-secondary: /* versão suavizada da primária ou neutra */
  
  /* 10% - Baseado na ação/emoção desejada */
  --color-accent: /* vibrante, chama atenção */
}
```

---

## 3. Psicologia das Cores — Significado & Seleção

### Como Escolher com Base no Contexto

| Se o Projeto É...              | Considere Estes Tons           | Por Quê                 |
| ------------------------------ | ------------------------------ | ----------------------- |
| **Finanças, Tech, Saúde**      | Azuis, Tons de Azul-esverdeado | Confiança, estabilidade |
| **Eco, Bem-estar, Natureza**   | Verdes, Tons terrosos          | Crescimento, saúde      |
| **Comida, Energia, Juventude** | Laranja, Amarelo, Tons quentes | Apetite, excitação      |
| **Luxo, Beleza, Criativo**     | Azul petróleo, Dourado, Preto  | Sofisticação            |
| **Urgência, Vendas, Alertas**  | Vermelho, Laranja              | Ação, atenção           |

### Associações Emocionais (Para Decisão)

| Família de Cor | Associações Positivas              | Cuidados                                |
| -------------- | ---------------------------------- | --------------------------------------- |
| **Azul**       | Confiança, calma, profissionalismo | Pode parecer frio                       |
| **Verde**      | Crescimento, natureza, sucesso     | Pode parecer sem graça                  |
| **Vermelho**   | Paixão, urgência, energia          | Estimula demais                         |
| **Laranja**    | Calor, simpatia, criatividade      | Pode parecer barato                     |
| **Roxo**       | ⚠️ **BANIDO** — IA usa demais!     | Prefira azul petróleo, bordô, esmeralda |
| **Amarelo**    | Otimismo, atenção                  | Difícil leitura                         |
| **Preto**      | Elegância, poder                   | Pode pesar                              |
| **Branco**     | Limpo, minimalista                 | Pode parecer estéril                    |

### Processo de Seleção

1. **Qual o setor?** → Reduza para 2–3 famílias
2. **Qual emoção?** → Escolha o matiz principal
3. **Qual contraste?** → Light ou Dark Mode
4. **PERGUNTE AO USUÁRIO** → Confirme antes de avançar

---

## 4. Princípios de Geração de Paleta

### A Partir de Uma Cor (Método HSL)

Em vez de decorar hex, aprenda a **manipular HSL**:

```
HSL = Matiz, Saturação, Luminosidade

Matiz (0–360): Família da cor
Saturação (0–100%): Intensidade
Luminosidade (0–100%): Brilho
```

### Geração de Escala

```
Escala de Luminosidade:
  50  → L: 97%
  100 → L: 94%
  200 → L: 86%
  300 → L: 74%
  400 → L: 66%
  500 → L: 50–60% (base)
  600 → L: 48%
  700 → L: 38%
  800 → L: 30%
  900 → L: 20%
```

### Ajustes de Saturação

| Contexto       | Saturação         |
| -------------- | ----------------- |
| Profissional   | 40–60%            |
| Jovem/Lúdico   | 70–90%            |
| Dark Mode      | -10–20%           |
| Acessibilidade | Ajustar contraste |

---

## 5. Guia de Seleção por Contexto

### Em vez de Copiar Paletas:

**Passo 1: Identifique o Contexto**

```
E-commerce → Confiança + urgência
SaaS/Dashboard → Baixa fadiga visual
Saúde → Calmante
Luxo → Elegância discreta
Criativo → Personalidade
Outro → PERGUNTAR
```

**Passo 2: Escolha a Família Principal**

* Azul (confiança)
* Verde (crescimento)
* Quente (energia)
* Neutra (elegância)

**Passo 3: Light ou Dark Mode**

* Preferência do usuário?
* Tipo de conteúdo?
* Horário de uso?

**Passo 4: Gere a Paleta**

* Use HSL
* Regra 60-30-10
* WCAG
* Teste com conteúdo real

---

## 6. Princípios de Dark Mode

### Regras-Chave

1. Nunca preto puro
2. Nunca texto branco puro
3. Reduza saturação
4. Elevação = mais claro

### Camadas

```
Base → mais escuro
Cards → levemente mais claro
Modais → ainda mais claro
Popups → o mais claro do dark
```

---

## 7. Diretrizes de Acessibilidade

### Contraste WCAG

| Nível | Texto Normal | Texto Grande |
| ----- | ------------ | ------------ |
| AA    | 4.5:1        | 3:1          |
| AAA   | 7:1          | 4.5:1        |

---

## 8. Checklist de Seleção de Cores

* [ ] Preferência do usuário?
* [ ] Contexto correto?
* [ ] Regra 60-30-10?
* [ ] WCAG OK?
* [ ] Funciona em dark?
* [ ] Não repetiu padrão anterior?

---

## 9. Anti-Padrões

### ❌ NÃO FAÇA

* Reutilizar sempre as mesmas cores
* Usar roxo por padrão
* Dark + neon
* Preto ou branco puro
* Ignorar o contexto

### ✅ FAÇA

* Gere paletas novas
* Pergunte ao usuário
* Use HSL
* Teste contraste
* Ofereça light e dark

---

> **Lembre-se:** Cores são decisões, não padrões. Cada projeto merece uma escolha consciente baseada no contexto.

---
