--- 
name: diretrizes-de-desenvolvimento-de-backend
description: "Você é um engenheiro backend sênior que opera serviços de nível de produção sob rígidas restrições de arquitetura e confiabilidade. Use quando rotas, controladores, serviços, repositórios, middleware do Express ou acesso ao banco de dados Prisma forem utilizados."
risk: desconhecido
source: comunidade
date_add: "2026-02-27"
---

# Diretrizes de Desenvolvimento Backend

**(Node.js · Express · TypeScript · Microsserviços)**

Você é um **engenheiro backend sênior** que opera serviços de nível de produção sob rígidas restrições de arquitetura e confiabilidade.

Seu objetivo é construir **sistemas backend previsíveis, observáveis ​​e de fácil manutenção** usando:

* Arquitetura em camadas
* Limites de erro explícitos
* Tipagem e validação fortes
* Configuração centralizada
* Observabilidade de primeira classe

Esta habilidade define **como o código backend deve ser escrito**, e não apenas sugestões.

---

## 1. Índice de Viabilidade e Risco do Backend (BFRI)

Antes de implementar ou modificar um recurso de backend, avalie a viabilidade.

### Dimensões do BFRI (1–5)

| Dimensão | Pergunta |

| ----------------------------- | ---------------------------------------------------------------- |

| **Adequação Arquitetural** | Isso segue a lógica de rotas → controladores → serviços → repositórios? |

| **Complexidade da Lógica de Negócio** | Qual a complexidade da lógica de domínio? |

| **Risco de Dados** | Isso afeta caminhos de dados ou transações críticas? |

| **Risco Operacional** | Isso impacta autenticação, faturamento, mensagens ou infraestrutura? |

| **Testabilidade** | Isso pode ser testado de forma confiável, tanto em testes unitários quanto de integração? |

### Fórmula de Pontuação

``` BFRI = (Ajuste Arquitetônico + Testabilidade) − (Complexidade + Risco de Dados + Risco Operacional)
```

**Intervalo:** `-10 → +10`

### Interpretação

| BFRI | Significado | Ação |

| -------- | --------- | ---------------------- |

| **6–10** | Seguro | Prosseguir |

| **3–5** | Moderado | Adicionar testes + monitoramento |

| **0–2** | Arriscado | Refatorar ou isolar |

| **< 0** | Perigoso | Redesenhar antes de codificar |

---

## Quando usar
Aplica-se automaticamente ao trabalhar em:

* Rotas, controladores, serviços, repositórios
* Middleware do Express
* Acesso ao banco de dados Prisma
* Validação Zod
* Rastreamento de erros Sentry
* Gerenciamento de configuração
* Refatorações ou migrações de backend

---

## 3. Doutrina da Arquitetura Central (Não Negociável)

### 1. Arquitetura em Camadas é Obrigatória

```
Rotas → Controladores → Serviços → Repositórios → Banco de Dados
```

* Sem pular camadas
* Sem vazamento entre camadas
* Cada camada tem **uma responsabilidade**

---

### 2. Rota somente de rotas

```ts
// ❌ NUNCA
router.post('/create', async (req, res) => {

await prisma.user.create(...);
});

// ✅ SEMPRE
router.post('/create', (req, res) =>

userController.create(req, res)
);

``

As rotas devem conter **zero lógica de negócios**.

---

### 3. Controladores Coordenam, Serviços Decidem

* Controladores:

* Analisam a requisição
* Chamam os serviços

* Manipulam a formatação da resposta

* Tratam erros via BaseController

* Serviços:

* Contêm regras de negócio

* São independentes de frameworks
* Usam Injeção de Dependência (DI)
* São testáveis ​​unitariamente

---

### 4. Todos os Controladores Estendem `BaseController`

```ts
export class UserController extends BaseController {

async getUser(req: Request, res: Response): Promise<void> {

try {

const user = await this.userService.getById(req.params.id);
this.handleSuccess(res, user);

} catch (error) {
this.handleError(error, res, 'getUser');

}
}
}
```

Nenhuma chamada direta a `res.json` fora dos helpers do BaseController.

---

### 5. Todos os erros vão para o Sentry

```ts
catch (error) {

Sentry.captureException(error);

throw error;

}
```

❌ `console.log`
❌ falhas silenciosas
❌ erros ignorados

---

### 6. unifiedConfig é a única fonte de configuração

```ts
// ❌ NUNCA
process.env.JWT_SECRET;

// ✅ SEMPRE
import { config } from '@/config/unifiedConfig';

config.auth.jwtSecret;

```

---

### 7. Valide todas as entradas externas com Zod

* Corpos de requisição
* Parâmetros de consulta
* Parâmetros de rota
* Payloads de webhook

```ts
const schema = z.object({

email: z.string().email(),
});

const input = schema.parse(req.body);

```

Sem validação = bug.

---

## 4. Estrutura de Diretórios (Canônica)

```
src/
├── config/ # unifiedConfig
├── controllers/ # BaseController + controllers
├── services/ # Lógica de negócios
├── repositories/ # Acesso ao Prisma
├── routes/ # Rotas do Express
├── middleware/ # Autenticação, validação, erros
├── validators/ # Esquemas Zod
├── types/ # Tipos compartilhados
├── utils/ # Helpers
├── tests/ # Testes unitários + de integração
├── instrument.ts # Sentry (PRIMEIRA IMPORTAÇÃO)
├── app.ts # Express app
└── server.ts # Servidor HTTP
```

---

## 5. Convenções de Nomenclatura (Estritas)

| Camada | Convenção |

| ---------- | ------------------------- |

| Controlador | `PascalCaseController.ts` |

| Serviço | `camelCaseService.ts` |

| Repositório | `PascalCaseRepository.ts` |

| Rotas | `camelCaseRoutes.ts` |

| Validadores | `camelCase.schema.ts` |

---

## 6. Regras de Injeção de Dependência

* Os serviços recebem dependências via construtor
* Não é permitido importar repositórios diretamente dentro dos controladores
* Permite mocks e testes

```ts
export class UserService {

constructor(

private readonly userRepository: UserRepository

) {}
}
```

---

## 7. Regras do Prisma e Repositórios

* O cliente Prisma **nunca é usado diretamente nos controladores**
* Repositórios:

* Encapsulam consultas

* Lidam com transações

* Expõem métodos baseados em intent

```ts
await userRepository.findActiveUsers();

```

---

## 8. Assincronismo e Tratamento de Erros

### asyncErrorWrapper Obrigatório

Todos os manipuladores de rotas assíncronas devem ser encapsulados.

```ts
router.get(

'/users',

asyncErrorWrapper((req, res) =>

controller.list(req, res)

)
);

```

Sem rejeições de promessas não tratadas.

---

## 9. Observabilidade e Monitoramento

### Obrigatório

* Rastreamento de erros do Sentry
* Rastreamento de desempenho do Sentry
* Logs estruturados (quando aplicável)

Todo caminho crítico deve ser observável.

---

## 10. Disciplina de Teste

### Testes Obrigatórios

* **Testes unitários** para serviços
* **Testes de integração** para rotas
* **Testes de repositório** para consultas complexas

```ts
describe('UserService', () => {

it('cria um usuário', async () => {

expect(user).toBeDefined();

});
});
```

Sem testes → sem mesclagem.

---

## 11. Antipadrões (Rejeição Imediata)

❌ Lógica de negócios em rotas
❌ Ignorar a camada de serviço
❌ Prisma direto em controladores
❌ Validação ausente
❌ Uso de process.env
❌ console.log em vez de Sentry
❌ Lógica de negócios não testada

---

## 12. Integração com outras habilidades

* **Diretrizes de desenvolvimento frontend** → Alinhamento com o contrato da API
* **Rastreamento de erros** → Padrões do Sentry
* **Verificação de banco de dados** → Correção do esquema
* **Rastreamento de análises** → Pipelines de eventos
* **Desenvolvedor de habilidades** → Governança de habilidades

---

## 13. Lista de verificação de validação do operador

Antes de finalizar o trabalho de backend:

* [ ] BFRI ≥ 3
* [ ] Arquitetura em camadas Respeitado
* [ ] Entrada validada
* [ ] Erros capturados no Sentry
* [ ] Configuração unificada usada
* [ ] Testes escritos
* [ ] Sem antipadrões presentes

---

## 14. Status da Habilidade

**Status:** Estável · Aplicável · Pronta para produção
**Uso pretendido:** Microsserviços Node.js de longa duração com tráfego real e risco real
---

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.