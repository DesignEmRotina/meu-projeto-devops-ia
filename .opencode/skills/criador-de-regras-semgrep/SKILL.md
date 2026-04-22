--- 
name: criador-de-regras-semgrep
description: Cria regras Semgrep personalizadas para detectar vulnerabilidades de segurança, padrões de bugs e padrões de código. Use ao escrever regras Semgrep ou criar detecções de análise estática personalizadas.
allowed-tools:
- Bash
- Leitura
- Escrita
- Edição
- Glob
- Grep
- WebFetch
risk: desconhecido
source: comunidade
---

# Criador de Regras Semgrep

Crie regras Semgrep de qualidade para produção com testes e validação adequados.

## Quando usar
**Cenários ideais:**
- Escrever regras Semgrep para padrões de bugs específicos
- Escrever regras para detectar vulnerabilidades de segurança em sua base de código
- Escrever regras no modo taint para vulnerabilidades de fluxo de dados
- Escrever regras para impor padrões de codificação

## Quando NÃO usar

NÃO use esta habilidade para:
- Executar conjuntos de regras Semgrep existentes
- Análise estática geral sem regras personalizadas (use a habilidade `static-analysis`)

## Justificativas para rejeitar

Ao escrever regras Semgrep, rejeite estes atalhos comuns:

- **"O padrão parece completo"** → Ainda assim, execute `semgrep --test --config <id-da-regra>.yaml <id-da-regra>.<ext>` para verificar. Regras não testadas podem ocultar falsos positivos/negativos.

- **"Corresponde ao caso vulnerável"** → Corresponder às vulnerabilidades é metade do trabalho. Verifique se os casos seguros não correspondem (falsos positivos quebram a confiança).

- **"O modo de contaminação é exagerado para isso"** → Se os dados fluem da entrada do usuário para um destino perigoso, o modo de contaminação oferece melhor precisão do que a correspondência de padrões.
- **"Um teste é suficiente"** → Inclua casos extremos: diferentes estilos de codificação, entradas sanitizadas, alternativas seguras e condições de contorno.

- **"Vou otimizar os padrões primeiro"** → Escreva padrões corretos primeiro e otimize-os depois que todos os testes forem aprovados. A otimização prematura causa regressões.

- **"O dump da AST é muito complexo"** → A AST revela exatamente como o Semgrep vê o código. Ignorá-la leva a padrões que não detectam variações sintáticas.

## Antipadrões

**Muito amplo** - corresponde a tudo, inútil para detecção:
```yaml
# RUIM: Corresponde a qualquer chamada de função
padrão: $FUNC(...)

# BOM: Função perigosa específica
padrão: eval(...)
```

**Falta de casos seguros nos testes** - leva a falsos positivos não detectados:
```python
# RUIM: Testa apenas o caso vulnerável
# ruleid: my-rule
dangerous(user_input)

# BOM: Inclui casos seguros para verificar a ausência de falsos positivos
# ruleid: my-rule
dangerous(user_input)

# ok: my-rule
dangerous(sanitize(user_input))

# ok: my-rule
dangerous("hardcoded_safe_value")
```

**Padrões excessivamente específicos** - ignora variações:
```yaml
# RUIM: Corresponde apenas ao valor exato formato
padrão: os.system("rm " + $VAR)

# BOM: Corresponde a todas as chamadas os.system com rastreamento de contaminação
modo: contaminação
destinos de padrão:

- padrão: os.system(...)
```

## Nível de Rigidez

Este fluxo de trabalho é **rigoroso** - não pule etapas:
- **Leia a documentação primeiro**: Consulte a [Documentação](#documentação) antes de escrever regras Semgrep
- **Teste primeiro é obrigatório**: Nunca escreva uma regra sem testes
- **100% de aprovação nos testes é necessária**: "A maioria dos testes passa" não é aceitável
- **A otimização vem por último**: Simplifique os padrões somente depois que todos os testes forem aprovados
- **Evite padrões genéricos**: As regras devem ser específicas e não corresponder a padrões amplos
- **Priorize o modo de contaminação**: Para vulnerabilidades de fluxo de dados
- **Um arquivo YAML - uma regra Semgrep**: Cada arquivo YAML deve conter apenas uma regra Semgrep; Não combine várias regras em um único arquivo.
- **Sem regras genéricas**: Ao direcionar regras Semgrep para um idioma específico, evite a correspondência de padrões genéricos (`languages: generic`).
- **Anotações de teste `todook` e `todook` proibidas**: Anotações `todook: <id-da-regra>` e `todook: <id-da-regra>` em arquivos de teste para futuras melhorias de regras são proibidas.

## Visão Geral

Esta habilidade orienta a criação de regras do Semgrep que detectam vulnerabilidades de segurança e padrões de código. As regras são criadas iterativamente: analise o problema, escreva os testes primeiro, analise a estrutura da AST (Árvore Sintática Abstrata), escreva a regra, itere até que todos os testes sejam aprovados e otimize a regra.

**Seleção da abordagem:**
- **Modo de contaminação** (priorizar): Problemas de fluxo de dados onde entradas não confiáveis ​​chegam a destinos perigosos.
- **Correspondência de padrões**: Padrões sintáticos simples sem requisitos de fluxo de dados.

**Por que priorizar o modo de contaminação?** A correspondência de padrões encontra a sintaxe, mas não o contexto. Um padrão `eval($X)` corresponde tanto a `eval(user_input)` (vulnerável) quanto a `eval("literal_seguro")` (seguro). O modo de contaminação rastreia o fluxo de dados, portanto, ele só alerta quando dados não confiáveis ​​realmente chegam ao destino — reduzindo drasticamente os falsos positivos para vulnerabilidades de injeção.

**Iterando entre abordagens:** É permitido experimentar. Se você começar com o modo de detecção de contaminação e ele não estiver funcionando bem (por exemplo, a contaminação não se propaga como esperado, muitos falsos positivos/negativos), mude para a correspondência de padrões. Por outro lado, se a correspondência de padrões produzir muitos falsos positivos em casos seguros, tente o modo de detecção de contaminação. O objetivo é uma regra funcional, não a adesão rígida a uma única abordagem.

**Estrutura de saída** - exatamente 2 arquivos em um diretório com o nome do ID da regra:
```
<id-da-regra>/
├── <id-da-regra>.yaml # Regra do Semgrep
└── <id-da-regra>.<ext> # Arquivo de teste com anotações ruleid/ok
```

## Início Rápido

```yaml
regras:

- id: insecure-eval

languages: [python]

severidade: ALTA

mensagem: A entrada do usuário passada para eval() permite a execução de código

modo: taint

origens-de-padrão:

- padrão: request.args.get(...)

destinos-de-padrão:

- padrão: eval(...)
```

Arquivo de teste (`insecure-eval.py`):
```python
# ruleid: insecure-eval
eval(request.args.get('code'))

# ok: insecure-eval
eval("print('safe')")
```

Executar testes (a partir do diretório de regras): `semgrep --test --config <rule-id>.yaml <rule-id>.<ext>`

## Referência rápida

- Para comandos, operadores de padrão e sintaxe do modo de taint, consulte quick-reference.md.

Para obter um fluxo de trabalho detalhado e exemplos, você DEVE consultar o arquivo workflow.md.

## Fluxo de Trabalho

Copie esta lista de verificação e acompanhe o progresso:

```
Progresso da Regra Semgrep:
- [ ] Etapa 1: Analisar o Problema
- [ ] Etapa 2: Escrever os Testes Primeiro
- [ ] Etapa 3: Analisar a estrutura AST
- [ ] Etapa 4: Escrever a regra
- [ ] Etapa 5: Iterar até que todos os testes sejam aprovados (semgrep --test)
- [ ] Etapa 6: Otimizar a regra (remover redundâncias, testar novamente)
- [ ] Etapa 7: Execução Final
```

## Documentação

**OBRIGATÓRIO**: Antes de escrever qualquer regra, use o WebFetch para ler **todos** estes 4 links com a documentação do Semgrep:

1. [Sintaxe da Regra](https://semgrep.dev/docs/writing-rules/rule-syntax)
2. [Padrão [Sintaxe](https://semgrep.dev/docs/writing-rules/pattern-syntax)
3. [Manual de Testes ToB - Semgrep](https://appsec.guide/docs/static-analysis/semgrep/advanced/)
4. [Propagação de constantes](https://semgrep.dev/docs/writing-rules/data-flow/constant-propagation)
5. [Índice de Regras de Escrita](https://github.com/semgrep/semgrep-docs/tree/main/docs/writing-rules/)