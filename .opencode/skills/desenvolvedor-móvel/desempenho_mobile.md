# Referência de Performance Mobile

> Aprofundamento em otimização de performance em **React Native** e **Flutter**, animações a 60fps, gerenciamento de memória e considerações de bateria.
> **Este arquivo cobre a área nº 1 onde código gerado por IA FALHA.**

---

## 1. Mentalidade de Performance Mobile

### Por que Performance Mobile é Diferente

```
DESKTOP:                          MOBILE:
├── Poder praticamente ilimitado  ├── Bateria importa
├── RAM abundante                 ├── RAM compartilhada e limitada
├── Rede estável                  ├── Rede instável
├── CPU sempre disponível         ├── CPU reduz clock quando esquenta
└── Usuário espera rápido         └── Usuário espera INSTANTÂNEO
```

### Conceito de Orçamento de Performance

```
Cada frame deve ser processado em:
├── 60fps → 16,67ms por frame
├── 120fps (ProMotion) → 8,33ms por frame

Se seu código demora mais que isso:
├── Frames caem → Scroll/animações travadas
├── Usuário percebe como "lento" ou "quebrado"
└── Ele VAI desinstalar o app
```

---

## 2. Performance em React Native

### 🚫 Erro nº 1 da IA: Usar ScrollView para Listas

```javascript
// ❌ NUNCA FAÇA ISSO — erro favorito das IAs
<ScrollView>
  {items.map(item => (
    <ItemComponent key={item.id} item={item} />
  ))}
</ScrollView>

// Por que isso é catastrófico:
// ├── Renderiza TODOS os itens de uma vez
// ├── Explosão de memória
// ├── Render inicial leva segundos
// └── Scroll fica travado

// ✅ SEMPRE USE FlatList
<FlatList
  data={items}
  renderItem={renderItem}
  keyExtractor={item => item.id}
/>
```

### Checklist de Otimização da FlatList

```javascript
// ✅ CORRETO: Todas as otimizações aplicadas

// 1. Memoizar o componente do item
const ListItem = React.memo(({ item }: { item: Item }) => {
  return (
    <Pressable style={styles.item}>
      <Text>{item.title}</Text>
    </Pressable>
  );
});

// 2. Memoizar renderItem com useCallback
const renderItem = useCallback(
  ({ item }: { item: Item }) => <ListItem item={item} />,
  []
);

// 3. keyExtractor estável (NUNCA use index!)
const keyExtractor = useCallback((item: Item) => item.id, []);

// 4. getItemLayout para itens de altura fixa
const getItemLayout = useCallback(
  (data: Item[] | null, index: number) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  }),
  []
);

// 5. Aplicação na FlatList
<FlatList
  data={items}
  renderItem={renderItem}
  keyExtractor={keyExtractor}
  getItemLayout={getItemLayout}
  removeClippedSubviews={true}
  maxToRenderPerBatch={10}
  windowSize={5}
  initialNumToRender={10}
  updateCellsBatchingPeriod={50}
/>
```

### Por que Cada Otimização Importa

| Otimização              | O que evita                  | Impacto    |
| ----------------------- | ---------------------------- | ---------- |
| `React.memo`            | Re-render desnecessário      | 🔴 Crítico |
| `useCallback`           | Nova função a cada render    | 🔴 Crítico |
| `keyExtractor` estável  | Reciclagem errada            | 🔴 Crítico |
| `getItemLayout`         | Cálculo async de layout      | 🟡 Alto    |
| `removeClippedSubviews` | Uso excessivo de memória     | 🟡 Alto    |
| `maxToRenderPerBatch`   | Bloqueio da thread principal | 🟢 Médio   |
| `windowSize`            | Uso de memória               | 🟢 Médio   |

### FlashList: A Opção Superior

```javascript
import { FlashList } from "@shopify/flash-list";

<FlashList
  data={items}
  renderItem={renderItem}
  estimatedItemSize={ITEM_HEIGHT}
  keyExtractor={keyExtractor}
/>

// Benefícios:
├── Reciclagem mais rápida
├── Melhor uso de memória
├── API mais simples
└── Menos props de otimização
```

### Performance de Animações

```javascript
// ❌ Animação controlada pelo JS (bloqueia a thread JS)
useNativeDriver: false

// ✅ Animação no driver nativo (thread de UI)
useNativeDriver: true
```

> Driver nativo suporta **apenas** `transform` e `opacity`.

Para propriedades mais complexas, use **Reanimated 3**, que roda totalmente na UI thread.

---

## 3. Performance em Flutter

### 🚫 Erro nº 1 da IA: Uso Excessivo de setState

```dart
// ❌ ERRADO: setState reconstrói a árvore inteira
setState(() {
  _counter++;
});
```

### Revolução do `const`

```dart
// ✅ CORRETO: const evita rebuilds
const ExpensiveWidget();
```

> **Regra:** todo widget que não depende de estado **DEVE** ser `const`.

### Gerenciamento de Estado Direcionado

```dart
// ✅ Reconstrói apenas o necessário
ValueListenableBuilder<int>(
  valueListenable: counter,
  builder: (_, value, __) => Text('$value'),
)
```

### Boas Práticas com Provider / Riverpod

```dart
// ❌ Reconstrói em qualquer mudança
ref.watch(myProvider);

// ✅ Reconstrói apenas quando a propriedade muda
ref.watch(myProvider.select((s) => s.name));
```

### Otimização de Listas

```dart
// ✅ Renderização preguiçosa
ListView.builder(
  itemBuilder: ...
)
```

> Use `itemExtent` sempre que a altura for fixa.

### Otimização de Imagens

```dart
CachedNetworkImage(
  memCacheWidth: 200,
  memCacheHeight: 200,
)
```

### Padrão Dispose

```dart
@override
void dispose() {
  controller.dispose();
  subscription.cancel();
  super.dispose();
}
```

---

## 4. Performance de Animação (Ambas Plataformas)

### O Imperativo dos 60fps

```
< 24fps  → Quebrado
30fps    → Travado
45fps    → Não suave
60fps    → Alvo mínimo
120fps   → Premium
```

### GPU vs CPU

```
RÁPIDO (GPU):              LENTO (CPU):
├── transform              ├── width / height
├── opacity                ├── margin / padding
└── composited             └── recalcula layout
```

> **Regra:** anime apenas `transform` e `opacity`.

---

## 5. Gerenciamento de Memória

### Vazamentos Comuns

| Fonte              | Solução         |
| ------------------ | --------------- |
| Timers             | Cleanup         |
| Listeners          | Remove          |
| Subscriptions      | Cancel          |
| Imagens grandes    | Resize + cache  |
| Async após unmount | AbortController |
| Controllers        | dispose()       |

### Memória de Imagens

```
Memória = largura × altura × 4 bytes
Imagem 4K ≈ 33MB
10 imagens 4K = CRASH
```

---

## 6. Otimização de Bateria

### Principais Vilões

| Fonte        | Impacto       |
| ------------ | ------------- |
| Tela ligada  | 🔴 Altíssimo  |
| GPS contínuo | 🔴 Muito alto |
| Requests     | 🟡 Alto       |
| Animações    | 🟡 Médio      |

### OLED e Dark Mode

```
Preto puro (#000000) = pixel desligado = economia máxima
```

---

## 7. Performance de Rede

### Arquitetura Offline-First

```
UI → Cache → Rede
```

Benefícios: UI instantânea, funciona offline, menos consumo.

### Otimizações

* Batch de requisições
* Cache com ETag
* Compressão gzip/brotli
* Paginação

---

## 8. Testes de Performance

### Sempre Testar em:

* Android barato
* iPhone antigo
* Build release/profile
* Dados reais (1000+ itens)

---

## 9. Cartão de Referência Rápida

### React Native

* FlatList / FlashList
* useCallback + React.memo
* useNativeDriver
* Cleanup em useEffect

### Flutter

* Widgets `const`
* ListView.builder
* Estado granular
* dispose() sempre

---

> **Lembre-se:** performance não é otimização, é qualidade básica.
> Um app lento é um app quebrado. Teste no pior dispositivo do seu usuário, não no melhor que você tem.
