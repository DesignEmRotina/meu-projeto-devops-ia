---

# Referência de Sistema de Cores Mobile

> Otimização para OLED, modo escuro, cores conscientes de bateria e visibilidade externa.
> **Cor no mobile não é só estética — é bateria e usabilidade.**

---

## 1. Fundamentos de Cor no Mobile

### Por que cor no mobile é diferente

```
DESKTOP:                           MOBILE:
├── Telas LCD (retroiluminadas)    ├── OLED comum (autoemissivo)
├── Iluminação controlada          ├── Exterior, sol forte
├── Energia estável                ├── Bateria importa
├── Preferência pessoal            ├── Modo escuro do sistema
└── Visualização estática          └── Ângulos variáveis, movimento
```

### Prioridades de Cor no Mobile

| Prioridade                      | Por quê                              |
| ------------------------------- | ------------------------------------ |
| **1. Legibilidade**             | Iluminação variável, uso externo     |
| **2. Eficiência de bateria**    | OLED = modo escuro economiza energia |
| **3. Integração com o sistema** | Suporte a claro/escuro               |
| **4. Semântica**                | Erro, sucesso, alerta                |
| **5. Marca**                    | Depois dos requisitos funcionais     |

---

## 2. Considerações sobre OLED

### Como o OLED funciona

```
LCD (Liquid Crystal Display):
├── Backlight sempre ligado
├── Preto = luz passando por filtro escuro
├── Consumo constante
└── Modo escuro não economiza bateria

OLED (Organic LED):
├── Cada pixel emite sua própria luz
├── Preto = pixel desligado (zero energia)
├── Quanto mais claro, mais consumo
└── Modo escuro economiza bateria
```

### Economia de bateria no OLED

```
Consumo relativo de energia por cor:

#000000 (Preto real)    ████░░░░░░   0%
#1A1A1A (Quase preto)   █████░░░░░   ~15%
#333333 (Cinza escuro)  ██████░░░░   ~30%
#666666 (Cinza médio)   ███████░░░   ~50%
#FFFFFF (Branco)        ██████████  100%

Cores saturadas também consomem mais:
├── Azul: mais eficiente
├── Verde: médio
├── Vermelho: menos eficiente
└── Cores dessaturadas economizam mais
```

### Preto real vs quase preto

```
#000000 (Preto real):
├── Máxima economia de bateria
├── Pode causar "borrão" ao rolar
├── Contraste muito agressivo
└── Usado pela Apple no dark mode puro

#121212 ou #1A1A1A (Quase preto):
├── Boa economia de bateria
├── Rolagem mais suave
├── Menos agressivo aos olhos
└── Recomendação do Material Design

RECOMENDAÇÃO:
#000000 para fundo
#0D0D0D–#1A1A1A para superfícies
```

---

## 3. Design para Modo Escuro

### Benefícios do modo escuro

```
Usuários ativam modo escuro por:
├── Economia de bateria (OLED)
├── Menor fadiga visual
├── Preferência pessoal
├── Estética AMOLED
└── Acessibilidade (sensibilidade à luz)
```

### Estratégia de cores no modo escuro

```
MODO CLARO                    MODO ESCURO
──────────                    ──────────
Fundo:      #FFFFFF     →     #000000 ou #121212
Superfície: #F5F5F5     →     #1E1E1E
Superfície2:#EEEEEE     →     #2C2C2C

Primária:   #1976D2     →     #90CAF9
Texto:      #212121     →     #E0E0E0
Secundária: #757575     →     #9E9E9E

Elevação no modo escuro:
├── Quanto maior, mais clara a superfície
├── 0dp →  0% overlay
├── 4dp →  9% overlay
├── 8dp → 12% overlay
└── Profundidade sem sombras
```

### Cores de texto no modo escuro

| Função       | Modo Claro | Modo Escuro |
| ------------ | ---------- | ----------- |
| Primário     | #000000    | #E8E8E8     |
| Secundário   | #666666    | #B0B0B0     |
| Desabilitado | #9E9E9E    | #6E6E6E     |
| Links        | #1976D2    | #8AB4F8     |

### Regras de inversão de cor

```
NÃO inverta cores automaticamente:
├── Cores saturadas ficam agressivas
├── Semântica se perde
├── Marca quebra
└── Contraste fica imprevisível

FAÇA:
├── Paleta escura intencional
├── Dessature cores primárias
├── Tons mais claros para ênfase
├── Preserve semântica
└── Valide contraste separadamente
```

---

## 4. Visibilidade em Ambiente Externo

### O problema do sol

```
No uso externo:
├── Sol forte reduz contraste
├── Reflexos atrapalham leitura
├── Óculos polarizados afetam cores
└── Usuário cobre a tela com a mão

Mais afetados:
├── Cinza claro no branco
├── Diferenças sutis de cor
├── Overlays com baixa opacidade
└── Tons pastel
```

### Estratégias de alto contraste

```
Recomendações:

CONTRASTE MÍNIMO:
├── Texto normal: 4.5:1 (WCAG AA)
├── Texto grande: 3:1
├── Ideal: 7:1+ (AAA)

EVITE:
├── #999 em #FFF
├── #BBB em #FFF
├── Cores claras em fundo claro
└── Gradientes sutis para info crítica

FAÇA:
├── Use cores semânticas do sistema
├── Teste ao sol
├── Ofereça modo alto contraste
└── Use cores sólidas em UI crítica
```

---

## 5. Cores Semânticas

### Significado consistente

| Semântica | Significado | iOS     | Android |
| --------- | ----------- | ------- | ------- |
| Erro      | Problema    | #FF3B30 | #B3261E |
| Sucesso   | Positivo    | #34C759 | #4CAF50 |
| Alerta    | Atenção     | #FF9500 | #FFC107 |
| Info      | Informação  | #007AFF | #2196F3 |

### Regras de uso semântico

```
NUNCA use cores semânticas para:
├── Branding
├── Decoração
├── Estilo arbitrário
└── Status sem ícones

SEMPRE:
├── Combine com ícones
├── Mantenha no claro e escuro
├── Use consistentemente
└── Siga padrões da plataforma
```

---

## 6. Cor Dinâmica (Android)

### Material You

```
Android 12+:
Papel de parede → Extração de cores → Tema do app

O app recebe:
├── Primária
├── Secundária
├── Terciária
├── Superfícies neutras
├── Cores "on" (texto)
```

### Fallback

```
Quando indisponível:
├── Android < 12
├── Usuário desativou
├── Launcher incompatível

Forneça esquema fixo:
├── Baseado na marca
├── Suporte claro/escuro
├── Funções equivalentes
└── Testado em ambos
```

---

## 7. Acessibilidade de Cores

### Daltonismo

```
~8% dos homens, ~0.5% das mulheres

Tipos:
├── Protanopia
├── Deuteranopia
├── Tritanopia
├── Monocromacia

Regras:
├── Nunca dependa só de cor
├── Use ícones, texto, padrões
├── Teste com simuladores
└── Evite apenas vermelho/verde
```

---

## 8. Anti-Patterns de Cor

### ❌ Erros comuns

| Erro                      | Problema      | Correção       |
| ------------------------- | ------------- | -------------- |
| Cinza claro no branco     | Invisível     | ≥ 4.5:1        |
| Branco puro no escuro     | Cansa visão   | Off-white      |
| Mesma saturação no escuro | Brilha demais | Dessaturar     |
| Só vermelho/verde         | Daltonismo    | Use ícones     |
| Ignorar modo escuro       | Ruptura UX    | Suporte nativo |

---

## 9. Checklist de Sistema de Cores

### Antes de escolher cores

* [ ] Claro e escuro definidos?
* [ ] Contraste validado?
* [ ] Economia OLED considerada?
* [ ] Semântica consistente?
* [ ] Seguro para daltonismo?

### Antes do release

* [ ] Testado ao sol?
* [ ] Testado em OLED?
* [ ] Respeita modo do sistema?
* [ ] Dynamic color (Android)?
* [ ] Erros/sucessos consistentes?

---

## 10. Referência Rápida

### Fundos no modo escuro

```
Preto real:        #000000
Quase preto:       #121212
Surface 1:         #1E1E1E
Surface 2:         #2C2C2C
Surface 3:         #3C3C3C
```

### Texto no escuro

```
Primário:   #E0E0E0 – #ECECEC
Secundário: #A0A0A0 – #B0B0B0
Desativado: #606060 – #707070
```

---

> **Lembre-se:** cores mobile precisam funcionar nas piores condições — sol forte, olhos cansados, daltonismo e bateria baixa. Cores bonitas que falham nesses cenários são cores inúteis.
