--- 
name: unreal-engine-cpp-pro
description: "Guia especializado para desenvolvimento em C++ com Unreal Engine 5.x, abordando práticas recomendadas de UObject, padrões de desempenho e boas práticas."
risk: seguro
source: própria
date_add: "27/02/2026"
---

# Unreal Engine C++ Pro

Esta habilidade fornece diretrizes de nível especialista para desenvolvimento com Unreal Engine 5 usando C++. Ela se concentra em escrever código robusto, de alto desempenho e em conformidade com os padrões.

## Quando usar
Use esta habilidade quando:
- Desenvolver código C++ para projetos da Unreal Engine 5.x
- Escrever Atores, Componentes ou classes derivadas de UObject
- Otimizar código crítico para o desempenho na Unreal Engine
- Depurar vazamentos de memória ou problemas de coleta de lixo
- Implementar funcionalidades expostas por Blueprint
- Seguir os padrões e convenções de codificação da Epic Games
- Trabalhar com o sistema de reflexão da Unreal (UCLASS, USTRUCT, UFUNCTION)
- Gerenciar o carregamento de ativos e referências fracas

Não use esta habilidade quando:
- Trabalhar com projetos que utilizam apenas Blueprint (sem código C++)
- Desenvolver para versões da Unreal Engine anteriores à 5.x
- Trabalhar em engines de jogos que não sejam da Unreal
- A tarefa não estiver relacionada ao desenvolvimento na Unreal Engine

## Princípios básicos

1. **UObject e Coleta de Lixo**:

* Sempre use `UPROPERTY()` para variáveis ​​de membro `UObject*` para garantir que elas sejam rastreadas pelo Coletor de Lixo (GC). * Use `TStrongObjectPtr<>` se precisar manter uma referência raiz fora de um grafo de UObject, mas geralmente prefira `addToRoot()`.

* Entenda a diferença entre a verificação `IsValid()` e `nullptr`. `IsValid()` lida com o estado de morte pendente de forma segura.

2. **Sistema de Reflexão do Unreal**:

* Use `UCLASS()`, `USTRUCT()`, `UENUM()` e `UFUNCTION()` para expor tipos ao sistema de reflexão e aos Blueprints.

* Minimize o uso de `BlueprintReadWrite` sempre que possível; prefira `BlueprintReadOnly` para estados que não devem ser sobrescritos pela lógica nos Blueprints de UI/Level.

3. **Prioridade ao Desempenho**:

* **Tick**: Desabilite o Ticking (`bCanEverTick = false`) por padrão. Habilite-o somente se absolutamente necessário. Prefira timers (`GetWorldTimerManager()`) ou lógica orientada a eventos.

* **Conversão de tipos**: Evite `Cast<T>()` em loops críticos. Armazene as referências em cache em `BeginPlay`.

* **Structs vs Classes**: Use structs `F` para tipos com grande volume de dados e que não sejam UObject para reduzir a sobrecarga.

## Convenções de Nomenclatura (Estritas)

Siga o padrão de codificação da Epic Games:

* **Templates**: Prefixo com `T` (ex.: `TArray`, `TMap`).

* **UObject**: Prefixo com `U` (ex.: `UCharacterMovementComponent`).

* **AActor**: Prefixo com `A` (ex.: `AMyGameMode`).

* **SWidget**: Prefixo com `S` (widgets Slate).

* **Structs**: Prefixo com `F` (ex.: `FVector`).

* **Enums**: Prefixo com `E` (ex.: `EWeaponState`).

* **Interfaces**: Prefixo com `I` (ex.: `IInteractable`).

* **Booleans**: Prefixo com `b` (ex.: `bIsDead`).

## Padrões Comuns

### 1. Busca Robusta de Componentes
Evite `GetComponentByClass` em `Tick`. Faça isso em `PostInitializeComponents` ou `BeginPlay`.

``cpp
void AMyCharacter::PostInitializeComponents() {

Super::PostInitializeComponents();

HealthComp = FindComponentByClass<UHealthComponent>();

check(HealthComp); // Falha grave em desenvolvimento se ausente
}
```

### 2. Implementação de Interface
Use interfaces para desacoplar sistemas (por exemplo, o sistema de interação).

```cpp
// Verificação de chamada de interface
if (TargetActor->Implements<UInteractable>()) {
IInteractable::Execute_OnInteract(TargetActor, this);

}
```

### 3. Carregamento Assíncrono (Referências Suaves)
Evite referências diretas (`UPROPERTY(EditDefaultsOnly) TSubclassOf<AActor>`) para recursos grandes que forçam ordens de carregamento. Use `TSoftClassPtr` ou `TSoftObjectPtr`.

```cpp
UPROPERTY(EditAnywhere, BlueprintReadWrite)
TSoftClassPtr<AWeapon> WeaponClassToLoad;

void AMyCharacter::Equip() {
if (WeaponClassToLoad.IsPending()) {
WeaponClassToLoad.LoadSynchronous(); // Ou use StreamableManager para assíncrono

}
}
```

## Depuração

* **Registro**: Use `UE_LOG` com categorias personalizadas.

```cpp

DEFINE_LOG_CATEGORY_STATIC(LogMyGame, Log, All);

UE_LOG(LogMyGame, Warning, TEXT("Saúde baixa: %f"), CurrentHealth);

```
* **Mensagens na tela**:

```cpp

if (GEngine) GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Red, TEXT("Morreu!"));

```
* **Registrador visual**: extremamente útil para depuração de IA. Implemente `IVisualLoggerDebugSnapshotInterface`.

## Lista de verificação antes do PR

- [ ] Este ator precisa de um Tick? Pode ser um Timer?

- [ ] Todos os membros `UObject*` estão encapsulados em `UPROPERTY`?

- [ ] Referências diretas (TSubclassOf) estão causando cadeias de carregamento? Podem ser ponteiros flexíveis?

- [ ] Você limpou os delegates verificados em `EndPlay`?