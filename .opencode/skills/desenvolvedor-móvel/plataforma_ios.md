# Diretrizes da Plataforma iOS

> Fundamentos das Human Interface Guidelines (HIG), convenções de design iOS, tipografia SF Pro e padrões nativos.
> **Leia este arquivo ao desenvolver para iPhone/iPad.**

---

## 1. Filosofia das Human Interface Guidelines

### Princípios Centrais de Design da Apple

```
CLAREZA:
├── Texto legível em qualquer tamanho
├── Ícones precisos e claros
├── Adornos sutis e apropriados
└── Foco na funcionalidade orienta o design

DEFERÊNCIA:
├── A UI ajuda as pessoas a entender e interagir
├── O conteúdo ocupa a tela
├── A UI nunca compete com o conteúdo
└── Transparência sugere mais conteúdo

PROFUNDIDADE:
├── Camadas visuais distintas indicam hierarquia
├── Transições transmitem sensação de profundidade
├── O toque revela funcionalidade
└── O conteúdo se sobrepõe à UI
```

### Valores de Design do iOS

| Valor                    | Implementação                                       |
| ------------------------ | --------------------------------------------------- |
| **Integridade Estética** | O design reflete a função (jogo ≠ produtividade)    |
| **Consistência**         | Use controles do sistema e padrões familiares       |
| **Manipulação Direta**   | O toque afeta diretamente o conteúdo                |
| **Feedback**             | Ações sempre recebem resposta                       |
| **Metáforas**            | Comparações com o mundo real facilitam entendimento |
| **Controle do Usuário**  | O usuário inicia ações e pode cancelá-las           |

---

## 2. Tipografia iOS

### Família de Fontes SF Pro

```
Fontes do Sistema iOS:
├── SF Pro Text: Texto de corpo (< 20pt)
├── SF Pro Display: Títulos grandes (≥ 20pt)
├── SF Pro Rounded: Contextos amigáveis
├── SF Mono: Código, dados tabulares
└── SF Compact: Apple Watch, telas menores
```

### Escala Tipográfica do iOS (Dynamic Type)

| Estilo          | Tamanho Padrão | Peso     | Uso                                    |
| --------------- | -------------- | -------- | -------------------------------------- |
| **Large Title** | 34pt           | Bold     | Barra de navegação (colapsa no scroll) |
| **Title 1**     | 28pt           | Bold     | Títulos de página                      |
| **Title 2**     | 22pt           | Bold     | Cabeçalhos de seção                    |
| **Title 3**     | 20pt           | Semibold | Sub-seções                             |
| **Headline**    | 17pt           | Semibold | Texto de destaque                      |
| **Body**        | 17pt           | Regular  | Conteúdo principal                     |
| **Callout**     | 16pt           | Regular  | Conteúdo secundário                    |
| **Subhead**     | 15pt           | Regular  | Conteúdo terciário                     |
| **Footnote**    | 13pt           | Regular  | Legendas, horários                     |
| **Caption 1**   | 12pt           | Regular  | Anotações                              |
| **Caption 2**   | 11pt           | Regular  | Texto auxiliar                         |

### Suporte a Dynamic Type (OBRIGATÓRIO)

```swift
// ❌ ERRADO: Tamanho fixo
Text("Olá")
    .font(.system(size: 17))

// ✅ CORRETO: Dynamic Type
Text("Olá")
    .font(.body) // Escala conforme preferência do usuário

// Equivalente em React Native
<Text style={{ fontSize: 17 }}> // ❌ Fixo
<Text style={styles.body}> // Use um sistema de escala dinâmica
```

### Uso de Peso da Fonte

| Peso           | Constante iOS | Uso                  |
| -------------- | ------------- | -------------------- |
| Regular (400)  | `.regular`    | Texto de corpo       |
| Medium (500)   | `.medium`     | Botões, ênfase       |
| Semibold (600) | `.semibold`   | Subtítulos           |
| Bold (700)     | `.bold`       | Títulos, info-chave  |
| Heavy (800)    | `.heavy`      | Raramente, marketing |

---

## 3. Sistema de Cores iOS

### Cores do Sistema (Semânticas)

```
Use cores semânticas para suporte automático ao modo escuro:

Primárias:
├── .label → Texto principal
├── .secondaryLabel → Texto secundário
├── .tertiaryLabel → Texto terciário
├── .quaternaryLabel → Marcas d’água

Fundos:
├── .systemBackground → Fundo principal
├── .secondarySystemBackground → Conteúdo agrupado
├── .tertiarySystemBackground → Conteúdo elevado

Preenchimentos:
├── .systemFill → Formas grandes
├── .secondarySystemFill → Formas médias
├── .tertiarySystemFill → Formas pequenas
├── .quaternarySystemFill → Formas sutis
```

### Cores de Destaque do Sistema

| Cor        | Modo Claro | Modo Escuro | Uso                |
| ---------- | ---------- | ----------- | ------------------ |
| Azul       | #007AFF    | #0A84FF     | Links, destaques   |
| Verde      | #34C759    | #30D158     | Sucesso            |
| Vermelho   | #FF3B30    | #FF453A     | Erros              |
| Laranja    | #FF9500    | #FF9F0A     | Avisos             |
| Amarelo    | #FFCC00    | #FFD60A     | Atenção            |
| Roxo       | #AF52DE    | #BF5AF2     | Recursos especiais |
| Rosa       | #FF2D55    | #FF375F     | Favoritos          |
| Verde-água | #5AC8FA    | #64D2FF     | Informações        |

### Considerações para Modo Escuro

```
Modo escuro no iOS não é inversão simples:

CLARO:                     ESCURO:
├── Fundos brancos          ├── Preto real ou quase preto
├── Cores saturadas         ├── Cores dessaturadas
├── Texto preto             ├── Texto claro
└── Sombras                 └── Brilhos ou sem sombra

REGRA: Sempre use cores semânticas.
```

---

## 4. Layout e Espaçamento iOS

### Áreas Seguras (Safe Areas)

```
REGRA: Nunca coloque elementos interativos fora das áreas seguras.
```

### Margens e Padding Padrão

| Elemento         | Margem          | Observações    |
| ---------------- | --------------- | -------------- |
| Borda → conteúdo | 16pt            | Padrão         |
| Seções agrupadas | 16pt            | Espaçamento    |
| Células de lista | 16pt            | Padding padrão |
| Cards internos   | 16pt            | Conteúdo       |
| Botões           | 12pt v / 16pt h | Mínimo         |

---

## 5. Padrões de Navegação iOS

### Tipos de Navegação

| Padrão                    | Uso                   |
| ------------------------- | --------------------- |
| **Tab Bar**               | 3–5 seções principais |
| **Navigation Controller** | Hierarquia            |
| **Modal**                 | Tarefas focadas       |
| **Sidebar**               | iPad                  |

### Tab Bar

Regras:

* Máx. 5 itens
* Ícones SF Symbols
* Labels sempre visíveis
* Barra sempre visível

### Navigation Bar

* Botão voltar padrão do sistema
* Título centralizado
* Máx. 2 ações à direita
* Prefira texto a ícones

---

## 6. Componentes iOS

### Botões

Estilos:

* Tinted (primário)
* Bordered (secundário)
* Plain (terciário)

Altura mínima: **44pt**

### Listas

Estilos:

* `.plain`
* `.insetGrouped`
* `.grouped`
* `.sidebar`

Acessórios:

* `>` Detalhe
* `(i)` Informação
* `✓` Seleção
* `≡` Reordenar
* `-` Excluir

---

## 7. Padrões Específicos do iOS

### Pull to Refresh

```
Sempre use UIRefreshControl nativo.
```

### Swipe Actions

* Deslize à esquerda: ações destrutivas
* Deslize à direita: ações construtivas
* Swipe completo executa ação primária

### Menus de Contexto

* Pressão longa
* Preview do conteúdo
* Ações relacionadas
* Destrutivas por último

---

## 8. SF Symbols

### Diretrizes

* Combine peso do ícone com o texto
* Use símbolos padrão
* Multicolor apenas quando fizer sentido

---

## 9. Acessibilidade iOS

### VoiceOver

Todo elemento precisa de:

* Label
* Hint (opcional)
* Trait
* Value

### Escala de Texto

```
OBRIGATÓRIO: Suporte total ao Dynamic Type
Até 53pt em tamanhos de acessibilidade
```

### Reduzir Movimento

Respeite a preferência do usuário para animações.

---

## 10. Checklist iOS

### Antes de Cada Tela

* [ ] SF Pro / SF Symbols
* [ ] Dynamic Type
* [ ] Safe Areas respeitadas
* [ ] Navegação conforme HIG
* [ ] Máx. 5 abas
* [ ] Alvos ≥ 44pt

### Antes do Release

* [ ] Modo escuro testado
* [ ] Tamanhos de texto testados
* [ ] VoiceOver testado
* [ ] Swipe back funcional
* [ ] Teclado tratado
* [ ] Notch/Dynamic Island tratados
* [ ] Área do Home Indicator respeitada
* [ ] Componentes nativos utilizados

---

> **Lembrete:** Usuários iOS têm expectativas altas baseadas em outros apps da plataforma. Fugir das HIG faz o app parecer “quebrado”. Quando houver dúvida, use o componente nativo.
