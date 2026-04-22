# Diretrizes da Plataforma Android

> Fundamentos do Material Design 3, convenções de design Android, tipografia Roboto e padrões nativos.
> **Leia este arquivo ao desenvolver para dispositivos Android.**

---

## 1. Filosofia do Material Design 3

### Princípios Centrais do Material

```
MATERIAL COMO METÁFORA:
├── Superfícies existem em um espaço 3D
├── Luz e sombra definem hierarquia
├── Movimento fornece continuidade
└── Design ousado, gráfico e intencional

DESIGN ADAPTATIVO:
├── Responde às capacidades do dispositivo
├── Uma UI para todos os formatos
├── Cores dinâmicas a partir do papel de parede
└── Personalização por usuário

ACESSÍVEL POR PADRÃO:
├── Alvos de toque grandes
├── Hierarquia visual clara
├── Cores semânticas
└── Movimento respeita preferências
```

### Valores do Material Design

| Valor              | Implementação                                              |
| ------------------ | ---------------------------------------------------------- |
| **Cor Dinâmica**   | Cores se adaptam ao papel de parede/preferência do usuário |
| **Personalização** | Temas específicos por usuário                              |
| **Acessibilidade** | Integrada em todos os componentes                          |
| **Responsividade** | Funciona em todos os tamanhos de tela                      |
| **Consistência**   | Linguagem visual unificada                                 |

---

## 2. Tipografia Android

### Família de Fontes Roboto

```
Fontes do Sistema Android:
├── Roboto: Sans-serif padrão
├── Roboto Flex: Fonte variável (API 33+)
├── Roboto Serif: Alternativa serifada
├── Roboto Mono: Monoespaçada
└── Google Sans: Produtos Google (licença especial)
```

### Escala Tipográfica do Material

| Papel               | Tamanho | Peso    | Altura de Linha | Uso                 |
| ------------------- | ------- | ------- | --------------- | ------------------- |
| **Display Large**   | 57sp    | Regular | 64sp            | Texto hero, splash  |
| **Display Medium**  | 45sp    | Regular | 52sp            | Cabeçalhos grandes  |
| **Display Small**   | 36sp    | Regular | 44sp            | Cabeçalhos médios   |
| **Headline Large**  | 32sp    | Regular | 40sp            | Títulos de página   |
| **Headline Medium** | 28sp    | Regular | 36sp            | Cabeçalhos de seção |
| **Headline Small**  | 24sp    | Regular | 32sp            | Sub-seções          |
| **Title Large**     | 22sp    | Regular | 28sp            | Diálogos, cards     |
| **Title Medium**    | 16sp    | Medium  | 24sp            | Listas, navegação   |
| **Title Small**     | 14sp    | Medium  | 20sp            | Abas, secundário    |
| **Body Large**      | 16sp    | Regular | 24sp            | Conteúdo principal  |
| **Body Medium**     | 14sp    | Regular | 20sp            | Conteúdo secundário |
| **Body Small**      | 12sp    | Regular | 16sp            | Legendas            |
| **Label Large**     | 14sp    | Medium  | 20sp            | Botões, FAB         |
| **Label Medium**    | 12sp    | Medium  | 16sp            | Navegação           |
| **Label Small**     | 11sp    | Medium  | 16sp            | Chips, badges       |

### Pixels Escaláveis (sp)

```
sp = pixels independentes de escala

sp escala automaticamente com:
├── Preferência de tamanho de fonte do usuário
├── Densidade da tela
└── Configurações de acessibilidade

REGRA: SEMPRE use sp para texto e dp para o resto.
```

### Uso de Peso da Fonte

| Peso          | Uso                            |
| ------------- | ------------------------------ |
| Regular (400) | Texto de corpo, displays       |
| Medium (500)  | Botões, labels, destaque       |
| Bold (700)    | Raramente, apenas ênfase forte |

---

## 3. Sistema de Cores Material

### Cores Dinâmicas (Material You)

```
Cores Dinâmicas Android 12+:

Papel de parede → Extração de cores → Tema do app

Seu app se adapta automaticamente a:
├── Cor primária (do papel de parede)
├── Cor secundária (complementar)
├── Cor terciária (destaque)
├── Cores de superfície (derivadas)
└── Todas as cores semânticas ajustadas
```

**Regra:** implemente cores dinâmicas para sensação personalizada.

### Papéis Semânticos de Cor

```
Cores de Superfície:
├── Surface → Fundo principal
├── SurfaceVariant → Cards, contêineres
├── SurfaceTint → Overlay de elevação
├── InverseSurface → Snackbars, tooltips

Cores Sobre Superfície:
├── OnSurface → Texto principal
├── OnSurfaceVariant → Texto secundário
├── Outline → Bordas, divisórias
├── OutlineVariant → Divisórias sutis

Cores Primárias:
├── Primary → Ações-chave, FAB
├── OnPrimary → Texto sobre primária
├── PrimaryContainer → Menor ênfase
├── OnPrimaryContainer → Texto no container
```

### Cores de Erro

| Papel          | Claro   | Escuro  | Uso                      |
| -------------- | ------- | ------- | ------------------------ |
| Error          | #B3261E | #F2B8B5 | Erros, ações destrutivas |
| OnError        | #FFFFFF | #601410 | Texto sobre erro         |
| ErrorContainer | #F9DEDC | #8C1D18 | Fundos de erro           |

### Tema Escuro

```
Tema Escuro Material:

├── Background: #121212 (não preto puro)
├── Surface: #1E1E1E, #232323, etc.
├── Elevação: Quanto maior, mais claro
├── Reduza saturação das cores
└── Verifique contraste
```

---

## 4. Layout e Espaçamento Android

### Grid de Layout

```
Android usa grid base de 8dp:

Espaçamento em múltiplos de 8dp:
├── 4dp: Interno de componentes
├── 8dp: Espaçamento mínimo
├── 16dp: Espaçamento padrão
├── 24dp: Entre seções
├── 32dp: Espaçamento grande
```

### Layout Responsivo

```
Classes de Tamanho de Janela:

COMPACT (< 600dp):
├── Telefones em retrato
├── Layout de coluna única
├── Navegação inferior

MEDIUM (600–840dp):
├── Tablets, dobráveis
├── 2 colunas
├── Navigation rail

EXPANDED (> 840dp):
├── Tablets grandes
├── Múltiplas colunas
├── Drawer de navegação
```

---

## 5. Padrões de Navegação Android

### Componentes de Navegação

| Componente            | Uso                     | Posição          |
| --------------------- | ----------------------- | ---------------- |
| **Bottom Navigation** | 3–5 destinos principais | Inferior         |
| **Navigation Rail**   | Tablets                 | Lateral esquerda |
| **Navigation Drawer** | Muitos destinos         | Lateral          |
| **Top App Bar**       | Contexto atual          | Superior         |

### Navegação Inferior

Regras:

* 3 a 5 destinos
* Ícones Material (24dp)
* Labels sempre visíveis
* Ícone ativo preenchido
* Badges para notificações

---

## 6. Componentes Material

### Botões

Tipos:

* Filled (primário)
* Tonal (secundário)
* Outlined (terciário)
* Text Button (menor ênfase)

Altura mínima de toque: **48dp**

### FAB (Floating Action Button)

* Padrão: 56dp
* Pequeno: 40dp
* Grande: 96dp
* Estendido: Ícone + texto

Posição: canto inferior direito, 16dp das bordas.

---

## 7. Padrões Específicos do Android

### Snackbars

* Posição: inferior
* Duração: 4–10s
* Uma ação opcional
* Não empilhar, usar fila

### Bottom Sheets

* Padrão ou Modal
* Raio superior: 28dp

### Ripple Effect

```
TODO elemento clicável deve ter ripple.

Obrigatório para sensação nativa Android.
```

---

## 8. Material Symbols

### Estilos

* Outlined (padrão)
* Rounded
* Sharp

### Tamanhos

| Tamanho | Uso    |
| ------- | ------ |
| 24dp    | Padrão |
| 48dp    | Ênfase |

---

## 9. Acessibilidade Android

### TalkBack

Todo elemento interativo precisa de:

* Descrição
* Semântica correta
* Estado (ativo, desabilitado)

### Alvos de Toque

```
OBRIGATÓRIO: 48dp × 48dp
```

### Escala de Fonte

Teste sempre com **200%** de escala.

---

## 10. Checklist Android

### Antes de Cada Tela

* [ ] Material 3
* [ ] Alvos ≥ 48dp
* [ ] Ripple em todos os toques
* [ ] Tipografia Roboto
* [ ] Cores semânticas
* [ ] Back funcionando

### Antes do Release

* [ ] Tema escuro
* [ ] Cores dinâmicas
* [ ] Fontes em 200%
* [ ] TalkBack testado
* [ ] Predictive Back (Android 14+)
* [ ] Edge-to-edge
* [ ] Tablets testados

---

> **Lembrete:** Usuários Android esperam Material Design. Ignorar esses padrões faz o app parecer estranho e quebrado. Use componentes Material como base e personalize com critério.
