---
nome: padrões_de_teste
descrição: Padrões e princípios de testes. Unitários, integração e estratégias de mocking.
ferramentas-permitidas: Ler, Escrever, Editar, Glob, Grep, Bash
---

# Padrões de Testes

> Princípios para suítes de testes confiáveis.

---

## 1. Pirâmide de Testes

```

```
    /\          E2E (Poucos)
   /  \         Fluxos críticos
  /----\
 /      \       Integração (Alguns)
/--------\      API, consultas ao banco
```

/          
/------------\    Unitários (Muitos)
Funções, classes

```

---

## 2. Padrão AAA

| Etapa | Objetivo |
|------|----------|
| **Arrange** | Preparar os dados do teste |
| **Act** | Executar o código sob teste |
| **Assert** | Verificar o resultado |

---

## 3. Seleção do Tipo de Teste

### Quando Usar Cada Um

| Tipo | Melhor Para | Velocidade |
|------|-------------|------------|
| **Unitário** | Funções puras, lógica | Rápido (<50ms) |
| **Integração** | API, banco de dados, serviços | Médio |
| **E2E** | Fluxos críticos do usuário | Lento |

---

## 4. Princípios de Testes Unitários

### Bons Testes Unitários

| Princípio | Significado |
|-----------|-------------|
| Rápidos | < 100ms cada |
| Isolados | Sem dependências externas |
| Repetíveis | Mesmo resultado sempre |
| Auto-verificáveis | Sem verificação manual |
| Oportunos | Escritos junto com o código |

### O Que Testar em Unitários

| Testar | Não Testar |
|--------|-----------|
| Lógica de negócio | Código de framework |
| Casos extremos | Bibliotecas de terceiros |
| Tratamento de erros | Getters simples |

---

## 5. Princípios de Testes de Integração

### O Que Testar

| Área | Foco |
|------|------|
| Endpoints de API | Requisição / resposta |
| Banco de dados | Consultas, transações |
| Serviços externos | Contratos |

### Setup / Teardown

| Fase | Ação |
|------|------|
| Before All | Conectar recursos |
| Before Each | Resetar estado |
| After Each | Limpar |
| After All | Desconectar |

---

## 6. Princípios de Mocking

### Quando Mockar

| Mockar | Não Mockar |
|-------|------------|
| APIs externas | Código sob teste |
| Banco de dados (unitário) | Dependências simples |
| Tempo / aleatoriedade | Funções puras |
| Rede | Armazenamento em memória |

### Tipos de Mock

| Tipo | Uso |
|------|-----|
| Stub | Retorna valores fixos |
| Spy | Rastreia chamadas |
| Mock | Define expectativas |
| Fake | Implementação simplificada |

---

## 7. Organização de Testes

### Nomenclatura

| Padrão | Exemplo |
|-------|---------|
| Deve + comportamento | "deve retornar erro quando..." |
| Quando + condição | "quando usuário não encontrado..." |
| Dado–quando–então | "dado X, quando Y, então Z" |

### Agrupamento

| Nível | Uso |
|------|-----|
| describe | Agrupar testes relacionados |
| it / test | Caso individual |
| beforeEach | Setup comum |

---

## 8. Dados de Teste

### Estratégias

| Abordagem | Uso |
|----------|-----|
| Factories | Gerar dados de teste |
| Fixtures | Conjuntos pré-definidos |
| Builders | Criação fluente de objetos |

### Princípios

- Use dados realistas
- Randomize valores não essenciais (faker)
- Compartilhe fixtures comuns
- Mantenha os dados mínimos

---

## 9. Boas Práticas

| Prática | Por quê |
|--------|---------|
| Um assert por teste | Falhas mais claras |
| Testes independentes | Sem dependência de ordem |
| Testes rápidos | Execução frequente |
| Nomes descritivos | Auto-documentação |
| Limpeza | Evita efeitos colaterais |

---

## 10. Anti-Padrões

| ❌ Não Faça | ✅ Faça |
|------------|--------|
| Testar implementação | Testar comportamento |
| Código de teste duplicado | Use factories |
| Setup de teste complexo | Simplifique ou divida |
| Ignorar testes instáveis | Corrija a causa raiz |
| Pular limpeza | Resetar estado |

---

> **Lembre-se:** Testes são documentação. Se alguém não consegue entender o que o código faz apenas olhando os testes, eles precisam ser reescritos.
```

