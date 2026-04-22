# Antipadrões de Teste

**Consulte esta referência quando:** escrever ou alterar testes, adicionar mocks ou sentir a tentação de adicionar métodos exclusivos de teste ao código de produção.

## Visão Geral

Os testes devem verificar o comportamento real, não o comportamento simulado. Mocks são um meio de isolar, não o que está sendo testado.

**Princípio fundamental:** Teste o que o código faz, não o que os mocks fazem.

**Seguir TDD rigorosamente evita esses antipadrões.**

## As Leis de Ferro

```
1. NUNCA teste o comportamento de mocks
2. NUNCA adicione métodos exclusivos para teste a classes de produção
3. NUNCA crie mocks sem entender as dependências
```

## Antipadrão 1: Testando o Comportamento de Mocks

**A violação:**
```typescript
// ❌ RUIM: Testar se o mock existe
test('renderiza a barra lateral', () => {

render(<Page />);

expect(screen.getByTestId('sidebar-mock')).toBeInTheDocument();
});

```

**Por que isso está errado:**

- Você está verificando se o mock funciona, não se o componente funciona
- O teste passa quando o mock está presente, falha quando não está
- Não informa nada sobre o comportamento real

**Correção do seu parceiro humano:** "Estamos testando o comportamento de um mock?" **A solução:**

```typescript
// ✅ BOM: Teste o componente real ou não o simule
test('renderiza a barra lateral', () => {

render(<Page />); // Não simule a barra lateral
expect(screen.getByRole('navigation')).toBeInTheDocument();
});

// OU se a barra lateral precisar ser simulada para isolamento:
// Não asserte no mock - teste o comportamento da Page com a barra lateral presente
```

### Função de Controle

```
ANTES de assertar em qualquer elemento simulado:

Pergunte: "Estou testando o comportamento real do componente ou apenas a existência do mock?"

SE estiver testando a existência de mocks:

PARE - Exclua a asserção ou remova o mock do componente

Teste o comportamento real em vez disso
```

## Antipadrão 2: Métodos exclusivos para testes em produção

**A violação:**
```typescript
// ❌ RUIM: destroy() usado apenas em testes
class Session {

async destroy() { // Parece API de produção!

await this._workspaceManager?.destroyWorkspace(this.id);

// ... limpeza
}
}

// Em testes
afterEach(() => session.destroy());
```

**Por que isso está errado:**
- Classe de produção poluída com código exclusivo de teste
- Perigoso se chamado acidentalmente em produção
- Viola o princípio YAGNI (You Ain't Gonna Need It - Você Não Vai Precisar Disso) e a separação de responsabilidades
- Confunde o ciclo de vida do objeto com o ciclo de vida da entidade

**A correção:**
```typescript
// ✅ BOM: Utilitários de teste lidam com a limpeza de testes
// A sessão não possui destroy() - ela é sem estado em produção

// Em test-utils/
export async function cleanupSession(session: Session) {

const workspace = session.getWorkspaceInfo();

if (workspace) {

await workspaceManager.destroyWorkspace(workspace.id);

}
}

// Nos testes
afterEach(() => cleanupSession(session));

```

### Função de Controle

```
ANTES de adicionar qualquer método à classe de produção:

Pergunte: "Isso é usado apenas por testes?"

SE sim:

PARE - Não adicione

Coloque em utilitários de teste

Pergunte: "Esta classe é responsável pelo ciclo de vida deste recurso?"

SE não:

PARE - Classe errada para este método
```

## Antipadrão 3: Simulação sem compreensão

**A violação:**
```typescript
// ❌ RUIM: Simulação quebra a lógica de teste
test('detecta servidor duplicado', () => {

// A simulação impede a gravação da configuração da qual o teste depende!

vi.mock('ToolCatalog', () => ({

discoverAndCacheTools: vi.fn().mockResolvedValue(undefined)

}));

await addServer(config);

await addServer(config); // Deveria lançar uma exceção - mas não lança!
});
```

**Por que isso está errado:**
- O método simulado tinha um efeito colateral do qual o teste dependia (gravação da configuração)
- O uso excessivo de mocks para "garantir a segurança" quebra o comportamento real
- O teste passa por um motivo errado ou falha misteriosamente

**A correção:**
```typescript
// ✅ BOM: Simule no nível correto
test('detecta servidor duplicado', () => {

// Simule a parte lenta, preservando o comportamento necessário para o teste

vi.mock('MCPServerManager'); // Simule apenas a inicialização lenta do servidor

await addServer(config); // Configuração gravada

await addServer(config); // Duplicado detectado ✓
});

```

### Função Gate

``` ANTES de simular qualquer método:

PARE - Não simule ainda

1. Pergunte: "Quais efeitos colaterais o método real possui?"

2. Pergunte: "Este teste depende de algum desses efeitos colaterais?"

3. Pergunte: "Eu entendo completamente o que este teste precisa?"

SE depender de efeitos colaterais:

Simule em um nível inferior (a operação lenta/externa real)

OU use dublês de teste que preservem o comportamento necessário
NÃO use o método de alto nível do qual o teste depende

SE não tiver certeza do que o teste depende:

Execute o teste com a implementação real PRIMEIRO

Observe o que realmente precisa acontecer

ENTÃO adicione a simulação mínima no nível correto

Sinais de alerta:

- "Vou simular isso para garantir"

- "Isso pode ser lento, melhor simular"

- Simulação sem entender a cadeia de dependências
```

## Antipadrão 4: Simulações Incompletas

**A violação:**
```typescript
// ❌ RUIM: Simulação parcial - apenas os campos que você acha que precisa
const mockResponse = {

status: 'success',

data: { userId: '123', name: 'Alice' }

// Ausente: metadados que o código subsequente usa
};

// Mais tarde: falha quando o código acessa response.metadata.requestId
```

**Por que isso está errado:**
- **Mocks parciais ocultam suposições estruturais** - Você só simulou os campos que conhece
- **O código subsequente pode depender de campos que você não incluiu** - Falhas silenciosas
- **Os testes passam, mas a integração falha** - Mock incompleto, API real completa
- **Confiança falsa** - O teste não prova nada sobre o comportamento real

**A Regra de Ferro:** Simule a estrutura de dados COMPLETA como ela existe na realidade, não apenas os campos que seu teste imediato usa.

**A correção:**
```typescript
// ✅ BOM: Espelha a API real completude
const mockResponse = {

status: 'success',

data: { userId: '123', name: 'Alice' },

metadata: { requestId: 'req-789', timestamp: 1234567890 }

// Todos os campos retornados pela API real
};

```

### Função Gate

```
ANTES de criar respostas simuladas:

Verifique: "Quais campos a resposta da API real contém?"

Ações:

1. Examine a resposta real da API a partir da documentação/exemplos

2. Inclua TODOS os campos que o sistema possa consumir posteriormente

3. Verifique se o mock corresponde completamente ao esquema da resposta real

Crítico:

Se você estiver criando um mock, você deve entender a estrutura COMPLETA

Mocks parciais falham silenciosamente quando o código depende de campos omitidos

Em caso de dúvida: Inclua todos os campos documentados
```

## Antipadrão 5: Testes de Integração como Reflexão Posterior

**A violação:**
```
✅ Implementação completa
❌ Nenhum teste escrito
"Pronto para teste"
```

**Por que isso está errado:**
- Testar faz parte da implementação, não é um acompanhamento opcional
- TDD teria detectado isso
- Não se pode declarar a conclusão sem testes

**A correção:**

```
Ciclo TDD:

1. Escrever um teste que falha
2. Implementar para passar
3. Refatorar
4. ENTÃO declarar a conclusão
```

## Quando os Mocks se Tornam Excessivos Complexo

**Sinais de alerta:**
- Configuração de mocks mais demorada que a lógica de teste
- Mocks para tudo para que o teste passe
- Mocks que não possuem métodos reais presentes nos componentes
- Teste falha quando o mock muda

**A pergunta do seu parceiro humano:** "Precisamos mesmo usar um mock aqui?"

**Considere:** Testes de integração com componentes reais geralmente são mais simples do que mocks complexos

## TDD previne esses antipadrões

**Por que o TDD ajuda:**

1. **Escreva o teste primeiro** → Obriga você a pensar sobre o que está realmente testando
2. **Observe a falha** → Confirma que o teste testa o comportamento real, não os mocks
3. **Implementação mínima** → Métodos exclusivos de teste não são adicionados
4. **Dependências reais** → Você vê o que o teste realmente precisa antes de criar mocks

**Se você está testando o comportamento de mocks, você violou o TDD** - você adicionou mocks sem observar a falha do teste em relação ao código real primeiro.

## Referência rápida

| Antipadrão | Correção |

--------------|-----|

| Asserções em elementos mock | Teste o componente real ou remova o mock |

| Métodos somente de teste em produção | Migre para utilitários de teste |

| Mocks sem compreensão | Entenda as dependências primeiro, use mocks mínimos |

| Mocks incompletos | Espelhe a API real completamente |

| Testes como reflexão tardia | TDD - testes primeiro |

| Mocks excessivamente complexos | Considere testes de integração |

## Sinais de alerta

- Asserções verificam IDs de teste `*-mock`
- Métodos chamados apenas em arquivos de teste
- Configuração de mocks representa mais de 50% do teste
- Teste falha ao remover o mock
- Não é possível explicar por que o mock é necessário
- Mocks "apenas por segurança"

## Conclusão

**Mocks são ferramentas para isolar, não coisas para testar.**

Se o TDD revelar que você está testando o comportamento de mocks, você errou.

Solução: Teste o comportamento real ou questione por que você está fazendo essa zombaria.