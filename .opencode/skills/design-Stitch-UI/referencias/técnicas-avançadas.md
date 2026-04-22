# Técnicas Avançadas do Stitch

Estratégias avançadas para maximizar os recursos do Stitch e criar designs prontos para produção.

## Sumário

1. [Fluxos de Trabalho de Imagem para Interface do Usuário](#image-to-ui-workflows)
2. [Integração de Sistemas de Design](#design-system-integration)
3. [Estratégias de Design Responsivo](#responsive-design-strategies)
4. [Considerações de Acessibilidade](#accessibility-considerations)
5. [Otimização de Desempenho](#performance-optimization)
6. [Reutilização de Componentes](#component-reusability)

---

## Fluxos de Trabalho de Imagem para Interface do Usuário

### Convertendo Esboços em Interfaces Digitais

O Stitch pode interpretar esboços à mão, wireframes e protótipos preliminares.

**Melhores práticas:**

1. **Estrutura clara** - Desenhe caixas distintas para os componentes
2. **Rotule os elementos** - Anote botões, campos de entrada e seções
3. **Mostre a hierarquia** - Use tamanho e posição para indicar importância
4. **Inclua notas** - Adicione texto descrevendo interações ou estados

**Exemplo de fluxo de trabalho:**

1. Esboce o wireframe em papel ou tablet
2. Tire uma foto nítida ou digitalize
3. Envie para o Stitch com a seguinte instrução:

"Converta este wireframe em uma interface web moderna com design glassmorphic e detalhes em gradiente roxo"
4. Refine o design gerado com anotações

### Design baseado em referência

Envie capturas de tela de designs existentes para criar layouts semelhantes com sua própria identidade visual.

**Estrutura do prompt:**
``` Crie um [tipo] semelhante a esta imagem de referência, mas com:
- [Seu esquema de cores]
- [Seu conteúdo/texto]
- [Seu estilo de marca]
- [Modificações específicas]
```

**Exemplo:**
```
Crie uma página de preços semelhante a esta referência, mas com:
- Esquema de cores azul-marinho e dourado
- 4 níveis de preços em vez de 3
- Opção de assinatura anual/mensal
- Tabela de comparação de recursos abaixo
- Seção de depoimentos na parte inferior
```

---

## Integração do Sistema de Design

### Estabelecendo Tokens de Design

Defina tokens de design reutilizáveis ​​no seu prompt inicial para garantir consistência entre as telas.

**Categorias de tokens:**
- Cores (primária, secundária, de destaque, neutra, semântica)
- Tipografia (famílias de fontes, tamanhos, pesos, alturas de linha)
- Espaçamento (escala: 4px, 8px, 16px, 24px, 32px, 48px, 64px)
- Raio da borda (nenhum, pequeno, médio, grande, completo)
- Sombras (níveis de elevação)

**Exemplo de prompt:**
```
Painel usando este sistema de design:

Cores:
- Primária: #2563EB (azul)
- Secundária: #7C3AED (roxo)
- Sucesso: #10B981 (verde)
- Aviso: #F59E0B (âmbar)
- Erro: #EF4444 (vermelho)
- Neutra: #6B7280 (cinza)

Tipografia:
- Títulos: Inter Negrito
- Corpo: Inter Regular
- Código: JetBrains Mono

Espaçamento: unidade base de 8px
Raio da borda: 8px para cartões, 4px para botões
Sombras: Elevação sutil com 0 4px 6px rgba(0,0,0,0.1)
```

### Abordagem de Biblioteca de Componentes

Crie uma biblioteca de componentes gerando componentes individuais primeiro e, em seguida, compondo-os em telas completas.

**Fluxo de trabalho:**

1. Gerar componentes básicos:

- Variantes de botões (primário, secundário, contorno, fantasma)

- Campos de entrada (texto, e-mail, senha, pesquisa)

- Cartões (básico, com imagem, com ações)

- Navegação (cabeçalho, barra lateral, abas)

2. Documentar as especificações dos componentes:

- Estados (padrão, foco, ativo, desativado)

- Tamanhos (pequeno, médio, grande)

- Variantes

3. Compor telas usando componentes estabelecidos:

"Criar uma página de configurações usando os componentes de botão e entrada

das gerações anteriores"

---

## Estratégias de Design Responsivo

### Abordagem Mobile-First

Comece com o design para dispositivos móveis e, em seguida, expanda para tablets e desktops.

**Sequência de instruções:**

**Etapa 1 - Dispositivos móveis (375px):**

```
Tela inicial do aplicativo móvel para plataforma de receitas

Layout:
- Seções verticais empilhadas
- Cartões de largura total
- Navegação inferior
- Menu hambúrguer

Conteúdo:
- Barra de pesquisa no topo
- Cartão principal com a receita em destaque
- Chips de categoria (rolagem horizontal)
- Grade de receitas (1 coluna)
```

**Etapa 2 - Tablet (768px):**

```
Adaptar a tela inicial de receitas para tablet:
- Grade de receitas com 2 colunas
- Navegação lateral permanente (substitui o menu hambúrguer)
- Cartão principal com a receita em destaque maior e layout lado a lado
- Chips de categoria permanecem roláveis
```

**Etapa 3 - Desktop (1440px):**

```
Adaptar para desktop:
- Grade de receitas com 3 colunas
- Barra lateral completa com categorias expandidas
- Seção principal com 3 receitas em destaque
- Barra de navegação superior com Pesquisa e menu do usuário
```

### Instruções específicas para breakpoints

Especifique breakpoints exatos e alterações de layout.

**Exemplo:**
```
Grade de produtos responsiva:

Dispositivos móveis (< 640px):
- 1 coluna
- Cartões de largura total
- Orientação vertical da imagem

Tablets (640px - 1024px):
- 2 colunas
- Imagens quadradas
- Layout de cartão compacto

Desktops (> 1024px):
- 4 colunas
- Efeitos de foco com sobreposição
- Botão de visualização rápida
```

---

## Considerações sobre acessibilidade

### Avisos de conformidade com as WCAG

Inclua os requisitos de acessibilidade diretamente nos avisos.

**Áreas-chave a especificar:**

1. **Contraste de cores**

``` Garanta que todo o texto atenda aos padrões WCAG AA:
- Texto normal: taxa de contraste mínima de 4,5:1
- Texto grande (18pt ou mais): taxa de contraste mínima de 3:1
- Elementos interativos: estados de foco claros com contraste de 3:1
```

2. **Áreas de toque**

``` Todos os elementos interativos com tamanho mínimo de 44x44px
Espaçamento adequado entre elementos clicáveis ​​(mínimo de 8px)
```

3. **Navegação por teclado**

```
Indicadores de foco claros em todos os elementos interativos
Ordem de tabulação lógica seguindo o fluxo visual
Link para pular a navegação para usuários de teclado
```

4. **Suporte a leitores de tela**

``` Rótulos de botões descritivos (não apenas "Clique aqui")
Texto alternativo para todas as imagens relevantes
Rótulos de formulário devidamente associados às entradas
Hierarquia de títulos (H1 → H2 → H3)
```

**Prompt de acessibilidade abrangente:**
```
Crie um formulário de contato acessível:

Campos:
- Nome (obrigatório, com aria-required)
- E-mail (obrigatório, com validação e mensagem de erro)
- Assunto (lista suspensa com rótulos claros)
- Mensagem (área de texto com contador de caracteres)

Recursos de acessibilidade:
- Todos os campos têm rótulos visíveis
- Campos obrigatórios marcados com asterisco e aria-required
- Mensagens de erro com role="alert"
- Botão Enviar com texto descritivo
- Indicadores de foco com contorno azul de 3px
- Contraste de cores em conformidade com as diretrizes WCAG AA
- Áreas de toque com tamanho mínimo de 44x44px

Estilo: Limpo, focado no formulário, alto contraste
Cores: Texto escuro em fundo claro, vermelho para erros
```

### Padrões de Design Inclusivo

**Considere usuários diversos:**

```
Projete uma interface de reprodutor de vídeo que suporte:
- Legendas Alternar
- Opção de descrição de áudio
- Atalhos de teclado (espaço para reproduzir/pausar, setas para avançar/retroceder)
- Controle de velocidade de reprodução
- Modo de alto contraste
- Opção de movimento reduzido (desativar animações)
```

---

## Otimização de desempenho

### Solicitações de recursos otimizadas

Solicite designs com foco em desempenho desde o início.

**Otimização de imagens:**
```
Galeria de produtos de e-commerce com otimização de desempenho:
- Carregamento lento para imagens abaixo da dobra
- Imagens em miniatura (200x200px) para a grade
- Imagens em tamanho real (1200x1200px) somente ao clicar
- Formato WebP com fallback para JPEG
- Desfoque do texto de exemplo durante o carregamento
```

**Eficiência do código:**
```
Geração de HTML/CSS leve, sem:
- Divs de encapsulamento desnecessárias
- Estilos embutidos (use classes)
- Grandes dependências externas
- Regras CSS redundantes
```

### Aprimoramento Progressivo

Projete primeiro a funcionalidade principal e, em seguida, aprimore-a.

**Exemplo:**

``` Crie uma lista de produtos filtrável com aprimoramento progressivo:

Base (sem JavaScript):
- Grade de produtos renderizada no servidor
- Filtros baseados em formulário com botão de envio
- Links de paginação

Aprimorado (com JavaScript):
- Atualizações de filtro AJAX sem recarregar a página
- Rolagem infinita
- Animações suaves
- Busca em tempo real
```

---

## Reutilização de Componentes

### Metodologia de Design Atômico

Construir a partir de átomos → moléculas → organismos → modelos → páginas.

**Átomos (elementos básicos):**

``` Gere átomos do sistema de design:
- Botão (primário, secundário, contorno, fantasma, perigo)
- Campo de entrada (texto, e-mail, senha, pesquisa, área de texto)
- Rótulo, distintivo, etiqueta
- Conjunto de ícones (24x24px, estilo consistente)
- Avatar (círculo, quadrado, com indicador de status)
```

**Moléculas (combinações simples):**

``` Crie moléculas usando átomos:
- Barra de pesquisa (entrada + botão + ícone)
- Campo de formulário (rótulo + entrada + mensagem de erro)
- Cabeçalho do cartão (avatar + nome + data e hora + menu)
- Cartão de estatísticas (ícone + rótulo + valor + tendência)

```

**Organismos (componentes complexos):**

``` Crie organismos a partir de moléculas:
- Barra de navegação (logotipo + barra de pesquisa + menu do usuário)
- Cartão do produto (imagem + título + preço + avaliação + botão)
- Tópico de comentários (avatar + nome + data e hora) + texto + ações)
- Tabela de dados (cabeçalhos + linhas + paginação + filtros)
```

**Modelos (layouts de página):**
```
Componha modelos a partir de componentes:
- Layout do painel (barra lateral + cabeçalho + grade de conteúdo)
- Layout do artigo (cabeçalho + destaque + conteúdo + barra lateral)
- Fluxo de finalização de compra (progresso + formulário + resumo)
```

### Geração de variantes

Crie variações sistemáticas de componentes.

**Opções para variantes do botão:**
``` Gere o componente de botão com todas as variantes:

Tamanhos: Pequeno (32px), Médio (40px), Grande (48px)

Tipos:
- Primário (preenchido, cor da marca)
- Secundário (preenchido, cinza)
- Contorno (apenas borda)
- Fantasma (transparente, fundo ao passar o mouse)
- Perigo (preenchido, vermelho)

Estados para cada variante:
- Padrão
- Ao passar o mouse
- Ativo (pressionado)
- Desativado
- Carregando (com indicador de carregamento)

Incluir: Suporte a ícones (esquerda/direita), opção de largura total
```

---

## Técnicas Avançadas de Iteração

### Variações Condicionais

Gere múltiplas versões com base em diferentes condições.

**Exemplo:**
```
Crie 3 variantes da seção principal para testes A/B:

Variante A - Focada em Imagem:
- Imagem de fundo grande
- Sobreposição de texto mínima
- Botão de chamada à ação único

Variante B - Focada em Texto:
- Fundo de cor sólida
- Texto detalhado com marcadores
- Dois botões de chamada à ação (principal + secundário)

Variante C - Focada em Vídeo:
- Vídeo de fundo
- Texto mínimo
- Botão de reprodução + chamada à ação

Todas as variantes usam as mesmas cores da marca e mantêm a responsividade para dispositivos móveis.
```

### Design Baseado em Estados

Projete para todos os estados possíveis, não apenas para o estado ideal.

**Prompt de estado abrangente:**

``` Projete uma tabela de dados com todos os estados:

Estado padrão:
- 10 linhas de dados
- Colunas classificáveis
- Paginação

Estado de carregamento:
- Carregadores básicos para as linhas
- Controles desativados

Estado vazio:
- Ilustração
- Mensagem "Nenhum dado encontrado"
- Botão CTA "Adicionar novo"

Estado de erro:
- Ícone de erro
- Mensagem de erro
- Botão "Tentar novamente"

Pesquisa/Filtro ativo:
- Filtros aplicados exibidos como marcadores
- Opção para limpar filtros
- Contagem de resultados

Linhas selecionadas:
- Seleção por caixa de seleção
- Barra de ferramentas de ações em massa
- Opção para selecionar tudo
```

---

## Melhores práticas de exportação e entrega

### Preparando para o desenvolvimento

Antes de exportar, certifique-se de que os designs estejam prontos para o desenvolvimento.

**Lista de verificação pré-exportação:**

1. **Convenções de nomenclatura**

- Use nomes de classe semânticos

- Siga a metodologia BEM ou uma metodologia consistente

- Nomeie os componentes claramente

2. **Documentação**

- Adicione comentários para interações complexas

- Documente os breakpoints responsivos

- Observe qualquer comportamento JavaScript necessário

3. **Organização de recursos**

- Exporte imagens nos tamanhos corretos

- Forneça SVG para ícones

- Inclua arquivos de fonte ou links de CDN

4. **Especificações**

- Documente os valores de espaçamento

- Liste os códigos hexadecimais das cores

- Especifique os tamanhos e pesos das fontes

### Integração com o Figma

Otimize o fluxo de trabalho Stitch → Figma.

**Passos:**

1. Gere o design no Stitch com especificações detalhadas
2. Use a opção "Colar no Figma" para exportar
3. No Figma:

- Organize as camadas com nomes claros
- Crie componentes a partir de elementos repetidos
- Configure o layout automático para comportamento responsivo
- Defina estilos de cor e texto

- Adicione a documentação do sistema de design
4. Compartilhe com os desenvolvedores usando o modo de inspeção do Figma

### Aprimoramento da Exportação de Código

Aprimore o HTML/CSS exportado para produção.

**Tarefas pós-exportação:**

1. **HTML semântico**

- Substituir divs por tags semânticas (cabeçalho, navegação, principal, artigo, seção, rodapé)

- Adicionar rótulos ARIA onde necessário

- Garantir a hierarquia correta dos títulos

2. **Otimização de CSS**

- Extrair estilos repetidos para classes utilitárias

- Usar propriedades CSS personalizadas para valores de tema

- Organizar com metodologia (BEM, SMACSS, etc.)

- Adicionar media queries responsivas, se necessário

3. **Acessibilidade**

- Adicionar texto alternativo às imagens

- Garantir que os rótulos dos formulários estejam associados

- Adicionar estilos de foco

- Testar com leitor de tela

4. **Desempenho**

- Otimizar imagens

- Minificar CSS

- Remover estilos não utilizados

- Adicionar estratégias de carregamento

---

## Conclusão

Essas técnicas avançadas ajudam você a ir além do uso básico do Stitch para criar designs prontos para produção, acessíveis e com bom desempenho. Combine essas estratégias com os princípios básicos de prompting para maximizar sua eficiência e a qualidade da saída.

**Principais conclusões:**
- Use imagens e referências para acelerar o design
- Estabeleça sistemas de design desde o início para garantir consistência
- Projete de forma responsiva desde o princípio
- Priorize a acessibilidade em cada etapa do processo
- Pense em componentes reutilizáveis
- Planeje para todos os cenários, não apenas para os ideais
- Refine as exportações antes do uso em produção