--- 
name: design-Stitch-UI
description: "Orientação especializada para criar prompts eficazes no Google Stitch, a ferramenta de design de interface do usuário com inteligência artificial do Google Labs. Esta habilidade ajuda a criar prompts precisos e acionáveis ​​que geram designs de interface do usuário de alta qualidade para aplicativos web e mobile."
risk: seguro
source: própria
date_add: "27/02/2026"
---

# Stitch UI Design Prompting

Orientação especializada para criar prompts eficazes no Google Stitch, a ferramenta de design de interface do usuário com inteligência artificial do Google Labs. Esta habilidade ajuda a criar prompts precisos e acionáveis ​​que geram designs de interface do usuário de alta qualidade para aplicativos web e mobile.

## O que é o Google Stitch?

O Google Stitch é um gerador de interface do usuário com inteligência artificial experimental, baseado no Gemini 2.5 Flash, que transforma prompts de texto e referências visuais em designs de interface do usuário funcionais. Suporta:

- Geração de texto para interface do usuário a partir de prompts em linguagem natural
- Conversão de imagem para interface do usuário a partir de esboços, wireframes ou capturas de tela
- Fluxos de aplicativos com várias telas e layouts responsivos
- Exportação para HTML/CSS, Figma e código
- Refinamento iterativo com variantes e anotações

## Princípios Básicos de Prompting

### 1. Seja Específico e Detalhado

Prompts genéricos geram resultados genéricos. Prompts específicos com requisitos claros produzem designs personalizados e profissionais.

**Exemplo de prompt ruim:**
```
Criar um painel
```

**Exemplo eficaz:**

```
Painel de membros com grade de módulos do curso, barra de acompanhamento de progresso e barra lateral de feed da comunidade usando o tema roxo e layout baseado em cartões

```

**Por que funciona:** Especifica componentes (módulos, progresso, feed), estrutura do layout (grade, barra lateral), estilo visual (tema roxo, cartões) e contexto (painel de membros).

### 2. Defina o Estilo Visual e o Tema

Sempre inclua esquemas de cores, estética de design e direção visual para evitar resultados genéricos de IA.

**Componentes a especificar:**
- Paleta de cores (cores primárias, cores de destaque)
- Estilo de design (minimalista, moderno, lúdico, profissional, translúcido)
- Preferências tipográficas (se houver)
- Espaçamento e densidade (compacto, espaçoso, equilibrado)

**Exemplo:**
```
Página de produto de e-commerce com galeria de imagens principais, botão de adicionar ao carrinho,
seção de avaliações e carrossel de produtos relacionados. Use um design minimalista e limpo
com detalhes em verde sálvia e amplo espaço em branco.

```

### 3. Estruture Fluxos de Múltiplas Telas com Clareza

Para aplicativos com várias telas, liste cada tela em tópicos antes da geração.

**Abordagem:**
``` Aplicativo de monitoramento de atividades físicas com:
- Tela de boas-vindas com seleção de metas
- Painel inicial com estatísticas diárias e anéis de atividade
- Biblioteca de treinos com filtros por categoria
- Tela de perfil com conquistas e configurações
```

O Stitch solicitará confirmação antes de gerar várias telas, garantindo o alinhamento com sua visão.

### 4. Especifique a Plataforma e o Comportamento Responsivo

Indique se o design é para dispositivos móveis, tablets, desktops ou web responsiva.

**Exemplos:**
``` Tela de login do aplicativo móvel (estilo iOS) com campos de e-mail/senha e botões de autenticação social

Página inicial responsiva que se adapta de dispositivos móveis (320px) a desktops (1440px)
com navegação recolhível
```

### 5. Inclua os Requisitos Funcionais

Descreva os elementos interativos, estados e fluxos de usuário para gerar designs mais completos.

**Elementos a especificar:**
- Ações de botões e CTAs (chamadas para ação)
- Campos de formulário e validação
- Padrões de navegação
- Estados de carregamento
- Estados vazios
- Tratamento de erros

**Exemplo:**
```
Fluxo de finalização de compra com:
- Resumo do carrinho com ajustes de quantidade
- Formulário de endereço de entrega com validação
- Seleção do método de pagamento (cartões, PayPal, Apple Pay)
- Confirmação do pedido com número de rastreamento
```

## Modelo de Estrutura de Prompt

Use este modelo para prompts abrangentes:

```
[Tipo de Tela/Componente] para [Usuário/Contexto]

Principais Recursos:
- [Recurso 1 com detalhes específicos]
- [Recurso 2 com detalhes específicos]
- [Recurso 3 com detalhes específicos]

Estilo Visual:
- [Esquema de cores]
- [Estética do design]
- [Abordagem de layout]

Plataforma: [Mobile/Web/Responsivo]
```

**Exemplo:**

```
Painel de controle para plataforma de análise SaaS

Principais Recursos:
- Cartões com as principais métricas, mostrando Receita Recorrente Mensal (MRR), usuários ativos e taxa de cancelamento (churn rate)
- Gráfico de linhas para tendências de receita (últimos 30 dias)
- Feed de atividades recentes com ações do usuário
- Botões de ação rápida para relatórios e exportações

Estilo Visual:
- Modo escuro com detalhes em gradiente azul/roxo
- Cartões modernos com efeito vítreo e sombras sutis
- Visualização de dados clara com cores acessíveis

Plataforma: Web responsiva (desktop-first)
```

## Estratégias de Iteração

### Refine com Anotações

Use o recurso "anotar para editar" do Stitch para fazer alterações específicas sem precisar reescrever todo o prompt.

**Fluxo de trabalho:**
1. Gere o design inicial a partir do prompt
2. Anote os elementos específicos que precisam de alterações
3. Descreva as modificações em linguagem natural
4. Aplique as atualizações somente às áreas anotadas

**Exemplos de anotações:**
- "Aumente o tamanho deste botão e use a cor primária"
- "Adicione mais espaço entre estes cards"
- "Mude para um layout horizontal"

### Gerar variantes

Solicite várias variações para explorar diferentes direções de design:

```
Gere 3 variantes desta seção principal:
1. Focada em imagem com texto mínimo
2. Com bastante texto e gráficos de apoio
3. Vídeo de fundo com conteúdo sobreposto
```

### Refinamento progressivo

Comece com uma abordagem ampla e, em seguida, adicione especificidade em prompts subsequentes:

**Inicial:**
```
Página inicial de e-commerce
```

**Refinamento 1:**

```
Adicione uma seção de produtos em destaque com grade de 4 colunas e efeito hover Efeitos
```

**Aprimoramento 2:**
```
Atualizar esquema de cores para tons terrosos (terracota, sálvia, creme)
e adicionar banner promocional no topo
```

## Casos de Uso Comuns

### Páginas de Destino

```
Página de destino SaaS para [nome do produto]

Seções:
- Hero com título, subtítulo, CTA e captura de tela do produto
- Prova social com logotipos de clientes
- Grade de recursos (3 colunas) com ícones
- Carrossel de depoimentos
- Tabela de preços (3 níveis)
- Acordeão de perguntas frequentes
- Rodapé com links e inscrição para newsletter

Estilo: Moderno, profissional, que inspira confiança
Cores: Azul marinho como cor principal, detalhes em azul claro, fundo branco
```

### Aplicativos Móveis

```
Tela inicial de aplicativo de entrega de comida

Componentes:
- Barra de pesquisa com seletor de localização
- Chips de categoria (Pizza, Hambúrgueres, Sushi, etc.)
- Cartões de restaurantes Com imagem, nome, avaliação, prazo de entrega e faixa de preço
- Navegação inferior (Página Inicial, Busca, Pedidos, Perfil)

Estilo: Vibrante, apetitoso, fácil de visualizar
Cores: Laranja como cor principal, fundo branco, fotografia de alimentos
Plataforma: iOS (375px de largura)
```

### Painéis

```
Painel administrativo para sistema de gerenciamento de conteúdo

Layout:
- Barra lateral esquerda com menu recolhível
- Barra superior com busca, notificações e perfil do usuário
- Área de conteúdo principal com:

- Visão geral das estatísticas (4 cartões de métricas)

- Tabela de posts recentes com ações

- Linha do tempo de atividades

- Painel de ações rápidas

Estilo: Limpo, focado em dados, profissional
Cores: Tons neutros de cinza com detalhes em azul
Plataforma: Web desktop (1440px)
```

### Formulários e Entradas

```
Formulário de cadastro em várias etapas para plataforma B2B

Etapas:
1. Detalhes da conta (empresa) Nome, e-mail, senha)
2. Informações da empresa (setor, tamanho, cargo)
3. Configuração da equipe (convidar membros)
4. Confirmação com mensagem de sucesso

Recursos:
- Indicador de progresso na parte superior
- Validação de campos com erros em linha
- Navegação Anterior/Próximo
- Opção para pular a etapa 3

Estilo: Minimalista, focado, de fácil utilização
Cores: Fundo branco, verde para estados de sucesso
```

## Fluxo de Trabalho de Design para Código

### Opções de Exportação

O Stitch oferece vários formatos de exportação:

1. **HTML/CSS** - Marcação limpa e semântica para projetos web
2. **Figma** - "Colar no Figma" para integração com sistemas de design
3. **Snippet de código** - Exportações em nível de componente para frameworks

### Boas Práticas para Exportação

**Antes de exportar:**
- Verifique os breakpoints responsivos
- Verifique o contraste de cores para acessibilidade
- Certifique-se de que os estados interativos estejam definidos
- Revise a nomenclatura e a estrutura dos componentes

**Após a exportação:**
- Refatorar o código gerado para padrões de produção
- Adicionar tags HTML semânticas adequadas
- Implementar atributos de acessibilidade (rótulos ARIA, texto alternativo)
- Otimizar imagens e recursos
- Adicionar animações e microinterações

## Antipadrões a Evitar

### ❌ Instruções Vagas
```
Crie um site atraente
```

### ✅ Instruções Específicas
```
Site de portfólio para fotógrafo com galeria de imagens em tela cheia,
estudos de caso de projetos e formulário de contato. Estética minimalista em preto e branco
com tipografia serifada.

```

---

### ❌ Falta de Contexto
```
Crie uma página de login
```

### ✅ Instruções Ricas em Contexto
```
Página de login para portal de saúde com campos de e-mail/senha,
caixa de seleção "Lembrar-me", link "Esqueci minha senha" e opções de SSO (Google, Microsoft).
Design profissional e confiável com
tema médico azul.

```

---

### ❌ Sem Direção Visual
```
Crie um aplicativo para gerenciamento de tarefas
```

### ✅ Direção Visual Clara
```
Aplicativo de gerenciamento de tarefas com layout de quadro Kanban, cartões com recurso de arrastar e soltar,
rótulos de prioridade e indicadores de data de vencimento.
Design moderno e focado em produtividade,
com detalhes em gradiente roxo/turquesa e suporte ao modo escuro.

```

## Dicas para Melhores Resultados

1. **Consulte designs existentes** - Faça o upload de capturas de tela ou esboços como referências visuais junto com as instruções de texto.

2. **Use terminologia de design** - Termos como "seção principal", "layout de cartão", "glassmorphic" e "grade bento" ajudam o Stitch a entender sua intenção.

3. **Especifique as interações** - Descreva os estados de foco, as ações de clique e as transições para designs mais completos.

4. **Pense em componentes** - Divida telas complexas em componentes reutilizáveis ​​(cabeçalho, cartão, formulário etc.).

5. **Ite incrementalmente** - Faça pequenas alterações focadas em vez de redesenhos completos.

6. **Teste a responsividade** - Sempre verifique os designs em vários breakpoints (celular, tablet, desktop).

7. **Considere a acessibilidade** - Mencione o contraste de cores, os tamanhos de fonte e os tamanhos dos alvos de toque nas instruções.

8. **Aproveite as variantes** - Gere várias opções para explorar diferentes direções de design rapidamente.

## Integração com o Fluxo de Trabalho de Desenvolvimento

### Stitch → Figma → Código
1. Gere a interface do usuário no Stitch com instruções detalhadas
2. Exporte para o Figma para integração com o sistema de design
3. Entregue aos desenvolvedores com as especificações de design
4. Implemente com código pronto para produção

### Stitch → HTML → Framework
1. Gere e refine a interface do usuário no Stitch
2. Exporte o código HTML/CSS
3. Converta para componentes React/Vue/Svelte
4. Integre ao código-fonte do aplicativo

### Prototipagem Rápida
1. Crie várias variações de tela rapidamente
2. Teste com usuários ou stakeholders
3. Itere com base no feedback
4. Finalize o design para desenvolvimento

## Conclusão

Instruções eficazes no Stitch são específicas, ricas em contexto e visualmente descritivas. Seguindo esses princípios e modelos, você pode gerar designs de interface do usuário profissionais que servem como bases sólidas para aplicativos de produção.

**Lembre-se:** O Stitch é um ponto de partida, não um produto final. Use-a para acelerar o processo de design, explorar ideias rapidamente e estabelecer uma direção visual — refinando-a em seguida com base no julgamento humano e nos padrões de produção.

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.