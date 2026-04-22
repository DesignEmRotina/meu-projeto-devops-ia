--- 
name: padrões-React-UI
description: "Padrões de interface de usuário React modernos para carregamento de estados, tratamento de erros e busca de dados. Use ao construir componentes de interface do usuário, lidar com dados assíncronos ou gerenciar estados da interface do usuário."
risk: desconhecido
source: comunidade
date_add: "2026-02-27"
---

# Padrões de UI do React

## Princípios Fundamentais

1. **Nunca mostre uma UI desatualizada** - Exiba indicadores de carregamento somente quando houver carregamento real
2. **Sempre exponha os erros** - Os usuários precisam saber quando algo falha
3. **Atualizações otimistas** - Faça a UI parecer instantânea
4. **Divulgação progressiva** - Mostre o conteúdo conforme ele se torna disponível
5. **Degradação elegante** - Dados parciais são melhores do que nenhum dado

## Padrões de Estado de Carregamento

### A Regra de Ouro

**Mostre o indicador de carregamento SOMENTE quando não houver dados para exibir.**

```typescript
// CORRETO - Mostre o carregamento somente quando não houver dados
const { data, loading, error } = useGetItemsQuery();

if (error) return <ErrorState error={error} onRetry={refetch} />;

if (loading && !data) return <LoadingState />;

if (!data?.items.length) return <EmptyState />;

return <ItemList items={data.items} />;

``

```typescript
// INCORRETO - Mostra o indicador de carregamento mesmo quando temos dados em cache
if (loading) return <LoadingState />; // Pisca ao buscar novamente!

```

### Árvore de Decisão do Estado de Carregamento

```
Há um erro?

→ Sim: Mostrar estado de erro com opção de nova tentativa
→ Não: Continuar

Está carregando E não temos dados?

→ Sim: Mostrar indicador de carregamento (spinner/esqueleto)

→ Não: Continuar

Temos dados?

→ Sim, com itens: Exibir os dados
→ Sim, mas vazio: Exibir estado vazio

→ Não: Exibir carregamento (alternativa)
```

### Esqueleto vs. Spinner

| Usar Esqueleto Quando | Usar Spinner Quando |

|-------------------|------------------|

| Formato de conteúdo conhecido | Formato de conteúdo desconhecido |

| Layouts de lista/cartão | Ações modais |

| Carregamento inicial da página | Envio de botões |

| Espaços reservados para conteúdo | Operações em linha |

## Padrões de Tratamento de Erros

### A Hierarquia de Tratamento de Erros

```
1. Erro embutido (nível de campo) → Erros de validação de formulário
2. Notificação Toast → Erros recuperáveis, o usuário pode tentar novamente
3. Banner de erro → Erros em nível de página, os dados ainda são parcialmente utilizáveis
4. Tela de erro completa → Irrecuperável, requer ação do usuário
```

### Sempre Exibir Erros

**CRÍTICO: Nunca ignore erros silenciosamente.**

```typescript
// CORRETO - O erro é sempre exibido ao usuário
const [createItem, { loading }] = useCreateItemMutation({

onCompleted: () => {

toast.success({ title: 'Item criado' });

},

onError: (error) => {

console.error('Falha ao criar o item:', error);

toast.error({ title: 'Falha ao criar o item' });

},
});

/ // INCORRETO - Erro capturado silenciosamente, o usuário não tem ideia
const [createItem] = useCreateItemMutation({

onError: (error) => {

console.error(error); // O usuário não vê nada!

},
});

```

### Padrão de Componente de Estado de Erro

```typescript
interface ErrorStateProps {

error: Error;

onRetry?: () => void;

title?: string;
}

const ErrorState = ({ error, onRetry, title }: ErrorStateProps) => (

<div className="error-state">

<Icon name="exclamation-circle" />

<h3>{title ?? 'Algo deu errado'}</h3>

<p>{error.message}</p>

{onRetry && (

<Button onClick={onRetry}>Tentar novamente</Button>

)}

</div>

);

```

## Padrões de Estado do Botão

### Estado de Carregamento do Botão

```tsx
<Button

onClick={handleSubmit}

isLoading={isSubmitting}

disabled={!isValid || isSubmitting}
>

Enviar
</Button>
```

### Desativar durante operações

**CRÍTICO: Sempre desative os gatilhos durante operações assíncronas.**

```tsx
// CORRETO - Botão desativado durante o carregamento
<Button

disabled={isSubmitting}

isLoading={isSubmitting}

onClick={handleSubmit}
>

Enviar
</Button>

// INCORRETO - O usuário pode tocar várias vezes
<Button onClick={handleSubmit}>

{isSubmitting ? 'Enviando...' : 'Enviar'}
</Button>
```

## Estados vazios

### Requisitos para estado vazio

Toda lista/coleção DEVE ter um estado vazio:

```tsx
// INCORRETO - Sem estado vazio
return <FlatList data={items} />;

// CORRETO - Estado vazio explícito
return (

<FlatList

data={items}

ListEmptyComponent={<EmptyState />}

/>
);
```

### Estados Vazios Contextuais

```tsx

// Busca sem resultados
<EmptyState

icon="search"

title="Nenhum resultado encontrado"

description="Tente outros termos de busca"

/>

// Lista sem itens
<EmptyState

icon="plus-circle"

title="Nenhum item ainda"

description="Crie seu primeiro item"

action={{ label: 'Criar Item', onClick: handleCreate }}
/>
```

## Padrão de Submissão de Formulário

```tsx
const MyForm = () => {

const [submit, { loading }] = useSubmitMutation({

onCompleted: handleSuccess,

onError: handleError,

});

const handleSubmit = async () => {

if (!isValid) {

toast.error({ title: 'Por favor, corrija os erros' });

return;

await submit({ variables: { input: values ​​} });

};

return (

<form>

<Input

value={values.name}

onChange={handleChange('name')}

error={touched.name ? errors.name : undefined}

/>

<Button

type="submit"

onClick={handleSubmit}

disabled={!isValid || loading}

isLoading={loading}

>

Submit

</Button>

</form>

);

};

```

## Antipadrões

### Estados de Carregamento

```typescript
// INCORRETO - Spinner quando há dados (causa flash)
if (loading) return <Spinner />;

/ // CORRETO - Exibir apenas o carregamento sem dados
if (loading && !data) return <Spinner />;

```

### Tratamento de Erros

```typescript
// INCORRETO - Erro ignorado
try {

await mutation();

} catch (e) {

console.log(e); // O usuário não tem ideia!

}

// CORRETO - Erro exibido
onError: (error) => {

console.error('operação falhou:', error);

toast.error({ title: 'Operação falhou' });
}
```

### Estados do Botão

```typescript
// INCORRETO - Botão não desabilitado durante o envio
<Button onClick={submit}>Enviar</Button>

// CORRETO - Desabilitado e exibe o indicador de carregamento
<Button onClick={submit} disabled={loading} isLoading={loading}>

Enviar
</Button>
```

## Lista de Verificação

Antes de concluir qualquer componente de interface do usuário:

**Estados da Interface do Usuário:**
- [ ] Estado de erro tratado e exibido ao usuário
- [ ] Estado de carregamento exibido somente quando não houver dados
- [ ] Estado vazio fornecido para coleções
- [ ] Botões desabilitados durante operações assíncronas
- [ ] Botões exibem indicador de carregamento quando apropriado

**Dados e Mutações:**

- [ ] Mutações possuem manipulador onError
- [ ] Todas as ações do usuário possuem feedback (toast/visual)

## Integração com Outras Habilidades

- **graphql-schema**: Usar mutação Padrões com tratamento de erros adequado
- **testing-patterns**: Testar todos os estados da interface do usuário (carregando, erro, vazio, sucesso)
- **formik-patterns**: Aplicar padrões de envio de formulário

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.