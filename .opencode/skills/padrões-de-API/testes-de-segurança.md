# Testes de Segurança em APIs

> Princípios para testes de segurança em APIs. OWASP API Top 10, testes de autenticação e autorização.

---

## OWASP API Security Top 10

| Vulnerabilidade | Foco do Teste |
|-----------------|---------------|
| **API1: BOLA** | Acessar recursos de outros usuários |
| **API2: Autenticação Quebrada** | JWT, sessões, credenciais |
| **API3: Autorização em Propriedades** | Mass assignment, exposição de dados |
| **API4: Consumo Excessivo de Recursos** | Rate limiting, DoS |
| **API5: Autorização de Funções** | Endpoints administrativos, bypass de papéis |
| **API6: Fluxo de Negócio** | Abuso de lógica, automação |
| **API7: SSRF** | Acesso à rede interna |
| **API8: Má Configuração** | Endpoints de debug, CORS |
| **API9: Inventário de APIs** | APIs sombra, versões antigas |
| **API10: Consumo Inseguro** | Confiança excessiva em APIs de terceiros |

---

## Testes de Autenticação

### Testes com JWT

| Verificação | O que Testar |
|-------------|--------------|
| Algoritmo | `none`, confusão de algoritmos |
| Segredo | Segredos fracos, brute force |
| Claims | Expiração, emissor, audience |
| Assinatura | Manipulação, injeção de chave |

### Testes de Sessão

| Verificação | O que Testar |
|-------------|--------------|
| Geração | Previsibilidade |
| Armazenamento | Segurança no lado do cliente |
| Expiração | Aplicação correta de timeout |
| Invalidação | Efetividade do logout |

---

## Testes de Autorização

| Tipo de Teste | Abordagem |
|---------------|-----------|
| **Horizontal** | Acessar dados de usuários no mesmo nível |
| **Vertical** | Acessar funções com privilégios mais altos |
| **Contextual** | Acessar fora do escopo permitido |

### Testes de BOLA / IDOR

1. Identificar IDs de recursos nas requisições
2. Capturar a requisição com a sessão do usuário A
3. Reexecutar a requisição com a sessão do usuário B
4. Verificar se ocorre acesso não autorizado

---

## Testes de Validação de Entrada

| Tipo de Injeção | Foco do Teste |
|-----------------|---------------|
| SQL | Manipulação de queries |
| NoSQL | Consultas em documentos |
| Command | Execução de comandos do sistema |
| LDAP | Consultas em diretórios |

**Abordagem:**  
Testar todos os parâmetros, tentar coerção de tipos, testar limites (boundary testing) e analisar mensagens de erro.

---

## Testes de Rate Limiting

| Aspecto | Verificação |
|--------|-------------|
| Existência | Existe algum limite? |
| Bypass | Headers, rotação de IP |
| Escopo | Por usuário, por IP, global |

**Técnicas de bypass comuns:**  
X-Forwarded-For, métodos HTTP diferentes, variações de caixa (case), versionamento da API.

---

## Segurança em GraphQL

| Teste | Foco |
|------|------|
| Introspection | Exposição do schema |
| Batching | DoS via múltiplas queries |
| Nesting | DoS por profundidade |
| Autorização | Controle de acesso por campo |

---

## Checklist de Testes de Segurança

### Autenticação
- [ ] Testar bypass
- [ ] Verificar força das credenciais
- [ ] Validar segurança dos tokens

### Autorização
- [ ] Testar BOLA / IDOR
- [ ] Verificar escalonamento de privilégios
- [ ] Validar acesso às funções

### Entrada de Dados
- [ ] Testar todos os parâmetros
- [ ] Verificar possibilidade de injeção

### Configuração
- [ ] Verificar CORS
- [ ] Validar headers de segurança
- [ ] Testar tratamento de erros

---

> **Lembre-se:** APIs são a espinha dorsal das aplicações modernas.  
> Teste-as exatamente como um atacante faria.
