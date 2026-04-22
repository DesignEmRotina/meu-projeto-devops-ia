---
name: fundamentos_de_seo
description: Fundamentos de SEO, E-E-A-T, Core Web Vitals e princípios do algoritmo do Google.
tools: Ler, Glob, Grep
---

# Fundamentos de SEO

> Princípios para visibilidade em mecanismos de busca.

---

## 1. Framework E-E-A-T

| Princípio                            | Sinais                                       |
| ------------------------------------ | -------------------------------------------- |
| **Experiência (Experience)**         | Conhecimento em primeira mão, exemplos reais |
| **Especialização (Expertise)**       | Credenciais, profundidade de conhecimento    |
| **Autoridade (Authoritativeness)**   | Backlinks, menções, reconhecimento no setor  |
| **Confiabilidade (Trustworthiness)** | HTTPS, transparência, informações precisas   |

---

## 2. Core Web Vitals

| Métrica | Meta    | O que mede                  |
| ------- | ------- | --------------------------- |
| **LCP** | < 2,5s  | Performance de carregamento |
| **INP** | < 200ms | Interatividade              |
| **CLS** | < 0,1   | Estabilidade visual         |

---

## 3. Princípios de SEO Técnico

### Estrutura do Site

| Elemento       | Finalidade                |
| -------------- | ------------------------- |
| Sitemap XML    | Facilitar o rastreamento  |
| robots.txt     | Controlar acesso dos bots |
| Tags canônicas | Evitar conteúdo duplicado |
| HTTPS          | Sinal de segurança        |

### Performance

| Fator                | Impacto                |
| -------------------- | ---------------------- |
| Velocidade da página | Core Web Vital         |
| Mobile-friendly      | Fator de ranqueamento  |
| URLs limpas          | Melhor rastreabilidade |

---

## 4. Princípios de SEO de Conteúdo

### Elementos da Página

| Elemento                | Boa Prática                               |
| ----------------------- | ----------------------------------------- |
| Title tag               | 50–60 caracteres, palavra-chave no início |
| Meta description        | 150–160 caracteres, persuasiva            |
| H1                      | Um por página, palavra-chave principal    |
| H2–H6                   | Hierarquia lógica                         |
| Texto alternativo (alt) | Descritivo, sem exageros                  |

### Qualidade do Conteúdo

| Fator         | Importância                |
| ------------- | -------------------------- |
| Profundidade  | Cobertura completa do tema |
| Atualização   | Revisões regulares         |
| Originalidade | Valor único                |
| Legibilidade  | Escrita clara              |

---

## 5. Tipos de Schema Markup

| Tipo           | Uso                               |
| -------------- | --------------------------------- |
| Article        | Posts de blog, notícias           |
| Organization   | Informações da empresa            |
| Person         | Perfis de autores                 |
| FAQPage        | Conteúdo de perguntas e respostas |
| Product        | E-commerce                        |
| Review         | Avaliações                        |
| BreadcrumbList | Navegação                         |

---

## 6. Diretrizes para Conteúdo com IA

### O que o Google Valoriza

| ✅ Faça                          | ❌ Não Faça                    |
| ------------------------------- | ----------------------------- |
| Rascunho com IA + edição humana | Publicar conteúdo bruto de IA |
| Adicionar insights originais    | Copiar sem valor agregado     |
| Revisão por especialista        | Ignorar checagem de fatos     |
| Seguir E-E-A-T                  | Keyword stuffing              |

---

## 7. Fatores de Ranqueamento (Prioridade)

| Prioridade | Fator                                   |
| ---------- | --------------------------------------- |
| 1          | Conteúdo relevante e de qualidade       |
| 2          | Backlinks de sites autoritativos        |
| 3          | Experiência da página (Core Web Vitals) |
| 4          | Otimização mobile                       |
| 5          | Fundamentos de SEO técnico              |

---

## 8. Medição e Monitoramento

| Métrica         | Ferramenta             |
| --------------- | ---------------------- |
| Posições        | Search Console, Ahrefs |
| Tráfego         | Analytics              |
| Core Web Vitals | PageSpeed Insights     |
| Indexação       | Search Console         |
| Backlinks       | Ahrefs, Semrush        |

---

> **Lembre-se:** SEO é um jogo de longo prazo. Conteúdo de qualidade + excelência técnica + paciência = resultados.

Verificador de SEO - Auditoria de Otimização para Motores de Busca
Verifica páginas HTML/JSX/TSX em busca de boas práticas de SEO.

OBJETIVO:
    - Verificar meta tags, títulos e descrições
    - Checar tags Open Graph para compartilhamento social
    - Validar a hierarquia de cabeçalhos (H1, H2, etc.)
    - Verificar acessibilidade de imagens (atributos alt)

O QUE ELE ANALISA:
    - Arquivos HTML (páginas web reais)
    - Arquivos JSX/TSX (componentes de página React)
    - Apenas arquivos que provavelmente são páginas PÚBLICAS

Uso:	
    python scripts/verificador_seo.py <caminho_do_projeto>