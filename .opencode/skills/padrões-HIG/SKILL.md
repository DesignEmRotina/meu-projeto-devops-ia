--- 
name: padrões-HIG
descripition: Diretrizes de Interface Humana da Apple para padrões de interação e UX.
risk: desconhecido
source: comunidade
date_add: '2026-02-27'
---

# Diretrizes de Interface Humana da Apple: Padrões de Interação

Verifique o arquivo `.claude/apple-design-context.md` antes de fazer perguntas. Use o contexto existente e pergunte apenas sobre informações que ainda não foram abordadas.

## Princípios-chave

1. **Minimize a modalidade.** Use a modalidade apenas quando for essencial para chamar a atenção, quando uma tarefa precisar ser concluída ou abandonada, ou quando salvar as alterações for fundamental. Prefira alternativas não modais.

2. **Forneça feedback claro.** Toda ação deve produzir uma resposta visível, sonora ou tátil. Indicadores de atividade para esperas indeterminadas, barras de progresso para esperas determinadas e feedback tátil para confirmação física.

3. **Prefira o recurso de desfazer em vez de diálogos de confirmação.** Ações destrutivas devem ser reversíveis sempre que possível. Desfazer é quase sempre melhor do que "Tem certeza?"

4. **Inicie rapidamente.** Exiba uma tela inicial que faça a transição perfeita para a primeira tela. Sem telas de apresentação com logotipos. Restaure o estado anterior.

5. **Adie o login.** Permita que os usuários explorem antes de exigir a criação de uma conta. Ofereça suporte ao Login com a Apple e chaves de acesso.

6. **Mantenha a integração breve.** No máximo três telas. Permita que os usuários pulem algumas etapas. Ensine por meio de divulgação progressiva e dicas contextuais.

7. **Use divulgação progressiva.** Mostre o essencial primeiro e permita que os usuários explorem os detalhes. Não sobrecarregue com todas as opções em uma única tela.

8. **Respeite a atenção do usuário.** Consolide as notificações, minimize as interrupções e dê aos usuários controle sobre os alertas. Nunca use notificações para marketing.

## Índice de Referências

| Referência | Tópico | Conteúdo principal |

|---|---|---|

| [charting-data.md](referencias/charting-data.md) | Gráficos de Dados | Padrões de visualização de dados, gráficos acessíveis, elementos interativos |
| [collaboration-and-sharing.md](referencias/collaboration-and-sharing.md) | Colaboração e Compartilhamento | Planilhas de compartilhamento, visualizações de atividades, edição colaborativa, SharePlay |
| [drag-and-drop.md](referencias/drag-and-drop.md) | Arrastar e Soltar | Origens de arrastar, destinos de soltar, carregamento por mola, arrastar vários itens, feedback visual |
| [entering-data.md](referencias/entering-data.md) | Inserção de Dados | Campos de texto, seletores, indicadores passo a passo, validação de entrada, tipos de teclado, preenchimento automático |
| [feedback.md](referencias/feedback.md) | Feedback | Alertas, folhas de ação, padrões táteis, feedback sonoro, indicadores visuais |
| [file-management.md](referencias/file-management.md) | Gerenciamento de Arquivos | Navegador de documentos, provedores de arquivos, integração com o iCloud, ciclo de vida do documento |
| [going-full-screen.md](referencias/going-full-screen.md) | Tela Cheia | Transições para tela cheia, conteúdo imersivo, saída da tela cheia |
| [launching.md](referencias/launching.md) | Inicialização | Telas de inicialização, restauração de estado, inicialização a frio vs. inicialização a quente |
| [live-viewing-apps.md](referencias/live-viewing-apps.md) | Aplicativos de Visualização ao Vivo | Exibição de conteúdo ao vivo, atualizações em tempo real, Atividades ao Vivo, Ilha Dinâmica |
| [loading.md](referencias/loading.md) | Carregamento | Indicadores de atividade, visualizações de progresso, telas de esqueleto, carregamento lento, espaços reservados |
| [managing-accounts.md](referencias/managing-accounts.md) | Gerenciando Contas | Iniciar sessão com a Apple, chaves de acesso, criação de conta, preenchimento automático de credenciais, exclusão de conta |
| [managing-notifications.md](referencias/managing-notifications.md) | Gerenciando Notificações | Solicitações de permissão, agrupamento, notificações acionáveis, entrega provisória |
| [modality.md](referencias/modality.md) | Modalidade | Folhas, alertas, pop-ups, modais em tela cheia, quando usar cada um |
| [multitasking.md](referencias/multitasking.md) | Multitarefa | Visualização dividida do iPad, Slide Over, Stage Manager, layout responsivo, transições de classe de tamanho |
| [offering-help.md](referencias/offering-help.md) | Oferecendo Ajuda | Dicas contextuais, dicas de integração, menus de ajuda, links de suporte |
| [onboarding.md](referencias/onboarding.md) | Integração | Telas de boas-vindas, destaques de recursos, integração progressiva, opções de pular |
| [playing-audio.md](referencias/playing-audio.md) | Reproduzindo áudio | Sessões de áudio, áudio em segundo plano, Reproduzindo agora, roteamento de áudio, interrupções |
| [playing-haptics.md](referencias/playing-haptics.md) | Reproduzindo feedback tátil | Feedback tátil principal, UIFeedbackGenerator, padrões táteis, feedback tátil personalizado |
| [playing-video.md](referencias/playing-video.md) | Reproduzindo vídeo | Controles do reprodutor de vídeo, imagem em imagem, AirPlay, vídeo em tela cheia |
| [printing.md](referencias/printing.md) | Impressão | Diálogos de impressão, configuração de página, integração com AirPrint |
| [ratings-and-reviews.md](referencias/ratings-and-reviews.md) | Avaliações e Comentários | SKStoreReviewController, tempo, limites de frequência, feedback no aplicativo |
| [searching.md](referencias/searching.md) | Busca | Barras de pesquisa, sugestões, pesquisa com escopo, exibição de resultados, recentes |
| [settings.md](referencias/settings.md) | Configurações | No aplicativo vs. aplicativo Configurações, organização de preferências, alternâncias, padrões |
| [undo-and-redo.md](referencias/undo-and-redo.md) | Desfazer e Refazer | Agitar para desfazer, pilha de desfazer/refazer, desfazer em vários níveis |
| [workouts.md](referencias/workouts.md) | Treinos | Sessões de treino, métricas ao vivo, exibição Sempre Ativa, resumos, HealthKit |

## Guia de Seleção de Padrões

| Objetivo do Usuário | Padrão Recomendado | Evitar |

|---|---|---|

| Primeira experiência com o aplicativo | Breve integração (máximo de 3 telas) + divulgação progressiva | Tutoriais longos, cadastro obrigatório |

| Aguardando conteúdo | Telas de esqueleto ou indicadores de progresso | Bloqueadores de carregamento sem contexto |

| Confirmando ação destrutiva | Suporte para desfazer | Diálogos excessivos de "Tem certeza?" |

| Coletando entrada do usuário | Validação em linha, valores padrão inteligentes, preenchimento automático | Formulários modais para entradas simples |

| Solicitando permissões | Contextual, no momento certo com explicação | Solicitando todas as permissões na inicialização |

| Fornecendo feedback | Háptica + indicador visual | Ações silenciosas sem confirmação |

| Organizando preferências | Configurações no aplicativo para itens frequentes | Ocultando todas as configurações no aplicativo Configurações do sistema |

## Formato de Saída

1. **Padrão recomendado com justificativa**, citando o arquivo de referência relevante.

2. **Implementação passo a passo**, abrangendo cada tela ou estado.
3. **Variações de plataforma** para as plataformas-alvo.

4. **Armadilhas comuns** que violam as Diretrizes de Interface Humana (HIG) para este padrão.

## Perguntas a fazer

1. Onde no aplicativo este padrão aparece? O que vem antes e depois?

2. Quais plataformas?

3. Está criando um novo design ou aprimorando um fluxo existente?

4. Isso envolve ações sensíveis? (Operações destrutivas, pagamentos, permissões)

## Habilidades relacionadas

- **hig-foundations** -- Princípios de acessibilidade, cor, tipografia e privacidade que fundamentam cada padrão
- **hig-platforms** -- Implementações de padrões específicas para cada plataforma
- **hig-components-layout** -- Componentes estruturais (barras de abas, barras laterais, visualizações divididas) para padrões de navegação
- **hig-components-content** -- Exibição de conteúdo em padrões (gráficos, coleções, resultados de pesquisa)

---

*Desenvolvido por [Raintree Technology](https://raintree.technology) · [Mais ferramentas para desenvolvedores](https://raintree.technology)*

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.