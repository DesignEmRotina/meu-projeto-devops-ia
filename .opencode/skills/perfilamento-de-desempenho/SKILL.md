nome: perfilamento_de_desempenho
descrição: Princípios de profiling de performance. Medição, análise e técnicas de otimização.
ferramentas-permitidas: Ler, Glob, Grep, Bash
---


# Performance Profiling (Análise de Performance)

> Meça, analise e otimize — **nesta ordem**.

## 🔧 Scripts de Runtime

**Execute estes scripts para profiling automatizado:**

| Script                        | Objetivo                                | Uso                                                      |
| ----------------------------- | --------------------------------------- | -------------------------------------------------------- |
| `scripts/auditoria_lighthouse.py` | Auditoria de performance com Lighthouse | `python scripts/auditoria_lighthouse.py https://example.com` |

---

## 1. Core Web Vitals

### Metas

| Métrica | Boa     | Ruim    | Mede                |
| ------- | ------- | ------- | ------------------- |
| **LCP** | < 2.5s  | > 4.0s  | Carregamento        |
| **INP** | < 200ms | > 500ms | Interatividade      |
| **CLS** | < 0.1   | > 0.25  | Estabilidade visual |

### Quando Medir

| Etapa           | Ferramenta                 |
| --------------- | -------------------------- |
| Desenvolvimento | Lighthouse local           |
| CI/CD           | Lighthouse CI              |
| Produção        | RUM (Real User Monitoring) |

---

## 2. Workflow de Profiling

### O Processo em 4 Etapas

```
1. BASELINE → Medir o estado atual
2. IDENTIFICAR → Encontrar o gargalo
3. CORRIGIR → Aplicar mudança direcionada
4. VALIDAR → Confirmar a melhoria
```

### Seleção de Ferramentas de Profiling

| Problema               | Ferramenta             |
| ---------------------- | ---------------------- |
| Carregamento da página | Lighthouse             |
| Tamanho do bundle      | Bundle analyzer        |
| Runtime                | DevTools – Performance |
| Memória                | DevTools – Memory      |
| Rede                   | DevTools – Network     |

---

## 3. Análise de Bundle

### O Que Observar

| Problema             | Indicador                |
| -------------------- | ------------------------ |
| Dependências grandes | Topo do bundle           |
| Código duplicado     | Múltiplos chunks         |
| Código não utilizado | Baixa cobertura          |
| Falta de splits      | Chunk único muito grande |

### Ações de Otimização

| Achado                   | Ação                          |
| ------------------------ | ----------------------------- |
| Biblioteca grande        | Importar módulos específicos  |
| Dependências duplicadas  | Deduplicar, atualizar versões |
| Rota no bundle principal | Code splitting                |
| Exports não usados       | Tree shaking                  |

---

## 4. Profiling em Runtime

### Análise da Aba Performance

| Padrão                  | Significado                   |
| ----------------------- | ----------------------------- |
| Long tasks (>50ms)      | Bloqueio da UI                |
| Muitas tarefas pequenas | Oportunidade de batching      |
| Layout / Paint          | Gargalo de renderização       |
| Script                  | Execução pesada de JavaScript |

### Análise da Aba Memory

| Padrão                  | Significado           |
| ----------------------- | --------------------- |
| Heap crescente          | Possível memory leak  |
| Objetos grandes retidos | Verificar referências |
| DOM desconectado        | Falta de limpeza      |

---

## 5. Gargalos Comuns

### Por Sintoma

| Sintoma                    | Causa Provável               |
| -------------------------- | ---------------------------- |
| Carregamento inicial lento | JS grande, render bloqueante |
| Interações lentas          | Handlers de eventos pesados  |
| Travamentos ao scrollar    | Layout thrashing             |
| Memória crescente          | Leaks, referências retidas   |

---

## 6. Prioridades de Quick Wins

| Prioridade | Ação                      | Impacto |
| ---------- | ------------------------- | ------- |
| 1          | Ativar compressão         | Alto    |
| 2          | Lazy load de imagens      | Alto    |
| 3          | Code split de rotas       | Alto    |
| 4          | Cache de assets estáticos | Médio   |
| 5          | Otimizar imagens          | Médio   |

---

## 7. Anti-Patterns

| ❌ Não faça             | ✅ Faça                    |
| ---------------------- | ------------------------- |
| Chutar problemas       | Profile primeiro          |
| Micro-otimizações      | Corrija o maior gargalo   |
| Otimizar cedo demais   | Otimize quando necessário |
| Ignorar usuários reais | Use dados de RUM          |

---

> **Lembre-se:** o código mais rápido é o código que **não roda**. Remova antes de otimizar.

```