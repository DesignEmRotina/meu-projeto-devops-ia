nome: desenvolvimento_de_jogos
descrição: Orquestrador de desenvolvimento de jogos. Direciona para habilidades específicas por plataforma com base nas necessidades do projeto.
ferramentas-permitidas: Ler, Escrever, Editar, Glob, Grep, Bash
---
```

# Desenvolvimento de Jogos

> **Skill orquestradora** que fornece os princípios centrais do desenvolvimento de jogos e direciona para sub-skills especializadas conforme o contexto.

---

## Quando Usar Esta Skill

Você está trabalhando em um projeto de **desenvolvimento de jogos**.
Esta skill ensina os **PRINCÍPIOS fundamentais** de game development e direciona você para a **sub-skill correta** com base no cenário.

---

## Roteamento de Sub-Skills

### Seleção por Plataforma

| Se o jogo for para...          | Use a Sub-Skill                 |
| ------------------------------ | ------------------------------- |
| Navegadores web (HTML5, WebGL) | `game-development/web-games`    |
| Mobile (iOS, Android)          | `game-development/mobile-games` |
| PC (Steam, Desktop)            | `game-development/pc-games`     |
| Headsets VR/AR                 | `game-development/vr-ar`        |

---

### Seleção por Dimensão

| Se o jogo for...       | Use a Sub-Skill             |
| ---------------------- | --------------------------- |
| 2D (sprites, tilemaps) | `game-development/2d-games` |
| 3D (meshes, shaders)   | `game-development/3d-games` |

---

### Áreas de Especialidade

| Se você precisar de...                      | Use a Sub-Skill                |
| ------------------------------------------- | ------------------------------ |
| GDD, balanceamento, psicologia do jogador   | `game-development/game-design` |
| Multiplayer, networking                     | `game-development/multiplayer` |
| Estilo visual, pipeline de assets, animação | `game-development/game-art`    |
| Design de som, música, áudio adaptativo     | `game-development/game-audio`  |

---

## Princípios Fundamentais (Todas as Plataformas)

### 1. O Game Loop

Todo jogo, independentemente da plataforma, segue este padrão:

```
INPUT  → Ler ações do jogador
UPDATE → Processar lógica do jogo (timestep fixo)
RENDER → Renderizar o frame (interpolado)
```

**Regra do Timestep Fixo:**

* Física / lógica: Taxa fixa (ex: 50Hz)
* Renderização: O mais rápido possível
* Interpolar estados para suavidade visual

---

### 2. Matriz de Seleção de Padrões

| Padrão                | Quando Usar                     | Exemplo                    |
| --------------------- | ------------------------------- | -------------------------- |
| **State Machine**     | 3–5 estados discretos           | Player: Idle → Walk → Jump |
| **Object Pooling**    | Criação/destruição frequente    | Balas, partículas          |
| **Observer / Events** | Comunicação entre sistemas      | Vida → Atualização de UI   |
| **ECS**               | Milhares de entidades similares | Unidades RTS, partículas   |
| **Command**           | Undo, replay, networking        | Gravação de input          |
| **Behavior Tree**     | IA complexa                     | IA de inimigos             |

**Regra de decisão:** Comece com **State Machine**.
Use **ECS** apenas quando a performance exigir.

---

### 3. Abstração de Input

Abstraia inputs em **AÇÕES**, não em teclas físicas:

```
"jump" → Espaço, Botão A do gamepad, Toque na tela
"move" → WASD, Analógico esquerdo, Joystick virtual
```

**Por quê:** Permite multiplataforma, remapeamento e acessibilidade.

---

### 4. Orçamento de Performance (60 FPS = 16,67ms)

| Sistema        | Orçamento |
| -------------- | --------- |
| Input          | 1ms       |
| Física         | 3ms       |
| IA             | 2ms       |
| Lógica do jogo | 4ms       |
| Renderização   | 5ms       |
| Buffer         | 1,67ms    |

**Prioridade de Otimização:**

1. Algoritmos (O(n²) → O(n log n))
2. Batching (reduzir draw calls)
3. Pooling (evitar picos de GC)
4. LOD (nível de detalhe por distância)
5. Culling (ignorar o que não é visível)

---

### 5. Seleção de IA por Complexidade

| Tipo de IA        | Complexidade | Quando Usar                           |
| ----------------- | ------------ | ------------------------------------- |
| **FSM**           | Baixa        | 3–5 estados, comportamento previsível |
| **Behavior Tree** | Média        | Modular, amigável para designers      |
| **GOAP**          | Alta         | Planejamento emergente                |
| **Utility AI**    | Alta         | Decisões baseadas em pontuação        |

---

### 6. Estratégia de Colisão

| Tipo             | Melhor Para                       |
| ---------------- | --------------------------------- |
| **AABB**         | Retângulos, checagens rápidas     |
| **Circle**       | Objetos redondos, baixo custo     |
| **Spatial Hash** | Muitos objetos de tamanho similar |
| **Quadtree**     | Mundos grandes, tamanhos variados |

---

## Anti-Padrões (Universais)

| ❌ Não faça                      | ✅ Faça                     |
| ------------------------------- | -------------------------- |
| Atualizar tudo a cada frame     | Use eventos e dirty flags  |
| Criar objetos em loops críticos | Object pooling             |
| Não cachear nada                | Cache referências          |
| Otimizar sem medir              | Faça profiling primeiro    |
| Misturar input com lógica       | Abstraia a camada de input |

---

## Exemplos de Roteamento

### Exemplo 1:

**"Quero fazer um jogo de plataforma 2D para navegador"**
→ Comece com `game-development/web-games` (framework e runtime)
→ Depois `game-development/2d-games` (sprites e tilemaps)
→ Consulte `game-development/game-design` para level design

---

### Exemplo 2:

**"Jogo mobile de puzzle para iOS e Android"**
→ Comece com `game-development/mobile-games` (touch e lojas)
→ Use `game-development/game-design` para balanceamento

---

### Exemplo 3:

**"FPS multiplayer em VR"**
→ `game-development/vr-ar` para conforto e imersão
→ `game-development/3d-games` para renderização
→ `game-development/multiplayer` para networking

---

> **Lembre-se:** Grandes jogos surgem da iteração, não da perfeição. Prototipe rápido, depois refine.
