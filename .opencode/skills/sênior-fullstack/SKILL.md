--- 
name: sênior-fullstack
description: "Kit de ferramentas completo para desenvolvedores fullstack sênior com ferramentas modernas e melhores práticas."
risk: crítico
source: comunidade
date_add: "27/02/2026"
---

# Senior Fullstack

Kit de ferramentas completo para desenvolvedores fullstack sênior com ferramentas modernas e melhores práticas.

## Início Rápido

### Principais Funcionalidades

Esta skill oferece três funcionalidades principais por meio de scripts automatizados:

```bash
# Script 1: Gerador de Scaffold Fullstack
python scripts/fullstack_scaffolder.py [opções]

# Script 2: Gerador de Scaffold de Projeto
python scripts/project_scaffolder.py [opções]

# Script 3: Analisador de Qualidade de Código
python scripts/code_quality_analyzer.py [opções]
```

## Funcionalidades Principais

### 1. Gerador de Scaffold Fullstack

Ferramenta automatizada para tarefas de scaffolding fullstack.

**Recursos:**
- Criação automática de código
- Melhores práticas integradas
- Modelos configuráveis
- Verificações de qualidade

**Uso:**
```bash
python scripts/fullstack_scaffolder.py <caminho-do-projeto> [opções]
```

### 2. Project Scaffolder

Ferramenta abrangente de análise e otimização.

**Recursos:**
- Análise detalhada
- Métricas de desempenho
- Recomendações
- Correções automáticas

**Uso:**
```bash
python scripts/project_scaffolder.py <caminho-de-destino> [--verbose]
```

### 3. Code Quality Analyzer

Ferramentas avançadas para tarefas especializadas.

**Recursos:**
- Automação de nível especialista
- Configurações personalizadas
- Pronto para integração
- Saída de nível de produção

**Uso:**
```bash
python scripts/code_quality_analyzer.py [argumentos] [opções]
```

## Documentação de Referência

### Guia de Tecnologias

Guia completo disponível em `references/tech_stack_guide.md`:

- Padrões e práticas detalhados
- Exemplos de código
- Melhores práticas
- Antipadrões a evitar
- Cenários do mundo real

### Padrões de Arquitetura

Documentação completa do fluxo de trabalho em `references/architecture_patterns.md`:

- Processos passo a passo
- Estratégias de otimização
- Integrações de ferramentas
- Ajuste de desempenho
- Guia de solução de problemas

### Fluxos de Trabalho de Desenvolvimento

Guia de referência técnica em `references/development_workflows.md`:

- Detalhes da pilha de tecnologias
- Exemplos de configuração
- Integração Padrões
- Considerações de segurança
- Diretrizes de escalabilidade

## Pilha de tecnologias

**Linguagens:** TypeScript, JavaScript, Python, Go, Swift, Kotlin
**Frontend:** React, Next.js, React Native, Flutter
**Backend:** Node.js, Express, GraphQL, APIs REST
**Banco de dados:** PostgreSQL, Prisma, NeonDB, Supabase
**DevOps:** Docker, Kubernetes, Terraform, GitHub Actions, CircleCI
**Nuvem:** AWS, GCP, Azure

## Fluxo de trabalho de desenvolvimento

### 1. Configuração e instalação

```bash
# Instalar dependências
npm install
# ou
pip install -r requirements.txt

# Configurar ambiente
cp .env.example .env
```

### 2. Executar verificações de qualidade

```bash
# Usar o script de análise
python scripts/project_scaffolder.py .

# Revisar recomendações
# Aplicar correções
```

### 3. Implementar as melhores práticas

Siga os padrões e práticas documentados em:
- `references/tech_stack_guide.md`
- `references/architecture_patterns.md`
- `references/development_workflows.md`

## Resumo das melhores práticas

### Qualidade do código
- Siga os padrões estabelecidos
- Escreva testes abrangentes
- Documente as decisões
- Revise regularmente

### Desempenho
- Meça antes de otimizar
- Use cache apropriado
- Otimize os caminhos críticos
- Monitore em produção

### Segurança
- Valide todas as entradas
- Use consultas parametrizadas
- Implemente autenticação adequada
- Mantenha as dependências atualizadas

### Manutenibilidade
- Escreva código claro
- Use nomenclatura consistente
- Adicione comentários úteis
- Mantenha a simplicidade

## Comandos comuns

```bash
# Desenvolvimento
npm run dev
npm run build
npm run test
npm run lint

# Análise
python scripts/project_scaffolder.py .

python scripts/code_quality_analyzer.py --analyze

# Implantação
docker build -t app:latest .

docker-compose up -d
kubectl apply -f k8s/
```

## Solução de Problemas

### Problemas Comuns

Consulte a seção completa de solução de problemas em `references/development_workflows.md`.

### Obtendo Ajuda

- Consulte a documentação de referência
- Verifique as mensagens de saída do script
- Consulte a documentação da pilha de tecnologias
- Analise os registros de erros

## Recursos

- Referência de Padrões: `references/tech_stack_guide.md`
- Guia de Fluxo de Trabalho: `references/architecture_patterns.md`
- Guia Técnico: `references/development_workflows.md`
- Scripts de Ferramentas: diretório `scripts/`

## Quando Usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.