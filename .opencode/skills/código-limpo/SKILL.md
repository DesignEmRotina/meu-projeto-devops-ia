---
nome: código_limpo
descrição: Padrões pragmáticos de codificação - conciso, direto, sem over-engineering, sem comentários desnecessários
ferramentas-permitidas: Ler, Escrever, Editar
versão: 2.0
prioridade: CRÍTICA
***

# Clean Code - Padrões Pragmáticos de Codificação com IA

> **HABILIDADE CRÍTICA** - Seja **conciso, direto e focado na solução**.

***

## Princípios Fundamentais

| Princípio | Regra |
|-----------|-------|
| **SRP** | Responsabilidade Única - cada função/classe faz UMA coisa |
| **DRY** | Don't Repeat Yourself - extraia duplicatas, reutilize |
| **KISS** | Keep It Simple - solução mais simples que funciona |
| **YAGNI** | You Aren't Gonna Need It - não construa funcionalidades não usadas |
| **Boy Scout** | Deixe o código mais limpo do que encontrou |

***

## Regras de Nomenclatura

| Elemento | Convenção |
|----------|-----------|
| **Variáveis** | Revele a intenção: `userCount` não `n` |
| **Funções** | Verbo + substantivo: `getUserById()` não `user()` |
| **Booleanos** | Forma de pergunta: `isActive`, `hasPermission`, `canEdit` |
| **Constantes** | SCREAMING_SNAKE: `MAX_RETRY_COUNT` |

> **Regra:** Se precisar de comentário para explicar um nome, renomeie-o.

***

## Regras de Funções

| Regra | Descrição |
|-------|-----------|
| **Pequena** | Máx. 20 linhas, ideal 5-10 |
| **Uma Coisa** | Faz uma coisa, faz bem |
| **Um Nível** | Um nível de abstração por função |
| **Poucos Args** | Máx. 3 argumentos, prefira 0-2 |
| **Sem Efeitos Colaterais** | Não muta entradas inesperadamente |

***

## Estrutura de Código

| Padrão | Aplicar |
|--------|---------|
| **Cláusulas de Guarda** | Retornos precoces para casos extremos |
| **Plano > Aninhado** | Evite aninhamento profundo (máx. 2 níveis) |
| **Composição** | Pequenas funções compostas juntas |
| **Colocação** | Mantenha código relacionado próximo |

***

## Estilo de Codificação com IA

| Situação | Ação |
|----------|------|
| Usuário pede funcionalidade | Escreva diretamente |
| Usuário reporta bug | Corrija, não explique |
| Sem requisito claro | Pergunte, não assuma |

***

## Anti-Padrões (NÃO FAÇA)

| ❌ Padrão | ✅ Correção |
|-----------|-------------|
| Comentar toda linha | Delete comentários óbvios |
| Helper para one-liner | Inline o código |
| Factory para 2 objetos | Instancie diretamente |
| utils.ts com 1 função | Coloque o código onde é usado |
| "Primeiro importamos..." | Apenas escreva o código |
| Aninhamento profundo | Cláusulas de guarda |
| Números mágicos | Constantes nomeadas |
| Funções Deus | Divida por responsabilidade |

***

## 🔴 Antes de Editar QUALQUER Arquivo (PENSE PRIMEIRO!)

**Antes de alterar um arquivo, pergunte-se:**

| Pergunta | Por quê |
|----------|---------|
| **O que importa este arquivo?** | Pode quebrar |
| **O que este arquivo importa?** | Mudanças de interface |
| **Quais testes cobrem isso?** | Testes podem falhar |
| **É um componente compartilhado?** | Múltiplos lugares afetados |

**Checagem Rápida:**
```
Arquivo a editar: UserService.ts
└── Quem importa isso? → UserController.ts, AuthController.ts
└── Eles precisam de mudanças também? → Verifique assinaturas de funções
```

> 🔴 **Regra:** Edite o arquivo + todos os arquivos dependentes na MESMA tarefa.
> 🔴 **Nunca deixe imports quebrados ou atualizações ausentes.**

***

## Resumo

| Faça | Não faça |
|------|----------|
| Escreva código diretamente | Escreva tutoriais |
| Deixe o código se auto-documentar | Adicione comentários óbvios |
| Corrija bugs imediatamente | Explique a correção primeiro |
| Inline coisas pequenas | Crie arquivos desnecessários |
| Nomeie coisas claramente | Use abreviações |
| Mantenha funções pequenas | Escreva funções de 100+ linhas |

> **Lembre-se: O usuário quer código funcionando, não uma aula de programação.**

***

## 🔴 Auto-Verificação Antes de Concluir (OBRIGATÓRIA)

**Antes de dizer "tarefa concluída", verifique:**

| Checagem | Pergunta |
|----------|----------|
| ✅ **Meta atingida?** | Fiz exatamente o que o usuário pediu? |
| ✅ **Arquivos editados?** | Modifiquei todos os arquivos necessários? |
| ✅ **Código funciona?** | Testei/verifiquei a mudança? |
| ✅ **Sem erros?** | Lint e TypeScript passam? |
| ✅ **Nada esquecido?** | Algum caso extremo perdido? |

> 🔴 **Regra:** Se QUALQUER checagem falhar, corrija antes de concluir.

***

## Scripts de Verificação (OBRIGATÓRIOS)

> 🔴 **CRÍTICO:** Cada agente executa APENAS os scripts de sua própria habilidade após concluir o trabalho.

### Mapeamento Agente → Script

| Agente | Script | Comando |
|--------|--------|---------|
| **especialista_em_front_end** | Auditoria UX | `python .agent/skills/especialista_em_front_end/scripts/auditoria_de_UX.py .` |
| **especialista_em_front_end** | Checagem A11y | `python .agent/skills/especialista_em_front_end/scripts/verificador_de_acessibilidade.py .` |
| **especialista_em_backend** | Validador API | `python .agent/skills/padrões_de_API/scripts/validador_api .` |
| **desenvolvedor_móvel** | Auditoria Mobile | `python .agent/skills/desenvolvedor_móvel/scripts/auditoria_móvel.py .` |
| **arquiteto_de_banco_de_dados** | Validar Schema | `python .agent/skills/design_de_banco_de_dados/scripts/validador_de_esquema.py .` |
| **auditor_de_segurança** | Scan de Segurança | `python .agent/skills/scanner_de_vulnerabilidades/scripts/verificação_de_segurança.py .` |
| **especialista_em_seo** | Checagem SEO | `python .agent/skills/fundamentos_de_seo/scripts/verificador_de_seo.py .` |
| **especialista_em_geo** | Checagem GEO | `python .agent/skills/fundamentos_de_geo/scripts/verificador_de_geo.py .` |
| **otimizador_de_desempenho** | Lighthouse | `python .agent/skills/perfilamento_de_desempenho/scripts/auditoria_lighthouse.py <url>` |
| **engenheiro_de_testes** | Executor de Testes | `python .agent/skills/padrões_de_teste/scripts/executor_de_testes.py .` |
| **engenheiro_de_testes** | Playwright | `python .agent/skills/testes_de_aplicativos_web/scripts/executor_de_playwright.py <url>` |
| **Qualquer agente** | Checagem Lint | `python .agent/skills/verificação_e_validação/scripts/executor_de_lint.py .` |
| **Qualquer agente** | Cobertura de Tipos | `python .agent/skills/verificação_e_validação/scripts/cobertura_de_tipos.py .` |
| **Qualquer agente** | Checagem i18n | `python .agent/skills/localização_i18n/scripts/verificador_i18n.py .` |

> ❌ **ERRADO:** `test-engineer` executando `auditoria_de_UX.py`
> ✅ **CORRETO:** `especialista-em-front-end` executando `auditoria_de_UX.py`

***

### 🔴 Tratamento de Saída de Scripts (LER → RESUMIR → PERGUNTAR)

**Ao executar um script de validação, VOCÊ DEVE:**

1. **Executar o script** e capturar TODA a saída
2. **Parsear a saída** - identificar erros, warnings e aprovações
3. **Resumir para o usuário** neste formato:

```markdown
## Resultados do Script: [nome_do_script.py]

### ❌ Erros Encontrados (X itens)
- [Arquivo:Linha] Descrição do erro 1
- [Arquivo:Linha] Descrição do erro 2

### ⚠️ Warnings (Y itens)
- [Arquivo:Linha] Descrição do warning

### ✅ Aprovado (Z itens)
- Checagem 1 aprovada
- Checagem 2 aprovada

**Devo corrigir os X erros?**
```

4. **Aguardar confirmação do usuário** antes de corrigir
5. **Após corrigir** → Re-executar o script para confirmar

> 🔴 **VIOLAÇÃO:** Executar script e ignorar saída = TAREFA FALHOU.
> 🔴 **VIOLAÇÃO:** Auto-corrigir sem perguntar = Não permitido.
> 🔴 **Regra:** Sempre LER saída → RESUMIR → PERGUNTAR → então corrigir.