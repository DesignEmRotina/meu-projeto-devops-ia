# Referência de Tipografia Mobile

> Escala tipográfica, fontes do sistema, Dynamic Type, acessibilidade e tipografia em modo escuro.
> **Falhas de tipografia são a causa nº 1 de apps mobile ilegíveis.**

---

## 1. Fundamentos da Tipografia Mobile

### Por que a tipografia mobile é diferente

```
DESKTOP:                        MOBILE:
├── Distância de visão 20-30"   ├── Distância de visão 12-15"
├── Viewport grande             ├── Viewport pequeno e estreito
├── Hover para detalhes         ├── Toque/scroll para detalhes
├── Iluminação controlada       ├── Variável (externo, etc.)
├── Tamanho de fonte fixo       ├── Tamanho controlado pelo usuário
└── Leitura prolongada          └── Leitura rápida / escaneamento
```

### Regras de Tipografia Mobile

| Regra                           | Desktop       | Mobile                                   |
| ------------------------------- | ------------- | ---------------------------------------- |
| **Tamanho mínimo do corpo**     | 14px          | 16px (14pt/14sp)                         |
| **Comprimento máximo da linha** | 75 caracteres | 40–60 caracteres                         |
| **Altura de linha**             | 1.4–1.5       | 1.4–1.6 (mais generosa)                  |
| **Peso da fonte**               | Variável      | Regular predominante, bold com moderação |
| **Contraste**                   | AA (4.5:1)    | AA mínimo, AAA preferível                |

---

## 2. Fontes do Sistema

### iOS: Família SF Pro

```
Família San Francisco (SF):
├── SF Pro Display: Texto grande (≥ 20pt)
├── SF Pro Text: Texto de corpo (< 20pt)
├── SF Pro Rounded: Contextos amigáveis
├── SF Mono: Monoespaçada
└── SF Compact: Apple Watch, UI compacta

Recursos:
├── Tamanho óptico (ajuste automático)
├── Espaçamento dinâmico
├── Algarismos tabulares/proporcionais
├── Excelente legibilidade
```

### Android: Família Roboto

```
Família Roboto:
├── Roboto: Sans-serif padrão
├── Roboto Flex: Fonte variável
├── Roboto Serif: Opção serifada
├── Roboto Mono: Monoespaçada
├── Roboto Condensed: Espaços estreitos

Recursos:
├── Otimizada para telas
├── Suporte amplo a idiomas
├── Múltiplos pesos
├── Boa em tamanhos pequenos
```

### Quando usar fontes do sistema

```
✅ USE fontes do sistema quando:
├── A marca não exige fonte customizada
├── Eficiência de leitura é prioridade
├── Sensação nativa/integrada é importante
├── Performance é crítica
├── Suporte amplo a idiomas é necessário

❌ EVITE fontes do sistema quando:
├── A identidade da marca exige customização
├── Diferenciação visual é necessária
├── Estilo editorial/revista
└── (Mas ainda suporte acessibilidade)
```

### Considerações para fontes customizadas

```
Ao usar fontes customizadas:
├── Inclua todos os pesos necessários
├── Faça subset para reduzir tamanho
├── Teste em todos os tamanhos do Dynamic Type
├── Forneça fallback para fonte do sistema
├── Teste qualidade de renderização
└── Verifique suporte a idiomas
```

---

## 3. Escala Tipográfica

### Escala iOS (Nativa)

| Estilo      | Tamanho | Peso     | Altura de Linha |
| ----------- | ------- | -------- | --------------- |
| Large Title | 34pt    | Bold     | 41pt            |
| Title 1     | 28pt    | Bold     | 34pt            |
| Title 2     | 22pt    | Bold     | 28pt            |
| Title 3     | 20pt    | Semibold | 25pt            |
| Headline    | 17pt    | Semibold | 22pt            |
| Body        | 17pt    | Regular  | 22pt            |
| Callout     | 16pt    | Regular  | 21pt            |
| Subhead     | 15pt    | Regular  | 20pt            |
| Footnote    | 13pt    | Regular  | 18pt            |
| Caption 1   | 12pt    | Regular  | 16pt            |
| Caption 2   | 11pt    | Regular  | 13pt            |

### Escala Android (Material 3)

| Papel           | Tamanho | Peso | Altura de Linha |
| --------------- | ------- | ---- | --------------- |
| Display Large   | 57sp    | 400  | 64sp            |
| Display Medium  | 45sp    | 400  | 52sp            |
| Display Small   | 36sp    | 400  | 44sp            |
| Headline Large  | 32sp    | 400  | 40sp            |
| Headline Medium | 28sp    | 400  | 36sp            |
| Headline Small  | 24sp    | 400  | 32sp            |
| Title Large     | 22sp    | 400  | 28sp            |
| Title Medium    | 16sp    | 500  | 24sp            |
| Title Small     | 14sp    | 500  | 20sp            |
| Body Large      | 16sp    | 400  | 24sp            |
| Body Medium     | 14sp    | 400  | 20sp            |
| Body Small      | 12sp    | 400  | 16sp            |
| Label Large     | 14sp    | 500  | 20sp            |
| Label Medium    | 12sp    | 500  | 16sp            |
| Label Small     | 11sp    | 500  | 16sp            |

### Criando uma escala customizada

```
Use proporção modular:

Proporções recomendadas:
├── 1.125 (segunda maior): UI densa
├── 1.200 (terça menor): Compacta
├── 1.250 (terça maior): Balanceada (comum)
├── 1.333 (quarta justa): Espaçosa
└── 1.500 (quinta justa): Dramática

Exemplo com base 16px e proporção 1.25:
├── xs: 10px
├── sm: 13px
├── base: 16px
├── lg: 20px
├── xl: 25px
├── 2xl: 31px
├── 3xl: 39px
└── 4xl: 49px
```

---

## 4. Dynamic Type / Escalonamento de Texto

### iOS Dynamic Type (OBRIGATÓRIO)

```swift
// ❌ ERRADO: tamanho fixo
Text("Hello")
    .font(.system(size: 17))

// ✅ CORRETO: Dynamic Type
Text("Hello")
    .font(.body)

// Fonte customizada com escalonamento
Text("Hello")
    .font(.custom("MyFont", size: 17, relativeTo: .body))
```

### Android Text Scaling (OBRIGATÓRIO)

```
SEMPRE use sp para texto:
├── sp = pixel independente de escala
├── Escala com preferência do usuário
├── dp NÃO escala (não use para texto)

Escala do usuário: 85% a 200%
├── Padrão: 14sp = 14dp
├── Máximo: 14sp = 28dp

Teste em 200%!
```

---

## 5. Acessibilidade Tipográfica

### Tamanhos Mínimos

| Elemento           | Mínimo     | Recomendado |
| ------------------ | ---------- | ----------- |
| Texto corpo        | 14px/pt/sp | 16px/pt/sp  |
| Texto secundário   | 12px       | 13–14px     |
| Legendas           | 11px       | 12px        |
| Botões             | 14px       | 14–16px     |
| **Nada menor que** | 11px       | —           |

### Requisitos de Contraste (WCAG)

```
Texto normal:
├── AA: 4.5:1 mínimo
├── AAA: 7:1 recomendado

Texto grande:
├── AA: 3:1 mínimo
├── AAA: 4.5:1 recomendado
```

---

## 6. Tipografia em Modo Escuro

### Ajustes de Cor

```
Modo Claro:               Modo Escuro:
├── Preto (#000)          ├── Branco/cinza claro (#E0E0E0)
├── Alto contraste        ├── Contraste levemente reduzido
├── Saturação total       ├── Cores dessaturadas
└── Escuro = ênfase       └── Claro = ênfase

REGRA: Evite branco puro (#FFF).
Use off-white (#E0E0E0–#F0F0F0).
```

### Peso em Modo Escuro

```
Texto parece mais fino em fundo escuro.

Considere:
├── Peso médio no corpo
├── Leve aumento de espaçamento
├── Testar em OLED real
└── Peso ligeiramente maior que no modo claro
```

---

## 7. Anti-Patterns de Tipografia

### ❌ Erros Comuns

| Erro            | Problema              | Correção          |
| --------------- | --------------------- | ----------------- |
| Tamanho fixo    | Ignora acessibilidade | Use escalonamento |
| Texto pequeno   | Ilegível              | ≥ 14pt/sp         |
| Baixo contraste | Invisível ao sol      | ≥ 4.5:1           |
| Linhas longas   | Difícil leitura       | ≤ 60 caracteres   |
| Altura baixa    | Texto espremido       | ≥ 1.4×            |

---

## 8. Checklist de Tipografia

### Antes do Release

* [ ] Texto corpo ≥ 16?
* [ ] Dynamic Type testado?
* [ ] Escala 200% testada (Android)?
* [ ] Contraste em modo escuro validado?
* [ ] Fallback de fontes configurado?
* [ ] Testado em dispositivos reais?

---

> **Lembre-se:** se o usuário não consegue ler, o app está quebrado. Tipografia não é decoração — é a interface principal.
