--- 
name: pesquisa-profunda
description: "Executa tarefas de pesquisa autônomas que planejam, pesquisam, leem e sintetizam informações em relatórios abrangentes."
risk: seguro
source: "https://github.com/sanjay3290/ai-skills/tree/main/skills/deep-research"
date_added: "2026-02-27"
---

# Habilidade de Pesquisa Profunda do Gemini

Executa tarefas de pesquisa autônomas que planejam, pesquisam, leem e sintetizam informações em relatórios abrangentes.

## Quando usar esta habilidade

Use esta habilidade quando:
- Realizar análises de mercado
- Conduzir mapeamento da concorrência
- Criar revisões bibliográficas
- Fazer pesquisas técnicas
- Realizar due diligence
- Precisar de relatórios de pesquisa detalhados e com citações

## Requisitos

- Python 3.8 ou superior
- httpx: `pip install -r requirements.txt`
- Variável de ambiente GEMINI_API_KEY

## Configuração

1. Obtenha uma chave da API Gemini no [Google AI Studio](https://aistudio.google.com/)
2. Defina a variável de ambiente:

``bash

export GEMINI_API_KEY=sua-chave-de-api-aqui

``
Ou crie um arquivo `.env` no diretório da habilidade.

## Uso

### Iniciar uma tarefa de pesquisa
```bash
python3 scripts/research.py ​​--query "Pesquisar a história do Kubernetes"
```

### Com formato de saída estruturado
```bash
python3 scripts/research.py ​​--query "Comparar frameworks web Python" \

--format "1. Resumo Executivo\n2. Tabela Comparativa\n3. Recomendações"
```

### Transmitir o progresso em tempo real
```bash
python3 scripts/research.py ​​--query "Analisar o mercado de baterias de veículos elétricos" --stream
```

### Iniciar sem esperar
```bash
python3 scripts/research.py ​​--query "Tópico de pesquisa" --no-wait
```

### Verificar o status da pesquisa em execução
```bash
python3 scripts/research.py ​​--status <interaction_id>
```

### Aguardar conclusão
```bash
python3 scripts/research.py ​​--wait <interaction_id>
```

### Continuar da pesquisa anterior
```bash
python3 scripts/research.py ​​--query "Elaborar sobre o ponto 2" --continue <interaction_id>
```

### Listar pesquisas recentes
```bash
python3 scripts/research.py ​​--list
```

## Formatos de saída

- **Padrão**: Relatório em Markdown legível por humanos
- **JSON** (`--json`): Dados estruturados para uso programático
- **Bruto** (`--raw`): Resposta da API não processada

## Custo e tempo

| Métrica | Valor |

|--------|-------|

| Tempo | 2 a 10 minutos por tarefa |

| Custo | US$ 2 a US$ 5 por tarefa (varia conforme a complexidade) |

| Uso de tokens | Entrada de ~250k-900k, saída de ~60k-80k |

## Melhores Casos de Uso

- Análise de mercado e mapeamento da concorrência
- Revisões de literatura técnica
- Pesquisa de due diligence
- Pesquisa histórica e cronogramas
- Análise comparativa (frameworks, produtos, tecnologias)

## Fluxo de Trabalho

1. O usuário solicita uma pesquisa → Execute `--query "..."`
2. Informe ao usuário o tempo estimado (2-10 minutos)
3. Monitore com `--stream` ou consulte com `--status`
4. Retorne os resultados formatados
5. Use `--continue` para perguntas de acompanhamento

## Códigos de Saída

- **0**: Sucesso
- **1**: Erro (erro de API, problema de configuração, tempo limite excedido)
- **130**: Cancelado pelo usuário (Ctrl+C)