---
nome: diretrizes_de_design_web
descrição: Revisa código de UI para conformidade com as Diretrizes de Interface Web. Use quando for solicitado “revisar minha UI”, “checar acessibilidade”, “auditar design”, “revisar UX” ou “verificar meu site contra boas práticas”.
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <arquivo-ou-padrão>
---

# Diretrizes de Interface Web

Revisão de arquivos para conformidade com as Diretrizes de Interface Web.

## Como Funciona

1. Buscar as diretrizes mais recentes a partir da URL de origem abaixo
2. Ler os arquivos especificados (ou solicitar ao usuário os arquivos/padrões)
3. Verificar a conformidade com todas as regras das diretrizes obtidas
4. Exibir os achados no formato conciso `arquivo:linha`

## Fonte das Diretrizes

Busque diretrizes atualizadas antes de cada revisão:

```

[https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md)

```

Use **WebFetch** para recuperar as regras mais recentes. O conteúdo obtido contém todas as regras e instruções de formato de saída.

## Uso

Quando o usuário fornecer um arquivo ou argumento de padrão:
1. Buscar as diretrizes na URL de origem acima
2. Ler os arquivos especificados
3. Aplicar todas as regras das diretrizes obtidas
4. Exibir os achados usando o formato especificado nas diretrizes

Se nenhum arquivo for especificado, pergunte ao usuário quais arquivos devem ser revisados.

---

## Skills Relacionadas

| Skill | Quando Usar |
|------|-------------|
| **[design_de_frontend](../design_de_frontend/SKILL.md)** | Antes de codar — Aprender princípios de design (cores, tipografia, psicologia de UX) |
| **diretrizes_de_design_web** (esta) | Depois de codar — Auditar acessibilidade, performance e boas práticas |

## Fluxo de Trabalho de Design

```

1. DESIGN   → Ler princípios de frontend-design
2. CODE     → Implementar o design
3. AUDIT    → Executar a revisão web-design-guidelines ← VOCÊ ESTÁ AQUI
4. FIX      → Corrigir os achados da auditoria

```
```

