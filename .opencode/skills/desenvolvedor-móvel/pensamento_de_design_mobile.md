# Mobile Design Thinking

> **Este arquivo impede que a IA use padrões memorizados e força raciocínio genuíno.**
> Mecanismos para evitar os padrões automáticos do treinamento de IA em desenvolvimento mobile.
> **O equivalente mobile da abordagem de decomposição de layout do frontend.**

---

## 🧠 PROTOCOLO DE RACIOCÍNIO MOBILE PROFUNDO

### Este Processo é Obrigatório Antes de Todo Projeto Mobile

```

┌─────────────────────────────────────────────────────────────────┐
│                  RACIOCÍNIO MOBILE PROFUNDO                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1️⃣ VARREDURA DE CONTEXTO                                      │
│     └── Quais são minhas suposições sobre este projeto?         │
│         └── QUESTIONE essas suposições                          │
│                                                                 │
│  2️⃣ ANÁLISE ANTI-PADRÃO                                        │
│     └── Estou aplicando um padrão memorizado?                  │
│         └── Esse padrão é REALMENTE o melhor para ESTE projeto? │
│                                                                 │
│  3️⃣ DECOMPOSIÇÃO POR PLATAFORMA                                │
│     └── Pensei em iOS e Android separadamente?                 │
│         └── Quais são os padrões específicos da plataforma?     │
│                                                                 │
│  4️⃣ QUEBRA DE INTERAÇÃO POR TOQUE                              │
│     └── Analisei cada interação individualmente?              │
│         └── Apliquei Lei de Fitts, Zona do Polegar?             │
│                                                                 │
│  5️⃣ ANÁLISE DE IMPACTO DE PERFORMANCE                           │
│     └── Considerei o impacto de performance de cada componente?│
│         └── A solução padrão é realmente performática?          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

```

---

## 🚫 PADRÕES DEFAULT DE IA EM MOBILE (LISTA PROIBIDA)

### Usar Estes Padrões Automaticamente é PROIBIDO!

Os padrões abaixo são “defaults” aprendidos por IA a partir de dados de treinamento.  
Antes de usar qualquer um deles, **QUESTIONE e CONSIDERE ALTERNATIVAS!**

```

┌─────────────────────────────────────────────────────────────────┐
│                 🚫 ZONA SEGURA DA IA MOBILE                     │
│        (Padrões Default — Nunca Usar sem Questionar)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PADRÕES DE NAVEGAÇÃO:                                          │
│  ├── Tab bar em todo projeto (Drawer não seria melhor?)         │
│  ├── Sempre 5 abas (3 bastam? 6+ → drawer?)                     │
│  ├── Aba "Home" à esquerda (O que o comportamento diz?)         │
│  └── Menu hamburger (Já não está ultrapassado?)                 │
│                                                                 │
│  PADRÕES DE GERENCIAMENTO DE ESTADO:                             │
│  ├── Redux em tudo (Zustand/Jotai não resolvem?)                │
│  ├── Estado global para tudo (Estado local não basta?)          │
│  ├── Inferno de Context Providers (Atoms são melhores?)         │
│  └── BLoC em todo Flutter (Riverpod não é mais moderno?)        │
│                                                                 │
│  PADRÕES DE LISTAS:                                             │
│  ├── FlatList por padrão (FlashList é mais performática?)       │
│  ├── windowSize=21 (Realmente necessário?)                      │
│  ├── removeClippedSubviews sempre (Sempre mesmo?)               │
│  └── ListView.builder (ListView.separated é melhor?)            │
│                                                                 │
│  PADRÕES DE UI:                                                 │
│  ├── FAB no canto inferior direito (Esquerdo é mais acessível?) │
│  ├── Pull-to-refresh em toda lista (Precisa mesmo?)             │
│  ├── Swipe para deletar da esquerda (Direita seria melhor?)     │
│  └── Bottom sheet para todo modal (Tela cheia não é melhor?)    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

```

---

## 🔍 DECOMPOSIÇÃO DE COMPONENTES (OBRIGATÓRIA)

### Análise de Decomposição para Cada Tela

Antes de projetar qualquer tela, faça esta análise:

```

TELA: [Nome da Tela]
├── AÇÃO PRINCIPAL: [Qual é a ação principal?]
│   └── Está na zona do polegar? [Sim/Não → Por quê?]
│
├── ALVOS DE TOQUE: [Todos os elementos clicáveis]
│   ├── [Elemento 1]: [Tamanho]pt → Adequado?
│   ├── [Elemento 2]: [Tamanho]pt → Adequado?
│   └── Espaçamento: [Gap]pt → Risco de toque acidental?
│
├── CONTEÚDO ROLÁVEL:
│   ├── É uma lista? → FlatList/FlashList [Por quê?]
│   ├── Quantidade de itens: ~[N] → Impacto de performance?
│   └── Altura fixa? → getItemLayout é necessário?
│
├── REQUISITOS DE ESTADO:
│   ├── Estado local é suficiente?
│   ├── Preciso elevar o estado?
│   └── Global é realmente necessário? [Por quê?]
│
├── DIFERENÇAS DE PLATAFORMA:
│   ├── iOS: [Algo precisa mudar?]
│   └── Android: [Algo precisa mudar?]
│
├── CONSIDERAÇÃO OFFLINE:
│   ├── Esta tela deve funcionar offline?
│   └── Estratégia de cache: [Sim/Não/Qual?]
│
└── IMPACTO DE PERFORMANCE:
├── Componentes pesados?
├── Memoização é necessária?
└── Performance de animações?

```

---

## 🎯 MATRIZ DE QUESTIONAMENTO DE PADRÕES

Faça estas perguntas para todo padrão default:

### Navegação

| Suposição | Pergunta | Alternativa |
|---------|---------|------------|
| "Vou usar tab bar" | Quantos destinos existem? | 3 → tabs mínimas, 6+ → drawer |
| "5 abas" | Todas são igualmente importantes? | Aba “Mais”? Híbrido? |
| "Bottom nav" | Há suporte a tablet? | Navigation rail |
| "Stack navigation" | Considerei deep links? | Estrutura de URL |

### Estado

| Suposição | Pergunta | Alternativa |
|---------|---------|------------|
| "Vou usar Redux" | Qual a complexidade do app? | Zustand / TanStack |
| "Estado global" | Isso é realmente global? | Estado local |
| "Context Provider" | Re-render será problema? | Zustand / Jotai |
| "BLoC" | Boilerplate vale a pena? | Riverpod |

### Listas

| Suposição | Pergunta | Alternativa |
|---------|---------|------------|
| "FlatList" | Performance é crítica? | FlashList |
| "renderItem padrão" | Está memoizado? | useCallback + memo |
| "Index como key" | Ordem muda? | item.id |
| "ListView" | Há separadores? | ListView.separated |

### UI

| Suposição | Pergunta | Alternativa |
|---------|---------|------------|
| "FAB à direita" | Usuário é destro/canhoto? | Ajustar acessibilidade |
| "Pull-to-refresh" | Precisa mesmo? | Apenas quando necessário |
| "Bottom sheet" | Quanto conteúdo existe? | Modal full screen |
| "Swipe actions" | É descobrível? | Botão visível |

---

## 🧪 TESTE ANTI-MEMORIZAÇÃO

### Pergunte a Si Mesmo Antes de Cada Solução

```

┌─────────────────────────────────────────────────────────────────┐
│                CHECKLIST ANTI-MEMORIZAÇÃO                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  □ Escolhi isso "porque sempre faço assim"?                     │
│    → Se SIM: PARE. Considere alternativas.                      │
│                                                                 │
│  □ Este padrão aparece muito nos dados de treino?               │
│    → Se SIM: Ele serve para ESTE projeto?                       │
│                                                                 │
│  □ Escrevi isso automaticamente, sem pensar?                   │
│    → Se SIM: Volte e decomponha.                                │
│                                                                 │
│  □ Considerei alternativas?                                     │
│    → Se NÃO: Pense em pelo menos 2.                             │
│                                                                 │
│  □ Pensei por plataforma?                                       │
│    → Se NÃO: Analise iOS e Android separadamente.               │
│                                                                 │
│  □ Considerei impacto de performance?                           │
│    → Se NÃO: CPU, memória, bateria?                             │
│                                                                 │
│  □ Esta solução serve para ESTE contexto?                       │
│    → Se NÃO: Personalize.                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

```

---

## 🎭 ESPÍRITO > CHECKLIST (Mobile)

> **Passar no checklist não é o objetivo. Criar uma UX mobile excelente é.**

---

## 📝 COMPROMISSO DE DESIGN MOBILE

```

📱 COMPROMISSO DE DESIGN MOBILE

Projeto: _______________
Plataforma: iOS / Android / Ambos

1. Padrão default que NÃO vou usar:
   └── _______________

2. Foco contextual do projeto:
   └── _______________

3. Diferenças por plataforma:
   └── iOS: _______________
   └── Android: _______________

4. Área que vou otimizar performance:
   └── _______________

5. Desafio único do projeto:
   └── _______________

🧠 Se não consigo preencher → não entendi o projeto.

```

---

> **Lembre-se:**  
> Se você escolheu algo “porque sempre foi assim”, você escolheu **sem pensar**.  
> Cada projeto é único. Cada contexto é diferente. Cada usuário se comporta de um jeito.  
> **PENSE, depois codifique.**
```
