nome: modelos_de_documentação
descrição: Templates de documentação e diretrizes de estrutura. README, docs de API, comentários de código e documentação amigável para IA.
ferramenta-permitidas: Ler, Glob, Grep
---
```

# Templates de Documentação

> Templates e diretrizes de estrutura para os tipos mais comuns de documentação.

---

## 1. Estrutura de README

### Seções Essenciais (Ordem de Prioridade)

| Seção                  | Propósito                 |
| ---------------------- | ------------------------- |
| **Título + One-liner** | O que é isso?             |
| **Quick Start**        | Rodar em menos de 5 min   |
| **Features**           | O que posso fazer?        |
| **Configuration**      | Como personalizar         |
| **API Reference**      | Link para docs detalhadas |
| **Contributing**       | Como ajudar               |
| **License**            | Aspectos legais           |

### Template de README

```markdown
# Nome do Projeto

Breve descrição em uma linha.

## Quick Start

[Passos mínimos para rodar]

## Features

- Funcionalidade 1
- Funcionalidade 2

## Configuration

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| PORT | Porta do servidor | 3000 |

## Documentation

- [Referência da API](./docs/api.md)
- [Arquitetura](./docs/architecture.md)

## License

MIT
```

---

## 2. Estrutura de Documentação de API

### Template por Endpoint

```markdown
## GET /users/:id

Obtém um usuário pelo ID.

**Parâmetros:**
| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id | string | Sim | ID do usuário |

**Resposta:**
- 200: Objeto do usuário
- 404: Usuário não encontrado

**Exemplo:**
[Exemplo de request e response]
```

---

## 3. Diretrizes para Comentários de Código

### Template JSDoc/TSDoc

```typescript
/**
 * Descrição breve do que a função faz.
 * 
 * @param paramName - Descrição do parâmetro
 * @returns Descrição do valor retornado
 * @throws ErrorType - Quando esse erro ocorre
 * 
 * @example
 * const result = functionName(input);
 */
```

### Quando Comentar

| ✅ Comentar                 | ❌ Não Comentar            |
| -------------------------- | ------------------------- |
| Por quê (regra de negócio) | O quê (óbvio)             |
| Algoritmos complexos       | Cada linha                |
| Comportamento não óbvio    | Código autoexplicativo    |
| Contratos de API           | Detalhes de implementação |

---

## 4. Template de Changelog (Keep a Changelog)

```markdown
# Changelog

## [Unreleased]
### Added
- Nova funcionalidade

## [1.0.0] - 2025-01-01
### Added
- Release inicial
### Changed
- Dependência atualizada
### Fixed
- Correção de bug
```

---

## 5. Architecture Decision Record (ADR)

```markdown
# ADR-001: [Título]

## Status
Aceito / Depreciado / Substituído

## Contexto
Por que estamos tomando essa decisão?

## Decisão
O que foi decidido?

## Consequências
Quais são os trade-offs?
```

---

## 6. Documentação Amigável para IA (2025)

### Template llms.txt

Para crawlers e agentes de IA:

```markdown
# Nome do Projeto
> Objetivo em uma linha.

## Arquivos Principais
- [src/index.ts]: Entrada principal
- [src/api/]: Rotas da API
- [docs/]: Documentação

## Conceitos-Chave
- Conceito 1: Breve explicação
- Conceito 2: Breve explicação
```

### Documentação Preparada para MCP

Para indexação RAG:

* Hierarquia clara de H1–H3
* Exemplos em JSON/YAML para estruturas de dados
* Diagramas Mermaid para fluxos
* Seções autocontidas

---

## 7. Princípios de Estrutura

| Princípio                    | Por quê                      |
| ---------------------------- | ---------------------------- |
| **Escaneável**               | Headers, listas, tabelas     |
| **Exemplos primeiro**        | Mostrar, não apenas explicar |
| **Detalhamento progressivo** | Simples → Complexo           |
| **Atualizada**               | Desatualizada = enganosa     |

---

> **Lembre-se:** templates são pontos de partida. Adapte às necessidades do seu projeto.
