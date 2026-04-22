--- 
name: avaliação-de-testes-de-desempenho
description: "Você é um especialista em revisão de código com IA, combinando análise estática automatizada, reconhecimento inteligente de padrões e práticas modernas de DevOps. Utilize ferramentas de IA (GitHub Copilot, Qodo, GPT-5, Claude 4.5 Sonnet) com plataformas comprovadas (SonarQube, CodeQL, Semgrep) para identificar bugs, vulnerabilidades e problemas de desempenho.
risk: desconhecido
source: comunidade
date_add: "2026-02-27"
--- 

- Use esta habilidade quando

- Estiver trabalhando em tarefas ou fluxos de trabalho de especialista em revisão de código com IA
- Precisar de orientação, melhores práticas ou listas de verificação para Especialista em revisão de código com IA

## Não utilize esta habilidade quando:

- A tarefa não estiver relacionada à revisão de código com IA
- Você precisar de um domínio ou ferramenta diferente, fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Contexto

Fluxos de trabalho de revisão de código em várias camadas, integrados a pipelines de CI/CD, que fornecem feedback instantâneo sobre pull requests com supervisão humana para decisões arquitetônicas. Revisões em mais de 30 linguagens combinam análise baseada em regras com compreensão contextual assistida por IA.

## Requisitos

Revisão: **$ARGUMENTS**

Realizar análise abrangente: segurança, desempenho, arquitetura, manutenibilidade, testes e preocupações específicas de IA/ML. Gerar comentários de revisão com referências de linha, exemplos de código e recomendações práticas.

## Revisão de Código Automatizada Fluxo de Trabalho

### Triagem Inicial
1. Analisar as diferenças para determinar os arquivos modificados e os componentes afetados
2. Combinar os tipos de arquivo com as ferramentas de análise estática ideais
3. Dimensionar a análise com base no tamanho do PR (superficial > 1000 linhas, profunda < 200 linhas)
4. Classificar o tipo de alteração: recurso, correção de bug, refatoração ou alteração que quebra a compatibilidade

### Análise Estática com Múltiplas Ferramentas
Executar em paralelo:
- **CodeQL**: Análise profunda de vulnerabilidades (injeção de SQL, XSS, bypass de autenticação)
- **SonarQube**: Código com problemas, complexidade, duplicação, manutenibilidade
- **Semgrep**: Regras e políticas de segurança específicas da organização
- **Snyk/Dependabot**: Segurança da cadeia de suprimentos
- **GitGuardian/TruffleHog**: Detecção de segredos

### Revisão Assistida por IA
```python
# Prompt de revisão contextualizado para Claude 4.5 Sonnet
review_prompt = f"""
Você está revisando Uma solicitação de pull para um aplicativo {language} {project_type}.

**Resumo das Alterações:** {pr_description}
**Código Modificado:** {code_diff}
**Análise Estática:** {sonarqube_issues}, {codeql_alerts}
**Arquitetura:** {system_architecture_summary}

Foco em:
1. Vulnerabilidades de segurança não detectadas por ferramentas estáticas
2. Implicações de desempenho em escala
3. Casos extremos e lacunas no tratamento de erros
4. Compatibilidade com contratos de API
5. Testabilidade e cobertura ausente
6. Alinhamento arquitetônico

Para cada problema:
- Especifique o caminho do arquivo e os números das linhas
- Classifique a gravidade: CRÍTICA/ALTA/MÉDIA/BAIXA
- Explique o problema (1-2 frases)
- Forneça um exemplo concreto de correção
- Inclua links para a documentação relevante

Formatar como um array JSON.

""
```

### Seleção de Modelo (2025)
- **Revisões rápidas (<200 linhas)**: GPT-4o-mini ou Claude 4.5 Haiku
- **Raciocínio profundo**: Claude 4.5 Sonnet ou GPT-4.5 (mais de 200 mil tokens)
- **Geração de código**: GitHub Copilot ou Qodo
- **Multilíngue**: Qodo ou CodeAnt AI (mais de 30 idiomas)

### Roteamento de revisão
```typescript
interface ReviewRoutingStrategy {

async routeReview(pr: PullRequest): Promise<ReviewEngine> {

const metrics = await this.analyzePRComplexity(pr);

if (metrics.filesChanged > 50 || metrics.linesChanged > 1000) {

return new HumanReviewRequired("Muito grande para automação");

}

if (metrics.securitySensitive || metrics.affectsAuth) {

return new AIEngine("claude-3.7-sonnet", {

temperatura: 0.1,

maxTokens: 4000,
systemPrompt: SECURITY_FOCUSED_PROMPT
});

}

if (metrics.testCoverageGap > 20) {
return new QodoEngine({ mode: "test-generation", coverageTarget: 80 });

}

return new AIEngine("gpt-4o", { temperature: 0.3, maxTokens: 2000 });

}
}
```

## Análise de Arquitetura

### Coerência Arquitetural
1. **Direção da Dependência**: Camadas internas não dependem de camadas externas
2. **Princípios SOLID**:

- Responsabilidade Única, Aberto/Fechado, Substituição de Liskov

- Segregação de Interfaces, Inversão de Dependência
3. **Antipadrões**:

- Singleton (estado global), Objetos Deus (>500 linhas, >20 métodos)

- Modelos anêmicos, Cirurgia de espingarda

### Revisão de Microsserviços
```go
type MicroserviceReviewChecklist struct {

CheckServiceCohesion bool // Capacidade única por serviço?

CheckDataOwnership bool // Cada serviço possui o banco de dados?

CheckAPIVersioning bool // Versionamento semântico?

CheckBackwardCompatibility bool // Alterações que quebram a compatibilidade sinalizadas?

CheckCircuitBreakers bool // Padrões de resiliência?

CheckIdempotency bool // Tratamento de eventos duplicados?
}

func (r *MicroserviceReviewer) AnalyzeServiceBoundaries(code string) []Issue {

issues := []Issue{}

if detectsSharedDatabase(code) {

issues = append(issues, Issue{
Severity: "HIGH",

Category: "Architecture",

Message: "Services sharing database violates bounded context",

Fix: "Implement database-per-service with eventual consistency",

})

}

if hasBreakingAPIChanges(code) && !hasDeprecationWarnings(code) {

issues = append(issues, Issue{

Severity: "CRITICAL",

Category: "API Design",

Message: "Breaking change without deprecation period",

Fix: "Mantain backward compatibility via versioning (v1, v2)",

})

}

return issues
}
```

## Detecção de Vulnerabilidades de Segurança

### Segurança em Múltiplas Camadas
**Camada SAST**: CodeQL, Semgrep, Bandit/Brakeman/Gosec

**Modelagem de Ameaças Aprimorada por IA**:
```python
security_analysis_prompt = """
Analisar o código de autenticação em busca de vulnerabilidades:
{code_snippet}

Verificar:
1. Bypass de autenticação, controle de acesso quebrado (IDOR)
2. Falhas na validação do token JWT
3. Fixação/sequestro de sessão, ataques de temporização
4. Ausência de limitação de taxa, armazenamento inseguro de senhas
5. Lacunas na proteção contra credential stuffing

Fornecer: identificador CWE, pontuação CVSS, cenário de exploração, código de correção
"""

findings = claude.analyze(security_analysis_prompt, temperature=0.1)
```

**Verificação de Segredos**:
```bash
trufflehog git file://. --json | \
jq '.[] | select(.Verified == true) | {

secret_type: .DetectorName,

file: .SourceMetadata.Data.Filename,

severity: "CRITICAL"

}'
```

### OWASP Top 10 (2025)
1. **A01 - Controle de Acesso Quebrado**: Ausência de autorização, IDOR
2. **A02 - Falhas Criptográficas**: Hash fraco, RNG inseguro
3. **A03 - Injeção**: SQL, NoSQL, injeção de comando via análise de contaminação
4. **A04 - Design Inseguro**: Ausência de modelagem de ameaças
5. **A05 - Configuração de Segurança Incorreta**: Credenciais padrão
6. **A06 - Componentes Vulneráveis**: Snyk/Dependabot para CVEs
7. **A07 - Falhas de Autenticação**: Gerenciamento de sessão fraco
8. **A08 - Falhas de Integridade de Dados**: JWTs não assinados
9. **A09 - Registro de Logs** Falhas**: Logs de auditoria ausentes
10. **A10 - SSRF**: URLs controladas pelo usuário não validadas

## Análise de Desempenho

### Perfil de Desempenho
```javascript
class PerformanceReviewAgent {

async analyzePRPerformance(prNumber) {

const baseline = await this.loadBaselineMetrics('main');

const prBranch = await this.runBenchmarks(`pr-${prNumber}`);

const regressions = this.detectRegressions(baseline, prBranch, {

cpuThreshold: 10, memoryThreshold: 15, latencyThreshold: 20

});

if (regressions.length > 0) {
await this.postReviewComment(prNumber, {
severity: 'HIGH',

title: '⚠️ Regressão de desempenho detectada',
body: this.formatRegressionReport(regressions),
suggestions: await this.aiGenerateOptimizations(regressions)
});
}

}
}
```

### Sinais de Alerta de Escalabilidade
- **Consultas N+1**, **Índices Ausentes**, **Chamadas Externas Síncronas**
- **Estado em Memória**, **Coleções Ilimitadas**, **Paginação Ausente**

- **Sem Pool de Conexões**, **Sem Limitação de Taxa**

```python
def detect_n_plus_1_queries(code_ast):

issues = []

for loop in find_loops(code_ast):

db_calls = find_database_calls_in_scope(loop.body)

if len(db_calls) > 0:

issues.append({

'severity': 'HIGH',

'line': loop.line_number,

'message': f'Consulta N+1: {len(db_calls)} chamadas ao banco de dados em loop',

'fix': 'Use eager loading' (JOIN) ou carregamento em lote'

})

retornar problemas
```

## Geração de Comentários de Revisão

### Formato Estruturado
```typescript
interface ReviewComment {

path: string; line: number;

severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW' | 'INFO';

category: 'Security' | 'Performance' | 'Bug' | 'Maintainability';

title: string; description: string;

codeExample?: string; references?: string[];

autoFixable: boolean; cwe?: string; cvss?: number;

effort: 'trivial' | 'easy' | 'medium' | 'hard';

}

const comment: ReviewComment = {

path: "src/auth/login.ts", line: 42,

severity: "CRITICAL", category: "Security",

title: "SQL Injection in Login Query",

description: `A concatenação de strings com a entrada do usuário permite injeção de SQL.

**Vetor de Ataque:** A entrada 'admin' OR '1'='1' ignora a autenticação.

**Impacto:** Ignora completamente a autenticação, acesso não autorizado.`,

codeExample: `
// ❌ Vulnerável
const query = \`SELECT * FROM users WHERE username = '\${username}'\`;

// ✅ Seguro
const query = 'SELECT * FROM users WHERE username = ?';

const result = await db.execute(query, [username]);
`,

references: ["https://cwe.mitre.org/data/definitions/89.html"],

autoFixable: false, cwe: "CWE-89", cvss: 9.8, effort: "easy"
};

```

## Integração CI/CD

### GitHub Actions
```yaml
name: AI Code Review
on:
pull_request:

types: [opened, synchronize, reopened]

jobs:

ai-review:

runs-on: ubuntu-latest

steps:

- uses: actions/checkout@v4

- name: Static Analysis

run: |

sonar-scanner -Dsonar.pullrequest.key=${{ github.event.number }}

codeql database create codeql-db --language=javascript,python

semgrep scan --config=auto --sarif --output=semgrep.sarif

- name: Revisão Aprimorada por IA (GPT-5)

env:

OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

run: |

python scripts/ai_review.py \

--pr-number ${{ github.event.number }} \

--model gpt-4o \

--static-analysis-results codeql.sarif,semgrep.sarif

- name: Postar Comentários
uses: actions/github-script@v7

with:

script: |
const comments = JSON.parse(fs.readFileSync('review-comments.json'));

for (const comment of comments) {
await github.rest.pulls.createReviewComment({
owner: context.repo.owner,
repo: context.repo.repo,
pull_number: context.issue.number,
body: comment.body, path: comment.path, line: comment.line

});

}

- name: Quality Gate

run: |

CRITICAL=$(jq '[.[] | select(.severity == "CRITICAL")] | length' review-comments.json)

if [ $CRITICAL -gt 0 ]; então

echo "❌ Encontrados $CRITICAL problemas críticos"

exit 1

fi
```

## Exemplo completo: Automação de revisão por IA

```python
#!/usr/bin/env python3
import os, json, subprocess
from dataclasses import dataclass
from typing import List, Dict, Any
from anthropic import Anthropic

@dataclass
class ReviewIssue:

file_path: str; line: int; severity: str

category: str; title: str; description: str

code_example: str = ""; auto_fixable: bool = False

class CodeReviewOrchestrator:

def __init__(self, pr_number: int, repo: str):

self.pr_number = pr_number; self.repo = repo

self.github_token = os.environ['GITHUB_TOKEN']

self.anthropic_client = Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

self.issues: List[ReviewIssue] = []

def run_static_analysis(self) -> Dict[str, Any]:

results = {}

# SonarQube

subprocess.run(['sonar-scanner', f'-Dsonar.projectKey={self.repo}'], check=True)

# Semgrep

semgrep_output = subprocess.check_output(['semgrep', 'scan', '--config=auto', '--json'])

results['semgrep'] = json.loads(semgrep_output)

return results

def ai_review(self, diff: str, static_results: Dict) -> List[ReviewIssue]:

prompt = f"""Revise este PR de forma abrangente.

**Diff:** {diff[:15000]}
**Análise Estática:** {json.dumps(static_results, indent=2)[:5000]}

Foco: Segurança, Desempenho, Arquitetura, Riscos de bugs, Manutenibilidade

Retorna um array JSON:
[{{
"file_path": "src/auth.py", "line": 42, "severity": "CRITICAL",

"category": "Segurança", "title": "Breve resumo",

"description": "Explicação detalhada", "code_example": "Código de correção"
}}]
"""

resposta = self.anthropic_client.messages.create(

modelo="claude-3-5-sonnet-20241022",
max_tokens=8000, temperatura=0.2,
mensagens=[{"role": "user", "content": prompt}]

)

conteúdo = resposta.content[0].texto

se '```json' em conteúdo:

conteúdo = conteúdo.split('```json')[1].split('```')[0]

return [ReviewIssue(**issue) for issue in json.loads(content.strip())]

def post_review_comments(self, issues: List[ReviewIssue]):

resumo = "## 🤖 Revisão de Código com IA\n\n"

por_gravidade = {}

para issue in issues:

por_gravidade.setdefault(issue.severity, []).append(issue)

for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:

count = len(by_severity.get(severity, []))

if count > 0:

summary += f"- **{severity}**: {count}\n"

critical_count = len(by_severity.get('CRITICAL', []))

view_data = {

'body': summary,

'event': 'REQUEST_CHANGES' if critical_count > 0 else 'COMMENT',

'comments': [issue.to_github_comment() for issue in issues]

}

# Postar na API do GitHub

print(f"✅ Publicou avaliação com {len(issues)} comentários")

if __name__ == '__main__':

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--pr-number', type=int, required=True)

parser.add_argument('--repo', required=True)

args = parser.parse_args()

reviewer = CodeReviewOrchestrator(args.pr_number, args.repo)

static_results = reviewer.run_static_analysis()

diff = reviewer.get_pr_diff()
ai_issues = reviewer.ai_review(diff, static_results)

reviewer.post_review_comments(ai_issues)
```

## Resumo

Revisão de código abrangente com IA, combinando:
1. Análise estática com múltiplas ferramentas (SonarQube, CodeQL, Semgrep)
2. Modelos de Aprendizado de Máquina de Liderança (LLMs) de última geração (GPT-5, Claude) 4.5 Sonnet)
3. Integração perfeita de CI/CD (GitHub Actions, GitLab, Azure DevOps)
4. Suporte para mais de 30 linguagens com linters específicos para cada linguagem
5. Comentários de revisão acionáveis ​​com gravidade e exemplos de correção
6. Rastreamento de métricas DORA para eficácia da revisão
7. Portões de qualidade que impedem código de baixa qualidade
8. Geração automática de testes via Qodo/CodiumAI

Use esta ferramenta para transformar a revisão de código de um processo manual para uma garantia de qualidade automatizada com auxílio de IA, detectando problemas precocemente e fornecendo feedback instantâneo.