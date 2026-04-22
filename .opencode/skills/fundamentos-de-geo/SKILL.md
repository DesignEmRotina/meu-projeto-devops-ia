---
nome: fundamentos-de-geo
descrição: Otimização para Motores Generativos (GEO) voltada a mecanismos de busca por IA (ChatGPT, Claude, Perplexity).
ferramentas-permitidas: Ler, Glob, Grep
---

# Fundamentos de GEO

> Otimização para mecanismos de busca baseados em IA.

---

## 1. O que é GEO?

**GEO** = *Generative Engine Optimization* (Otimização para Motores Generativos)

| Objetivo | Plataforma |
|--------|------------|
| Ser citado em respostas de IA | ChatGPT, Claude, Perplexity, Gemini |

### SEO vs GEO

| Aspecto | SEO | GEO |
|-------|-----|-----|
| Objetivo | Rankear em #1 | Ser citado por IAs |
| Plataforma | Google | Motores de IA |
| Métricas | Ranking, CTR | Taxa de citação |
| Foco | Palavras-chave | Entidades, dados |

---

## 2. Ecossistema de Motores de IA

| Motor | Estilo de Citação | Oportunidade |
|------|------------------|--------------|
| **Perplexity** | Numerado [1][2] | Maior taxa de citação |
| **ChatGPT** | Inline / rodapé | GPTs personalizados |
| **Claude** | Contextual | Conteúdo long-form |
| **Gemini** | Seção de fontes | Interseção com SEO |

---

## 3. Fatores de Recuperação (RAG)

Como os motores de IA selecionam conteúdos para citar:

| Fator | Peso |
|-----|------|
| Relevância semântica | ~40% |
| Correspondência de keywords | ~20% |
| Sinais de autoridade | ~15% |
| Atualidade | ~10% |
| Diversidade de fontes | ~15% |

---

## 4. Conteúdo que é Citado

| Elemento | Por que Funciona |
|--------|------------------|
| **Estatísticas originais** | Dados únicos e citáveis |
| **Citações de especialistas** | Transferência de autoridade |
| **Definições claras** | Fácil extração |
| **Guias passo a passo** | Valor prático |
| **Tabelas comparativas** | Informação estruturada |
| **Seções de FAQ** | Respostas diretas |

---

## 5. Checklist de Conteúdo GEO

### Elementos de Conteúdo

- [ ] Títulos baseados em perguntas
- [ ] Resumo / TL;DR no topo
- [ ] Dados originais com fontes
- [ ] Citações de especialistas (nome, cargo)
- [ ] Seção FAQ (3–5 perguntas e respostas)
- [ ] Definições claras
- [ ] Data de “última atualização”
- [ ] Autor com credenciais

### Elementos Técnicos

- [ ] Schema de Article com datas
- [ ] Schema Person para o autor
- [ ] Schema FAQPage
- [ ] Carregamento rápido (< 2.5s)
- [ ] Estrutura HTML limpa e semântica

---

## 6. Construção de Entidade

| Ação | Finalidade |
|----|------------|
| Painel de Conhecimento do Google | Reconhecimento de entidade |
| Wikipédia (se notável) | Fonte de autoridade |
| Informações consistentes na web | Consolidação da entidade |
| Menções no setor | Sinais de autoridade |

---

## 7. Acesso de Crawlers de IA

### Principais User-Agents de IA

| Crawler | Motor |
|------|-------|
| GPTBot | ChatGPT / OpenAI |
| Claude-Web | Claude |
| PerplexityBot | Perplexity |
| Googlebot | Gemini (compartilhado) |

### Decisão de Acesso

| Estratégia | Quando Usar |
|----------|-------------|
| Permitir todos | Deseja citações por IA |
| Bloquear GPTBot | Não quer treino pela OpenAI |
| Seletivo | Permitir alguns, bloquear outros |

---

## 8. Mensuração

| Métrica | Como Medir |
|-------|------------|
| Citações por IA | Monitoramento manual |
| Menções “Segundo [Marca]” | Buscar em IAs |
| Citações de concorrentes | Comparar share |
| Tráfego vindo de IA | Parâmetros UTM |

---

## 9. Anti-Padrões

| ❌ Não Faça | ✅ Faça |
|-----------|---------|
| Publicar sem datas | Inclua timestamps |
| Atribuições vagas | Nomeie fontes |
| Omitir autor | Mostre credenciais |
| Conteúdo raso | Cobertura profunda |

---

> **Lembre-se:** IAs citam conteúdos claros, autoritativos e fáceis de extrair. Seja a melhor resposta.

---

## Script

| Script | Finalidade | Comando |
|------|------------|---------|
| `scripts/verificador_de_geo.py` | Auditoria GEO (prontidão para citação por IA) | `python scripts/verificador_de_geo.py <caminho_do_projeto>` |
