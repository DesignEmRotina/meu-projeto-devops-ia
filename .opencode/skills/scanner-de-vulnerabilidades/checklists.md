# Checklists de Segurança

> Checklists de referência rápida para auditorias de segurança. Use em conjunto com os princípios do **scanner_de_vulnerabilidades**.

---

## Checklist de Auditoria OWASP Top 10

### A01: Controle de Acesso Quebrado (Broken Access Control)
- [ ] Autorização aplicada em todas as rotas protegidas
- [ ] Negar por padrão
- [ ] Rate limiting implementado
- [ ] CORS configurado corretamente

### A02: Falhas Criptográficas (Cryptographic Failures)
- [ ] Senhas com hash (bcrypt/argon2, custo 12+)
- [ ] Dados sensíveis criptografados em repouso
- [ ] TLS 1.2+ em todas as conexões
- [ ] Nenhum segredo em código ou logs

### A03: Injeção (Injection)
- [ ] Queries parametrizadas
- [ ] Validação de input em todos os dados do usuário
- [ ] Codificação de saída para XSS
- [ ] Nenhum uso de eval() ou execução dinâmica de código

### A04: Design Inseguro (Insecure Design)
- [ ] Threat modeling realizado
- [ ] Requisitos de segurança definidos
- [ ] Lógica de negócio validada

### A05: Configuração Insegura (Security Misconfiguration)
- [ ] Funcionalidades desnecessárias desativadas
- [ ] Mensagens de erro sanitizadas
- [ ] Headers de segurança configurados
- [ ] Credenciais padrão alteradas

### A06: Componentes Vulneráveis (Vulnerable Components)
- [ ] Dependências atualizadas
- [ ] Nenhuma vulnerabilidade conhecida
- [ ] Dependências não utilizadas removidas

### A07: Falhas de Autenticação (Authentication Failures)
- [ ] MFA disponível
- [ ] Invalidação de sessão no logout
- [ ] Timeout de sessão implementado
- [ ] Proteção contra brute force

### A08: Falhas de Integridade (Integrity Failures)
- [ ] Integridade de dependências verificada
- [ ] Pipeline de CI/CD protegido
- [ ] Mecanismo de atualização seguro

### A09: Falhas de Logging (Logging Failures)
- [ ] Eventos de segurança registrados
- [ ] Logs protegidos
- [ ] Nenhum dado sensível em logs
- [ ] Alertas configurados

### A10: SSRF
- [ ] Validação de URLs implementada
- [ ] Allow-list para chamadas externas
- [ ] Segmentação de rede

---

## Checklist de Autenticação

- [ ] Política de senha forte
- [ ] Bloqueio de conta
- [ ] Reset de senha seguro
- [ ] Gerenciamento de sessão
- [ ] Expiração de token
- [ ] Invalidação no logout

---

## Checklist de Segurança de API

- [ ] Autenticação obrigatória
- [ ] Autorização por endpoint
- [ ] Validação de input
- [ ] Rate limiting
- [ ] Sanitização de saída
- [ ] Tratamento de erros

---

## Checklist de Proteção de Dados

- [ ] Criptografia em repouso
- [ ] Criptografia em trânsito
- [ ] Gerenciamento de chaves
- [ ] Minimização de dados
- [ ] Exclusão segura

---

## Headers de Segurança

| Header | Finalidade |
|--------|------------|
| **Content-Security-Policy** | Prevenção de XSS |
| **X-Content-Type-Options** | Prevenção de MIME sniffing |
| **X-Frame-Options** | Proteção contra clickjacking |
| **Strict-Transport-Security** | Forçar HTTPS |
| **Referrer-Policy** | Controle de referenciador |

---

## Comandos Rápidos de Auditoria

| Verificação | O que procurar |
|-------------|----------------|
| Segredos no código | password, api_key, secret |
| Padrões perigosos | eval, innerHTML, concatenação SQL |
| Problemas em dependências | npm audit, snyk |

---

> **Uso:** Copie os checklists relevantes para o seu `PLAN.md` ou relatório de segurança.
