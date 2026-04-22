--- 
name: melhores-práticas-do-Nodejs
description: "Princípios de desenvolvimento e tomada de decisões em Node.js. Seleção de frameworks, padrões assíncronos, segurança e arquitetura. Ensina a pensar, não a copiar."
risk: desconhecido
source: comunidade
date_add: "27/02/2026"
---

# Melhores Práticas de Node.js

> Princípios e tomada de decisões para o desenvolvimento em Node.js em 2025.
> **Aprenda a PENSAR, não a memorizar padrões de código.**

## Quando usar
Use esta habilidade ao tomar decisões sobre a arquitetura do Node.js, escolher frameworks, projetar padrões assíncronos ou aplicar as melhores práticas de segurança e implantação.

---

## ⚠️ Como usar esta habilidade

Esta habilidade ensina **princípios de tomada de decisão**, não código fixo para copiar.

- PERGUNTE ao usuário sobre suas preferências quando não estiverem claras
- Escolha o framework/padrão com base no CONTEXTO
- Não use sempre a mesma solução por padrão

---

## 1. Seleção de Framework (2025)

### Árvore de Decisão

``` O que você está construindo?
│
├── Edge/Serverless (Cloudflare, Vercel)
│ └── Hono (sem dependências, inicializações a frio ultrarrápidas)
│
├── API de Alto Desempenho
│ └── Fastify (2 a 3 vezes mais rápido que o Express)
│
├── Familiaridade com ambientes corporativos/de equipe
│ └── NestJS (estruturado, injeção de dependência, decoradores)
│
├── Ecossistema legado/estável/máximo
│ └── Express (maduro, maioria dos middlewares)
│
└── Full-stack com frontend

└── Rotas de API Next.js ou tRPC
```

### Comparação Princípios

| Factor | Hono | Fastify | Express |

|--------|------|---------|---------|

| **Ideal para** | Edge, serverless | Desempenho | Legado, aprendizado |

| **Inicialização a frio** | Mais rápido | Rápido | Moderado |

| **Ecossistema** | Em crescimento | Bom | Maior |

| **TypeScript** | Nativo | Excelente | Bom |

| **Curva de aprendizado** | Baixa | Média | Baixa |

### Perguntas para seleção:
1. Qual é o objetivo da implantação?

2. O tempo de inicialização a frio é crítico?

3. A equipe tem experiência prévia?

4. Existe código legado para manter?

---

## 2. Considerações de Tempo de Execução (2025)

### TypeScript Nativo

``` Node.js 22+: --experimental-strip-types
├── Executar arquivos .ts diretamente
├── Nenhuma etapa de build necessária para projetos simples
└── Considerar para: scripts, APIs simples
```

### Decisão sobre Sistema de Módulos

```
ESM (importar/exportar)
├── Padrão moderno
├── Melhor tree-shaking
├── Carregamento assíncrono de módulos
└── Usar para: novos projetos

CommonJS (require)
├── Compatibilidade com versões anteriores
├── Suporte a mais pacotes npm
└── Usar para: bases de código existentes, algumas versões de ponta casos
```

### Seleção de Ambiente de Execução

| Ambiente de Execução | Melhor para |

|---------|----------|

| **Node.js** | Uso geral, maior ecossistema |

| **Bun** | Desempenho, bundler integrado |

| **Deno** | Segurança em primeiro lugar, TypeScript integrado |

---

## 3. Princípios de Arquitetura

### Conceito de Estrutura em Camadas

```
Fluxo de Requisição:
│
├── Camada de Controlador/Rota
│ ├── Lida com especificidades do HTTP
│ ├── Validação de entrada no limite
│ └── Chama a camada de serviço
│
├── Camada de Serviço
│ ├── Lógica de negócio
│ ├── Independente de framework
│ └── Chama a camada de repositório
│
└── Camada de Repositório

├── Somente acesso a dados

├── Consultas ao banco de dados

└── Interações com ORM
```

### Por que isso? Questões importantes:
- **Testabilidade**: Simule camadas independentemente
- **Flexibilidade**: Troque o banco de dados sem alterar a lógica de negócios
- **Clareza**: Cada camada tem uma única responsabilidade

### Quando simplificar:
- Scripts pequenos → Um único arquivo é aceitável
- Protótipos → Menos estrutura é aceitável
- Sempre pergunte: "Isso vai crescer?"

---

## 4. Princípios de Tratamento de Erros

### Tratamento de Erros Centralizado

```
Padrão:
├── Criar classes de erro personalizadas
├── Lançar erros de qualquer camada
├── Capturar erros no nível superior (middleware)
└── Formatar a resposta de forma consistente
```

### Filosofia de Resposta a Erros

```
O cliente recebe:
├── Status HTTP apropriado
├── Código de erro para tratamento programático
├── Mensagem amigável ao usuário
└── Sem detalhes internos (segurança!)

Os logs recebem:
├── Stack trace completo
├── Contexto da requisição
├── ID do usuário (se aplicável)
└── Timestamp
```

### Seleção de Código de Status

| Situação | Status | Quando |

|-----------|--------|------|

| Entrada inválida | 400 | Cliente enviou dados inválidos |

| Sem autenticação | 401 | Credenciais ausentes ou inválidas |

| Sem permissão | 403 | Autenticação válida, mas não permitida |

| Não encontrado | 404 | Recurso não existe |

| Conflito | 409 | Duplicado ou conflito de estado |

| Validação | 422 | Esquema válido, mas as regras de negócio falham |

| Erro do servidor | 500 | Nossa culpa, registre tudo |

---

## 5. Princípios de Padrões Assíncronos

### Quando Usar Cada

| Padrão | Usar Quando |

|---------|----------|

| `async/await` | Operações assíncronas sequenciais |

| `Promise.all` | Operações paralelas independentes |

| `Promise.allSettled` | Paralelismo onde algumas podem falhar |

| `Promise.race` | Tempo limite ou a primeira resposta vence |

### Consciência do Loop de Eventos

```
Operações com uso intensivo de E/S (o uso assíncrono ajuda):
├── Consultas a banco de dados
├── Requisições HTTP
├── Sistema de arquivos
└── Operações de rede

Operações com uso intensivo de CPU (o uso assíncrono não ajuda):
├── Operações criptográficas
├── Processamento de imagens
├── Cálculos complexos
└── → Use threads de trabalho ou descarregue a CPU
```

### Evitando o Bloqueio do Loop de Eventos

- Nunca use métodos síncronos em produção (fs.readFileSync, etc.)
- Descarregue tarefas que exigem muito da CPU
- Use streaming para grandes volumes de dados

---

## 6. Princípios de Validação

### Validar nos Limites

```
Onde validar:
├── Ponto de entrada da API (corpo/parâmetros da requisição)
├── Antes das operações no banco de dados
├── Dados externos (respostas da API, uploads de arquivos)
└── Variáveis ​​de ambiente (inicialização)
```

### Seleção de Biblioteca de Validação

| Biblioteca | Melhor para |

|---------|----------|

| **Zod** | Prioridade ao TypeScript, inferência |

| **Valibot** | Pacote menor (reproduzível com tree-shaking) |

| **ArkType** | Crítica em termos de desempenho |

| **Yup** | Uso existente de formulários React |

### Filosofia de Validação

- Falhe rápido: Valide cedo
- Seja específico: Mensagens de erro claras
- Não confie: Nem mesmo em dados "internos"

---

## 7. Princípios de Segurança

### Lista de Verificação de Segurança (Não é Código)

- [ ] **Validação de entrada**: Todas as entradas validadas
- [ ] **Consultas parametrizadas**: Sem concatenação de strings para SQL
- [ ] **Hash de senha**: bcrypt ou argon2
- [ ] **Verificação de JWT**: Sempre verifique a assinatura e a expiração
- [ ] **Limitação de taxa**: Proteja contra abusos
- [ ] **Cabeçalhos de segurança**: Helmet.js ou equivalente
- [ ] **HTTPS**: Em toda a produção
- [ ] **CORS**: Configurado corretamente
- [ ] **Segredos**: Somente variáveis ​​de ambiente
- [ ] **Dependências**: Auditadas regularmente

### Segurança Mentalidade

``` Não confie em nada:

├── Parâmetros de consulta → validar
├── Corpo da requisição → validar
├── Cabeçalhos → verificar
├── Cookies → validar
├── Uploads de arquivos → analisar
└── APIs externas → validar resposta
```

---

## 8. Princípios de Teste

### Seleção da Estratégia de Teste

| Tipo | Objetivo | Ferramentas |

|------|---------|-------|

| **Unidade** | Lógica de negócios | node:test, Vitest |

| **Integração** | Endpoints de API | Supertest |

| **E2E** | Fluxos completos | Playwright |

### O que testar (Prioridades)

1. **Caminhos críticos**: Autenticação, pagamentos, negócios principais
2. **Casos extremos**: Entradas vazias, limites
3. **Tratamento de erros**: O que acontece quando algo falha?
4. **Não vale a pena testar**: Código do framework, getters triviais

### Executador de Testes Integrado (Node.js 22+)

```
node --test src/**/*.test.ts
├── Sem dependências externas
├── Boa cobertura de testes
└── Modo de observação disponível
```

---

## 10. Antipadrões a Evitar

### ❌ NÃO:
- Usar Express para novos projetos de ponta (use Hono)
- Usar métodos síncronos em código de produção
- Colocar lógica de negócios em controladores
- Ignorar validação de entrada
- Codificar segredos diretamente no código
- Confiar em dados externos sem validação
- Bloquear o loop de eventos com processamento de CPU

### ✅ FAÇA:
- Escolher o framework com base no contexto
- Perguntar ao usuário sobre suas preferências quando não estiverem claras
- Usar arquitetura em camadas para projetos em crescimento
- Validar todas as entradas
- Usar variáveis ​​de ambiente para segredos
- Criar perfis Antes de otimizar

---

## 11. Lista de Verificação de Decisão

Antes de implementar:

- [ ] **Perguntou ao usuário sobre a preferência de stack?**
- [ ] **Framework escolhido para ESTE contexto?** (não apenas o padrão)
- [ ] **Considerou o alvo de implantação?**
- [ ] **Estratégia planejada para tratamento de erros?**
- [ ] **Pontos de validação identificados?**

- [ ] **Requisitos de segurança considerados?**

---

> **Lembre-se**: As melhores práticas do Node.js são sobre tomada de decisão, não memorização de padrões. Cada projeto merece uma análise personalizada com base em seus requisitos.