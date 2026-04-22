---

# Referência de Psicologia do Toque

> Aprofundamento em interação por toque no mobile, Lei de Fitts aplicada ao toque, anatomia da zona do polegar, psicologia de gestos e feedback háptico.
> **Este é o equivalente mobile de `psicologia_de_UX.md` — CRÍTICO para todo trabalho mobile.**

---

## 1. Lei de Fitts para Toque

### A Diferença Fundamental

```
DESKTOP (Mouse/Trackpad):
├── Tamanho do cursor: 1 pixel (precisão)
├── Feedback visual: Estados de hover
├── Custo de erro: Baixo (fácil tentar novamente)
└── Aquisição de alvo: Rápida e precisa

MOBILE (Dedo):
├── Área de contato: ~7mm de diâmetro (impreciso)
├── Feedback visual: Sem hover, apenas toque
├── Custo de erro: Alto (tentativas frustrantes)
├── Oclusão: O dedo cobre o alvo
└── Aquisição de alvo: Mais lenta, exige alvos maiores
```

### Fórmula da Lei de Fitts (Adaptada)

```
Tempo de aquisição por toque = a + b × log₂(1 + D/W)

Onde:
├── D = Distância até o alvo
├── W = Largura do alvo
└── Para toque: W deve ser MUITO maior que no desktop
```

### Tamanhos Mínimos de Alvos de Toque

| Plataforma             | Mínimo      | Recomendado | Uso                               |
| ---------------------- | ----------- | ----------- | --------------------------------- |
| **iOS (HIG)**          | 44pt × 44pt | 48pt+       | Todos os elementos tocáveis       |
| **Android (Material)** | 48dp × 48dp | 56dp+       | Todos os elementos tocáveis       |
| **WCAG 2.2**           | 44px × 44px | -           | Conformidade com acessibilidade   |
| **Ações Críticas**     | -           | 56–64px     | CTAs primários, ações destrutivas |

### Tamanho Visual vs Área de Toque

```
┌─────────────────────────────────────┐
│                                     │
│    ┌─────────────────────────┐      │
│    │                         │      │
│    │    [  BOTÃO  ]          │ ← Visual: 36px
│    │                         │      │
│    └─────────────────────────┘      │
│                                     │ ← Área de toque: 48px (padding estendido)
└─────────────────────────────────────┘

✅ CORRETO: O visual pode ser menor se a área de toque for ≥ 44–48px
❌ ERRADO: Fazer a área de toque igual ao visual pequeno
```

### Regras de Aplicação

| Elemento         | Tamanho Visual | Área de Toque                              |
| ---------------- | -------------- | ------------------------------------------ |
| Botões de ícone  | 24–32px        | 44–48px (com padding)                      |
| Links de texto   | Qualquer       | Altura mínima de 44px                      |
| Itens de lista   | Largura total  | Altura de 48–56px                          |
| Checkbox / Radio | 20–24px        | Área de toque de 44–48px                   |
| Botão fechar/X   | 24px           | Mínimo de 44px                             |
| Itens da tab bar | Ícone 24–28px  | Largura total da aba, 49px de altura (iOS) |

---

## 2. Anatomia da Zona do Polegar

### Uso do Celular com Uma Mão

```
Pesquisas mostram: 49% dos usuários seguram o celular com uma mão.

┌─────────────────────────────────────┐
│                                     │
│  ┌─────────────────────────────┐    │
│  │      DIFÍCIL DE ALCANÇAR     │    │ ← Barra de status, navegação superior
│  │    (exige esticar o dedo)    │    │    Colocar: Voltar, menu, configurações
│  │                             │    │
│  ├─────────────────────────────┤    │
│  │                             │    │
│  │        OK DE ALCANÇAR        │    │ ← Área de conteúdo
│  │        (confortável)         │    │    Colocar: Ações secundárias
│  │                             │    │
│  ├─────────────────────────────┤    │
│  │                             │    │
│  │      FÁCIL DE ALCANÇAR       │    │ ← Tab bar, zona do FAB
│  │     (arco do polegar)        │    │    Colocar: CTAs PRIMÁRIOS!
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│           [   HOME   ]               │
└─────────────────────────────────────┘
```

### Arco do Polegar (Usuário Destro)

```
Mão direita segurando o celular:

┌───────────────────────────────┐
│  ESTICAR     ESTICAR     OK   │
│                               │
│  ESTICAR       OK       FÁCIL │
│                               │
│     OK        FÁCIL     FÁCIL │
│                               │
│   FÁCIL       FÁCIL     FÁCIL │
└───────────────────────────────┘

Mão esquerda é espelhada.
→ Projete para AMBAS ou assuma dominância da direita
```

### Diretrizes de Posicionamento

| Tipo de Elemento      | Posição Ideal                | Motivo                             |
| --------------------- | ---------------------------- | ---------------------------------- |
| **CTA Primário**      | Inferior centro/direita      | Fácil alcance do polegar           |
| **Tab bar**           | Inferior                     | Posição natural do polegar         |
| **FAB**               | Inferior direita             | Fácil para destros                 |
| **Navegação**         | Topo (difícil)               | Uso menos frequente                |
| **Ações destrutivas** | Superior esquerda            | Mais difícil de tocar por acidente |
| **Cancelar/Fechar**   | Superior esquerda            | Convenção + segurança              |
| **Confirmar/Done**    | Superior direita ou inferior | Convenção                          |

### Considerações para Celulares Grandes (>6")

```
Em telas grandes, os 40% superiores viram "zona morta" para uso com uma mão.

Soluções:
├── Recursos de alcance (iOS)
├── Interfaces com puxar para baixo
├── Navegação por bottom sheet
├── Botões de ação flutuantes
└── Gestos alternativos para ações do topo
```

---

## 3. Psicologia do Toque vs Clique

### Diferenças de Expectativa

| Aspecto               | Clique (Desktop)   | Toque (Mobile)              |
| --------------------- | ------------------ | --------------------------- |
| **Tempo de feedback** | Pode esperar 100ms | Espera instantâneo (<50ms)  |
| **Feedback visual**   | Hover → Clique     | Resposta imediata ao toque  |
| **Tolerância a erro** | Fácil refazer      | Frustrante, parece quebrado |
| **Precisão**          | Alta               | Baixa                       |
| **Menu de contexto**  | Clique direito     | Pressão longa               |
| **Cancelar ação**     | Tecla ESC          | Swipe ou toque fora         |

### Requisitos de Feedback ao Toque

```
Toque → Mudança visual imediata (< 50ms)
├── Estado de destaque (mudança de fundo)
├── Leve redução de escala (0.95–0.98)
├── Efeito ripple (Material Android)
├── Feedback háptico de confirmação
└── Nunca "nada"!

Carregamento → Mostrar em até 100ms
├── Se ação levar > 100ms
├── Mostrar spinner/progresso
├── Desabilitar botão (evitar duplo toque)
└── UI otimista quando possível
```

### O Problema do “Dedo Gordo” (Fat Finger)

```
Problema: O dedo cobre o alvo durante o toque
├── Usuário não vê exatamente onde tocou
├── Feedback aparece SOB o dedo
└── Aumenta a taxa de erro

Soluções:
├── Mostrar feedback ACIMA do ponto de toque
├── Offset tipo cursor para tarefas de precisão
├── Lupa de ampliação para seleção de texto
└── Alvos grandes o suficiente para não exigir precisão
```

---

## 4. Psicologia dos Gestos

### O Problema da Descoberta de Gestos

```
Problema: Gestos são INVISÍVEIS.
├── Usuário precisa descobrir/lembrar
├── Não há hover ou dica visual
├── Modelo mental diferente do toque
└── Muitos usuários nunca descobrem

Solução: Sempre fornecer alternativa visível
├── Arrastar para deletar → Botão/menu de deletar
├── Puxar para atualizar → Botão de atualizar
├── Pinçar para zoom → Controles de zoom
└── Gestos como atalhos, nunca como único caminho
```

### Convenções Comuns de Gestos

| Gesto                     | Significado Universal | Uso                |
| ------------------------- | --------------------- | ------------------ |
| **Toque**                 | Selecionar, ativar    | Ação primária      |
| **Duplo toque**           | Zoom, curtir          | Ação rápida        |
| **Pressão longa**         | Menu de contexto      | Opções secundárias |
| **Swipe horizontal**      | Navegação, deletar    | Ações em listas    |
| **Swipe para baixo**      | Atualizar, dispensar  | Pull to refresh    |
| **Pinça**                 | Zoom in/out           | Mapas, imagens     |
| **Scroll com dois dedos** | Scroll interno        | Scrolls aninhados  |

### Design de Afordância para Gestos

```
Ações por swipe precisam de dicas visuais:

┌─────────────────────────────────────────┐
│  ┌───┐                                  │
│  │ ≡ │  Item com ações ocultas...   →  │ ← Dica na borda (cor parcial)
│  └───┘                                  │
└─────────────────────────────────────────┘

✅ Bom: Cor visível na borda sugerindo swipe
✅ Bom: Ícone de alça ( ≡ ) sugerindo reordenação
✅ Bom: Tooltip explicando o gesto
❌ Ruim: Gestos ocultos sem qualquer pista visual
```

### Diferenças de Gestos por Plataforma

| Gesto                | iOS                         | Android                |
| -------------------- | --------------------------- | ---------------------- |
| **Voltar**           | Swipe da borda esquerda     | Botão/gesto do sistema |
| **Compartilhar**     | Action sheet                | Share sheet            |
| **Menu de contexto** | Pressão longa / Force Touch | Pressão longa          |
| **Fechar modal**     | Swipe para baixo            | Botão voltar ou swipe  |
| **Excluir em lista** | Swipe e confirmar           | Swipe direto ou undo   |

---

## 5. Padrões de Feedback Háptico

### Por Que Hápticos Importam

```
Hápticos fornecem:
├── Confirmação sem olhar
├── Sensação mais rica/premium
├── Acessibilidade (usuários cegos)
├── Redução de erros
└── Satisfação emocional

Sem hápticos:
├── Sensação de app “barato” ou web
├── Usuário não sabe se a ação ocorreu
└── Oportunidade perdida de encantamento
```

### Tipos de Hápticos no iOS

| Tipo        | Intensidade | Uso                |
| ----------- | ----------- | ------------------ |
| `selection` | Leve        | Pickers, seleção   |
| `light`     | Leve        | Ações menores      |
| `medium`    | Média       | Confirmação padrão |
| `heavy`     | Forte       | Ações importantes  |
| `success`   | Padrão      | Tarefa concluída   |
| `warning`   | Padrão      | Avisos             |
| `error`     | Padrão      | Erros              |

### Tipos de Hápticos no Android

| Tipo           | Uso                |
| -------------- | ------------------ |
| `CLICK`        | Toque padrão       |
| `HEAVY_CLICK`  | Ações importantes  |
| `DOUBLE_CLICK` | Confirmações       |
| `TICK`         | Scroll/slider      |
| `LONG_PRESS`   | Pressão longa      |
| `REJECT`       | Erro/ação inválida |

### Diretrizes de Uso de Hápticos

```
✅ USE hápticos para:
├── Toque em botões
├── Toggles
├── Pickers/sliders
├── Pull to refresh
├── Conclusão de ações
├── Erros e avisos
├── Limites de swipe
└── Mudanças importantes de estado

❌ NÃO use hápticos para:
├── Todo scroll
├── Cada item de lista
├── Eventos em background
├── Elementos passivos
└── Uso excessivo (fadiga háptica)
```

---

## 6. Carga Cognitiva no Mobile

### Diferenças em Relação ao Desktop

| Fator                   | Desktop             | Mobile                  | Implicação          |
| ----------------------- | ------------------- | ----------------------- | ------------------- |
| **Atenção**             | Sessões focadas     | Interrupções constantes | Micro-sessões       |
| **Contexto**            | Ambiente controlado | Qualquer lugar          | Lidar com luz/ruído |
| **Multitarefa**         | Várias janelas      | Um app visível          | Completar no app    |
| **Entrada**             | Teclado rápido      | Digitação lenta         | Minimizar inputs    |
| **Recuperação de erro** | Fácil               | Mais difícil            | Prevenir erros      |

### Reduzindo Carga Cognitiva

```
1. UMA AÇÃO PRINCIPAL por tela
2. DIVULGAÇÃO PROGRESSIVA
3. PADRÕES INTELIGENTES
4. QUEBRA EM ETAPAS
5. RECONHECIMENTO > MEMORIZAÇÃO
6. PERSISTÊNCIA DE CONTEXTO
```

---

## 7. Acessibilidade ao Toque

### Considerações Motoras

```
Usuários podem:
├── Ter tremores
├── Usar tecnologias assistivas
├── Ter alcance limitado
├── Precisar de mais tempo
└── Tocar acidentalmente

Respostas de design:
├── Alvos grandes (48dp+)
├── Gestos com timing ajustável
├── Undo para ações destrutivas
├── Suporte a switch control
└── Controle por voz
```

---

## 8. Emoção no Toque

### Sensação Premium

```
Toque premium exige:
├── Resposta < 50ms
├── Háptico correto
├── Animações a 60fps
├── Física realista
└── Atenção aos detalhes
```

---

## 9. Checklist de Psicologia do Toque

### Antes de Cada Tela

* [ ] Alvos ≥ 44–48px?
* [ ] CTA primário na zona do polegar?
* [ ] Confirmação para ações destrutivas?
* [ ] Alternativa visível aos gestos?
* [ ] Feedback háptico?
* [ ] Feedback visual imediato?
* [ ] Loading para ações > 100ms?

---

## 10. Cartão de Referência Rápida

```
MÍNIMO DE TOQUE:
iOS: 44pt | Android: 48dp | WCAG: 44px

ZONA DO POLEGAR:
Topo: Navegação
Meio: Conteúdo
Inferior: CTA primário
```

---

