# Árvores de Decisão & Templates de Contexto

> **PENSAMENTO** de design baseado em contexto, não soluções fixas.
> **Este material é um GUIA de decisão, não templates de copiar e colar.**
> **Para princípios de psicologia em UX (Hick, Fitts, etc.), veja:** [ux-psychology.md](ux-psychology.md)

---

## ⚠️ Como Usar Este Arquivo

Este arquivo ajuda você a **DECIDIR**, não a copiar.

* Árvores de decisão → ajudam você a **PENSAR** nas opções
* Templates → mostram **ESTRUTURA e PRINCÍPIOS**, não valores exatos
* **Sempre pergunte as preferências do usuário** antes de aplicar
* **Gere paletas novas** com base no contexto, não copie códigos hex
* **Aplique leis de UX** do arquivo `ux-psychology.md` para validar decisões

---

## 1. Árvore de Decisão Mestre

```
┌─────────────────────────────────────────────────────────────┐
│                    O QUE VOCÊ ESTÁ CONSTRUINDO?              │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   E-COMMERCE            SaaS / APP              CONTEÚDO
   - Páginas produto     - Dashboard             - Blog
   - Checkout            - Ferramentas           - Portfólio
   - Catálogo            - Admin                 - Landing Page
        │                     │                     │
        ▼                     ▼                     ▼
   PRINCÍPIOS:           PRINCÍPIOS:             PRINCÍPIOS:
   - Confiança           - Funcionalidade        - Storytelling
   - Ação                - Clareza               - Emoção
   - Urgência            - Eficiência            - Criatividade
```

---

## 2. Árvore de Decisão por Público

### Quem é o seu usuário-alvo?

```
PÚBLICO-ALVO
      │
      ├── Geração Z (18–25)
      │   ├── Cores: Ousadas, vibrantes, combinações inesperadas
      │   ├── Tipografia: Grande, expressiva, variável
      │   ├── Layout: Mobile-first, vertical, consumo rápido
      │   ├── Efeitos: Movimento, gamificação, interação
      │   └── Abordagem: Autêntica, rápida, sem cara corporativa
      │
      ├── Millennials (26–41)
      │   ├── Cores: Suaves, terrosas, sofisticadas
      │   ├── Tipografia: Limpa, legível, funcional
      │   ├── Layout: Responsivo, baseado em cards, organizado
      │   ├── Efeitos: Sutis e com propósito
      │   └── Abordagem: Valor, transparência, sustentabilidade
      │
      ├── Geração X (42–57)
      │   ├── Cores: Profissionais, confiáveis, conservadoras
      │   ├── Tipografia: Familiar, clara, objetiva
      │   ├── Layout: Hierarquia tradicional, previsível
      │   ├── Efeitos: Mínimos, apenas feedback funcional
      │   └── Abordagem: Direta, eficiente, confiável
      │
      ├── Baby Boomers (58+)
      │   ├── Cores: Alto contraste, simples, claras
      │   ├── Tipografia: Tamanhos grandes, alta legibilidade
      │   ├── Layout: Simples, linear, sem poluição visual
      │   ├── Efeitos: Nenhum ou quase nenhum
      │   └── Abordagem: Clara, detalhada, confiável
      │
      └── B2B / Corporativo
          ├── Cores: Paleta profissional, discreta
          ├── Tipografia: Limpa, orientada a dados, escaneável
          ├── Layout: Grid, organizado, eficiente
          ├── Efeitos: Profissionais e sutis
          └── Abordagem: Especialista, foco em solução e ROI
```

---

## 3. Árvore de Decisão para Escolha de Cores

### Em vez de códigos hex fixos, use este processo:

```
QUAL EMOÇÃO OU AÇÃO VOCÊ QUER GERAR?
            │
            ├── Confiança & Segurança
            │   └── Considere: família dos azuis, neutros profissionais
            │       → PERGUNTE ao usuário o tom preferido
            │
            ├── Crescimento & Saúde
            │   └── Considere: família dos verdes, tons naturais
            │       → PERGUNTE se há foco eco / natureza / bem-estar
            │
            ├── Urgência & Ação
            │   └── Considere: cores quentes (laranja/vermelho) como DESTAQUE
            │       → Use com moderação, PERGUNTE se é apropriado
            │
            ├── Luxo & Premium
            │   └── Considere: tons escuros profundos, metálicos, paleta contida
            │       → PERGUNTE sobre posicionamento da marca
            │
            ├── Criativo & Divertido
            │   └── Considere: multicores, combinações inesperadas
            │       → PERGUNTE sobre a personalidade da marca
            │
            └── Calmo & Minimalista
                └── Considere: neutros com um único destaque
                    → PERGUNTE qual cor de destaque combina com a marca
```

### Processo:

1. Identifique a emoção necessária
2. Restrinja para uma **família de cores**
3. **Pergunte ao usuário** a preferência dentro da família
4. Gere uma paleta nova usando princípios de HSL

---

## 4. Árvore de Decisão Tipográfica

```
QUAL É O TIPO DE CONTEÚDO?
          │
          ├── Dados Intensivos (Dashboard, SaaS)
          │   ├── Estilo: Sans-serif, clara, compacta
          │   ├── Escala: Mais fechada (1.125–1.2)
          │   └── Prioridade: Escaneabilidade e densidade
          │
          ├── Editorial (Blog, Revista)
          │   ├── Estilo: Títulos serifados + corpo sans funciona bem
          │   ├── Escala: Mais dramática (1.333+)
          │   └── Prioridade: Conforto de leitura e hierarquia
          │
          ├── Tech Moderna (Startup, Marketing SaaS)
          │   ├── Estilo: Sans geométrica ou humanista
          │   ├── Escala: Balanceada (1.25)
          │   └── Prioridade: Modernidade e clareza
          │
          ├── Luxo (Moda, Premium)
          │   ├── Estilo: Serifada elegante ou sans fina
          │   ├── Escala: Dramática (1.5–1.618)
          │   └── Prioridade: Sofisticação e espaço em branco
          │
          └── Divertido (Infantil, Jogos, Casual)
              ├── Estilo: Fontes arredondadas e amigáveis
              ├── Escala: Variada e expressiva
              └── Prioridade: Diversão, proximidade e legibilidade
```

### Processo de Seleção:

1. Identifique o tipo de conteúdo
2. Escolha a **direção de estilo**
3. **Pergunte** se o usuário já possui fontes da marca
4. Selecione fontes coerentes com essa direção

---

## 5. Diretrizes para E-commerce {#e-commerce}

### Princípios-Chave (não regras fixas)

* **Confiança primeiro:** como você demonstra segurança?
* **Foco em ação:** onde estão os CTAs?
* **Escaneável:** o usuário compara rápido?

### Pensamento de Cores:

```
E-commerce geralmente precisa de:
├── Cor de confiança (geralmente azul) → PERGUNTE preferência
├── Fundo limpo (branco/neutro) → depende da marca
├── Cor de ação (CTA, promoções) → depende da urgência
├── Semântica sucesso/erro → padrões ajudam
└── Integração com a marca → PERGUNTE cores existentes
```

### Princípios de Layout:

```
┌────────────────────────────────────────────────────┐
│  HEADER: Marca + Busca + Carrinho                  │
│  (Ações essenciais sempre visíveis)                │
├────────────────────────────────────────────────────┤
│  ZONA DE CONFIANÇA: Por que confiar?                │
│  (Entrega, devolução, segurança)                   │
├────────────────────────────────────────────────────┤
│  HERO: Oferta ou mensagem principal                │
│  (CTA claro, foco único)                            │
├────────────────────────────────────────────────────┤
│  CATEGORIAS: Navegação fácil                       │
├────────────────────────────────────────────────────┤
│  PRODUTOS: Comparação simples                      │
│  (Preço, avaliação, ações rápidas)                 │
├────────────────────────────────────────────────────┤
│  PROVA SOCIAL: Avaliações, depoimentos             │
├────────────────────────────────────────────────────┤
│  FOOTER: Políticas, contato, selos                 │
└────────────────────────────────────────────────────┘
```

### Psicologia Aplicável:

* Lei de Hick: limite opções
* Lei de Fitts: CTAs bem dimensionados
* Prova social: quando relevante
* Escassez: use com honestidade

---

## 6. Diretrizes para Dashboard SaaS {#saas}

### Princípios-Chave

* **Função acima da estética**
* **UI calma:** reduza carga cognitiva
* **Consistência:** padrões previsíveis

### Pensamento de Cores:

```
Dashboards normalmente precisam:
├── Fundo: claro OU escuro (PERGUNTE preferência)
├── Superfícies: leve contraste
├── Destaque primário: ações-chave
├── Cores de dados: sucesso/alerta/erro
└── Tons neutros: info secundária
```

### Padrões de Layout:

```
OPÇÃO A: Sidebar + Conteúdo
OPÇÃO B: Top navigation
OPÇÃO C: Sidebar recolhível

→ PERGUNTE qual o padrão preferido
```

---

## 7. Diretrizes para Landing Pages {#landing-page}

### Princípios-Chave

* **Hero dominante**
* **Um único CTA principal**
* **Conexão emocional antes da venda**

*(estrutura mantida conforme original)*

---

## 8. Diretrizes para Portfólio {#portfolio}

### Princípios-Chave

* **Personalidade**
* **Foco no trabalho**
* **Memorável, não genérico**

*(estrutura e psicologia mantidas)*

---

## 9. Checklists Pré-Design

### Antes de Começar QUALQUER Design

* [ ] Público definido?
* [ ] Objetivo principal claro?
* [ ] Restrições conhecidas?
* [ ] Conteúdo disponível?
* [ ] Preferências do usuário perguntadas?

### Antes de Entregar

* [ ] Parece premium?
* [ ] Diferente do último projeto?
* [ ] Você se orgulharia disso?

---

## 10. Estimativa de Complexidade

### Projetos Rápidos (Horas)

* Landing simples
* Portfólio pequeno
* Formulário básico

### Projetos Médios (Dias)

* Site multipáginas
* Dashboard modular
* E-commerce parcial

### Projetos Grandes (Semanas)

* SaaS completo
* Plataforma e-commerce
* Design system customizado

---

> **Lembre-se:** estes templates mostram **PROCESSO e RACIOCÍNIO**.
> Todo projeto exige decisões novas de cor, tipografia e estilo com base no contexto.
> **Pergunte sempre que houver dúvida.**

