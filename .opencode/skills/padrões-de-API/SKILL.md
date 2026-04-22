---
nome: padrões_de_API
descrição: Princípios de design de APIs e tomada de decisão. Seleção entre REST vs GraphQL vs tRPC, formatos de resposta, versionamento e paginação.
ferramentas-permitidas: Ler, Escrever, Editar, Glob, Grep
---

# Padrões de API

> Princípios de design e tomada de decisão para APIs em 2026.  
> **Aprenda a PENSAR, não a copiar padrões fixos.**

---

## 🎯 Regra de Leitura Seletiva

**Leia APENAS os arquivos relevantes para a solicitação!**  
Consulte o mapa de conteúdo e identifique exatamente o que você precisa.

---

## 📑 Mapa de Conteúdo

| Arquivo | Descrição | Quando Ler |
|-------|-----------|------------|
| `estilo-de-API.md` | Árvore de decisão REST vs GraphQL vs tRPC | Escolha do tipo de API |
| `rest.md` | Nomeação de recursos, métodos HTTP, status codes | Design de API REST |
| `resposta.md` | Envelope de resposta, formato de erro, paginação | Estrutura de resposta |
| `graphql.md` | Design de schema, quando usar, segurança | Avaliação de GraphQL |
| `trpc.md` | Monorepo TypeScript, type safety | Projetos fullstack em TS |
| `controle-de-versão.md` | Versionamento por URI/Header/Query | Planejamento de evolução da API |
| `autenticação.md` | JWT, OAuth, Passkey, API Keys | Seleção de padrão de autenticação |
| `limitação-de-taxa.md` | Token bucket, sliding window | Proteção da API |
| `documentação.md` | Boas práticas OpenAPI/Swagger | Documentação |
| `testes-de-segurança.md` | OWASP API Top 10, testes de auth/authz | Auditorias de segurança |

---

## 🔗 Habilidades Relacionadas

| Necessidade | Skill |
|-----------|-------|
| Implementação de API | `@[skill/especialista_em_backend]` |
| Estrutura de dados | `@[skills/design_de_banco_de_dados]` |
| Detalhes de segurança | `@[skills/scanner_de_vulnerabilidades]` |

---

## ✅ Checklist de Decisão

Antes de projetar uma API, verifique:

- [ ] **Perguntou quem são os consumidores da API?**
- [ ] **Escolheu o estilo de API adequado para ESTE contexto?** (REST / GraphQL / tRPC)
- [ ] **Definiu um formato de resposta consistente?**
- [ ] **Planejou a estratégia de versionamento?**
- [ ] **Considerou as necessidades de autenticação?**
- [ ] **Planejou rate limiting?**
- [ ] **Definiu a abordagem de documentação?**

---

## ❌ Anti-Padrões

### NÃO FAÇA:
- Usar REST como padrão para tudo
- Utilizar verbos em endpoints REST (`/getUsers`)
- Retornar formatos de resposta inconsistentes
- Expor erros internos ao cliente
- Ignorar rate limiting

### FAÇA:
- Escolha o estilo de API com base no contexto
- Pergunte sobre os requisitos dos clientes
- Documente de forma completa
- Utilize status codes HTTP apropriados

---

## Script

| Script | Finalidade | Comando |
|------|------------|---------|
| `scripts/validador_api.py` | Validação de endpoints de API | `python scripts/validador_api.py <project_path>` |
