--- 
name: melhores-práticas-de-segurança-de-API
description: "Implemente padrões de design de API seguros, incluindo autenticação, autorização, validação de entrada, limitação de taxa e proteção contra vulnerabilidades comuns de API"
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Melhores Práticas de Segurança de API

## Visão Geral

Ouça desenvolvedores na criação de APIs seguras implementando autenticação, autorização, validação de entrada, limitação de taxa e proteção contra vulnerabilidades comuns. Esta habilidade abrange padrões de segurança para APIs REST, GraphQL e WebSocket.

## Quando usar esta habilidade

- Use ao projetar novos endpoints de API
- Use ao proteger APIs existentes
- Use ao implementar autenticação e autorização
- Use ao proteger contra ataques de API (injeção, DDoS, etc.)
- Use ao realizar revisões de segurança de API
- Use ao se preparar para auditorias de segurança
- Use ao implementar limitação de taxa e controle de requisições
- Use ao lidar com dados sensíveis em APIs

## Como funciona

### Etapa 1: Autenticação e Autorização

Eu ajudarei você a implementar autenticação segura:
- Escolher o método de autenticação (JWT, OAuth 2.0, chaves de API)
- Implementar autenticação baseada em token
- Configurar controle de acesso baseado em função (RBAC)
- Gerenciamento seguro de sessão
- Implementar autenticação multifator (MFA)

### Etapa 2: Validação e Sanitização de Entrada

Proteção contra ataques de injeção:
- Validar todos os dados de entrada
- Sanitizar as entradas do usuário
- Usar consultas parametrizadas
- Implementar validação de esquema de requisição
- Prevenir injeção de SQL, XSS e Injeção de comandos

### Etapa 3: Limitação de Taxa e Controle de Requisições

Prevenir abusos e ataques DDoS:
- Implementar limitação de taxa por usuário/IP
- Configurar controle de requisições da API
- Configurar cotas de requisições
- Lidar com erros de limite de taxa de forma adequada
- Monitorar atividades suspeitas

### Etapa 4: Proteção de Dados

Proteger dados sensíveis:
- Criptografar dados em trânsito (HTTPS/TLS)
- Criptografar dados sensíveis em repouso
- Implementar tratamento de erros adequado (sem vazamentos de dados)
- Sanitizar mensagens de erro
- Usar cabeçalhos seguros

### Etapa 5: Teste de Segurança da API

Verificar a implementação de segurança:
- Testar autenticação e autorização
- Realizar testes de penetração
- Verificar vulnerabilidades comuns (OWASP API Top 10)
- Validar o tratamento de entrada
- Testar a limitação de taxa

## Exemplos

### Exemplo 1: Implementando Autenticação JWT

```markdown

## Implementação Segura de Autenticação JWT

### Autenticação Fluxo

1. O usuário faz login com suas credenciais
2. O servidor valida as credenciais
3. O servidor gera um token JWT
4. O cliente armazena o token com segurança
5. O cliente envia o token com cada requisição
6. O servidor valida o token

### Implementação
#### 1. Generate Secure JWT Tokens

\`\`\`javascript
// auth.js
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

// Login endpoint
app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    
    // Validate input
    if (!email || !password) {
      return res.status(400).json({ 
        error: 'Email and password are required' 
      });
    }
    
    // Find user
    const user = await db.user.findUnique({ 
      where: { email } 
    });
    
    if (!user) {
      // Don't reveal if user exists
      return res.status(401).json({ 
        error: 'Invalid credentials' 
      });
    }
    
    // Verify password
    const validPassword = await bcrypt.compare(
      password, 
      user.passwordHash
    );
    
    if (!validPassword) {
      return res.status(401).json({ 
        error: 'Invalid credentials' 
      });
    }
    
    // Generate JWT token
    const token = jwt.sign(
      { 
        userId: user.id,
        email: user.email,
        role: user.role
      },
      process.env.JWT_SECRET,
      { 
        expiresIn: '1h',
        issuer: 'your-app',
        audience: 'your-app-users'
      }
    );
    
    // Generate refresh token
    const refreshToken = jwt.sign(
      { userId: user.id },
      process.env.JWT_REFRESH_SECRET,
      { expiresIn: '7d' }
    );
    
    // Store refresh token in database
    await db.refreshToken.create({
      data: {
        token: refreshToken,
        userId: user.id,
        expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
      }
    });
    
    res.json({
      token,
      refreshToken,
      expiresIn: 3600
    });
    
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ 
      error: 'An error occurred during login' 
    });
  }
});
\`\`\`

#### 2. Verify JWT Tokens (Middleware)

\`\`\`javascript
// middleware/auth.js
const jwt = require('jsonwebtoken');

function authenticateToken(req, res, next) {
  // Get token from header
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN
  
  if (!token) {
    return res.status(401).json({ 
      error: 'Access token required' 
    });
  }
  
  // Verify token
  jwt.verify(
    token, 
    process.env.JWT_SECRET,
    { 
      issuer: 'your-app',
      audience: 'your-app-users'
    },
    (err, user) => {
      if (err) {
        if (err.name === 'TokenExpiredError') {
          return res.status(401).json({ 
            error: 'Token expired' 
          });
        }
        return res.status(403).json({ 
          error: 'Invalid token' 
        });
      }
      
      // Attach user to request
      req.user = user;
      next();
    }
  );
}

module.exports = { authenticateToken };
\`\`\`

#### 3. Protect Routes

\`\`\`javascript
const { authenticateToken } = require('./middleware/auth');

// Protected route
app.get('/api/user/profile', authenticateToken, async (req, res) => {
  try {
    const user = await db.user.findUnique({
      where: { id: req.user.userId },
      select: {
        id: true,
        email: true,
        name: true,
        // Don't return passwordHash
      }
    });
    
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: 'Server error' });
  }
});
\`\`\`

#### 4. Implement Token Refresh

\`\`\`javascript
app.post('/api/auth/refresh', async (req, res) => {
  const { refreshToken } = req.body;
  
  if (!refreshToken) {
    return res.status(401).json({ 
      error: 'Refresh token required' 
    });
  }
  
  try {
    // Verify refresh token
    const decoded = jwt.verify(
      refreshToken, 
      process.env.JWT_REFRESH_SECRET
    );
    
    // Check if refresh token exists in database
    const storedToken = await db.refreshToken.findFirst({
      where: {
        token: refreshToken,
        userId: decoded.userId,
        expiresAt: { gt: new Date() }
      }
    });
    
    if (!storedToken) {
      return res.status(403).json({ 
        error: 'Invalid refresh token' 
      });
    }
    
    // Generate new access token
    const user = await db.user.findUnique({
      where: { id: decoded.userId }
    });
    
    const newToken = jwt.sign(
      { 
        userId: user.id,
        email: user.email,
        role: user.role
      },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );
    
    res.json({
      token: newToken,
      expiresIn: 3600
    });
    
  } catch (error) {
    res.status(403).json({ 
      error: 'Invalid refresh token' 
    });
  }
});
\`\`\`

### Security Best Practices

- ✅ Use strong JWT secrets (256-bit minimum)
- ✅ Set short expiration times (1 hour for access tokens)
- ✅ Implement refresh tokens for long-lived sessions
- ✅ Store refresh tokens in database (can be revoked)
- ✅ Use HTTPS only
- ✅ Don't store sensitive data in JWT payload
- ✅ Validate token issuer and audience
- ✅ Implement token blacklisting for logout
```


### Example 2: Input Validation and SQL Injection Prevention

```markdown
## Preventing SQL Injection and Input Validation

### The Problem

**❌ Vulnerable Code:**
\`\`\`javascript
// NEVER DO THIS - SQL Injection vulnerability
app.get('/api/users/:id', async (req, res) => {
  const userId = req.params.id;
  
  // Dangerous: User input directly in query
  const query = \`SELECT * FROM users WHERE id = '\${userId}'\`;
  const user = await db.query(query);
  
  res.json(user);
});

// Attack example:
// GET /api/users/1' OR '1'='1
// Returns all users!
\`\`\`

### The Solution

#### 1. Use Parameterized Queries

\`\`\`javascript
// ✅ Safe: Parameterized query
app.get('/api/users/:id', async (req, res) => {
  const userId = req.params.id;
  
  // Validate input first
  if (!userId || !/^\d+$/.test(userId)) {
    return res.status(400).json({ 
      error: 'Invalid user ID' 
    });
  }
  
  // Use parameterized query
  const user = await db.query(
    'SELECT id, email, name FROM users WHERE id = $1',
    [userId]
  );
  
  if (!user) {
    return res.status(404).json({ 
      error: 'User not found' 
    });
  }
  
  res.json(user);
});
\`\`\`

#### 2. Use ORM with Proper Escaping

\`\`\`javascript
// ✅ Safe: Using Prisma ORM
app.get('/api/users/:id', async (req, res) => {
  const userId = parseInt(req.params.id);
  
  if (isNaN(userId)) {
    return res.status(400).json({ 
      error: 'Invalid user ID' 
    });
  }
  
  const user = await prisma.user.findUnique({
    where: { id: userId },
    select: {
      id: true,
      email: true,
      name: true,
      // Don't select sensitive fields
    }
  });
  
  if (!user) {
    return res.status(404).json({ 
      error: 'User not found' 
    });
  }
  
  res.json(user);
});
\`\`\`

#### 3. Implement Request Validation with Zod

\`\`\`javascript
const { z } = require('zod');

// Define validation schema
const createUserSchema = z.object({
  email: z.string().email('Invalid email format'),
  password: z.string()
    .min(8, 'Password must be at least 8 characters')
    .regex(/[A-Z]/, 'Password must contain uppercase letter')
    .regex(/[a-z]/, 'Password must contain lowercase letter')
    .regex(/[0-9]/, 'Password must contain number'),
  name: z.string()
    .min(2, 'Name must be at least 2 characters')
    .max(100, 'Name too long'),
  age: z.number()
    .int('Age must be an integer')
    .min(18, 'Must be 18 or older')
    .max(120, 'Invalid age')
    .optional()
});

// Validation middleware
function validateRequest(schema) {
  return (req, res, next) => {
    try {
      schema.parse(req.body);
      next();
    } catch (error) {
      res.status(400).json({
        error: 'Validation failed',
        details: error.errors
      });
    }
  };
}

// Use validation
app.post('/api/users', 
  validateRequest(createUserSchema),
  async (req, res) => {
    // Input is validated at this point
    const { email, password, name, age } = req.body;
    
    // Hash password
    const passwordHash = await bcrypt.hash(password, 10);
    
    // Create user
    const user = await prisma.user.create({
      data: {
        email,
        passwordHash,
        name,
        age
      }
    });
    
    // Don't return password hash
    const { passwordHash: _, ...userWithoutPassword } = user;
    res.status(201).json(userWithoutPassword);
  }
);
\`\`\`

#### 4. Sanitize Output to Prevent XSS

\`\`\`javascript
const DOMPurify = require('isomorphic-dompurify');

app.post('/api/comments', authenticateToken, async (req, res) => {
  const { content } = req.body;
  
  // Validate
  if (!content || content.length > 1000) {
    return res.status(400).json({ 
      error: 'Invalid comment content' 
    });
  }
  
  // Sanitize HTML to prevent XSS
  const sanitizedContent = DOMPurify.sanitize(content, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],
    ALLOWED_ATTR: ['href']
  });
  
  const comment = await prisma.comment.create({
    data: {
      content: sanitizedContent,
      userId: req.user.userId
    }
  });
  
  res.status(201).json(comment);
});
\`\`\`

### Validation Checklist

- [ ] Validate all user inputs
- [ ] Use parameterized queries or ORM
- [ ] Validate data types (string, number, email, etc.)
- [ ] Validate data ranges (min/max length, value ranges)
- [ ] Sanitize HTML content
- [ ] Escape special characters
- [ ] Validate file uploads (type, size, content)
- [ ] Use allowlists, not blocklists
```


### Example 3: Rate Limiting and DDoS Protection

```markdown
## Implementing Rate Limiting

### Why Rate Limiting?

- Prevent brute force attacks
- Protect against DDoS
- Prevent API abuse
- Ensure fair usage
- Reduce server costs

### Implementation with Express Rate Limit

\`\`\`javascript
const rateLimit = require('express-rate-limit');
const RedisStore = require('rate-limit-redis');
const Redis = require('ioredis');

// Create Redis client
const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT
});

// General API rate limit
const apiLimiter = rateLimit({
  store: new RedisStore({
    client: redis,
    prefix: 'rl:api:'
  }),
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: {
    error: 'Too many requests, please try again later',
    retryAfter: 900 // seconds
  },
  standardHeaders: true, // Return rate limit info in headers
  legacyHeaders: false,
  // Custom key generator (by user ID or IP)
  keyGenerator: (req) => {
    return req.user?.userId || req.ip;
  }
});

// Strict rate limit for authentication endpoints
const authLimiter = rateLimit({
  store: new RedisStore({
    client: redis,
    prefix: 'rl:auth:'
  }),
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // Only 5 login attempts per 15 minutes
  skipSuccessfulRequests: true, // Don't count successful logins
  message: {
    error: 'Too many login attempts, please try again later',
    retryAfter: 900
  }
});

// Apply rate limiters
app.use('/api/', apiLimiter);
app.use('/api/auth/login', authLimiter);
app.use('/api/auth/register', authLimiter);

// Custom rate limiter for expensive operations
const expensiveLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 10, // 10 requests per hour
  message: {
    error: 'Rate limit exceeded for this operation'
  }
});

app.post('/api/reports/generate', 
  authenticateToken,
  expensiveLimiter,
  async (req, res) => {
    // Expensive operation
  }
);
\`\`\`

### Advanced: Per-User Rate Limiting

\`\`\`javascript
// Different limits based on user tier
function createTieredRateLimiter() {
  const limits = {
    free: { windowMs: 60 * 60 * 1000, max: 100 },
    pro: { windowMs: 60 * 60 * 1000, max: 1000 },
    enterprise: { windowMs: 60 * 60 * 1000, max: 10000 }
  };
  
  return async (req, res, next) => {
    const user = req.user;
    const tier = user?.tier || 'free';
    const limit = limits[tier];
    
    const key = \`rl:user:\${user.userId}\`;
    const current = await redis.incr(key);
    
    if (current === 1) {
      await redis.expire(key, limit.windowMs / 1000);
    }
    
    if (current > limit.max) {
      return res.status(429).json({
        error: 'Rate limit exceeded',
        limit: limit.max,
        remaining: 0,
        reset: await redis.ttl(key)
      });
    }
    
    // Set rate limit headers
    res.set({
      'X-RateLimit-Limit': limit.max,
      'X-RateLimit-Remaining': limit.max - current,
      'X-RateLimit-Reset': await redis.ttl(key)
    });
    
    next();
  };
}

app.use('/api/', authenticateToken, createTieredRateLimiter());
\`\`\`

### DDoS Protection with Helmet

\`\`\`javascript
const helmet = require('helmet');

app.use(helmet({
  // Content Security Policy
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", 'data:', 'https:']
    }
  },
  // Prevent clickjacking
  frameguard: { action: 'deny' },
  // Hide X-Powered-By header
  hidePoweredBy: true,
  // Prevent MIME type sniffing
  noSniff: true,
  // Enable HSTS
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));
\`\`\`

### Rate Limit Response Headers

\`\`\`
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1640000000
Retry-After: 900
\`\`\`
```

## Boas Práticas

### ✅ Faça Isto

- **Use HTTPS em todos os lugares** - Nunca envie dados sensíveis por HTTP
- **Implemente Autenticação** - Exija autenticação para endpoints protegidos
- **Valide Todas as Entradas** - Nunca confie na entrada do usuário
- **Use Consultas Parametrizadas** - Previna injeção de SQL
- **Implemente Limitação de Taxa** - Proteja-se contra ataques de força bruta e DDoS
- **Criptografe Senhas** - Use bcrypt com número de rodadas de salt >= 10
- **Use Tokens de Curta Duração** - Tokens de acesso JWT devem expirar rapidamente
- **Implemente CORS Corretamente** - Permita apenas origens confiáveis
- **Registre Eventos de Segurança** - Monitore atividades suspeitas
- **Mantenha as Dependências Atualizadas** - Atualize os pacotes regularmente
- **Use Cabeçalhos de Segurança** - Implemente Helmet.js
- **Sanitize Mensagens de Erro** - Não vaze informações sensíveis

### ❌ Não Faça Isto

- **Não armazene senhas em texto simples** - Sempre use hash nas senhas
- **Não use segredos fracos** - Use segredos JWT fortes e aleatórios
- **Não confie na entrada do usuário** - Sempre valide e higienize os dados
- **Não exponha rastreamentos de pilha** - Oculte os detalhes do erro em produção
- **Não use concatenação de strings para SQL** - Use consultas parametrizadas
- **Não armazene dados confidenciais em JWT** - JWTs não são criptografados
- **Não ignore atualizações de segurança** - Atualize as dependências regularmente
- **Não use credenciais padrão** - Altere todas as senhas padrão
- **Não desative o CORS completamente** - Configure-o corretamente
- **Não registre dados confidenciais** - Higienize os logs

## Armadilhas comuns

## Common Pitfalls

### Problem: JWT Secret Exposed in Code
**Symptoms:** JWT secret hardcoded or committed to Git
**Solution:**
\`\`\`javascript
// ❌ Bad
const JWT_SECRET = 'my-secret-key';

// ✅ Good
const JWT_SECRET = process.env.JWT_SECRET;
if (!JWT_SECRET) {
  throw new Error('JWT_SECRET environment variable is required');
}

// Generate strong secret
// node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"
\`\`\`

### Problem: Weak Password Requirements
**Symptoms:** Users can set weak passwords like "password123"
**Solution:**
\`\`\`javascript
const passwordSchema = z.string()
  .min(12, 'Password must be at least 12 characters')
  .regex(/[A-Z]/, 'Must contain uppercase letter')
  .regex(/[a-z]/, 'Must contain lowercase letter')
  .regex(/[0-9]/, 'Must contain number')
  .regex(/[^A-Za-z0-9]/, 'Must contain special character');

// Or use a password strength library
const zxcvbn = require('zxcvbn');
const result = zxcvbn(password);
if (result.score < 3) {
  return res.status(400).json({
    error: 'Password too weak',
    suggestions: result.feedback.suggestions
  });
}
\`\`\`

### Problem: Missing Authorization Checks
**Symptoms:** Users can access resources they shouldn't
**Solution:**
\`\`\`javascript
// ❌ Bad: Only checks authentication
app.delete('/api/posts/:id', authenticateToken, async (req, res) => {
  await prisma.post.delete({ where: { id: req.params.id } });
  res.json({ success: true });
});

// ✅ Good: Checks both authentication and authorization
app.delete('/api/posts/:id', authenticateToken, async (req, res) => {
  const post = await prisma.post.findUnique({
    where: { id: req.params.id }
  });
  
  if (!post) {
    return res.status(404).json({ error: 'Post not found' });
  }
  
  // Check if user owns the post or is admin
  if (post.userId !== req.user.userId && req.user.role !== 'admin') {
    return res.status(403).json({ 
      error: 'Not authorized to delete this post' 
    });
  }
  
  await prisma.post.delete({ where: { id: req.params.id } });
  res.json({ success: true });
});
\`\`\`

### Problem: Verbose Error Messages
**Symptoms:** Error messages reveal system details
**Solution:**
\`\`\`javascript
// ❌ Bad: Exposes database details
app.post('/api/users', async (req, res) => {
  try {
    const user = await prisma.user.create({ data: req.body });
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
    // Error: "Unique constraint failed on the fields: (`email`)"
  }
});

// ✅ Good: Generic error message
app.post('/api/users', async (req, res) => {
  try {
    const user = await prisma.user.create({ data: req.body });
    res.json(user);
  } catch (error) {
    console.error('User creation error:', error); // Log full error
    
    if (error.code === 'P2002') {
      return res.status(400).json({ 
        error: 'Email already exists' 
      });
    }
    
    res.status(500).json({ 
      error: 'An error occurred while creating user' 
    });
  }
});
\`\`\`

## Lista de Verificação de Segurança

### Autenticação e Autorização
- [ ] Implementar autenticação forte (JWT, OAuth 2.0)
- [ ] Usar HTTPS para todos os endpoints
- [ ] Criptografar senhas com bcrypt (número de rodadas de salt >= 10)
- [ ] Implementar expiração de token
- [ ] Adicionar mecanismo de token de atualização
- [ ] Verificar a autorização do usuário para cada requisição
- [ ] Implementar controle de acesso baseado em funções (RBAC)

### Validação de Entrada
- [ ] Validar todas as entradas do usuário
- [ ] Usar consultas parametrizadas ou ORM
- [ ] Sanitizar conteúdo HTML
- [ ] Validar uploads de arquivos
- [ ] Implementar validação de esquema de requisição
- [ ] Usar listas de permissão, não listas de bloqueio

### Limitação de Taxa e Proteção contra DDoS
- [ ] Implementar limitação de taxa por usuário/IP
- [ ] Adicionar limites mais rigorosos para endpoints de autenticação
- [ ] Usar Redis para limitação de taxa distribuída
- [ ] Retornar cabeçalhos de limite de taxa adequados
- [ ] Implementar limitação de requisições

### Proteção de Dados
- [ ] Usar HTTPS/TLS para todo o tráfego
- [ ] Criptografar dados sensíveis em repouso
- [ ] Não armazenar dados sensíveis em JWT
- [ ] Sanitizar mensagens de erro
- [ ] Implementar configuração CORS adequada
- [ ] Usar cabeçalhos de segurança (Helmet.js)

### Monitoramento e Registro
- [ ] Registrar eventos de segurança
- [ ] Monitorar atividades suspeitas
- [ ] Configurar alertas para tentativas de autenticação com falha
- [ ] Rastrear padrões de uso da API
- [ ] Não registrar dados sensíveis

## OWASP API Security Top 10

1. **Autorização em Nível de Objeto Quebrada** - Sempre verificar se o usuário pode acessar o recurso
2. **Autenticação Quebrada** - Implementar mecanismos de autenticação fortes
3. **Autorização em Nível de Propriedade de Objeto Quebrada** - Validar quais propriedades o usuário pode acessar
4. **Consumo Irrestrito de Recursos** - Implementar limitação de taxa e cotas
5. **Autorização de Nível de Função Quebrada** - Verificar a função do usuário para cada função
6. **Acesso Irrestrito a Fluxos de Negócios Sensíveis** - Proteger fluxos de trabalho críticos
7. **Falsificação de Solicitação do Lado do Servidor (SSRF)** - Validar e sanitizar URLs
8. **Configuração de Segurança Incorreta** - Usar as melhores práticas e cabeçalhos de segurança
9. **Gerenciamento de Inventário Inadequado** - Documentar e proteger todos os endpoints da API
10. **Consumo Inseguro de APIs** - Validar dados de APIs de terceiros

## Habilidades Relacionadas

- `@ethical-hacking-methodology` - Perspectiva de teste de segurança
- `@sql-injection-testing` - Teste de injeção de SQL
- `@xss-html-injection` - Teste de vulnerabilidades XSS
- `@broken-authentication` - Vulnerabilidades de autenticação
- `@backend-dev-guidelines` - Padrões de desenvolvimento de backend
- `@systematic-debugging` - Depure problemas de segurança

## Recursos adicionais

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [Melhores práticas de JWT](https://tools.ietf.org/html/rfc8725)
- [Melhores práticas de segurança do Express](https://expressjs.com/en/advanced/best-practice-security.html)
- [Lista de verificação de segurança do Node.js](https://blog.risingstack.com/node-js-security-checklist/)
- [Lista de verificação de segurança de API](https://github.com/shieldfy/API-Security-Checklist)

---

**Dica profissional:** Segurança não é uma tarefa pontual - audite suas APIs regularmente, mantenha as dependências atualizadas e fique por dentro de novas vulnerabilidades!