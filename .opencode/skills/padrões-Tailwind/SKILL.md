--- 
name: padrões-Tailwind
description: "Princípios do Tailwind CSS v4. Configuração CSS-first, consultas de contêiner, padrões modernos, arquitetura de tokens de design."
risk: desconhecido
source: comunidade
date_add: "2026-02-27"
---

# Padrões do Tailwind CSS (v4 - 2025)

> CSS moderno com foco em utilidade e configuração nativa do CSS.

## Quando usar
Use esta habilidade ao configurar o Tailwind v4, usar temas CSS-first e tokens de design ou implementar consultas de contêiner e padrões modernos do Tailwind.

---

## 1. Arquitetura do Tailwind v4

### O que mudou em relação à v3

| v3 (Legado) | v4 (Atual) |

|-------------|--------------|

| `tailwind.config.js` | Diretiva `@theme` baseada em CSS |

| Plugin PostCSS | Motor Oxide (10x mais rápido) |

| Modo JIT | Nativo, sempre ativo |

| Sistema de plugins | Recursos nativos de CSS |

| Diretiva `@apply` | Ainda funciona, mas não é recomendada |

### Conceitos principais da v4

| Conceito | Descrição |

|---------|-------------|
| **CSS em primeiro lugar** | Configuração em CSS, não em JavaScript |

| **Motor Oxide** | Compilador baseado em Rust, muito mais rápido |

| **Aninhamento nativo** | Aninhamento de CSS sem PostCSS |

| **Variáveis ​​CSS** | Todos os tokens expostos como variáveis ​​`--*` |

---

## 2. Configuração baseada em CSS

### Definição de tema

```
@theme {

/* Cores - use nomes semânticos */

--color-primary: oklch(0.7 0.15 250);
--color-surface: oklch(0.98 0 0);

--color-surface-dark: oklch(0.15 0 0);

/* Escala de espaçamento */

--spacing-xs: 0.25rem;

--spacing-sm: 0.5rem;

--spacing-md: 1rem;

--spacing-lg: 2rem;

/* Tipografia */

--font-sans: 'Inter', system-ui, sans-serif;

--font-mono: 'JetBrains Mono', monospace;

}
```

### Quando estender ou substituir

| Ação | Usar quando |

|--------|----------|

| **Estender** | Adicionando novos valores junto com os padrões |

| **Substituir** | Substituindo completamente a escala padrão |

| **Tokens semânticos** | Nomenclatura específica do projeto (primário, superficial) |

---

## 3. Consultas de contêiner (v4 Nativo)

### Ponto de interrupção vs. Contêiner

| Tipo | Responde a |

|------|-------------|

| **Ponto de interrupção** (`md:`) | Largura da viewport |

| **Contêiner** (`@container`) | Largura do elemento pai |

### Uso de consultas de contêiner

| Padrão | Classes |

|---------|---------|

| Definir contêiner | `@container` no elemento pai |

| Ponto de interrupção do contêiner | `@sm:`, `@md:`, `@lg:` nos elementos filhos |

| Contêineres nomeados | `@container/card` para especificidade |

### Quando usar

| Cenário | Uso |

|----------|-----|

| Layouts de página | Pontos de interrupção da viewport |

| Responsividade em nível de componente | Consultas de contêiner |

| Componentes reutilizáveis ​​| Consultas de contêiner (independentes de contexto) |


---

## 4. Design Responsivo

### Sistema de Pontos de Interrupção

| Prefixo | Largura Mínima | Alvo |

|--------|-----------|--------|

| (nenhum) | 0px | Base mobile-first |

| `sm:` | 640px | Celular grande / tablet pequeno |

| `md:` | 768px | Tablet |

| `lg:` | 1024px | Laptop |

| `xl:` | 1280px | Desktop |

| `2xl:` | 1536px | Desktop grande |

### Princípio Mobile-First

1. Escreva os estilos para dispositivos móveis primeiro (sem prefixo)
2. Adicione estilos para telas maiores com prefixos
3. Exemplo: `w-full md:w-1/2 lg:w-1/3`

---

## 5. Modo Escuro

### Estratégias de Configuração

| Método | Comportamento | Usar Quando |

|--------|----------|----------|

| `class` | A classe `.dark` alterna | Seletor manual de temas |

| `media` | Segue a preferência do sistema | Sem controle do usuário |

| `selector` | Seletor personalizado (v4) | Temas complexos |

### Padrão do Modo Escuro

| Elemento | Claro | Escuro |

|---------|-------|------|

| Fundo | `bg-white` | `dark:bg-zinc-900` |

| Texto | `text-zinc-900` | `dark:text-zinc-100` |

| Bordas | `border-zinc-200` | `dark:border-zinc-700` |

---

## 6. Padrões de Layout Modernos

### Padrões Flexbox

| Padrão | Classes |

|---------|---------|

| Centralizar (ambos os eixos) | `flex items-center justify-center` |

| Pilha vertical | `flex flex-col gap-4` |

| Linha horizontal | `flex gap-4` |

| Espaço entre | `flex justify-between items-center` |

| Grade com quebra de linha | `flex flex-wrap gap-4` |

### Padrões de Grade

| Padrão | Classes |

|---------|---------|

| Ajuste automático responsivo | `grid grid-cols-[repeat(auto-fit,minmax(250px,1fr))]` |

| Assimétrico (Bento) | `grid grid-cols-3 grid-rows-2` com spans |

| Layout com barra lateral | `grid grid-cols-[auto_1fr]` |

> **Nota:** Prefira layouts assimétricos/Bento a grades simétricas de 3 colunas.

---

## 7. Sistema de Cores Moderno

### OKLCH vs RGB/HSL

| Formato | Vantagem |

|--------|-----------|

| **OKLCH** | Perceptualmente uniforme, melhor para design |

| **HSL** | Matiz/saturação intuitivos |

| **RGB** | Compatibilidade com sistemas legados |

### Arquitetura de Tokens de Cor

| Camada | Exemplo | Finalidade |

|-------|---------|---------|

| **Primitivo** | `--blue-500` | Valores de cor brutos |

| **Semântico** | `--color-primary` | Nomenclatura baseada na finalidade |

| **Componente** | `--button-bg` | Específico do componente |

---

## 8. Sistema Tipográfico

### Padrão de Pilha de Fontes

| Tipo | Recomendado |

|------|-------------|

| Sans | `'Inter', 'SF Pro', system-ui, sans-serif` |

| Mono | `'JetBrains Mono', 'Fira Code', monospace` |

| Display | `'Outfit', 'Poppins', sans-serif` |

### Escala Tipográfica

| Classe | Tamanho | Uso |

|-------|------|-----|

| `text-xs` | 0,75rem | Rótulos, legendas |

| `text-sm` | 0,875rem | Texto secundário |

| `text-base` | 1rem | Texto corrido |

| `text-lg` | 1,125rem | Texto principal |

| `text-xl`+ | 1.25rem+ | Títulos |

---

## 9. Animações e Transições

### Animações Integradas

| Classe | Efeito |

|-------|--------|

| `animate-spin` | Rotação contínua |

| `animate-ping` | Pulso de atenção |

| `animate-pulse` | Pulso sutil de opacidade |

| `animate-bounce` | Efeito de quique |

### Padrões de Transição

| Padrão | Classes |

|---------|---------|

| Todas as propriedades | `transition-all duration-200` |

| Específico | `transition-colors duration-150` |

| Com suavização | `ease-out` ou `ease-in-out` |

| Efeito de foco | `hover:scale-105 transition-transform` |

---

## 10. Extração de Componentes

### Quando Extrair

| Sinal | Ação |

|--------|--------|

| Combinação de classes igual 3 ou mais vezes | Extrair componente |

| Variantes de estado complexas | Extrair componente |

| Elemento do sistema de design | Extrair + documento |

### Métodos de Extração

| Método | Usar Quando |

|--------|----------|

| **Componente React/Vue** | Dinâmico, requer JS |

| **@apply em CSS** | Estático, não requer JS |

| **Tokens de design** | Valores reutilizáveis ​​|

---

## 11. Antipadrões

| Não | Faça |

|-------|-----|

| Valores arbitrários em todos os lugares | Usar a escala do sistema de design |

| `!important` | Corrigir especificidade corretamente |

| `style=` embutido | Usar utilitários |

| Listas de classes longas duplicadas | Extrair componente |

| Misturar configuração v3 com v4 | Migrar totalmente para CSS-first |

| Usar `@apply` extensivamente | Priorizar componentes |


---

## 12. Princípios de Desempenho

| Princípio | Implementação |

|-----------|----------------|

| **Remover não utilizado** | Automático na v4 |

| **Evitar dinamismo** | Sem classes de string de modelo |

| **Usar Oxide** | Padrão na v4, 10x mais rápido |

| **Cachear builds** | Cache de CI/CD |

---

> **Lembre-se:** O Tailwind v4 prioriza o CSS. Adote variáveis ​​CSS, consultas de contêiner e recursos nativos. O arquivo de configuração agora é opcional.