--- 
name: arquiteto-sênior
description: "Kit de ferramentas completo para arquitetos seniores com ferramentas modernas e melhores práticas."
risk: desconhecido
source: comunidade
date_added "27/02/2026"
---

# Arquiteto Sênior

Kit de ferramentas completo para arquitetos seniores com ferramentas modernas e melhores práticas.

## Início Rápido

### Principais Funcionalidades

Esta skill oferece três funcionalidades principais por meio de scripts automatizados:

```bash
# Script 1: Gerador de Diagramas de Arquitetura
python scripts/gerador-de-diagrama-de-arquitetura.py [opções]

# Script 2: Arquiteto de Projetos
python scripts/arquiteto-de-projeto.py [opções]

# Script 3: Analisador de Dependências
python scripts/analisador-de-dependências.py [opções]

```

## Funcionalidades Principais

### 1. Gerador de Diagramas de Arquitetura

Ferramenta automatizada para tarefas de geração de diagramas de arquitetura.

**Recursos:**
- Criação automática de diagramas de arquitetura
- Melhores práticas integradas
- Modelos configuráveis
- Verificações de qualidade

**Uso:**
```bash
python scripts/gerador-de-diagrama-de-arquitetura.py <caminho-do-projeto> [opções]
```

### 2. Arquiteto de Projetos

Ferramenta abrangente de análise e otimização.

**Recursos:**
- Análise detalhada
- Métricas de desempenho
- Recomendações
- Correções automáticas

**Uso:**
```bash
python scripts/arquiteto-de-projeto.py <caminho-de-destino> [--verbose]
```

### 3. Analisador de Dependências

Ferramentas avançadas para tarefas especializadas.

**Recursos:**
- Automação de nível especialista
- Configurações personalizadas
- Pronto para integração
- Saída de nível de produção

**Uso:**
```bash
python scripts/analisador-de-dependências.py [argumentos] [opções]
```

## Documentação de Referência

### Padrões de Arquitetura

Guia completo disponível em `referencias/padrões-de-arquitetura.md`:

- Padrões e práticas detalhados
- Exemplos de código
- Melhores práticas
- Antipadrões a evitar
- Cenários do mundo real

### Fluxos de Trabalho de Design de Sistemas

Documentação completa do fluxo de trabalho em `referencias/fluxo-de-trabalho-de-projeto-de-sistemas.md`:

- Processos passo a passo
- Estratégias de otimização
- Integrações de ferramentas
- Ajuste de desempenho
- Guia de solução de problemas

### Guia de Decisão Técnica

Guia de referência técnica em `referencias/tech_decision_guide.md`:

- Detalhes da pilha de tecnologia
- Configuração Exemplos
- Padrões de integração
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
python scripts/arquiteto-de-projeto.py .

# Revisar recomendações
# Aplicar correções
```

### 3. Implementar as melhores práticas

Siga os padrões e práticas documentados em:
- `referencias/padrões-de-arquitetura.md`
- `referencias/fluxo-de-trabalho-de-projeto-de-sistemas.md`
- `referencias/tech_decision_guide.md`

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
python scripts/arquiteto-de-projeto.py .

python scripts/analisador-de-dependências.py --analyze

# Implantação
docker build -t app:latest .

docker-compose up -d
kubectl apply -f k8s/
```

## Solução de Problemas

### Problemas Comuns

Consulte a seção completa de solução de problemas em `referencias/tech_decision_guide.md`.

### Obtendo Ajuda

- Consulte a documentação de referência
- Verifique as mensagens de saída do script
- Consulte a documentação da pilha de tecnologias
- Analise os logs de erros

## Recursos

- Referência de Padrões: `referencias/padrões-de-arquitetura.md`
- Guia de Fluxo de Trabalho: `referencias/fluxo-de-trabalho-de-projeto-de-sistemas.md`
- Guia Técnico: `referencias/tech_decision_guide.md`
- Scripts de Ferramentas: diretório `scripts/`

## Quando Usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.