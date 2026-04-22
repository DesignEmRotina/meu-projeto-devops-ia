--- 
name: teste-de-segurança-de-API
description: "Fluxo de trabalho para testes de segurança de APIs REST e GraphQL, abrangendo autenticação, autorização, limitação de taxa, validação de entrada e melhores práticas de segurança."
category: pacote-de-fluxo-de-trabalho-granular
risk: seguro
source: pessoal
date_add: "27/02/2026"
---

# Fluxo de trabalho para testes de segurança de API

## Visão geral

Fluxo de trabalho especializado para testes de segurança de APIs REST e GraphQL, incluindo autenticação, autorização, limitação de taxa, validação de entrada e vulnerabilidades específicas da API.

## Quando usar este fluxo de trabalho

Use este fluxo de trabalho quando:
- Testar a segurança de APIs REST
- Avaliar endpoints GraphQL
- Validar a autenticação de API
- Testar a limitação de taxa de requisições em APIs
- Testar APIs para programas de recompensas por bugs

## Fases do fluxo de trabalho

### Fase 1: Descoberta de API

#### Skills a serem invocadas
- `api-fuzzing-bug-bounty` - Fuzzing de API
- `scanning-tools` - Varredura de API

#### Ações
1. Enumerar endpoints
2. Documentar métodos da API
3. Identificar parâmetros
4. Mapear fluxos de dados
5. Revisar a documentação

#### Instruções para copiar e colar
```
Use @api-fuzzing-bug-bounty para descobrir endpoints da API
```

### Fase 2: Teste de autenticação

#### Skills a serem invocadas
- `broken-authentication` - Teste de autenticação
- `api-security-best-practices` - Autenticação de API

#### Ações
1. Testar a validação da chave de API
2. Testar tokens JWT
3. Testar fluxos OAuth2
4. Testar a expiração do token
5. Testar tokens de atualização

#### Instruções para copiar e colar
``` Use @broken-authentication para testar a autenticação da API
```

### Fase 3: Teste de Autorização

#### Skills para Invocar
- `idor-testing` - Teste IDOR

#### Ações
1. Testar a autorização em nível de objeto
2. Testar a autorização em nível de função
3. Testar o acesso baseado em função
4. Testar a escalação de privilégios
5. Testar o isolamento multi-tenant

#### Instruções para copiar e colar
``` Use @idor-testing para testar a autorização da API
```

### Fase 4: Validação de Entrada

#### Skills para Invocar
- `api-fuzzing-bug-bounty` - Fuzzing de API
- `sql-injection-testing` - Teste de injeção

#### Ações
1. Testar validação de parâmetros
2. Testar injeção SQL
3. Testar injeção NoSQL
4. Testar injeção de comandos
5. Testar injeção XXE

#### Instruções para copiar e colar
``` Use @api-fuzzing-bug-bounty para realizar fuzzing de parâmetros da API
```

### Fase 5: Limitação de taxa

#### Habilidades a serem invocadas
- `api-security-best-practices` - Limitação de taxa

#### Ações
1. Testar cabeçalhos de limite de taxa
2. Testar proteção contra força bruta
3. Testar esgotamento de recursos
4. Testar técnicas de bypass
5. Documentar limitações

#### Instruções para copiar e colar
``` Use @api-security-best-practices para testar a limitação de taxa
```

### Fase 6: Teste de GraphQL

#### Habilidades a serem invocadas
- `api-fuzzing-bug-bounty` - Fuzzing de GraphQL

#### Ações
1. Testar introspecção
2. Testar profundidade de consulta
3. Testar complexidade de consulta
4. Testar consultas em lote
5. Testar sugestões de campos

#### Instruções para copiar e colar
``` Use @api-fuzzing-bug-bounty para testar a segurança do GraphQL
```

### Fase 7: Tratamento de erros

#### Habilidades a serem invocadas
- `api-security-best-practices` - Tratamento de erros

#### Ações
1. Testar mensagens de erro
2. Verificar a divulgação de informações
3. Testar rastreamentos de pilha
4. Verificar o registro de logs
5. Documentar as descobertas

#### Instruções para copiar e colar
``` Use @api-security-best-practices para auditar erros da API Manipulação
```

## Lista de Verificação de Segurança da API

- [ ] Autenticação funcionando
- [ ] Autorização aplicada
- [ ] Entrada validada
- [ ] Limitação de taxa ativa
- [ ] Erros tratados
- [ ] Registro de logs habilitado
- [ ] CORS configurado
- [ ] HTTPS aplicado

## Critérios de Qualidade

- [ ] Todos os endpoints testados
- [ ] Vulnerabilidades documentadas
- [ ] Correção fornecida
- [ ] Relatório gerado

## Pacotes de Fluxo de Trabalho Relacionados

- `security-audit` - Auditoria de segurança
- `web-security-testing` - Segurança web
- `api-development` - Desenvolvimento de API