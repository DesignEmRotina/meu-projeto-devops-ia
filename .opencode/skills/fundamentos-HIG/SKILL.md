--- 
name: fundamentos-HIG
description: Fundamentos de design das Diretrizes de Interface Humana da Apple.
risk: desconhecido
source: comunidade
date_add: '2026-02-27'
---

# Diretrizes de Interface Humana da Apple: Fundamentos de Design

Verifique o arquivo `.claude/apple-design-context.md` antes de fazer perguntas. Use o contexto existente e pergunte apenas sobre informações que ainda não foram abordadas.

## Princípios-chave

1. **Priorize o conteúdo em relação à interface.** Reduza a poluição visual. Use materiais fornecidos pelo sistema e separadores sutis em vez de bordas e fundos pesados.

2. **Incorpore a acessibilidade desde o início.** Projete para VoiceOver, Tipografia Dinâmica, Reduzir Movimento, Aumentar Contraste e Controle por Botão desde o primeiro dia. Todo elemento interativo precisa de um rótulo de acessibilidade.

3. **Use as cores e materiais do sistema.** As cores do sistema se adaptam ao modo claro/escuro, ao aumento do contraste e à vivacidade. Prefira cores semânticas (`label`, `secondaryLabel`, `systemBackground`) em vez de valores fixos.

4. **Use fontes e ícones da plataforma.** SF Pro, SF Compact e SF Mono por padrão. New York para fontes serifadas. Siga a hierarquia tipográfica nos tamanhos recomendados. Use SF Symbols para iconografia.

5. **Respeite as convenções da plataforma.** Alinhe a aparência e o comportamento com os padrões do sistema. Forneça manipulação direta e responsiva e feedback claro para cada ação.

6. **Respeite a privacidade.** Solicite permissões somente quando necessário, explique o motivo claramente e forneça valor antes de solicitar dados. Projete para coleta mínima de dados.

7. **Suporte à internacionalização.** Acomode a expansão de texto, scripts da direita para a esquerda e formatos variados de data/número. Use o Auto Layout para dimensionamento dinâmico de conteúdo.

8. **Use movimento com propósito.** A animação deve comunicar significado e relações espaciais. Respeite a opção Reduzir Movimento, fornecendo alternativas de transição gradual.

## Índice de Referências

| Referências | Tópico | Conteúdo principal |
|---|---|---|
| [accessibility.md](referencias/accessibility.md) | Acessibilidade | VoiceOver, Tipo Dinâmico, contraste de cores, acessibilidade motora, Controle por Botão, descrições de áudio |
| [app-icons.md](referencias/app-icons.md) | Ícones de Aplicativos | Grade de ícones, tamanhos específicos da plataforma, ponto focal único, sem transparência |
| [branding.md](referencias/branding.md) | Identidade Visual | Integrando a identidade da marca à linguagem de design da Apple, identidade visual sutil, tonalidades personalizadas |
| [color.md](referencias/color.md) | Cor | Cores do sistema, Cores Dinâmicas, cores semânticas, paletas personalizadas, taxas de contraste |
| [dark-mode.md](referencias/dark-mode.md) | Modo Escuro | Superfícies elevadas, cores semânticas, paletas adaptadas, vivacidade, testes em ambos os modos |
| [icons.md](referencias/icons.md) | Ícones | Ícones de glifos, integração com SF Symbols, design de ícones personalizados, pesos de ícones, alinhamento óptico |
| [images.md](referencias/images.md) | Imagens | Resolução de imagem, recursos @2x/@3x, recursos vetoriais, acessibilidade de imagem |
| [immersive-experiences.md](referencias/immersive-experiences.md) | Experiências Imersivas | Design de RA/RV, imersão espacial, zonas de conforto, níveis progressivos de imersão |
| [inclusion.md](referencias/inclusion.md) | Inclusão | Representação diversa, linguagem neutra em termos de gênero, sensibilidade cultural, configurações padrão inclusivas |
| [layout.md](referencias/layout.md) | Layout | Margens, espaçamento, alinhamento, áreas seguras, layouts adaptáveis, guias de conteúdo legíveis |
| [materials.md](referencias/materials.md) | Materiais | Vibração, desfoque, translucidez, materiais do sistema, espessura do material |
| [motion.md](referencias/motion.md) | Movimento | Curvas de animação, transições, continuidade, suporte a Reduzir Movimento, movimento baseado em física |
| [privacy.md](referencias/privacy.md) | Privacidade | Solicitações de permissão, descrições de uso, rótulos nutricionais de privacidade, coleta mínima de dados |
| [right-to-left.md](referencias/right-to-left.md) | Da direita para a esquerda | Espelhamento de layout RTL, texto bidirecional, ícones que invertem, exceções |
| [sf-symbols.md](referencias/sf-symbols.md) | Símbolos SF | Categorias de símbolos, modos de renderização, cor variável, símbolos personalizados, correspondência de peso |
| [spatial-layout.md](referencias/spatial-layout.md) | Layout Espacial | posicionamento de janelas do visionOS, profundidade, zonas ergonômicas, design do eixo Z |
| [typography.md](referencias/typography.md) | Tipografia | SF Pro, tamanhos de texto dinâmicos, estilos de texto, fontes personalizadas, hierarquia de pesos de fonte, espaçamento entre linhas |
| [writing.md](referencias/writing.md) | Escrita | Diretrizes de texto da interface do usuário, tom, regras de capitalização, mensagens de erro, rótulos de botões, concisão |

## Aplicando os Fundamentos em Conjunto

Considere como os princípios interagem:

1. **Cor + Modo Escuro + Acessibilidade** -- Paletas personalizadas devem funcionar em ambos os modos, mantendo as taxas de contraste das WCAG. Comece com as cores semânticas do sistema.

2. **Tipografia + Acessibilidade + Layout** -- O Dynamic Type deve ser dimensionado sem quebrar os layouts. Use estilos de texto e Auto Layout para toda a gama de tamanhos de fonte.

3. **Ícones + Identidade Visual + Símbolos SF** -- Ícones personalizados devem corresponder à espessura e ao tamanho óptico dos Símbolos SF. Elementos da marca devem se integrar sem sobrescrever as convenções do sistema.

4. **Movimento + Acessibilidade + Feedback** -- Toda animação deve ter uma alternativa de Redução de Movimento. O movimento deve reforçar as relações espaciais, não apenas decorar.

5. **Privacidade + Escrita + Integração** -- As solicitações de permissão precisam de descrições de uso claras e específicas. Programe-as para que o usuário entenda o benefício.

## Formato de Saída

1. **Cite o fundamento HIG específico** com arquivo e seção.

2. **Observe as diferenças entre as plataformas** para as plataformas-alvo do usuário.
3. **Forneça padrões de código concretos** (SwiftUI/UIKit/AppKit).

4. **Explique o impacto na acessibilidade** (taxas de contraste, dimensionamento do Dynamic Type, comportamento do VoiceOver).

## Perguntas a fazer

1. Quais plataformas você está visando?

2. Você já possui diretrizes de marca?

3. Qual o nível de acessibilidade que você está buscando? (WCAG AA, AAA, Apple Baseline?)
4. Cores do sistema ou personalizadas?

## Habilidades Relacionadas

- **hig-platforms** -- Como os fundamentos se aplicam a cada plataforma (por exemplo, diferenças de escala tipográfica no watchOS versus macOS)
- **hig-patterns** -- Padrões de interação onde fundamentos como escrita e acessibilidade são essenciais
- **hig-components-layout** -- Componentes estruturais que implementam princípios de layout
- **hig-components-content** -- Exibição de conteúdo usando cores, tipografia e imagens

---

*Desenvolvido por [Raintree Technology](https://raintree.technology) · [Mais ferramentas para desenvolvedores](https://raintree.technology)*

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.