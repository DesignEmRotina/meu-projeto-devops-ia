# Padrões de Backend para Mobile

> **Este arquivo cobre padrões de backend/API ESPECÍFICOS para clientes mobile.**
> Padrões genéricos de backend estão em `nodejs-best-practices` e `api-patterns`.
> **Backend mobile NÃO é o mesmo que backend web. Restrições diferentes, padrões diferentes.**

---

## 🧠 MENTALIDADE DE BACKEND MOBILE

```
Clientes mobile são DIFERENTES de clientes web:
├── Rede instável (2G, metrô, elevador)
├── Restrições de bateria (minimizar ativações)
├── Armazenamento limitado (não dá para cachear tudo)
├── Sessões interrompidas (ligações, notificações)
├── Dispositivos diversos (celulares antigos até topo de linha)
└── Atualizações binárias são lentas (review da App Store)
```

**Seu backend deve compensar TODOS esses fatores.**

---

## 🚫 ANTI-PADRÕES DE BACKEND MOBILE COM IA

### Erros comuns que IAs cometem ao criar backends mobile:

| ❌ Padrão da IA                 | Por que está errado                   | ✅ Correto para Mobile                           |
| ------------------------------ | ------------------------------------- | ----------------------------------------------- |
| Mesma API para web e mobile    | Mobile precisa de respostas compactas | Endpoints mobile separados OU seleção de campos |
| Respostas com objeto completo  | Desperdício de banda e bateria        | Respostas parciais, paginação                   |
| Nenhuma consideração offline   | App quebra sem rede                   | Design offline-first, filas de sincronização    |
| WebSocket para tudo            | Drena bateria                         | Push notifications + fallback com polling       |
| Sem versionamento de app       | Mudanças quebram apps antigos         | Headers de versão, versão mínima                |
| Erros genéricos                | Usuário não sabe o que fazer          | Códigos de erro mobile + ações de recuperação   |
| Autenticação baseada em sessão | Apps reiniciam                        | Tokens com refresh                              |
| Ignorar info do dispositivo    | Difícil depurar problemas             | Device ID, versão do app nos headers            |

---

## 1. Push Notifications

### Arquitetura das Plataformas

```
┌─────────────────────────────────────────────────────────────────┐
│                    SEU BACKEND                                   │
├─────────────────────────────────────────────────────────────────┤
│                         │                                        │
│              ┌──────────┴──────────┐                            │
│              ▼                     ▼                            │
│    ┌─────────────────┐   ┌─────────────────┐                    │
│    │   FCM (Google)  │   │  APNs (Apple)   │                    │
│    │   Firebase      │   │  Direto ou FCM  │                    │
│    └────────┬────────┘   └────────┬────────┘                    │
│             │                     │                              │
│             ▼                     ▼                              │
│    ┌─────────────────┐   ┌─────────────────┐                    │
│    │ Android Device  │   │   Dispositivo iOS│                    │
│    └─────────────────┘   └─────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
```

### Tipos de Push

| Tipo        | Caso de Uso                     | O que o usuário vê    |
| ----------- | ------------------------------- | --------------------- |
| **Display** | Nova mensagem, status de pedido | Banner de notificação |
| **Silent**  | Sync em background, atualização | Nada (background)     |
| **Data**    | Lógica customizada do app       | Depende do app        |

### Anti-padrões

| ❌ NUNCA                        | ✅ SEMPRE                                          |
| ------------------------------ | ------------------------------------------------- |
| Enviar dados sensíveis no push | Push diz “Nova mensagem”, app busca o conteúdo    |
| Excesso de notificações        | Agrupar, deduplicar, respeitar horário silencioso |
| Mesma mensagem para todos      | Segmentar por preferências e fuso                 |
| Ignorar tokens inválidos       | Limpar tokens inválidos regularmente              |
| Ignorar APNs no iOS            | FCM sozinho não garante entrega no iOS            |

### Gerenciamento de Tokens

```
CICLO DE VIDA DO TOKEN:
├── App registra → Obtém token → Envia ao backend
├── Token pode mudar → App re-registra ao iniciar
├── Token expira → Remover do banco
├── App desinstalado → Token inválido (detectado por erro)
└── Múltiplos dispositivos → Vários tokens por usuário
```

---

## 2. Sincronização Offline & Resolução de Conflitos

### Escolha da Estratégia de Sync

```
QUAL O TIPO DE DADO?
        │
        ├── Somente leitura (notícias, catálogo)
        │   └── Cache simples + TTL
        │       └── ETag / Last-Modified
        │
        ├── Dados do usuário (notas, tarefas)
        │   └── Last-write-wins (simples)
        │       └── Ou merge por timestamp
        │
        ├── Colaborativo (docs compartilhados)
        │   └── CRDT ou OT obrigatório
        │       └── Considere Firebase/Supabase
        │
        └── Crítico (pagamentos, estoque)
            └── Servidor é a fonte da verdade
                └── UI otimista + confirmação do servidor
```

### Estratégias de Resolução de Conflitos

| Estratégia          | Como funciona                 | Ideal para                |
| ------------------- | ----------------------------- | ------------------------- |
| **Last-write-wins** | Último timestamp sobrescreve  | Dados simples             |
| **Server-wins**     | Servidor sempre vence         | Transações críticas       |
| **Client-wins**     | Mudanças offline priorizadas  | Apps offline-first        |
| **Merge**           | Combina campo a campo         | Documentos                |
| **CRDT**            | Sem conflitos matematicamente | Colaboração em tempo real |

### Padrão de Fila de Sync

```
CLIENTE:
├── Usuário altera → Salva no banco local
├── Adiciona à fila → { ação, dados, timestamp, tentativas }
├── Rede disponível → Processa FIFO
├── Sucesso → Remove da fila
├── Falha → Retry com backoff (máx 5)
└── Conflito → Aplica estratégia

SERVIDOR:
├── Recebe com timestamp do cliente
├── Compara com versão do servidor
├── Resolve conflito
├── Retorna estado final
└── Cliente atualiza o local
```

---

## 3. Otimização de APIs para Mobile

### Redução do Tamanho da Resposta

| Técnica               | Economia | Implementação               |
| --------------------- | -------- | --------------------------- |
| **Seleção de campos** | 30–70%   | `?fields=id,name,thumbnail` |
| **Compressão**        | 60–80%   | gzip / brotli               |
| **Paginação**         | Variável | Cursor-based                |
| **Imagens variantes** | 50–90%   | `/image?w=200&q=80`         |
| **Delta sync**        | 80–95%   | Apenas dados alterados      |

### Paginação: Cursor vs Offset

```
OFFSET (Ruim):
├── OFFSET 0 LIMIT 20
├── OFFSET 20 LIMIT 20
├── Item novo → duplicação
└── Offset grande = lento

CURSOR (Bom):
├── ?limit=20
├── ?limit=20&after=cursor_x
├── Cursor codificado
├── Sem duplicação
└── Performance constante
```

### Requisições em Lote

```
Em vez de:
GET /users/1
GET /users/2
GET /users/3

Use:
POST /batch
{ requests: [...] }
```

---

## 4. Versionamento do App

### Endpoint de Configuração

*(mantém igual ao original, apenas tradução conceitual)*

Controla:

* Versão mínima
* Atualização forçada
* Feature flags
* Manutenção

---

## 5. Autenticação para Mobile

### Estratégia de Tokens

* **Access Token**: curto, em memória
* **Refresh Token**: longo, SecureStore/Keychain
* **Device Token**: identifica o dispositivo

### Reautenticação Silenciosa

Fluxo automático sem impacto para o usuário quando possível.

---

## 6. Tratamento de Erros para Mobile

### Formato de Erro Mobile

Inclui:

* Código técnico
* Mensagem amigável
* Ação sugerida
* Política de retry

### Categorias de Erro

Inclui tratamento específico para:

* Offline
* Conflito
* Auth expirada
* Rate limit
* Erro de servidor

---

## 7. Mídia & Binários

### Otimização de Imagens

* WebP (Android)
* HEIC (iOS)
* CDN
* Cache agressivo

### Upload em Partes

* Upload resiliente
* Retomável

### Streaming

* HLS / DASH
* Bitrate adaptativo
* Suporte a offline

---

## 8. Segurança Mobile

### Atestação de Dispositivo

* iOS: DeviceCheck
* Android: Play Integrity API

### Assinatura de Requisições

* HMAC
* Timestamp
* Device ID

### Rate Limit

* Por dispositivo
* Por usuário
* Sliding window

---

## 9. Monitoramento & Analytics

### Headers Obrigatórios

Versão, plataforma, SO, modelo, timezone, request ID.

### Alertas

* Erro por versão
* Latência
* Falhas de push
* Falhas de autenticação

---

## 📝 CHECKLIST DE BACKEND MOBILE

### Antes do Design

* [ ] Requisitos mobile claros
* [ ] Offline planejado
* [ ] Estratégia de sync definida

### Para Cada Endpoint

* [ ] Resposta mínima
* [ ] Cursor-based pagination
* [ ] Cache correto
* [ ] Erros acionáveis

### Autenticação

* [ ] Refresh automático
* [ ] Logout multi-device

### Push

* [ ] FCM + APNs
* [ ] Tokens gerenciados
* [ ] Sem dados sensíveis

### Release

* [ ] Controle de versão
* [ ] Feature flags
* [ ] Atualização forçada
* [ ] Monitoramento ativo

---

> **Lembre-se:** backend mobile precisa ser resiliente a redes ruins, respeitar bateria e lidar com sessões interrompidas. O cliente não é confiável — mas também não pode ser abandonado. Forneça offline, sync e caminhos claros de recuperação de erro.
