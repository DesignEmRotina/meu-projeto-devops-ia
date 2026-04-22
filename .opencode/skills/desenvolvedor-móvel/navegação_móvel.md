# Referência de Navegação Mobile

> Padrões de navegação, deep linking, tratamento do botão voltar e decisões entre tab/stack/drawer.
> **A navegação é o esqueleto do seu app — se você errar aqui, tudo parece quebrado.**

---

## 1. Árvore de Decisão para Seleção de Navegação

```
QUE TIPO DE APP?
        │
        ├── 3–5 seções de alto nível (importância igual)
        │   └── ✅ Barra de Abas / Navegação Inferior
        │       Exemplos: Social, E-commerce, Utilitários
        │
        ├── Conteúdo hierárquico profundo (drill down)
        │   └── ✅ Navegação em Stack
        │       Exemplos: Configurações, pastas de e-mail
        │
        ├── Muitos destinos (>5 de alto nível)
        │   └── ✅ Navegação em Drawer
        │       Exemplos: Gmail, apps corporativos complexos
        │
        ├── Fluxo linear único
        │   └── ✅ Apenas Stack (wizard/onboarding)
        │       Exemplos: Checkout, fluxo de configuração
        │
        └── Tablet / Dobrável
            └── ✅ Navigation Rail + Lista-Detalhe
                Exemplos: Mail, Notas no iPad
```

---

## 2. Navegação por Abas (Tab Bar)

### Quando Usar

```
✅ USE Tab Bar quando:
├── 3–5 destinos de alto nível
├── Destinos têm a mesma importância
├── Usuário alterna com frequência entre eles
├── Cada aba tem stack de navegação independente
└── App é usado em sessões curtas

❌ EVITE Tab Bar quando:
├── Mais de 5 destinos
├── Destinos possuem hierarquia clara
├── Abas seriam usadas de forma muito desigual
└── Conteúdo segue um fluxo sequencial
```

### Boas Práticas para Tab Bar

```
Tab Bar no iOS:
├── Altura: 49pt (83pt com indicador de home)
├── Máx. itens: 5
├── Ícones: SF Symbols, 25×25pt
├── Rótulos: Sempre visíveis (acessibilidade)
├── Indicador ativo: Cor de destaque

Bottom Navigation no Android:
├── Altura: 80dp
├── Máx. itens: 5 (ideal 3–5)
├── Ícones: Material Symbols, 24dp
├── Rótulos: Sempre visíveis
├── Indicador ativo: Formato pill + ícone preenchido
```

### Preservação de Estado das Abas

```
REGRA: Cada aba mantém sua própria stack de navegação.

Jornada do usuário:
1. Aba Home → Entrar em um item → Adicionar ao carrinho
2. Trocar para a aba Perfil
3. Voltar para a aba Home
→ Deve retornar à tela "Adicionar ao carrinho", NÃO à raiz da Home

Implementação:
├── React Navigation: Cada aba tem seu próprio navigator
├── Flutter: IndexedStack para preservar estado
└── Nunca resetar a stack ao trocar de aba
```

---

## 3. Navegação em Stack

### Conceitos Básicos

```
Metáfora da Stack: Cartas empilhadas umas sobre as outras

Push: Adiciona uma tela no topo
Pop: Remove a tela do topo (voltar)
Replace: Substitui a tela atual
Reset: Limpa a stack e define uma nova raiz

Visual: Nova tela desliza da direita para a esquerda (LTR)
Voltar: Tela desliza para a direita
```

### Padrões de Stack

| Padrão             | Caso de Uso              | Implementação       |
| ------------------ | ------------------------ | ------------------- |
| **Stack Simples**  | Fluxo linear             | Push a cada etapa   |
| **Stack Aninhada** | Seções com sub-navegação | Stack dentro da aba |
| **Stack Modal**    | Tarefas focadas          | Apresentação modal  |
| **Stack de Auth**  | Login vs App principal   | Raiz condicional    |

### Tratamento do Botão Voltar

```
iOS:
├── Swipe da borda esquerda (sistema)
├── Botão voltar na barra (opcional)
├── Gesto interativo de pop
└── Nunca sobrescreva o swipe sem um bom motivo

Android:
├── Botão/gesto voltar do sistema
├── Botão “Up” na toolbar (opcional)
├── Animação de back preditivo (Android 14+)
└── Deve tratar corretamente o back (Activity/Fragment)

Regra Multiplataforma:
├── Voltar SEMPRE sobe na stack
├── Nunca hijack do botão voltar
├── Confirmar antes de descartar dados não salvos
└── Deep links devem permitir navegação completa de volta
```

---

## 4. Navegação em Drawer

### Quando Usar

```
✅ USE Drawer quando:
├── Mais de 5 destinos de alto nível
├── Destinos menos acessados com frequência
├── App complexo com muitos recursos
├── Necessidade de branding/info do usuário
└── Tablet/tela grande com drawer persistente

❌ EVITE Drawer quando:
├── 5 ou menos destinos (use abas)
├── Todos os destinos são igualmente importantes
├── App simples, mobile-first
└── Descoberta é crítica (drawer fica escondido)
```

### Padrões de Drawer

```
Drawer Modal:
├── Abre sobre o conteúdo (com scrim)
├── Swipe da borda para abrir
├── Ícone hambúrguer ( ☰ )
└── Mais comum em mobile

Drawer Permanente:
├── Sempre visível (telas grandes)
├── Conteúdo desloca para o lado
├── Bom para apps de produtividade
└── Tablets e desktops

Navigation Rail (Android):
├── Faixa vertical estreita
├── Ícones + rótulos opcionais
├── Para tablets em retrato
└── Largura de 80dp
```

---

## 5. Navegação Modal

### Modal vs Push

```
PUSH (Stack):                  MODAL:
├── Slide horizontal           ├── Slide vertical (sheet)
├── Parte da hierarquia        ├── Tarefa separada
├── Voltar retorna             ├── Fechar (X) retorna
├── Mesmo contexto             ├── Contexto próprio
└── “Explorar”                 └── “Focar na tarefa”

USE MODAL para:
├── Criar novo conteúdo
├── Configurações/preferências
├── Concluir uma transação
├── Fluxos autocontidos
├── Ações rápidas
```

### Tipos de Modal

| Tipo             | iOS                | Android           | Caso de Uso           |
| ---------------- | ------------------ | ----------------- | --------------------- |
| **Sheet**        | `.sheet`           | Bottom Sheet      | Tarefas rápidas       |
| **Tela Cheia**   | `.fullScreenCover` | Activity inteira  | Formulários complexos |
| **Alerta**       | Alert              | Dialog            | Confirmações          |
| **Action Sheet** | Action Sheet       | Menu/Bottom Sheet | Escolha de opções     |

### Fechamento de Modais

```
Usuários esperam fechar modais por:
├── Botão X / Fechar
├── Swipe para baixo (sheet)
├── Toque no fundo (não crítico)
├── Botão voltar do sistema (Android)
├── Botão físico voltar (Android antigo)

REGRA: Só bloqueie o fechamento se houver dados não salvos.
```

---

## 6. Deep Linking

### Por que Planejar Deep Links desde o Início

```
Deep links permitem:
├── Navegação a partir de push notifications
├── Compartilhamento de conteúdo
├── Campanhas de marketing
├── Integração com busca/Spotlight
├── Navegação via widgets
├── Integração com outros apps

Implementar depois é DIFÍCIL:
├── Exige refatorar navegação
├── Dependências de tela ficam confusas
├── Passagem de parâmetros complexa
└── Sempre planeje deep links no início
```

### Estrutura de URL

```
Scheme://host/path?params

Exemplos:
├── myapp://product/123
├── https://myapp.com/product/123 (Universal/App Link)
├── myapp://checkout?promo=SAVE20
├── myapp://tab/profile/settings

A hierarquia deve refletir a navegação:
├── myapp://home
├── myapp://home/product/123
├── myapp://home/product/123/reviews
└── Caminho da URL = caminho de navegação
```

### Regras de Navegação com Deep Link

```
1. CONSTRUÇÃO COMPLETA DA STACK
   Deep link para myapp://product/123 deve:
   ├── Colocar Home como raiz da stack
   ├── Dar push na tela de Produto
   └── Botão voltar retorna para Home

2. CONSCIÊNCIA DE AUTENTICAÇÃO
   Se o deep link exigir login:
   ├── Salvar destino pretendido
   ├── Redirecionar para login
   ├── Após login, navegar para o destino

3. LINKS INVÁLIDOS
   Se o destino não existir:
   ├── Navegar para fallback (home)
   ├── Mostrar mensagem de erro
   └── Nunca crashar ou tela em branco

4. NAVEGAÇÃO COM ESTADO
   Deep link durante sessão ativa:
   ├── Não destruir a stack atual
   ├── Dar push no topo OU
   ├── Perguntar se o usuário deseja navegar
```

---

## 7. Persistência do Estado de Navegação

### O que Persistir

```
DEVE persistir:
├── Aba atual selecionada
├── Posição de scroll em listas
├── Rascunho de formulários
├── Stack de navegação recente
└── Preferências do usuário

NÃO deve persistir:
├── Estado de modais
├── Estados temporários de UI
├── Dados obsoletos
├── Estado de autenticação (usar storage seguro)
```

### Implementação (React Navigation)

```javascript
// Persistência de estado
const [isReady, setIsReady] = useState(false);
const [initialState, setInitialState] = useState();

useEffect(() => {
  const loadState = async () => {
    const savedState = await AsyncStorage.getItem('NAV_STATE');
    if (savedState) setInitialState(JSON.parse(savedState));
    setIsReady(true);
  };
  loadState();
}, []);

const handleStateChange = (state) => {
  AsyncStorage.setItem('NAV_STATE', JSON.stringify(state));
};

<NavigationContainer
  initialState={initialState}
  onStateChange={handleStateChange}
>
```

---

## 8. Animações de Transição

### Padrões por Plataforma

```
iOS:
├── Push: Slide da direita
├── Modal: Slide de baixo (sheet) ou fade
├── Troca de abas: Cross-fade
├── Interativo: Swipe para voltar

Android:
├── Push: Fade + slide da direita
├── Modal: Slide de baixo
├── Troca de abas: Cross-fade ou nenhuma
├── Elemento compartilhado: Hero animations
```

### Transições Customizadas

```
Quando customizar:
├── Identidade visual exige
├── Elementos compartilhados
├── Efeitos especiais
└── Manter sutil, <300ms

Quando usar padrão:
├── Na maioria dos casos
├── Drill-down comum
├── Consistência com a plataforma
└── Caminhos críticos de performance
```

### Transições com Elementos Compartilhados

```
Conectam elementos entre telas:

Tela A: Card de produto com imagem
            ↓ (tap)
Tela B: Detalhe do produto com a mesma imagem

A imagem anima da posição do card para o detalhe.

Implementação:
├── React Navigation: biblioteca de shared elements
├── Flutter: Widget Hero
├── SwiftUI: matchedGeometryEffect
└── Compose: Shared element transitions
```

---

## 9. Anti-Padrões de Navegação

### ❌ Pecados de Navegação

| Anti-Padrão                    | Problema                 | Solução                           |
| ------------------------------ | ------------------------ | --------------------------------- |
| **Voltar inconsistente**       | Usuário confuso          | Sempre pop da stack               |
| **Navegação escondida**        | Recursos não descobertos | Tabs visíveis / gatilho do drawer |
| **Aninhamento profundo**       | Usuário se perde         | Máx. 3–4 níveis                   |
| **Quebrar swipe back**         | Frustração no iOS        | Nunca sobrescrever gesto          |
| **Sem deep links**             | Ruim para share/push     | Planejar desde o início           |
| **Resetar stack da aba**       | Perda de contexto        | Preservar estado                  |
| **Modal como fluxo principal** | Não dá para voltar       | Usar stack                        |

### ❌ Erros Comuns de IA

```
IA tende a:
├── Usar modal para tudo (errado)
├── Esquecer preservação de abas (errado)
├── Ignorar deep linking (errado)
├── Sobrescrever back da plataforma (errado)
├── Resetar stack ao trocar de aba (errado)
└── Ignorar back preditivo (Android 14+)

REGRA: Use padrões nativos de navegação.
Não reinvente a navegação.
```

---

## 10. Checklist de Navegação

### Antes da Arquitetura

* [ ] Tipo de app definido (tabs/drawer/stack)
* [ ] Número de destinos de alto nível contado
* [ ] Esquema de deep links planejado
* [ ] Fluxo de autenticação integrado
* [ ] Tablets/telas grandes considerados

### Antes de Cada Tela

* [ ] Usuário consegue voltar?
* [ ] Deep link para esta tela planejado
* [ ] Estado preservado ao sair/voltar
* [ ] Transição adequada ao contexto
* [ ] Requer auth? Tratado?

### Antes do Release

* [ ] Todos os deep links testados
* [ ] Botão voltar funciona em todo lugar
* [ ] Estado das abas preservado
* [ ] Swipe back funciona (iOS)
* [ ] Back preditivo funciona (Android 14+)
* [ ] Universal/App Links configurados
* [ ] Push notifications com deep link funcionando

---

> **Lembre-se:** A navegação é invisível quando feita corretamente. O usuário não deveria pensar em COMO chegar a algum lugar — ele simplesmente chega. Se o usuário percebe a navegação, algo está errado.
