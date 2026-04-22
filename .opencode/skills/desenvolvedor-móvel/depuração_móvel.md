# Guia de Depuração Mobile

> **Pare de depurar apenas com `console.log()`!**
> Apps mobile possuem camadas nativas complexas. Logs de texto não são suficientes.
> **Este arquivo ensina estratégias eficazes de depuração mobile.**

---

## 🧠 MENTALIDADE DE DEPURAÇÃO MOBILE

```
Depuração Web:        Depuração Mobile:
┌──────────────┐     ┌──────────────┐
│  Browser     │     │  Bridge JS   │
│  DevTools    │     │  UI Nativa   │
│  Network Tab │     │  GPU/Memória │
└──────────────┘     │  Threads     │
                     └──────────────┘
```

**Diferenças-chave:**

1. **Camada Nativa:** O código JS funciona, mas o app crasha? Provavelmente é nativo (Java/Obj-C/Swift).
2. **Deploy:** Não existe “refresh” simples. O estado pode se perder ou ficar inconsistente.
3. **Rede:** SSL Pinning e proxies são mais difíceis de configurar.
4. **Logs do Dispositivo:** `adb logcat` e `Console.app` são a fonte da verdade.

---

## 🚫 ANTI-PADRÕES DE DEPURAÇÃO COM IA

| ❌ Padrão                 | ✅ Correto para Mobile                                        |
| ------------------------ | ------------------------------------------------------------ |
| “Adicione console.logs”  | Use Flipper / Reactotron                                     |
| “Veja a aba Network”     | Use Charles Proxy / Proxyman                                 |
| “Funciona no simulador”  | **Teste em dispositivo real** (bugs específicos de hardware) |
| “Reinstale node_modules” | **Clean build nativo** (cache do Gradle/Pods)                |
| Ignorar logs nativos     | Ler `logcat` / logs do Xcode                                 |

---

## 1. Conjunto de Ferramentas

### ⚡ React Native & Expo

| Ferramenta           | Finalidade            | Melhor para                |
| -------------------- | --------------------- | -------------------------- |
| **Reactotron**       | Estado / API / Redux  | Depuração do lado JS       |
| **Flipper**          | Layout / Network / DB | Nativo + bridge JS         |
| **Ferramentas Expo** | Inspetor de elementos | Verificações rápidas de UI |

### 🛠️ Camada Nativa (Análise Profunda)

| Ferramenta           | Plataforma | Comando        | Por que usar              |
| -------------------- | ---------- | -------------- | ------------------------- |
| **Logcat**           | Android    | `adb logcat`   | Crashes nativos, ANRs     |
| **Console**          | iOS        | via Xcode      | Exceções nativas, memória |
| **Layout Inspector** | Android    | Android Studio | Bugs de hierarquia de UI  |
| **View Inspector**   | iOS        | Xcode          | Bugs de hierarquia de UI  |

---

## 2. Fluxos Comuns de Depuração

### 🕵️ “O app acabou de crashar” (Tela vermelha vs Fecha sozinho)

**Cenário A: Tela Vermelha (Erro JS)**

* **Causa:** `undefined is not an object`, erro de importação.
* **Correção:** Leia o stack trace na tela. Normalmente é claro.

**Cenário B: App fecha e volta para a Home (Crash Nativo)**

* **Causa:** Falha em módulo nativo, OOM (memória), uso de permissão não declarada.
* **Ferramentas:**

  * **Android:** `adb logcat *:E` (filtrar erros)
  * **iOS:** Xcode → Window → Devices → View Device Logs

> 💡 **Dica Pro:** Se o app crasha imediatamente ao abrir, em 99% dos casos é problema de configuração nativa (Info.plist, AndroidManifest.xml).

---

### 🌐 “A requisição de API falhou” (Rede)

**Web:** Chrome DevTools → Network
**Mobile:** *Normalmente não é visível com facilidade.*

**Solução 1: Reactotron / Flipper**

* Visualizar requisições diretamente na ferramenta.

**Solução 2: Proxy (Charles / Proxyman)**

* **Difícil, mas poderoso.** Mostra TODO o tráfego, inclusive de SDKs nativos.
* Exige instalação de certificado SSL no dispositivo.

---

### 🐢 “A UI está travando” (Performance)

**Não chute. Meça.**

* **React Native:** Performance Monitor (menu de shake).
* **Android:** “Profile GPU Rendering” nas Developer Options.
* **Problemas comuns:**

  * **Queda de FPS JS:** Cálculo pesado na thread JS.
  * **Queda de FPS UI:** Muitas views, hierarquia profunda, imagens pesadas.

---

## 3. Pesadelos Específicos por Plataforma

### Android

* **Falha no Gradle Sync:** Geralmente versão de Java incompatível ou classes duplicadas.
* **Rede no Emulador:** `localhost` no emulador é `10.0.2.2`, NÃO `127.0.0.1`.
* **Build em cache:** `./gradlew clean` é seu melhor amigo.

### iOS

* **Problemas com Pods:** `pod deintegrate && pod install`.
* **Erros de Signing:** Verifique Team ID e Bundle Identifier.
* **Cache:** Xcode → Product → Clean Build Folder.

---

## 📝 CHECKLIST DE DEPURAÇÃO

* [ ] **É crash JS ou Nativo?** (Tela vermelha ou fecha sozinho?)
* [ ] **Você fez clean build?** (Caches nativos são agressivos)
* [ ] **Está em dispositivo real?** (Simuladores escondem bugs de concorrência)
* [ ] **Verificou os logs nativos?** (Não apenas o terminal)

> **Lembre-se:** Se o JavaScript parece perfeito, mas o app falha, investigue a camada nativa com atenção.

Se quiser, posso **integrar este guia como regra obrigatória na sua Engenharia de Contexto**, ou criar uma **versão resumida para troubleshooting rápido do time**.
