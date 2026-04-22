name: scanner_de_vulnerabilidades
description: Princípios avançados de análise de vulnerabilidades. OWASP 2025, Segurança de Supply Chain, mapeamento de superfície de ataque, priorização de riscos.
allowed-tools: Leitura, Glob, Grep, Bash
---
```

# Scanner de Vulnerabilidades

> Pense como um atacante, defenda como um especialista. Consciência do cenário de ameaças em 2025.

---

## 🔧 Scripts de Execução

**Execute para validação automatizada:**

| Script                                | Finalidade                                            | Uso                                                         |
| ------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------- |
| `scripts/verificação_de_segurança.py` | Validar se os princípios de segurança foram aplicados | `python scripts/verificação_de_segurança.py <project_path>` |

---

## 📋 Arquivos de Referência

| Arquivo                        | Finalidade                                                        |
| ------------------------------ | ----------------------------------------------------------------- |
| [checklists.md](checklists.md) | Checklists de OWASP Top 10, Autenticação, API e Proteção de Dados |

---

## 1. Mindset de Especialista em Segurança

### Princípios Fundamentais

| Princípio                  | Aplicação                                       |
| -------------------------- | ----------------------------------------------- |
| **Assumir Violação**       | Projetar como se o atacante já estivesse dentro |
| **Zero Trust**             | Nunca confiar, sempre verificar                 |
| **Defesa em Profundidade** | Múltiplas camadas, sem ponto único              |
| **Menor Privilégio**       | Apenas o acesso mínimo necessário               |
| **Falha Segura**           | Em caso de erro, negar acesso                   |

---

### Perguntas de Threat Modeling

Antes de escanear, pergunte:

1. O que estamos protegendo? (Ativos)
2. Quem atacaria? (Atores de ameaça)
3. Como atacariam? (Vetores de ataque)
4. Qual é o impacto? (Risco de negócio)

---

## 2. OWASP Top 10 – 2025

### Categorias de Risco

| Rank    | Categoria                           | Pense Sobre                               |
| ------- | ----------------------------------- | ----------------------------------------- |
| **A01** | Controle de Acesso Quebrado         | Quem pode acessar o quê? IDOR, SSRF       |
| **A02** | Configuração de Segurança Incorreta | Defaults, headers, serviços expostos      |
| **A03** | Supply Chain de Software 🆕         | Dependências, CI/CD, integridade de build |
| **A04** | Falhas Criptográficas               | Criptografia fraca, segredos expostos     |
| **A05** | Injeção                             | Entrada do usuário → comandos do sistema  |
| **A06** | Design Inseguro                     | Arquitetura falha                         |
| **A07** | Falhas de Autenticação              | Sessão, gestão de credenciais             |
| **A08** | Falhas de Integridade               | Updates sem assinatura, dados alterados   |
| **A09** | Logging e Alertas                   | Pontos cegos, ausência de monitoramento   |
| **A10** | Condições Excepcionais 🆕           | Tratamento de erros, estados fail-open    |

---

### Principais Mudanças em 2025

```
Mudanças 2021 → 2025:
├── SSRF incorporado ao A01 (Controle de Acesso)
├── A02 elevado (Configurações Cloud/Containers)
├── A03 NOVO: Supply Chain (grande foco)
├── A10 NOVO: Condições Excepcionais
└── Mudança de foco: Causas raiz > Sintomas
```

---

## 3. Segurança de Supply Chain (A03)

### Superfície de Ataque

| Vetor                 | Risco                  | Pergunta-Chave        |
| --------------------- | ---------------------- | --------------------- |
| **Dependências**      | Pacotes maliciosos     | Auditamos novas deps? |
| **Lock files**        | Ataques de integridade | Estão versionados?    |
| **Pipeline de build** | Comprometimento CI/CD  | Quem pode alterar?    |
| **Registry**          | Typosquatting          | Fontes verificadas?   |

---

### Princípios de Defesa

* Verificar integridade de pacotes (checksums)
* Fixar versões e auditar atualizações
* Usar registries privados para deps críticas
* Assinar e validar artefatos

---

## 4. Mapeamento da Superfície de Ataque

### O Que Mapear

| Categoria                | Elementos                             |
| ------------------------ | ------------------------------------- |
| **Pontos de Entrada**    | APIs, formulários, upload de arquivos |
| **Fluxos de Dados**      | Entrada → Processamento → Saída       |
| **Limites de Confiança** | Onde auth/authz são verificados       |
| **Ativos**               | Segredos, PII, dados de negócio       |

---

### Matriz de Priorização

```
Risco = Probabilidade × Impacto

Alto Impacto + Alta Probabilidade → CRÍTICO
Alto Impacto + Baixa Probabilidade → ALTO
Baixo Impacto + Alta Probabilidade → MÉDIO
Baixo Impacto + Baixa Probabilidade → BAIXO
```

---

## 5. Priorização de Riscos

### CVSS + Contexto

| Fator              | Peso                        | Pergunta                 |
| ------------------ | --------------------------- | ------------------------ |
| **Score CVSS**     | Severidade base             | Quão grave é a falha?    |
| **Score EPSS**     | Probabilidade de exploração | Está sendo explorada?    |
| **Valor do Ativo** | Contexto de negócio         | O que está em risco?     |
| **Exposição**      | Superfície de ataque        | Está exposto à internet? |

---

### Árvore de Decisão

```
Está sendo explorado ativamente (EPSS > 0.5)?
├── SIM → CRÍTICO: ação imediata
└── NÃO → Verificar CVSS
         ├── CVSS ≥ 9.0 → ALTO
         ├── CVSS 7.0–8.9 → Considerar valor do ativo
         └── CVSS < 7.0 → Planejar correção
```

---

## 6. Condições Excepcionais (A10 – Novo)

### Fail-Open vs Fail-Closed

| Cenário              | Fail-Open (RUIM)       | Fail-Closed (BOM) |
| -------------------- | ---------------------- | ----------------- |
| Erro de autenticação | Permitir acesso        | Negar acesso      |
| Falha de parsing     | Aceitar entrada        | Rejeitar entrada  |
| Timeout              | Tentar indefinidamente | Limitar + abortar |

---

### O Que Verificar

* Handlers genéricos que capturam exceções e ignoram erros
* Falta de tratamento em operações críticas de segurança
* Race conditions em auth/authz
* Cenários de exaustão de recursos

---

## 7. Metodologia de Scan

### Abordagem por Fases

```
1. RECONHECIMENTO
   └── Entender o alvo
       ├── Stack tecnológica
       ├── Pontos de entrada
       └── Fluxos de dados

2. DESCOBERTA
   └── Identificar potenciais problemas
       ├── Revisão de configuração
       ├── Análise de dependências
       └── Busca por padrões de código

3. ANÁLISE
   └── Validar e priorizar
       ├── Eliminação de falsos positivos
       ├── Score de risco
       └── Mapeamento de cadeias de ataque

4. RELATÓRIO
   └── Achados acionáveis
       ├── Passos claros de reprodução
       ├── Impacto no negócio
       └── Guia de correção
```

---

## 8. Análise de Padrões de Código

### Padrões de Alto Risco

| Padrão                             | Risco     | Procure Por                       |
| ---------------------------------- | --------- | --------------------------------- |
| Concatenação de strings em queries | Injeção   | `"SELECT * FROM " + user_input`   |
| Execução dinâmica de código        | RCE       | `eval()`, `exec()`, `Function()`  |
| Desserialização insegura           | RCE       | `pickle.loads()`, `unserialize()` |
| Manipulação de paths               | Traversal | Input do usuário em caminhos      |
| Segurança desativada               | Diversos  | `verify=False`, `--insecure`      |

---

### Padrões de Segredos

| Tipo          | Indicadores                        |
| ------------- | ---------------------------------- |
| Chaves de API | `api_key`, `apikey`, alta entropia |
| Tokens        | `token`, `bearer`, `jwt`           |
| Credenciais   | `password`, `secret`, `key`        |
| Cloud         | Prefixos `AWS_`, `AZURE_`, `GCP_`  |

---

## 9. Considerações de Segurança em Cloud

### Responsabilidade Compartilhada

| Camada         | Sua Responsabilidade | Provedor |
| -------------- | -------------------- | -------- |
| Dados          | ✅                    | ❌        |
| Aplicação      | ✅                    | ❌        |
| SO / Runtime   | Depende              | Depende  |
| Infraestrutura | ❌                    | ✅        |

---

### Checks Específicos de Cloud

* IAM: menor privilégio aplicado?
* Storage: buckets públicos?
* Rede: security groups restritos?
* Segredos: uso de secrets manager?

---

## 10. Anti-Padrões

| ❌ Não Faça                  | ✅ Faça                                |
| --------------------------- | ------------------------------------- |
| Escanear sem entender       | Mapear superfície de ataque           |
| Alertar todo CVE            | Priorizar por explorabilidade + ativo |
| Ignorar falsos positivos    | Manter baseline validado              |
| Corrigir apenas sintomas    | Tratar causas raiz                    |
| Escanear só antes do deploy | Scan contínuo                         |
| Confiar cegamente em deps   | Verificar integridade e auditar       |

---

## 11. Princípios de Relatório

### Estrutura de um Achado

Cada finding deve responder:

1. **O quê?** – Descrição clara da vulnerabilidade
2. **Onde?** – Local exato (arquivo, linha, endpoint)
3. **Por quê?** – Explicação da causa raiz
4. **Impacto?** – Consequência para o negócio
5. **Como corrigir?** – Remediação específica

---

### Classificação de Severidade

| Severidade  | Critérios                                  |
| ----------- | ------------------------------------------ |
| **Crítico** | RCE, bypass de auth, vazamento massivo     |
| **Alto**    | Exposição de dados, escalada de privilégio |
| **Médio**   | Escopo limitado, requer condições          |
| **Baixo**   | Informativo, boas práticas                 |

---

> **Lembre-se:** scanners encontram problemas.
> Pensamento especialista prioriza o que realmente importa.
> Sempre pergunte: **“O que um atacante faria com isso?”**

---

