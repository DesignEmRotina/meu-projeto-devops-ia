descrição: Comando de geração e execução de testes. Cria e executa testes para o código.
---

# /teste - Geração e Execução de Testes

$ARGUMENTS

---

## Objetivo

Este comando gera testes, executa testes existentes ou verifica a cobertura de testes.

---

## Subcomandos

```

/teste - Executa todos os testes
/teste [arquivo/feature] - Gerar testes para um alvo específico
/teste cobertura - Exibir relatório de cobertura de testes
/teste relógio - Executa testes no modo watch

````

---

## Comportamento

### Geração de Testes

Quando solicitado testar um arquivo ou funcionalidade:

1. **Analisar o código**
   - Identificar funções e métodos
   - Encontrar casos de borda
   - Detectar dependências que precisam de mock

2. **Gerar casos de teste**
   - Testes de caminho feliz (happy path)
   - Casos de erro
   - Casos de borda
   - Testes de integração (se necessário)

3. **Escrever os testes**
   - Usar o framework de testes do projeto (Jest, Vitest, etc.)
   - Seguir os padrões de testes existentes
   - Mockar dependências externas

---

## Formato de Saída

### Para Geração de Testes

```markdown
## 🧪 Testes: [Alvo]

### Plano de Testes
| Caso de Teste | Tipo | Cobertura |
|---------------|------|-----------|
| Deve criar usuário | Unitário | Caminho feliz |
| Deve rejeitar email inválido | Unitário | Validação |
| Deve lidar com erro de banco | Unitário | Caso de erro |

### Testes Gerados

`tests/[arquivo].test.ts`

[Bloco de código com os testes]

---

Executar com: `npm test`
````

### Para Execução de Testes

```
🧪 Executando testes...

✅ auth.test.ts (5 passaram)
✅ user.test.ts (8 passaram)
❌ order.test.ts (2 passaram, 1 falhou)

Falha:
  ✗ deve calcular total com desconto
    Esperado: 90
    Recebido: 100

Total: 15 testes (14 passaram, 1 falhou)
```

---

## Exemplos

```
/teste src/services/auth.service.ts
/teste fluxo de cadastro de usuário
/teste cobertura
/teste corrigir testes com falha
```

---

## Padrões de Teste

### Estrutura de Teste Unitário

```typescript
describe('AuthService', () => {
  describe('login', () => {
    it('should return token for valid credentials', async () => {
      // Arrange
      const credentials = { email: 'test@test.com', password: 'pass123' };
      
      // Act
      const result = await authService.login(credentials);
      
      // Assert
      expect(result.token).toBeDefined();
    });

    it('should throw for invalid password', async () => {
      // Arrange
      const credentials = { email: 'test@test.com', password: 'wrong' };
      
      // Act & Assert
      await expect(authService.login(credentials)).rejects.toThrow('Invalid credentials');
    });
  });
});
```

---

## Princípios-Chave

* **Testar comportamento, não implementação**
* **Uma asserção por teste** (quando possível)
* **Nomes de testes descritivos**
* **Padrão Arrange-Act-Assert**
* **Mockar dependências externas**

