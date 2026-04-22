# Geração Dinâmica de Perguntas

> **PRINCÍPIO:** Perguntas não servem apenas para coletar dados — elas existem para **revelar consequências arquiteturais**.
>
> Toda pergunta deve se conectar a uma decisão concreta de implementação que impacte custo, complexidade ou prazo.

---

## 🧠 Princípios Fundamentais

### 1. Perguntas Revelam Consequências

Uma boa pergunta não é “Qual cor você quer?”, mas sim:

```markdown
❌ RUIM: "Qual método de autenticação?"
✅ BOM: "Os usuários devem se cadastrar com e-mail/senha ou login social?

   Impacto:
   - E-mail/Senha → Necessita reset de senha, hashing, infraestrutura de 2FA
   - Social → Provedores OAuth, mapeamento de perfil, menos controle

   Trade-off: Segurança vs. Tempo de desenvolvimento vs. Fricção para o usuário"
````

### 2. Contexto Antes do Conteúdo

Primeiro, entenda **onde** esse pedido se encaixa:

| Contexto                      | Foco das Perguntas                                                     |
| ----------------------------- | ---------------------------------------------------------------------- |
| **Greenfield** (projeto novo) | Decisões de base: stack, hospedagem, escala                            |
| **Adição de Feature**         | Pontos de integração, padrões existentes, mudanças quebráveis          |
| **Refatoração**               | Por que refatorar? Performance? Manutenibilidade? O que está quebrado? |
| **Debug**                     | Sintomas → Causa raiz → Caminho de reprodução                          |

### 3. Perguntas Minimamente Viáveis

**PRINCÍPIO:** Cada pergunta deve eliminar uma bifurcação no caminho de implementação.

```
Antes da Pergunta:
├── Caminho A: Fazer X (5 min)
├── Caminho B: Fazer Y (15 min)
└── Caminho C: Fazer Z (1 hora)

Depois da Pergunta:
└── Caminho Confirmado: Fazer X (5 min)
```

Se uma pergunta não reduz caminhos de implementação → **EXCLUA-A**.

### 4. Perguntas Geram Dados, Não Suposições

```markdown
❌ SUPOSIÇÃO: "O usuário provavelmente quer Stripe para pagamentos"
✅ PERGUNTA: "Qual provedor de pagamento atende melhor às suas necessidades?

   Stripe → Melhor documentação, 2,9% + US$0,30, foco EUA
   LemonSqueezy → Merchant of Record, 5% + US$0,50, impostos globais
   Paddle → Precificação complexa, gerencia VAT da UE, foco enterprise"
```

---

## 📋 Algoritmo de Geração de Perguntas

```
ENTRADA: Pedido do usuário + Contexto (greenfield/feature/refactor/debug)
│
├── PASSO 1: Analisar o Pedido
│   ├── Extrair domínio (ecommerce, auth, realtime, cms, etc.)
│   ├── Extrair funcionalidades (explícitas e implícitas)
│   └── Extrair indicadores de escala (usuários, volume de dados, frequência)
│
├── PASSO 2: Identificar Pontos de Decisão
│   ├── O que DEVE ser decidido antes de codar? (bloqueante)
│   ├── O que PODE ser decidido depois? (adiável)
│   └── O que tem IMPACTO ARQUITETURAL? (alto impacto)
│
├── PASSO 3: Gerar Perguntas (Ordem de Prioridade)
│   ├── P0: Decisões bloqueantes (não avança sem resposta)
│   ├── P1: Alto impacto (afeta >30% da implementação)
│   ├── P2: Impacto médio (afeta features específicas)
│   └── P3: Opcional (edge cases, otimizações)
│
└── PASSO 4: Formatar Cada Pergunta
    ├── O quê: Pergunta clara
    ├── Por quê: Impacto na implementação
    ├── Opções: Trade-offs (não apenas A vs B)
    └── Padrão: O que acontece se o usuário não responder
```

---

## 🎯 Bancos de Perguntas por Domínio

### E-Commerce

| Pergunta                          | Por que Importa                                                        | Trade-offs                           |
| --------------------------------- | ---------------------------------------------------------------------- | ------------------------------------ |
| **Single ou Multi-vendor?**       | Multi-vendor → Comissão, dashboards de vendedores, split de pagamentos | +Receita, -Complexidade              |
| **Controle de Estoque?**          | Tabelas de estoque, lógica de reserva, alertas de baixo estoque        | +Precisão, -Tempo de desenvolvimento |
| **Produtos Digitais ou Físicos?** | Digital → Links de download, sem frete                                 | Físico → APIs de envio, rastreio     |
| **Assinatura ou Compra Única?**   | Assinatura → Cobrança recorrente, dunning, proration                   | +Receita, -Complexidade              |

### Autenticação

| Pergunta                         | Por que Importa                                | Trade-offs           |
| -------------------------------- | ---------------------------------------------- | -------------------- |
| **Login Social é necessário?**   | OAuth vs. infraestrutura de reset de senha     | +UX, -Controle       |
| **Permissões por Papel (RBAC)?** | Tabelas RBAC, políticas, UI admin              | +Segurança, -Tempo   |
| **2FA obrigatório?**             | Infra TOTP/SMS, códigos de backup, recuperação | +Segurança, -Fricção |
| **Verificação de E-mail?**       | Tokens, serviço de e-mail, reenvio             | +Segurança, -Fricção |

### Tempo Real

| Pergunta                            | Por que Importa                                                 | Trade-offs                             |
| ----------------------------------- | --------------------------------------------------------------- | -------------------------------------- |
| **WebSocket ou Polling?**           | WS → Escala do servidor, conexões                               | Polling → Mais simples, maior latência |
| **Usuários simultâneos esperados?** | <100 → 1 servidor; >1000 → Redis pub/sub; >10k → infra dedicada | +Escala, -Complexidade                 |
| **Persistência de mensagens?**      | Tabelas de histórico, custo de storage                          | +UX, -Custo                            |
| **Efêmero ou Durável?**             | Efêmero → Memória; Durável → DB antes de emitir                 | +Confiabilidade, -Latência             |

### Conteúdo / CMS

| Pergunta                    | Por que Importa                        | Trade-offs                      |
| --------------------------- | -------------------------------------- | ------------------------------- |
| **Rich Text ou Markdown?**  | Rich Text → Sanitização, risco XSS     | Markdown → Simples, sem WYSIWYG |
| **Fluxo Draft/Publicação?** | Status, jobs agendados, versionamento  | +Controle, -Complexidade        |
| **Mídia (uploads)?**        | Endpoints, storage, otimização         | +Features, -Tempo               |
| **Multi-idioma?**           | Tabelas i18n, UI de tradução, fallback | +Alcance, -Complexidade         |

---

## 📐 Template Dinâmico de Perguntas

```markdown
Com base no seu pedido de [DOMÍNIO] [FEATURE]:

## 🔴 CRÍTICO (Decisões Bloqueantes)

### 1. **[PONTO DE DECISÃO]**

**Pergunta:** [Pergunta clara e específica]

**Por que isso importa:**
- [Explique a consequência arquitetural]
- [Impacta: custo / complexidade / prazo / escala]

**Opções:**
| Opção | Prós | Contras | Melhor Para |
|------|------|---------|-------------|
| A | [Vantagem] | [Desvantagem] | [Caso de uso] |
| B | [Vantagem] | [Desvantagem] | [Caso de uso] |

**Se não especificado:** [Escolha padrão + justificativa]

---

## 🟡 ALTO IMPACTO (Afeta Implementação)

### 2. **[PONTO DE DECISÃO]**
[Mesmo formato]

---

## 🟢 OPCIONAL (Casos de Borda)

### 3. **[PONTO DE DECISÃO]**
[Mesmo formato]
```

---

## 🔄 Questionamento Iterativo

### Primeira Passagem (3–5 Perguntas)

Foque nas **decisões bloqueantes**. Não avance sem respostas.

### Segunda Passagem (Após Implementação Inicial)

Conforme padrões surgirem, pergunte:

* “Essa feature implica [X]. Devemos tratar o [edge case] agora ou adiar?”
* “Estamos usando o [Padrão A]. A [Feature B] deve seguir o mesmo padrão?”

### Terceira Passagem (Otimização)

Quando a funcionalidade estiver pronta:

* “Gargalo de performance em [X]. Otimizar agora ou é aceitável?”
* “Refatorar [Y] para manutenibilidade ou entregar como está?”

---

## 🎭 Exemplo: Geração Completa de Perguntas

```
PEDIDO DO USUÁRIO: "Criar um clone do Instagram"

PASSO 1: Análise
├── Domínio: Mídias Sociais
├── Features: Compartilhamento de fotos, engajamento (likes/comentários), perfis
├── Implícito: Feed, seguir usuários, autenticação
└── Escala: Potencialmente alta (apps sociais viralizam)

PASSO 2: Pontos de Decisão
├── Bloqueantes: Estratégia de storage, autenticação, tipo de feed
├── Alto impacto: Notificações em tempo real, modelo de dados
└── Adiáveis: Analytics, busca avançada, reels/vídeo

PASSO 3: Perguntas (Prioridade)

P0 (Bloqueantes):
1. Estratégia de Storage → Impacta arquitetura, custo, velocidade
2. Algoritmo de Feed → Impacta queries e complexidade
3. Método de Auth → Impacta tempo, UX e segurança

P1 (Alto impacto):
4. Notificações em tempo real → WebSocket vs polling
5. Processamento de mídia → Cliente vs servidor

P2 (Adiáveis):
6. Stories/Reels → Feature grande, adiar para v2
7. DM/Chat → Subsistema separado, adiar para v2

PASSO 4: Formatar Saída
```

---

## 📊 Saída Gerada (Exemplo)

```
Com base no seu pedido de clone do Instagram:

## 🔴 DECISÕES CRÍTICAS (Não avançamos sem resposta)

### 1. **Estratégia de Armazenamento de Fotos**

**Pergunta:** Onde as fotos dos usuários serão armazenadas e servidas?

**Por que isso importa:**
- Impacta: custos mensais, velocidade de carregamento, complexidade de CDN
- Apps sociais: 1000 usuários × 10 fotos × 2MB = 20GB

**Opções:**
| Opção | Custo | Velocidade | Complexidade | Melhor Para |
|------|-------|------------|--------------|-------------|
| **Cloudinary** | US$89/mês (25GB) | Rápida (CDN) | Baixa | MVP, lançamento rápido |
| **AWS S3 + CloudFront** | US$0,023/GB | Rápida | Média | Produção, custo otimizado |
| **Supabase Storage** | Free 1GB | Média | Baixa | Escala pequena |
| **Local** | Custo servidor | Lenta | Baixa | Apenas dev |

**Se não especificado:** Cloudinary (equilíbrio para MVP)

---

### 2. **Algoritmo do Feed**

**Pergunta:** Como deve funcionar o feed principal?

**Por que isso importa:**
- Impacta: complexidade de queries, cache, tempo de dev
- Feed algorítmico requer ML e sinais de ranking

**Opções:**
| Opção | Complexidade | Impacto no DB | Melhor Para |
|------|--------------|---------------|-------------|
| **Cronológico** | Baixa | Query simples | Estágio inicial |
| **Apenas Seguindo** | Média | JOIN + paginação | Apps sociais comuns |
| **Algorítmico** | Alta | Tabelas pré-computadas | Concorrente do Instagram |

**Se não especificado:** Apenas Seguindo (equilíbrio)

---

### 3. **Abordagem de Autenticação**

**Pergunta:** Como os usuários se cadastram e fazem login?

**Por que isso importa:**
- Impacta: tempo de dev (2–5h), segurança, UX

**Opções:**
| Opção | Tempo Dev | Segurança | UX | Melhor Para |
|------|-----------|-----------|----|-------------|
| **E-mail/Senha** | 4–5h | Alta (com 2FA) | Média | Controle total |
| **Apenas Social** | 1–2h | Dependente | Suave | B2C |
| **Magic Link** | 2–3h | Média | Muito suave | Segurança |
| **Clerk/Auth0** | 1h | Alta | Suave | Time-to-market |

**Se não especificado:** Clerk (mais rápido para MVP)

---

## 🟡 ALTO IMPACTO (Afeta Arquitetura)

### 4. **Notificações em Tempo Real**

**Pergunta:** Os usuários precisam de notificações instantâneas?

**Por que isso importa:**
- WebSocket adiciona complexidade (Redis pub/sub)
- Polling é mais simples, porém com latência

**Opções:**
| Opção | Complexidade | Custo | Melhor Para |
|------|--------------|-------|-------------|
| **WebSocket + Redis** | Alta | US$10+/mês | >1000 usuários |
| **Polling (30s)** | Baixa | Queries no DB | <1000 usuários |
| **Sem tempo real** | Nenhuma | Nenhum | MVP |

**Se não especificado:** Polling (MVP)

---

## 🟢 OPCIONAL (v2)

### 5. **Vídeo/Reels**
- Alta complexidade (processamento/streaming)
- Recomendação: lançar só com fotos

### 6. **Mensagens Diretas**
- Subsistema separado
- Recomendação: usar serviço pronto ou adiar

---

## 📋 Resumo

| Decisão | Recomendação | Se Mudar |
|--------|---------------|----------|
| Storage | Cloudinary | +3h setup |
| Feed | Apenas seguindo | +2h otimização |
| Auth | Clerk | -3h dev |
| Tempo real | Polling | +5h WebSocket |
| Vídeo | Adiar v2 | N/A |
| DM | Adiar v2 | N/A |

**Tempo estimado do MVP:** 15–20 horas
```

---

## 🎯 Recapitulando os Princípios

1. **Toda pergunta = decisão arquitetural** → Não é coleta de dados
2. **Mostre trade-offs** → Usuário entende consequências
3. **Priorize decisões bloqueantes** → Sem elas, não avança
4. **Forneça padrões** → Se não responder, seguimos
5. **Sensível ao domínio** → Ecommerce ≠ Auth ≠ Tempo real
6. **Iterativo** → Novas perguntas surgem durante a implementação

```
