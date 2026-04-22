--- 
name: especialista-em-ecs-bevy
description: "Domine o Sistema de Componentes de Entidade (ECS) do Bevy em Rust, abordando Sistemas, Consultas, Recursos e agendamento paralelo."
risk: seguro
source: comunidade
date_add: "2026-02-27"
---

# Especialista em ECS do Bevy

## Visão Geral

Um guia para construir lógica de jogos de alto desempenho usando a arquitetura ECS orientada a dados do Bevy. Aprenda como estruturar sistemas, otimizar consultas, gerenciar recursos e aproveitar a execução paralela.

## Quando usar esta habilidade

- Use ao desenvolver jogos com o motor Bevy em Rust.

- Use ao projetar sistemas de jogos que precisam ser executados em paralelo.

- Use ao otimizar o desempenho do jogo minimizando falhas de cache.

- Use ao refatorar lógica orientada a objetos em padrões ECS orientados a dados.

## Guia Passo a Passo

### 1. Definindo Componentes

Use structs simples para dados. Derive `Component` e `Reflect`.

``rust
#[derive(Component, Reflect, Default)]
#[reflect(Component)]
struct Velocity {
x: f32,

y: f32,
}

#[derive(Component)]
struct Player;

``

### 2. Escrevendo Sistemas

Sistemas são funções Rust comuns que consultam componentes.

``rust
fn movement_system(
time: Res<Time>,

mut query: Query<(&mut Transform, &Velocity), With<Player>>,
) {

for (mut transform, velocity) in &mut query {

transform.translation.x += velocity.x * time.delta_seconds();

transform.translation.y += velocity.y * time.delta_seconds();

}
}
```

### 3. Gerenciando Recursos

Use `Resource` para dados globais (pontuação, estado do jogo).

``rust
#[derive(Resource)]
struct GameState {
score: u32,
}

fn score_system(mut game_state: ResMut<GameState>) {
game_state.score += 10;

}
```

### 4. Agendando Sistemas

Adicione sistemas ao construtor `App`, definindo a ordem de execução, se necessário.

``rust
fn main() {

App::new()

.add_plugins(DefaultPlugins)

.init_resource::<GameState>()

.add_systems(Update, (movement_system, score_system).chain())

.run();

}
```

## Exemplos

### Exemplo 1: Criando Entidades com o Componente `require`

```rust
use bevy::prelude::*;

#[derive(Component, Reflect, Default)]
#[require(Velocity, Sprite)]
struct Player;

#[derive(Component, Default)]
struct Velocity {
x: f32,

y: f32,
}

fn setup(mut commands: Commands, asset_server: Res<AssetServer>) {

commands.spawn((
Player,

Velocity { x: 10.0, y: 0.0 },

Sprite::from_image(asset_server.load("player.png")),
));

}
```

### Exemplo 2: Filtros de Consulta

Use `With` e `Without` para filtrar entidades de forma eficiente.

```rust
fn enemy_behavior(
query: Query<&Transform, (With<Enemy>, Without<Dead>)>,
) {

for transform in &query {

// Somente inimigos ativos são processados ​​aqui

}
}
```

## Boas Práticas

- ✅ **Faça:** Use filtros `Query` (`With`, `Without`, `Changed`) para reduzir o número de iterações.

- ✅ **Faça:** Prefira `Res` a `ResMut` quando o acesso somente leitura for suficiente para permitir a execução paralela.

- ✅ **Faça:** Use `Bundle` para gerar entidades complexas atomicamente.

- ❌ **Não faça:** Armazene lógica pesada dentro de Componentes; mantenha-os como dados puros.

- ❌ **Não faça:** Use `RefCell` ou mutabilidade interna dentro de componentes; deixe o ECS lidar com empréstimos.

## Solução de Problemas

**Problema:** O sistema entra em pânico com o erro "Conflito".

**Solução:** Provavelmente você está tentando acessar o mesmo componente de forma mutável em dois sistemas em execução paralela. Use `.chain()` para ordená-los ou divida a lógica.