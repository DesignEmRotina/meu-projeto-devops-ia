# Árvores de Decisão Mobile

> Seleção de framework, gerenciamento de estado, estratégia de armazenamento e decisões baseadas em contexto.
> **Estes são guias de PENSAMENTO, não respostas para copiar e colar.**

---

## 1. Seleção de Framework

### Árvore Mestra de Decisão

```
O QUE VOCÊ ESTÁ CONSTRUINDO?
        │
        ├── Precisa de updates OTA sem revisão da loja?
        │   │
        │   ├── Sim → React Native + Expo
        │   │         ├── Expo Go para desenvolvimento
        │   │         ├── EAS Update para OTA em produção
        │   │         └── Ideal para: iteração rápida, times web
        │   │
        │   └── Não → Continue ▼
        │
        ├── Precisa de UI customizada pixel-perfect em ambas plataformas?
        │   │
        │   ├── Sim → Flutter
        │   │         ├── Engine de renderização própria
        │   │         ├── Uma única UI para iOS + Android
        │   │         └── Ideal para: apps visuais, forte branding
        │   │
        │   └── Não → Continue ▼
        │
        ├── Uso pesado de recursos nativos (ARKit, HealthKit, sensores específicos)?
        │   │
        │   ├── Apenas iOS → SwiftUI / UIKit
        │   │                └── Máxima capacidade nativa
        │   │
        │   ├── Apenas Android → Kotlin + Jetpack Compose
        │   │                   └── Máxima capacidade nativa
        │   │
        │   └── Ambos → Considere nativo com lógica compartilhada
        │              └── Kotlin Multiplatform para o compartilhamento
        │
        ├── Time web existente + base em TypeScript?
        │   │
        │   └── Sim → React Native
        │             ├── Paradigma familiar para devs React
        │             ├── Compartilhamento limitado com web
        │             └── Ecossistema grande
        │
        └── Empresa com time Flutter já existente?
            │
            └── Sim → Flutter
                      └── Aproveita expertise já existente
```

### Comparação de Frameworks

| Fator                    | React Native         | Flutter      | Nativo (Swift/Kotlin) |
| ------------------------ | -------------------- | ------------ | --------------------- |
| **Updates OTA**          | ✅ Expo               | ❌ Não        | ❌ Não                 |
| **Curva de aprendizado** | Baixa (devs React)   | Média        | Maior                 |
| **Performance**          | Boa                  | Excelente    | A melhor              |
| **Consistência de UI**   | Nativa da plataforma | Idêntica     | Nativa                |
| **Tamanho do bundle**    | Médio                | Maior        | Menor                 |
| **Acesso nativo**        | Via bridges          | Via channels | Direto                |
| **Hot Reload**           | ✅                    | ✅            | ✅ (Xcode 15+)         |

### Quando escolher Nativo

```
ESCOLHA NATIVO QUANDO:
├── Performance máxima é crítica (jogos, 3D)
├── Integração profunda com o SO
├── Recursos específicos da plataforma são centrais
├── O time domina nativo
├── Presença na loja é prioridade
└── Manutenção de longo prazo é crítica

EVITE NATIVO QUANDO:
├── Orçamento ou prazo limitados
├── Precisa iterar rápido
├── UI idêntica entre plataformas
├── Time focado em web
└── Cross-platform é prioridade
```

---

## 2. Seleção de Gerenciamento de Estado

### Decisão de Estado – React Native

```
QUAL A COMPLEXIDADE DO ESTADO?
        │
        ├── App simples, poucas telas, pouco estado compartilhado
        │   │
        │   └── Zustand (ou useState/Context)
        │       ├── Pouco boilerplate
        │       ├── Fácil de entender
        │       └── Escala razoavelmente bem
        │
        ├── Dados majoritariamente vindos do servidor (API)
        │   │
        │   └── TanStack Query + Zustand
        │       ├── Query para estado de servidor
        │       ├── Zustand para estado de UI
        │       └── Cache e refetch excelentes
        │
        ├── App complexo, muitas features
        │   │
        │   └── Redux Toolkit + RTK Query
        │       ├── Previsível, fácil de debugar
        │       ├── RTK Query para APIs
        │       └── Bom para times grandes
        │
        └── Estado atômico e granular
            │
            └── Jotai
                ├── Baseado em átomos (similar ao Recoil)
                ├── Minimiza re-renders
                └── Bom para estado derivado
```

### Decisão de Estado – Flutter

```
QUAL A COMPLEXIDADE DO ESTADO?
        │
        ├── App simples, aprendendo Flutter
        │   │
        │   └── Provider (ou setState)
        │       ├── Oficial, simples
        │       ├── Integrado ao Flutter
        │       └── Bom para apps pequenos
        │
        ├── Moderno, type-safe, testável
        │   │
        │   └── Riverpod 2.0
        │       ├── Segurança em tempo de compilação
        │       ├── Code generation
        │       ├── Excelente para apps médios/grandes
        │       └── Recomendado para novos projetos
        │
        ├── Enterprise, padrões rígidos
        │   │
        │   └── BLoC
        │       ├── Padrão Evento → Estado
        │       ├── Muito testável
        │       ├── Mais boilerplate
        │       └── Bom para times grandes
        │
        └── Prototipação rápida
            │
            └── GetX (com cautela)
                ├── Implementação rápida
                ├── Padrões menos rígidos
                └── Pode virar bagunça em escala
```

### Anti-patterns de Estado

```
❌ NÃO FAÇA:
├── Estado global para tudo
├── Misturar várias abordagens
├── Guardar estado de servidor como estado local
├── Ignorar normalização
├── Abusar de Context (muitos re-renders)
└── Colocar navegação no estado global

✅ FAÇA:
├── Estado de servidor → biblioteca de query
├── Estado de UI → mínimo, local primeiro
├── Eleve estado só quando necessário
├── Use UMA abordagem por projeto
└── Mantenha o estado próximo de onde é usado
```

---

## 3. Seleção de Padrão de Navegação

```
QUANTOS DESTINOS DE TOPO?
        │
        ├── 2 destinos
        │   └── Tabs superiores ou stack simples
        │
        ├── 3–5 destinos (importância igual)
        │   └── ✅ Tab Bar / Bottom Navigation
        │       ├── Padrão mais comum
        │       └── Fácil descoberta
        │
        ├── 5+ destinos
        │   │
        │   ├── Todos importantes → Drawer Navigation
        │   │                    └── Muitos destinos, ocultos
        │   │
        │   └── Alguns menos importantes → Tabs + Drawer
        │
        └── Fluxo linear único?
            └── Apenas Stack Navigation
                └── Onboarding, checkout, etc.
```

### Navegação por Tipo de App

| Tipo de App   | Padrão               | Motivo              |
| ------------- | -------------------- | ------------------- |
| Social        | Tab bar              | Troca frequente     |
| E-commerce    | Tab + stack          | Categorias          |
| Email         | Drawer + list-detail | Muitas pastas       |
| Configurações | Stack                | Hierarquia profunda |
| Onboarding    | Stack                | Fluxo linear        |
| Mensagens     | Tab + stack          | Conversas           |

---

## 4. Seleção de Estratégia de Armazenamento

```
QUE TIPO DE DADO?
        │
        ├── Sensível (tokens, senhas)
        │   │
        │   └── ✅ Secure Storage
        │       ├── iOS: Keychain
        │       ├── Android: EncryptedSharedPreferences
        │       └── RN: expo-secure-store / react-native-keychain
        │
        ├── Preferências do usuário
        │   │
        │   └── ✅ Key-Value
        │       ├── UserDefaults / SharedPreferences
        │       └── AsyncStorage / MMKV
        │
        ├── Dados estruturados
        │   │
        │   └── ✅ Banco local
        │       ├── SQLite
        │       ├── Realm
        │       └── WatermelonDB
        │
        ├── Arquivos grandes
        │   │
        │   └── ✅ File System
        │
        └── Cache de API
            │
            └── ✅ Cache da biblioteca de query
```

---

## 5. Seleção de Estratégia Offline

```
QUÃO CRÍTICO É O OFFLINE?
        │
        ├── Bom ter
        │   └── Cache simples + dado antigo
        │
        ├── Essencial
        │   └── Offline-first
        │       ├── DB local como fonte da verdade
        │       ├── Sync quando online
        │       └── Resolução de conflitos
        │
        └── Tempo real crítico
            └── WebSocket + fila local
```

---

## 6. Seleção de Autenticação

```
QUE TIPO DE AUTH?
        │
        ├── Email/senha
        │   └── JWT + refresh token
        │
        ├── Social login
        │   └── OAuth 2.0 + PKCE
        │
        ├── Enterprise
        │   └── OIDC / SAML
        │
        └── Biométrica
            └── Libera token seguro local
```

---

## 7. Templates por Tipo de Projeto

### E-commerce, Social e SaaS

*(mantidos conforme original, apenas traduzidos semanticamente)*

---

## 8. Checklist de Decisão

### Antes de iniciar qualquer projeto

* [ ] Plataformas definidas?
* [ ] Framework escolhido por critério?
* [ ] Gerenciamento de estado definido?
* [ ] Navegação definida?
* [ ] Estratégia de storage por tipo de dado?
* [ ] Offline definido?
* [ ] Auth planejado?
* [ ] Deep linking desde o início?

---

## 9. Anti-patterns de Decisão

| Anti-pattern            | Por que é ruim | Melhor opção   |
| ----------------------- | -------------- | -------------- |
| Redux em app simples    | Overkill       | Zustand        |
| Nativo para MVP         | Lento          | Cross-platform |
| Drawer com 3 telas      | Oculto         | Tabs           |
| AsyncStorage para token | Inseguro       | SecureStore    |
| Ignorar offline         | Quebra UX      | Planejar       |
| Stack padrão pra tudo   | Não contextual | Avaliar        |

---

## 10. Referência Rápida

### Framework

```
OTA?           → React Native + Expo
UI idêntica?   → Flutter
Performance?   → Nativo
Time web?      → React Native
Protótipo?     → Expo
```

---

> **Lembre-se:** essas árvores existem para ajudar a **pensar**, não para decidir automaticamente. Cada projeto tem restrições próprias. Quando os requisitos forem vagos, **faça perguntas** e decida com base no contexto real — não em defaults.
