---
nome: desenvolvedor_móvel
descrição: Pensamento e tomada de decisão em design mobile-first para apps iOS e Android. Interação por toque, padrões de performance, convenções de plataforma. Ensina princípios, não valores fixos. Use ao construir apps mobile com React Native, Flutter ou nativos.
ferramentas-permitidas: Ler, Glob, Grep, Bash
---

# Sistema de Design Mobile

> **Filosofia:** Prioridade ao toque. Consciência de bateria. Respeito à plataforma. Capaz de funcionar offline.  
> **Princípio Central:** Mobile NÃO é um desktop pequeno. PENSE nas restrições mobile, PERGUNTE a plataforma.

---

## 🔧 Scripts de Execução

**Execute estes scripts para validação (não leia, apenas execute):**

| Script | Objetivo | Uso |
|------|----------|-----|
| `scripts/auditoria_móvel.py` | Auditoria de UX Mobile e Interação por Toque | `python scripts/auditoria_móvel.py <caminho_do_projeto>` |

---

## 🔴 OBRIGATÓRIO: Leia os Arquivos de Referência Antes de Trabalhar!

**⛔ NÃO inicie o desenvolvimento sem ler os arquivos relevantes:**

### Universais (Sempre Ler)

| Arquivo | Conteúdo | Status |
|------|---------|--------|
| **[pensamento_de_design_mobile.md](pensamento_de_design_mobile.md)** | **⚠️ ANTI-MEMORIZAÇÃO: Força raciocínio e evita padrões automáticos de IA** | **⬜ CRÍTICO PRIMEIRO** |
| **[psicologia_do_toque.md](psicologia_do_toque.md)** | **Lei de Fitts, gestos, háptica, zona do polegar** | **⬜ CRÍTICO** |
| **[desempenho_mobile.md](desempenho_mobile.md)** | **Performance RN/Flutter, 60fps, memória** | **⬜ CRÍTICO** |
| **[backend_mobile.md](backend_mobile.md)** | **Push notifications, sync offline, APIs mobile** | **⬜ CRÍTICO** |
| **[teste_mobile.md.md](teste_mobile.md.md)** | **Pirâmide de testes, E2E, testes por plataforma** | **⬜ CRÍTICO** |
| **[depuração_móvel.md](depuração_móvel.md)** | **Debug nativo vs JS, Flipper, Logcat** | **⬜ CRÍTICO** |
| [navegação_móvel.md](navegação_móvel.md) | Tab/Stack/Drawer, deep linking | ⬜ Ler |
| [tipografia_móvel.md](tipografia_móvel.md) | Fontes de sistema, Dynamic Type, acessibilidade | ⬜ Ler |
| [sistema_de_cores_móvel.md](sistema_de_cores_móvel.md) | OLED, dark mode, consumo de bateria | ⬜ Ler |
| [decision-trees.md](decision-trees.md) | Seleção de framework/estado/storage | ⬜ Ler |

> 🧠 **mobile-design-thinking.md é PRIORIDADE!**  
> Este arquivo garante que a IA pense, em vez de reutilizar padrões memorizados.

### Específicos por Plataforma (Leia conforme o alvo)

| Plataforma | Arquivo | Conteúdo | Quando Ler |
|----------|--------|----------|------------|
| **iOS** | [plataforma_ios.md](plataforma_ios.md) | Human Interface Guidelines, SF Pro, padrões SwiftUI | Apps para iPhone/iPad |
| **Android** | [plataforma_android.md](plataforma_android.md) | Material Design 3, Roboto, padrões Compose | Apps Android |
| **Cross-Platform** | Ambos acima | Pontos de divergência de plataforma | React Native / Flutter |

> 🔴 **iOS → Leia platform-ios.md PRIMEIRO!**  
> 🔴 **Android → Leia platform-android.md PRIMEIRO!**  
> 🔴 **Cross-platform → Leia AMBOS e aplique lógica condicional por plataforma!**

---

## ⚠️ CRÍTICO: PERGUNTE ANTES DE ASSUMIR (OBRIGATÓRIO)

> **PARE! Se o pedido do usuário for aberto, NÃO assuma seus padrões favoritos.**

### Você DEVE Perguntar se Não Estiver Especificado:

| Aspecto | Pergunta | Por quê |
|------|--------|--------|
| **Plataforma** | “iOS, Android ou ambos?” | Impacta TODA decisão de design |
| **Framework** | “React Native, Flutter ou nativo?” | Define padrões e ferramentas |
| **Navegação** | “Tab bar, drawer ou stack?” | Decisão central de UX |
| **Estado** | “Qual gerenciamento de estado?” | Base da arquitetura |
| **Offline** | “Precisa funcionar offline?” | Estratégia de dados |
| **Dispositivos alvo** | “Somente celular ou tablet também?” | Complexidade de layout |

---

## ⛔ ANTI-PADRÕES MOBILE DE IA (LISTA PROIBIDA)

> 🚫 **Tendências automáticas de IA que DEVEM ser evitadas**

### Pecados de Performance

| ❌ NUNCA FAÇA | Por que está errado | ✅ SEMPRE FAÇA |
|-------------|--------------------|---------------|
| `ScrollView` para listas longas | Renderiza tudo, explode memória | `FlatList` / `FlashList` / `ListView.builder` |
| `renderItem` inline | Re-renderiza tudo | `useCallback` + `React.memo` |
| Sem `keyExtractor` | Bugs em reordenação | ID único e estável |
| Ignorar `getItemLayout` | Scroll travado | Definir quando altura é fixa |
| `setState()` em tudo | Rebuilds desnecessários | Estado direcionado |
| Driver nativo falso | Bloqueia animações | `useNativeDriver: true` |
| `console.log` em produção | Trava thread JS | Remover antes do release |
| Sem memoização | Re-render constante | Memoizar SEMPRE |

### Pecados de Toque / UX

| ❌ NUNCA FAÇA | Por que está errado | ✅ SEMPRE FAÇA |
|-------------|--------------------|---------------|
| Alvo < 44px | Impossível tocar com precisão | 44pt (iOS) / 48dp (Android) |
| Espaço < 8px | Toques acidentais | 8–12px mínimo |
| Apenas gestos | Exclui usuários | Botão alternativo |
| Sem loading | Usuário acha que travou | Feedback sempre |
| Sem erro | Usuário fica preso | Erro com retry |
| Ignorar offline | App quebra | Degradação graciosa |
| Ignorar convenções | Confunde usuários | iOS é iOS, Android é Android |

### Pecados de Segurança

| ❌ NUNCA FAÇA | Por que está errado | ✅ SEMPRE FAÇA |
|-------------|--------------------|---------------|
| Token em AsyncStorage | Fácil de roubar | SecureStore / Keychain |
| API key hardcoded | Reversível | Variáveis de ambiente |
| Ignorar SSL pinning | Ataques MITM | Pin em produção |
| Logar dados sensíveis | Logs são extraíveis | Nunca logar PII |

### Pecados de Arquitetura

| ❌ NUNCA FAÇA | Por que está errado | ✅ SEMPRE FAÇA |
|-------------|--------------------|---------------|
| Lógica de negócio na UI | Não testável | Camada de serviços |
| Estado global para tudo | Re-renders | Local por padrão |
| Deep link tardio | Push/share quebram | Planejar desde o início |
| Sem cleanup | Memory leaks | Dispose/cleanup |

---

## 📱 Matriz de Decisão por Plataforma

### Quando Unificar vs Divergir

```

UNIFICAR                         DIVERGIR
────────────────────            ─────────────────────
Lógica de negócio               Navegação
Camada de dados                 Gestos
Funcionalidades core            Ícones
Pickers de data
Modais / Sheets
Tipografia
Alertas de erro

```

---

## 🧠 Psicologia de UX Mobile (Resumo)

- Dedo ≠ cursor → impreciso
- Ações importantes na **zona do polegar**
- Ações destrutivas longe do alcance fácil
- Atenção fragmentada
- Um fluxo por vez

---

## 📝 CHECKPOINT (OBRIGATÓRIO)

```

🧠 CHECKPOINT:

Plataforma:   [ iOS / Android / Ambos ]
Framework:    [ RN / Flutter / Nativo ]
Arquivos lidos:

3 Princípios que aplicarei:
1.
2.
3.

Anti-padrões que evitarei:
1.
2.

```

> 🔴 **Não consegue preencher? → Volte e leia os arquivos.**

---

> **Lembre-se:**  
> Usuários mobile estão com pressa, distraídos, usando uma mão, sob sol forte e bateria baixa.  
> Projete para o PIOR cenário.  
> Se funciona lá, funciona em qualquer lugar.
```
