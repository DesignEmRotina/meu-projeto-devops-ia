--- 
name: teste-QA
description: "Fluxo de trabalho abrangente para testes e garantia de qualidade, incluindo testes unitários, testes de integração, testes de ponta a ponta, automação de navegadores e controle de qualidade."
category: pacote de fluxo de trabalho
risk: seguro
source: pessoal
date_add: "27/02/2026"
---

# Pacote de Fluxo de Trabalho de Testes/Garantia de Qualidade

## Visão Geral

Fluxo de trabalho abrangente para testes e garantia de qualidade, incluindo testes unitários, testes de integração, testes de ponta a ponta, automação de navegadores e controles de qualidade para software pronto para produção.

## Quando usar este fluxo de trabalho

Use este fluxo de trabalho quando:
- Configurar a infraestrutura de testes
- Escrever testes unitários e de integração
- Implementar testes de ponta a ponta (E2E)
- Automatizar testes de navegador
- Estabelecer critérios de qualidade
- Realizar revisão de código

## Fases do fluxo de trabalho

### Fase 1: Estratégia de teste

#### Habilidades a serem invocadas
- `test-automator` - Automação de testes
- `test-driven-development` - Desenvolvimento orientado a testes (TDD)

#### Ações
1. Definir a estratégia de teste
2. Escolher frameworks de teste
3. Planejar a cobertura de testes
4. Configurar a infraestrutura de testes
5. Configurar a integração contínua (CI)

#### Instruções para copiar e colar
```
Use @test-automator para definir a estratégia de teste
```

```
Use @test-driven-development para implementar o fluxo de trabalho TDD
```

### Fase 2: Testes unitários

#### Habilidades a serem invocadas
- `javascript-testing-patterns` - Jest/Vitest
- `python-testing-patterns` - pytest
- `unit-testing-test-generate` - Geração de testes
- `tdd-orchestrator` - Orquestração de TDD

#### Ações
1. Escrever testes unitários
2. Configurar fixtures de teste
3. Configurar mocks
4. Medir a cobertura
5. Integrar com CI

#### Instruções para copiar e colar
``` Use @javascript-testing-patterns para escrever testes Jest
```

``` Use @python-testing-patterns para escrever testes pytest
```

``` Use @unit-testing-test-generate para gerar testes unitários
```

### Fase 3: Teste de Integração

#### Skills a serem invocadas
- `api-testing-observability-api-mock` - Teste de API
- `e2e-testing-patterns` - Padrões de integração

#### Ações
1. Projetar testes de integração
2. Configurar bancos de dados de teste
3. Configurar mocks de API
4. Testar interações de serviço
5. Verificar fluxos de dados

#### Instruções para copiar e colar
``` Use @api-testing-observability-api-mock para testar APIs
```

### Fase 4: Teste E2E

#### Skills a serem invocadas
- `playwright-skill` - Teste Playwright
- `e2e-testing-patterns` - Padrões E2E
- `webapp-testing` - Teste de aplicativos web

#### Ações
1. Projetar cenários E2E
2. Escrever scripts de teste
3. Configurar dados de teste
4. Configurar execução paralela
5. Implementar regressão visual

#### Instruções para copiar e colar
``` Use @playwright-skill para criar cenários E2E testes

```

``` Use @e2e-testing-patterns para projetar a estratégia E2E

```

### Fase 5: Automação do Navegador

#### Habilidades a serem invocadas
- `browser-automation` - Automação do navegador
- `webapp-testing` - Teste do navegador
- `screenshots` - Automação de capturas de tela

#### Ações
1. Configurar a automação do navegador
2. Configurar testes headless
3. Implementar testes visuais
4. Capturar screenshots
5. Testar o design responsivo

#### Instruções para copiar e colar
```
Use @browser-automation para automatizar tarefas do navegador
```

```
Use @screenshots para capturar screenshots de marketing
```

### Fase 6: Teste de desempenho

#### Habilidades a serem invocadas
- `performance-engineer` - Engenharia de desempenho
- `performance-profiling` - Criação de perfil de desempenho
- `web-performance-optimization` - Desempenho web

#### Ações
1. Projetar testes de desempenho
2. Configurar testes de carga
3. Medir tempos de resposta
4. Identificar gargalos
5. Otimizar o desempenho

#### Instruções para copiar e colar
```
Use @performance-engineer para testar o desempenho do aplicativo
```

### Fase 7: Codificação Revisão

#### Habilidades a serem invocadas
- `code-reviewer` - Revisão de código com IA
- `code-review-excellence` - Melhores práticas de revisão
- `find-bugs` - Detecção de bugs
- `security-scanning-security-sast` - Varredura de segurança

#### Ações
1. Configurar ferramentas de revisão
2. Executar revisões automatizadas
3. Verificar bugs
4. Verificar segurança
5. Aprovar alterações

#### Instruções de copiar e colar
```
Use @code-reviewer para revisar pull requests
```

```
Use @find-bugs para detectar bugs no código
```

### Fase 8: Portões de Qualidade

#### Habilidades a serem invocadas
- `lint-and-validate` - Linting
- `verification-before-completion` - Verificação

#### Ações
1. Configurar linters
2. Configurar formatadores
3. Definir Métricas de qualidade
4. Implementar portões de controle
5. Monitorar a conformidade

#### Instruções de copiar e colar
``` Use @lint-and-validate para verificar a qualidade do código
```

```
Use @verification-before-completion para verificar as alterações
```

## Pirâmide de testes

```

/ / \ Testes E2E (10%)

/---- / \ Testes de integração (20%)

/-------- / \ Testes unitários (70%)

/------------```

## Lista de verificação de portões de qualidade

- [ ] Cobertura de testes unitários > 80%
- [ ] Todos os testes aprovados
- [ ] Testes E2E para caminhos críticos
- [ ] Metas de desempenho atendidas
- [ ] Verificação de segurança aprovada
- [ ] Revisão de código aprovada
- [ ] Lint limpo

## Pacotes de fluxo de trabalho relacionados

- `development` - Fluxo de trabalho de desenvolvimento
- `security-audit` - Teste de segurança
- `cloud-devops` - Integração CI/CD
- `ai-ml` - Testes de IA