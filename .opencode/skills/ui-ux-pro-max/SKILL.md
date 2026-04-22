--- 
name: ui-ux-pro-max
description: "Guia de design completo para aplicações web e mobile. Use ao projetar novos componentes ou páginas de interface do usuário, escolher paletas de cores e tipografia ou revisar o código em busca de problemas de UX."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# UI/UX Pro Max - Inteligência de Design

Guia de design completo para aplicações web e mobile. Contém mais de 50 estilos, 97 paletas de cores, 57 combinações de fontes, 99 diretrizes de UX e 25 tipos de gráficos em 9 stacks de tecnologia. Banco de dados pesquisável com recomendações baseadas em prioridade.

## Quando usar
Consulte estas diretrizes quando:
- Projetar novos componentes ou páginas de interface do usuário
- Escolher paletas de cores e tipografia
- Revisar o código em busca de problemas de UX
- Criar landing pages ou dashboards
- Implementar requisitos de acessibilidade

## Categorias de Regras por Prioridade

| Prioridade | Categoria | Impacto | Domínio |
|----------|----------|--------|--------|
| 1 | Acessibilidade | CRÍTICA | `ux` |

| 2 | Toque e Interação | CRÍTICA | `ux` |

| 3 | Desempenho | ALTO | `ux` |

| 4 | Layout e Responsividade | ALTO | `ux` |

| 5 | Tipografia e Cor | MÉDIO | `typography`, `color` |

| 6 | Animação | MÉDIO | `ux` |

| 7 | Seleção de Estilo | MÉDIO | `style`, `product` |

| 8 | Gráficos e Dados | BAIXO | `chart` |

## Referência Rápida

### 1. Acessibilidade (CRÍTICA)

- `color-contrast` - Proporção mínima de 4,5:1 para texto normal
- `focus-states` - Anéis de foco visíveis em elementos interativos
- `alt-text` - Texto alternativo descritivo para imagens relevantes
- `aria-labels` - Aria-label para botões com ícones
- `keyboard-nav` - A ordem de tabulação corresponde à ordem visual
- `form-labels` - Usar o atributo `label` para o rótulo

### 2. Toque e Interação (CRÍTICA)

- `touch-target-size` - Tamanho mínimo dos alvos de toque: 44x44px
- `hover-vs-tap` - Usar clique/toque para as interações principais
- `loading-buttons` - Desativar o botão durante operações assíncronas
- `error-feedback` - Limpar as mensagens de erro próximas ao problema
- `cursor-pointer` - Adicionar um cursor aos elementos clicáveis

### 3. Desempenho (ALTA)

- `image-optimization` - Usar WebP, srcset e carregamento lento (lazy loading)
- `reduced-motion` - Verificar prefers-reduced-motion
- `content-jumping` - Reservar espaço para conteúdo assíncrono

### 4. Layout e Responsividade (ALTA)

- `viewport-meta` - width=device-width initial-scale=1
- `readable-font-size` - Texto do corpo com tamanho mínimo de 16px em dispositivos móveis
- `horizontal-scroll` - Garantir que o conteúdo se ajuste à largura da viewport
- `z-index-management` - Definir escala de z-index (10, 20, 30, 50)

### 5. Tipografia e Cor (MÉDIA)

- `line-height` - Usar 1,5-1,75 para o texto do corpo
- `line-length` - Limitar a 65-75 caracteres por linha
- `font-pairing` - Combinar Personalidade da fonte para títulos e corpo do texto

### 6. Animação (MÉDIO)

- `duration-timing` - Use 150-300 ms para microinterações
- `transform-performance` - Use transform/opacity, não width/height
- `loading-states` - Telas de esqueleto ou spinners

### 7. Seleção de estilo (MÉDIO)

- `style-match` - Combine o estilo com o tipo de produto
- `consistency` - Use o mesmo estilo em todas as páginas
- `no-emoji-icons` - Use ícones SVG, não emojis

### 8. Gráficos e dados (BAIXO)

- `chart-type` - Combine o tipo de gráfico com o tipo de dados
- `color-guidance` - Use paletas de cores acessíveis
- `data-table` - Forneça uma tabela alternativa para acessibilidade

## Como usar

## Como usar

Pesquise domínios específicos usando a ferramenta de linha de comando abaixo.

---

## Pré-requisitos

Verifique se o Python está instalado:

```bash
python3 --version || python --version
```

Se o Python não estiver instalado, instale-o de acordo com o sistema operacional do usuário:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## Como usar esta habilidade

Quando um usuário solicitar serviços de UI/UX (design, desenvolvimento, criação, implementação, revisão, correção, melhoria), siga este fluxo de trabalho:

### Etapa 1: Analisar os requisitos do usuário

Extraia as principais informações da solicitação do usuário:
- **Tipo de produto**: SaaS, e-commerce, portfólio, painel de controle, landing page, etc.
- **Palavras-chave de estilo**: minimalista, lúdico, profissional, elegante, modo escuro, etc.
- **Setor**: saúde, fintech, jogos, educação, etc.
- **Stack**: React, Vue, Next.js ou, por padrão, `html-tailwind`

### Etapa 2: Gerar Sistema de Design (OBRIGATÓRIO)

**Sempre comece com `--design-system`** para obter recomendações abrangentes com justificativas:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"<product_type> <industry> <keywords>" --design-system [-p "Nome do Projeto"]
```

Este comando:
1. Busca em 5 domínios em paralelo (produto, estilo, cor, página inicial, tipografia)
2. Aplica regras de justificativa de `ui-reasoning.csv` para selecionar as melhores correspondências
3. Retorna um sistema de design completo: padrão, estilo, cores, tipografia, efeitos
4. Inclui antipadrões a serem evitados

**Exemplo:**
```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"beauty spa wellness service" --design-system -p "Serenity Spa"
```

### Etapa 3: Complemente com buscas detalhadas (conforme necessário)

Após obter o sistema de design, use buscas por domínio para obter detalhes adicionais:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"<palavra-chave>" --domain <domínio> [-n <max_resultados>]
```

**Quando usar buscas detalhadas:**

| Necessidade | Domínio | Exemplo |

|------|--------|---------|

| Mais opções de estilo | `style` | `--domain style "glassmorphism dark"` |

| Recomendações de gráficos | `chart` | `--domain chart "real-time dashboard"` |

| Melhores práticas de UX | `ux` | `--domain ux "animation accessibility"` |
| Fontes alternativas | `typography` | `--domain typography "elegant luxury"` |

| Estrutura da página de destino | `landing` | `--domain landing "hero social-proof"` |

### Etapa 4: Diretrizes de pilha (Padrão: html-tailwind)

Obtenha as melhores práticas específicas da implementação. Se o usuário não especificar uma pilha, **o padrão será `html-tailwind`**.

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"<palavra-chave>" --stack html-tailwind
```

Stacks disponíveis: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`

---

## Referência de Busca

### Domínios Disponíveis

| Domínio | Uso | Exemplos de Palavras-chave |

|--------|---------|------------------|

| `product` | Recomendações de tipo de produto | SaaS, e-commerce, portfólio, saúde, beleza, serviço |

| `style` | Estilos de UI, cores, efeitos | glassmorphism, minimalismo, modo escuro, brutalismo |

| `typography` | Combinações de fontes, Google Fonts | elegante, lúdico, profissional, moderno | | `color` | Paletas de cores por tipo de produto | SaaS, e-commerce, saúde, beleza, fintech, serviços |

| `landing` | Estrutura da página, estratégias de CTA | hero, hero-centric, depoimento, preço, prova social |

| `chart` | Tipos de gráficos, recomendações de bibliotecas | tendência, comparação, linha do tempo, funil, pizza |

| `ux` | Melhores práticas, antipadrões | animação, acessibilidade, z-index, carregamento |

| `react` | Desempenho do React/Next.js | waterfall, bundle, suspense, memo, rerender, cache |

| `web` | Diretrizes de interface web | aria, focus, keyboard, semantic, virtualize |

| `prompt` | Prompts de IA, palavras-chave CSS | (nome do estilo) |

### Stacks Disponíveis

| Stack | Focus |

|-------|-------|

| `html-tailwind` | Utilitários Tailwind, responsivo, acessibilidade (PADRÃO) |

| `react` | Estado, hooks, desempenho, padrões |

| `nextjs` | SSR, roteamento, imagens, rotas de API |

| `vue` | Composition API, Pinia, Vue Router |

| `svelte` | Runes, stores, SvelteKit |

| `swiftui` | Views, Estado, Navegação, Animação |

| `react-native` | Componentes, Navegação, Listas |

| `flutter` | Widgets, Estado, Layout, Temas |

| `shadcn` | Componentes shadcn/ui, temas, formulários, padrões |

---

---

## Exemplo de Fluxo de Trabalho

**Solicitação do usuário:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

### Etapa 1: Analisar Requisitos
- Tipo de produto: Serviço de beleza/spa
- Palavras-chave de estilo: elegante, profissional, suave
- Setor: Beleza/Bem-estar
- Stack: html-tailwind (padrão)

### Etapa 2: Gerar Sistema de Design (OBRIGATÓRIO)

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

**Saída:** Sistema de design completo com padrão, estilo, cores, tipografia, efeitos e antipadrões.

### Etapa 3: Complementar com pesquisas detalhadas (conforme necessário)

```bash
# Obter diretrizes de UX para animação e acessibilidade
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"animation accessibility" --domain ux

# Obter opções alternativas de tipografia, se necessário
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"elegant luxury serif" --domain typography
```

### Etapa 4: Diretrizes de layout

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"layout responsive form" --stack html-tailwind
```

**Em seguida:** Sintetizar o sistema de design + pesquisas detalhadas e implementar o design.

---

## Formatos de Saída

A flag `--design-system` suporta dois formatos de saída:

```bash
# Caixa ASCII (padrão) - melhor para exibição no terminal
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"fintech crypto" --design-system

# Markdown - melhor para documentação
python3 .claude/skills/ui-ux-pro-max/scripts/search.py ​​"fintech crypto" --design-system -f markdown
```

---

## Dicas para Melhores Resultados

1. **Seja específico com as palavras-chave** - "painel de controle SaaS de saúde" > "aplicativo"
2. **Pesquise várias vezes** - Palavras-chave diferentes revelam insights diferentes
3. **Combine domínios** - Estilo + Tipografia + Cor = Sistema de design completo
4. **Sempre verifique a experiência do usuário (UX)** - Pesquise por "animação", "z-index", "acessibilidade" para problemas comuns
5. **Use a pilha de tecnologias** **Sinalizar** - Obtenha as melhores práticas específicas para a implementação
6. **Iterar** - Se a primeira pesquisa não corresponder, tente palavras-chave diferentes

---

## Regras Comuns para uma Interface de Usuário Profissional

Estes são problemas frequentemente ignorados que fazem com que a interface de usuário pareça pouco profissional:

### Ícones e Elementos Visuais

| Regra | Fazer | Não Fazer |

|------|----|----- |

| **Sem ícones de emoji** | Use ícones SVG (Heroicons, Lucide, Simple Icons) | Use emojis como 🎨 🚀 ⚙️ como ícones da interface de usuário |

| **Estados de foco estáveis** | Use transições de cor/opacidade ao passar o mouse | Use transformações de escala que alterem o layout |

| **Logotipos de marca corretos** | Pesquise o SVG oficial do Simple Icons | Evite adivinhar ou usar caminhos de logotipo incorretos |

| **Dimensionamento consistente de ícones** | Use viewBox fixo (24x24) com largura 6x16 | Evite misturar tamanhos de ícones diferentes aleatoriamente | ### Interação e Cursor

| Regra | Fazer | Não fazer |

|------|----|----- |

| **Ponteiro do cursor** | Adicionar `cursor-pointer` a todos os cards clicáveis/com efeito de passar o mouse | Manter o cursor padrão em elementos interativos |

| **Feedback ao passar o mouse** | Fornecer feedback visual (cor, sombra, borda) | Sem indicação de que o elemento é interativo |

| **Transições suaves** | Usar `transition-colors duration-200` | Mudanças de estado instantâneas ou muito lentas (>500ms) |

### Contraste nos modos claro/escuro

| Regra | Fazer | Não fazer |

|------|----|----- |

| **Modo claro para cards de vidro** | Usar `bg-white/80` ou opacidade maior | Usar `bg-white/10` (muito transparente) |

| **Contraste de texto claro** | Use `#0F172A` (cinza-ardósia-900) para o texto | Use `#94A3B8` (cinza-ardósia-400) para o corpo do texto |
| **Texto claro e discreto** | Use `#475569` (cinza-ardósia-600) no mínimo | Use cinza-400 ou mais claro |
| **Visibilidade da borda** | Use `border-gray-200` no modo claro | Use `border-white/10` (invisível) |

### Layout e Espaçamento

| Regra | Fazer | Não fazer |

|------|----|----- |

| **Barra de navegação flutuante** | Adicione espaçamento `top-4 left-4 right-4` | Fixe a barra de navegação em `top-0 left-0 right-0` |

| **Preenchimento do conteúdo** | Considere a altura fixa da barra de navegação | Permita que o conteúdo fique oculto atrás de elementos fixos |

| **Largura máxima consistente** | Use o mesmo `max-w-6xl` ou `max-w-7xl` | Misture larguras de contêiner diferentes |

---

## Lista de Verificação Pré-Entrega

Antes de entregar o código da interface do usuário, verifique os seguintes itens:

### Qualidade Visual
- [ ] Nenhum emoji usado como ícone (use SVG em vez disso)
- [ ] Todos os ícones pertencem a um conjunto de ícones consistente (Heroicons/Lucide)
- [ ] Os logotipos das marcas estão corretos (verificados no Simple Icons)
- [ ] Os estados de foco não causam alterações no layout
- [ ] Use as cores do tema diretamente (bg-primary), não o wrapper var()

### Interação
- [ ] Todos os elementos clicáveis ​​possuem `cursor-pointer`
- [ ] Os estados de foco fornecem feedback visual claro
- [ ] As transições são suaves (150-300 ms)
- [ ] Os estados de foco são visíveis para navegação por teclado

### Modo Claro/Escuro
- [ ] O texto no modo claro possui contraste suficiente (mínimo de 4,5:1)
- [ ] Elementos transparentes/de vidro visíveis no modo claro
- [ ] As bordas são visíveis em ambos os modos
- [ ] Teste ambos os modos antes da entrega

### Layout
- [ ] Elementos flutuantes têm espaçamento adequado das bordas
- [ ] Nenhum conteúdo oculto atrás de barras de navegação fixas
- [ ] Responsivo em 375px, 768px, 1024px e 1440px
- [ ] Sem rolagem horizontal em dispositivos móveis

### Acessibilidade
- [ ] Todas as imagens têm texto alternativo
- [ ] Os campos de formulário têm rótulos
- [ ] A cor não é o único indicador
- [ ] `prefers-reduced-motion` respeitado

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.