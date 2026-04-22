# Padrões de Testes Mobile

> **Testes mobile NÃO são testes web. Restrições diferentes, estratégias diferentes.**
> Este arquivo ensina **QUANDO** usar cada abordagem de teste e **POR QUÊ**.
> **Os exemplos de código são mínimos — o foco é na tomada de decisão.**

---

## 🧠 MENTALIDADE DE TESTES MOBILE

```
Testes mobile diferem dos testes web:
├── Dispositivos reais importam (emuladores escondem bugs)
├── Diferenças de plataforma (comportamento iOS vs Android)
├── Condições de rede extremamente variáveis
├── Bateria e performance sob teste
├── Ciclo de vida do app (background, encerrado, restaurado)
├── Permissões e diálogos do sistema
└── Interações por toque vs cliques
```

---

## 🚫 ANTI-PADRÕES DE TESTES MOBILE COM IA

| ❌ Padrão da IA                | Por que está errado             | ✅ Correto para Mobile             |
| ----------------------------- | ------------------------------- | --------------------------------- |
| Apenas Jest                   | Ignora a camada nativa          | Jest + E2E em dispositivo         |
| Padrões do Enzyme             | Depreciado, focado em web       | React Native Testing Library      |
| E2E em browser (Cypress)      | Não testa recursos nativos      | Detox / Maestro                   |
| Mockar tudo                   | Perde bugs de integração        | Testes em dispositivo real        |
| Ignorar testes por plataforma | iOS e Android diferem           | Casos específicos por plataforma  |
| Ignorar testes de performance | Performance é crítica no mobile | Profiling em dispositivo fraco    |
| Testar só o caminho feliz     | Mobile tem muitos edge cases    | Offline, permissões, interrupções |
| 100% cobertura unitária       | Falsa sensação de segurança     | Equilíbrio da pirâmide            |
| Copiar testes web             | Ambiente diferente              | Ferramentas específicas mobile    |

---

## 1. Seleção de Ferramentas de Teste

### Árvore de Decisão

```
O QUE VOCÊ ESTÁ TESTANDO?
        │
        ├── Funções puras, utilitários, helpers
        │   └── Jest (testes unitários)
        │       └── Sem setup mobile especial
        │
        ├── Componentes isolados
        │   ├── React Native → React Native Testing Library
        │   └── Flutter → flutter_test (widget tests)
        │
        ├── Componentes com hooks, contexto, navegação
        │   ├── React Native → RNTL + providers mockados
        │   └── Flutter → integration_test
        │
        ├── Fluxos completos do usuário (login, checkout)
        │   ├── Detox (React Native, rápido, confiável)
        │   ├── Maestro (Cross-platform, YAML)
        │   └── Appium (legado, lento, último recurso)
        │
        └── Performance, memória, bateria
            ├── Flashlight (performance RN)
            ├── Flutter DevTools
            └── Profiling em dispositivo real (Xcode/Android Studio)
```

### Comparação de Ferramentas

| Ferramenta       | Plataforma | Velocidade | Confiabilidade | Quando usar              |
| ---------------- | ---------- | ---------- | -------------- | ------------------------ |
| **Jest**         | RN         | ⚡⚡⚡        | ⚡⚡⚡            | Testes unitários, lógica |
| **RNTL**         | RN         | ⚡⚡⚡        | ⚡⚡             | Testes de componentes    |
| **flutter_test** | Flutter    | ⚡⚡⚡        | ⚡⚡⚡            | Widget tests             |
| **Detox**        | RN         | ⚡⚡         | ⚡⚡⚡            | E2E, fluxos críticos     |
| **Maestro**      | Ambos      | ⚡⚡         | ⚡⚡             | E2E cross-platform       |
| **Appium**       | Ambos      | ⚡          | ⚡              | Legado, último recurso   |

---

## 2. Pirâmide de Testes para Mobile

```
                    ┌────────────────┐
                    │     Testes E2E │  10%
                    │ (Dispositivo) │  Lentos, caros, essenciais
                    ├────────────────┤
                    │   Integração   │  20%
                    │     Testes     │  Componente + contexto
                    ├────────────────┤
                    │  Componentes  │  30%
                    │     Testes     │  UI isolada
                    ├────────────────┤
                    │   Unitários   │  40%
                    │    (Jest)     │  Lógica pura
                    └────────────────┘
```

### Por que essa distribuição?

| Nível               | Motivo                                   |
| ------------------- | ---------------------------------------- |
| **E2E 10%**         | Lentos e instáveis, mas pegam bugs reais |
| **Integração 20%**  | Fluxos reais sem rodar o app inteiro     |
| **Componentes 30%** | Feedback rápido sobre UI                 |
| **Unitários 40%**   | Mais rápidos e estáveis                  |

> 🔴 **Se você tem 90% de testes unitários e 0% E2E, está testando as coisas erradas.**

---

## 3. O Que Testar em Cada Nível

### Testes Unitários (Jest)

```
✅ TESTAR:
├── Funções utilitárias
├── Reducers (Redux, Zustand)
├── Transformadores de resposta da API
├── Lógica de validação
└── Regras de negócio

❌ NÃO TESTAR:
├── Renderização de componentes
├── Navegação
├── Módulos nativos
└── Bibliotecas de terceiros
```

### Testes de Componentes (RNTL / flutter_test)

```
✅ TESTAR:
├── Renderização correta
├── Interações do usuário (tap, digitar, swipe)
├── Estados de loading/erro/vazio
├── Labels de acessibilidade
└── Mudança de comportamento por props

❌ NÃO TESTAR:
├── Detalhes internos de implementação
├── Snapshot em tudo
├── Estilo específico
└── Internals de componentes terceiros
```

### Testes de Integração

```
✅ TESTAR:
├── Fluxos de formulário
├── Navegação entre telas
├── Persistência de estado
├── Integração com API (mockada)
└── Interação entre contextos/providers

❌ NÃO TESTAR:
├── Todos os caminhos possíveis
├── Serviços terceiros
└── Lógica de backend
```

### Testes E2E

```
✅ TESTAR:
├── Jornadas críticas (login, compra)
├── Transição offline → online
├── Deep links
├── Navegação via push
├── Fluxos de permissão
└── Pagamentos

❌ NÃO TESTAR:
├── Todos os edge cases
├── Regressão visual
├── Funcionalidades não críticas
└── Lógica exclusiva do backend
```

---

## 4. Testes Específicos por Plataforma

### Diferenças entre iOS e Android

| Área            | iOS               | Android                | Testar ambos? |
| --------------- | ----------------- | ---------------------- | ------------- |
| **Voltar**      | Swipe lateral     | Botão do sistema       | ✅ Sim         |
| **Permissões**  | Uma vez           | Repetido com rationale | ✅ Sim         |
| **Teclado**     | Diferente         | Diferente              | ✅ Sim         |
| **Date picker** | Roda/modal        | Dialog Material        | ⚠️ Se custom  |
| **Push**        | Payload APNs      | Payload FCM            | ✅ Sim         |
| **Deep links**  | Universal Links   | App Links              | ✅ Sim         |
| **Gestos**      | Alguns exclusivos | Material gestures      | ⚠️ Se custom  |

### Estratégia

```
PARA CADA PLATAFORMA:
├── Rodar testes unitários
├── Rodar testes de componentes
├── Rodar E2E em DISPOSITIVO REAL
│   ├── iOS: iPhone físico
│   └── Android: intermediário (não flagship)
└── Testar features específicas separadamente
```

---

## 5. Testes Offline & Rede

### Cenários Offline

| Cenário              | Verificar                |
| -------------------- | ------------------------ |
| Abrir app offline    | Mostra cache ou mensagem |
| Cair offline no meio | Ação enfileirada         |
| Voltar online        | Sync sem duplicar        |
| Rede lenta (2G)      | Loadings e timeouts      |
| Rede instável        | Retry e recuperação      |

### Como Testar Rede

```
ABORDAGEM:
├── Unitário: mock NetInfo
├── Integração: mock da API
├── E2E (Detox): URL blacklist
├── E2E (Maestro): condições de rede
└── Manual: Charles / Network Link Conditioner
```

---

## 6. Testes de Performance

### Métricas

| Métrica   | Alvo             |
| --------- | ---------------- |
| Startup   | < 2s             |
| Transição | < 300ms          |
| Scroll    | 60 FPS           |
| Memória   | Sem leaks        |
| Bundle    | O menor possível |

### Quando Testar

```
TESTAR PERFORMANCE:
├── Antes do release
├── Após features pesadas
├── Após upgrades
├── Reclamações de lentidão
└── CI (opcional)

ONDE:
├── Dispositivo real (OBRIGATÓRIO)
├── Dispositivo fraco
├── NÃO emulador
└── Dados realistas
```

---

## 7. Testes de Acessibilidade

### Verificar

* Labels acessíveis
* Tamanho de toque
* Contraste
* Leitores de tela
* Texto grande
* Movimento reduzido

---

## 8. Integração com CI/CD

### Onde Rodar

| Etapa       | Testes                  |
| ----------- | ----------------------- |
| PR          | Unitários + Componentes |
| Main        | + Integração            |
| Pré-release | + E2E                   |
| Nightly     | Tudo                    |

---

## 📝 CHECKLIST DE TESTES MOBILE

### Antes do PR

* [ ] Testes unitários
* [ ] Testes de componentes
* [ ] CI verde

### Antes do Release

* [ ] E2E em iOS real
* [ ] E2E em Android real
* [ ] Dispositivo fraco testado
* [ ] Offline validado
* [ ] Performance ok
* [ ] Acessibilidade ok

---

## 🎯 Perguntas-Chave de Testes

Antes de escrever testes:

1. **O que pode quebrar?**
2. **O que é crítico para o usuário?**
3. **Onde está a lógica complexa?**
4. **O que muda por plataforma?**
5. **O que acontece offline?**

> **Lembre-se:** bons testes mobile focam no que IMPORTA. Um E2E instável é pior do que nenhum teste. Um teste unitário que evita um bug real vale mais do que 100 testes triviais passando.
