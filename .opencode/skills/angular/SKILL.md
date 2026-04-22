--- 
name: angular
description: Especialista em Angular moderno (v20+) com profundo conhecimento em Signals, componentes independentes, aplicações sem zonas, SSR/Hidratação e padrões reativos.
risk: seguro
source: próprio
date_add: '2026-02-27'
---

# Especialista em Angular

Domine o desenvolvimento Angular moderno com Signals, componentes independentes, aplicações sem zonas, SSR/Hidratação e os mais recentes padrões reativos.

## Quando usar esta habilidade

- Construindo novas aplicações Angular (v20+)
- Implementando padrões reativos baseados em Signals
- Criando componentes independentes e migrando de NgModules
- Configurando aplicações Angular sem zonas (Zoneless)
- Implementando SSR, pré-renderização e hidratação
- Otimizando o desempenho do Angular
- Adotando padrões modernos e boas práticas do Angular

## Não use esta habilidade quando

- Migrando do AngularJS (1.x) → use a habilidade `angular-migration`
- Trabalhando com aplicações Angular legadas que não podem ser atualizadas
- Problemas gerais com TypeScript → use a habilidade `typescript-expert`

## Instruções

1. Avalie a versão do Angular e a estrutura do projeto
2. Aplique padrões modernos (Signals, Standalone, Zoneless)
3. Implemente com tipagem e reatividade adequadas
4. Valide com build e testes

## Segurança

- Sempre teste as alterações em desenvolvimento antes de produção
- Migração gradual para aplicações existentes (não faça uma mudança radical) (Refatoração)
- Manter a compatibilidade com versões anteriores durante as transições

---

## Linha do Tempo das Versões do Angular

| Versão | Lançamento | Principais Recursos |

| -------------- | ------- | ------------------------------------------------------ |

| **Angular 20** | 2º trimestre de 2025 | Sinais estáveis, Zoneless estável, Hidratação incremental |

| **Angular 21** | 4º trimestre de 2025 | Sinais como padrão, SSR aprimorado |

| **Angular 22** | 2º trimestre de 2026 | Formulários de sinal, Componentes sem seletor |

---

## 1. Sinais: A Nova Primitiva Reativa

Sinais são o sistema de reatividade granular do Angular, substituindo a detecção de mudanças baseada em zone.js.

### Conceitos Básicos

```typescript
import { signal, computed, effect } from "@angular/core";

// Sinal gravável
const count = signal(0);

// Ler valor
console.log(count()); // 0

// Atualizar valor
count.set(5); // Atribuição direta
count.update((v) => v + 1); // Atualização funcional

// Sinal computado (derivado)
const doubled = computed(() => count() * 2);

/ // Efeito (efeitos colaterais)
effect(() => {

console.log(`Contagem alterada para: ${count()}`);
});

```

### Entradas e Saídas Baseadas em Sinais

```typescript
import { Component, input, output, model } from "@angular/core";

@Component({

selector: "app-user-card",

standalone: ​​true,

template: `

<div class="card">

<h3>{{ name() }}</h3>

<span>{{ role() }}</span>

<button (click)="select.emit(id())">Selecionar</button>

</div>

`,
})
export class UserCardComponent {

// Entradas de sinal (somente leitura)

id = input.required<string>();

name = input.required<string>();

role = input<string>("Usuário"); // Com valor padrão

// Saída

select = output<string>();

// Vinculação bidirecional (modelo)

isSelected = model(false);
}

// Uso:
// <app-user-card [id]="'123'" [name]="'John'" [(isSelected)]="selected" />
```

### Consultas de sinal (ViewChild/ContentChild)

```typescript
import {

Component,

viewChild,

viewChildren,

contentChild,
} from "@angular/core";

@Component({

selector: "app-container",

standalone: ​​true,

template: `

<input #searchInput />

<app-item *ngFor="let item of items()" />

`,
})
export class ContainerComponent {

// Consultas baseadas em sinal
searchInput = viewChild<ElementRef>("searchInput");

items = viewChildren(ItemComponent);

projectedContent = contentChild(HeaderDirective);

focusSearch() {
this.searchInput()?.nativeElement.focus();

}
}
```

### Quando usar Signals vs RxJS

| Caso de uso | Signals | RxJS |

| ----------------------- | --------------- | -------------------------------- |

| Estado local do componente | ✅ Preferencial | Exagerado |
| Valores derivados/computados | ✅ `computed()` | `combineLatest` funciona |

| Efeitos colaterais | ✅ `effect()` | Operador `tap` |

| Requisições HTTP | ❌ | ✅ HttpClient retorna Observable |

| Fluxos de eventos | ❌ | ✅ `fromEvent`, operadores |

| Fluxos assíncronos complexos | ❌ | ✅ `switchMap`, `mergeMap` |

---

## 2. Componentes Independentes

Componentes independentes são autocontidos e não requerem declarações de NgModule.

### Criando Componentes Independentes

```typescript
import { Component } from "@angular/core";

import { CommonModule } from "@angular/common";

import { RouterLink } from "@angular/router";

@Component({

selector: "app-header",

standalone: ​​true,

imports: [CommonModule, RouterLink], // Importações diretas

template: `

<header>

<a routerLink="/">Home</a>

<a routerLink="/about">About</a>

</header>

`,
})
export class HeaderComponent {}
```

### Inicialização sem NgModule

```typescript
// main.ts
import { bootstrapApplication } from "@angular/platform-browser";

import { provideRouter } from "@angular/router";

import { provideHttpClient } from "@angular/common/http";

import { AppComponent } from "./app/app.component";

import { routes } from "./app/app.routes";

bootstrapApplication(AppComponent, {
providers: [provideRouter(routes), provideHttpClient()],
});

```

### Carregamento sob demanda de componentes independentes

```typescript
// app.routes.ts
import { Routes } from "@angular/router";

export const routes: Routes = [

{
path: "dashboard",

loadComponent: () =>

import("./dashboard/dashboard.component").then(

(m) => m.DashboardComponent,

),

},

{
path: "admin",

loadChildren: () =>

import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES),

},
];

```

---

## 3. Angular sem zonas

Aplicações sem zonas não usam zone.js, melhorando o desempenho e a depuração.

### Habilitando o Modo sem Zonas

```typescript
// main.ts
import { bootstrapApplication } from "@angular/platform-browser";

import { provideZonelessChangeDetection } from "@angular/core";
import { AppComponent } from "./app/app.component";

bootstrapApplication(AppComponent, {
providers: [provideZonelessChangeDetection()],
});

``

### Padrões de Componentes Sem Zona

```typescript
import { Component, signal, ChangeDetectionStrategy } from "@angular/core";

@Component({
selector: "app-counter",

standalone: ​​true,

changeDetection: ChangeDetectionStrategy.OnPush,

template: `

<div>Contagem: {{ count() }}</div>

<button (click)="increment()">+</button>

`,
})
export class CounterComponent {

count = signal(0);

increment() {
this.count.update((v) => v + 1);
// Sem necessidade de zone.js - Sinal aciona a detecção de mudanças

}
}
```

### Principais benefícios sem zone.js

- **Desempenho**: Sem correções de zone.js em APIs assíncronas
- **Depuração**: Rastreamento de pilha limpo sem wrappers de zona
- **Tamanho do pacote**: Menor sem zone.js (economia de ~15 KB)
- **Interoperabilidade**: Melhor com Web Components e microfrontends

---

## 4. Renderização e Hidratação no Lado do Servidor

### Configuração de SSR com Angular CLI

```bash
ng add @angular/ssr
```

### Configuração de Hidratação

```typescript
// app.config.ts
import { ApplicationConfig } from "@angular/core";

import {
provideClientHydration,

withEventReplay,
} from "@angular/platform-browser";

export const appConfig: ApplicationConfig = {

provideClientHydration(withEventReplay())],
};

``

### Hidratação Incremental (v20+)

```typescript
import { Component } from "@angular/core";

@Component({

selector: "app-page",

standalone: ​​true,

template: `

<app-hero />

@defer (hydrate on viewport) {
<app-comments />

}

@defer (hydrate on interaction) {

<app-chat-widget />

}
`,
})
export class PageComponent {}
```

### Gatilhos de Hidratação

| Gatilho | Quando usar |

| ---------------- | --------------------------------------- |

| `on idle` | Baixa prioridade, hidrata quando o navegador está ocioso |

| `on viewport` | Hidratar quando o elemento entra na área visível |

| `on interaction` | Hidratar na primeira interação do usuário |

| `on hover` | Hidratar quando o usuário passa o mouse sobre o elemento |

| `on timer(ms)` | Hidratar após um atraso especificado |

---

## 5. Padrões de Roteamento Modernos

### Guardas de Rota Funcionais

```typescript
// auth.guard.ts
import { inject } from "@angular/core";

import { Router, CanActivateFn } from "@angular/router";

import { AuthService } from "./auth.service";

export const authGuard: CanActivateFn = (route, state) => {

const auth = inject(AuthService);

const router = inject(Router);

if (auth.isAuthenticated()) {

return true;
}

return router.createUrlTree(["/login"], {
queryParams: { returnUrl: state.url },

});

};

// Uso em rotas
export const routes: Routes = [

{
path: "dashboard",

loadComponent: () => import("./dashboard.component"),

canActivate: [authGuard],

},
];

```

### Resolvedores de Dados em Nível de Rota

```typescript
import { inject } from '@angular/core';

import { ResolveFn } from '@angular/router';

import { UserService } from './user.service';

import { User } from './user.model';

export const userResolver: ResolveFn<User> = (route) => {

const userService = inject(UserService); return userService.getUser(route.paramMap.get('id')!);

};

// Nas rotas
{

path: 'user/:id',

loadComponent: () => import('./user.component'),

resolve: { user: userResolver }
}

// No componente
export class UserComponent {
private route = inject(ActivatedRoute);

user = toSignal(this.route.data.pipe(map(d => d['user'])));

}
```

---

## 6. Padrões de Injeção de Dependência

### Função inject() moderna

```typescript
import { Component, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { UserService } from './user.service';

@Component({...})
export class UserComponent {

// inject() moderno - sem necessidade de construtor

private http = inject(HttpClient);

private userService = inject(UserService);

// Funciona em qualquer contexto de injeção

users = toSignal(this.userService.getUsers());

}
```

### Tokens de Injeção para Configuração

```typescript
import { InjectionToken, inject } from "@angular/core";

// Define o token
export const API_BASE_URL = new InjectionToken<string>("API_BASE_URL");

// Fornecer na configuração
bootstrapApplication(AppComponent, {

providers: [{ provide: API_BASE_URL, useValue: "https://api.example.com" }],
});

// Injetar no serviço
@Injectable({ providedIn: "root" })
export class ApiService {

private baseUrl = inject(API_BASE_URL);

get(endpoint: string) {
return this.http.get(`${this.baseUrl}/${endpoint}`);
}
}
```

---

## 7. Composição e Reutilização de Componentes

### Projeção de Conteúdo (Slots)

```typescript
@Component({

selector: 'app-card',

template: `

<div class="card">

<div class="header">

<!-- Selecionar por atributo -->

<ng-content select="[card-header]"></ng-content>

</div>

<div class="body">

<!-- Slot padrão -->

<ng-content></ng-content>

</div>

</div>

`
})
export class CardComponent {}

// Uso
<app-card>

<h3 card-header>Título</h3>

<p>Conteúdo do corpo</p>

</app-card>
```

### Diretivas de Host (Composição)

```typescript
// Comportamentos reutilizáveis ​​sem herança
@Directive({
standalone: ​​true,

selector: '[appTooltip]',

inputs: ['tooltip'] // Alias ​​de entrada do Signal
})
export class TooltipDirective { ... }

@Component({
selector: 'app-button',

standalone: ​​true,

hostDirectives: [

{
directive: TooltipDirective,

inputs: ['tooltip: title'] // Entrada do Map

}

],

template: `<ng-content />`
})
export class ButtonComponent {}
```

---

## 8. Padrões de Gerenciamento de Estado

### Serviço de Estado Baseado em Signal

```typescript
import { Injectable, signal, computed } from "@angular/core";

interface AppState {

user: User | null;

theme: "light" | "dark";

notifications: Notification[];
}

@Injectable({ providedIn: "root" })
export class StateService {

// Sinais privados graváveis

private _user = signal<User | null>(null);

private _theme = signal<"light" | "dark">("light");

private _notifications = signal<Notification[]>([]);

// Valores computados públicos somente leitura

readonly user = computed(() => this._user());

readonly theme = computed(() => this._theme());

readonly notifications = computed(() => this._notifications());

readonly unreadCount = computed(

() => this._notifications().filter((n) => !n.read).length,

);

// Ações

setUser(user: User | null) {
this._user.set(user);
}

toggleTheme() {
this._theme.update((t) => (t === "light" ? "dark" : "light"));

}

addNotification(notification: Notification) {
this._notifications.update((n) => [...n, notification]);

}
}
```

### Padrão Component Store com Sinais

```typescript
import { Injectable, signal, computed, inject } from "@angular/core";

import { HttpClient } from "@angular/common/http";

import { toSignal } from "@angular/core/rxjs-interop";

@Injectable()
export class ProductStore {

private http = inject(HttpClient);

// Estado

private _products = signal<Product[]>([]);
private _loading = signal(false);

private _filter = signal("");

// Seletores

readonly products = computed(() => this._products());

readonly loading = computed(() => this._loading());

readonly filteredProducts = computed(() => {

const filter = this._filter().toLowerCase();

return this._products().filter((p) =>

p.name.toLowerCase().includes(filter),
);

});

// Ações

loadProducts() {
this._loading.set(true);
this.http.get<Product[]>("/api/products").subscribe({

next: (products) => {
this._products.set(products);

this._loading.set(false);

},

error: () => this._loading.set(false),

});

}

setFilter(filter: string) {
this._filter.set(filter);

}
}
```

---

## 9. Formulários com Sinais (Disponível na versão 22+)

### Formulários Reativos Atuais

```typescript
import { Component, inject } from "@angular/core";

import { FormBuilder, Validators, ReactiveFormsModule } from "@angular/forms";

@Component({

selector: "app-user-form",

standalone: ​​true,

imports: [ReactiveFormsModule],

template: `

<form [formGroup]="form" (ngSubmit)="onSubmit()">

<input formControlName="name" placeholder="Nome" />

<input formControlName="email" type="email" placeholder="Email" />

<button [disabled]="form.invalid">Enviar</button>

</form>

`,
})
export class UserFormComponent {

private fb = inject(FormBuilder);

form = this.fb.group({

name: ["", Validators.required],

email: ["", [Validators.required, Validators.email]],

});

onSubmit() {

if (this.form.valid) {
console.log(this.form.value);

}
}
}
```

### Padrões de Formulário com Reconhecimento de Sinal (Prévia)

```typescript
// Futura API de Formulários Signal (experimental)
import { Component, signal } from '@angular/core';

@Component({...})
export class SignalFormComponent {

name = signal('');

email = signal('');

// Validação computada

isValid = computed(() =>

this.name().length > 0 &&

this.email().includes('@')

);

submit() {
if (this.isValid()) {
console.log({ name: this.name(), email: this.email() });
}

}
}
```

---

## 10. Otimização de Desempenho

### Estratégias de Detecção de Mudanças

```typescript
@Component({

changeDetection: ChangeDetectionStrategy.OnPush,

// Verifica apenas quando:

// 1. O sinal/referência de entrada muda
// 2. O manipulador de eventos é executado
// 3. O pipe assíncrono emite
// 4. O valor do sinal muda
})
```

### Blocos Defer para Carregamento Lento

```typescript
@Component({

template: `

<!-- Carregamento imediato -->

<app-header />

<!-- Carregamento lento quando visível -->

@defer (on viewport) {

<app-heavy-chart />

} @placeholder {

<div class="skeleton" />

} @loading (minimum 200ms) {
<app-spinner />

} @error {

<p>Falha ao carregar o gráfico</p>

}

`
})
```

### NgOptimizedImage

```typescript
import { NgOptimizedImage } from '@angular/common';

@Component({

imports: [NgOptimizedImage],

template: `

<img

ngSrc="hero.jpg"

width="800"

height="600"

priority

/>

<img

ngSrc="thumbnail.jpg"

width="200"

height="150"

loading="lazy"

placeholder="blur"

/>

`
})

```

---

## 11. Testando o Angular Moderno

### Testando Componentes de Sinalização

```typescript
import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CounterComponent } from "./counter.component";

describe("CounterComponent", () => {

let component: CounterComponent;

let fixture: ComponentFixture<CounterComponent>;

beforeEach(async () => {

await TestBed.configureTestingModule({

imports: [CounterComponent], // Importação independente
}).compileComponents();

fixture = TestBed.createComponent(CounterComponent);

component = fixture.componentInstance;

fixture.detectChanges();

});

it("deve incrementar a contagem", () => {
expect(component.count()).toBe(0);

component.increment();

expect(component.count()).toBe(1);

});

it("deve atualizar o DOM ao sinalizar a mudança", () => {
component.count.set(5);

fixture.detectChanges();

const el = fixture.nativeElement.querySelector(".count");

expect(el.textContent).toContain("5");

});
});
```

### Testando com Entradas de Sinal

```typescript
import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ComponentRef } from "@angular/core";

import { UserCardComponent } from "./user-card.component";

describe("UserCardComponent", () => {

let fixture: ComponentFixture<UserCardComponent>;

let componentRef: ComponentRef<UserCardComponent>;

beforeEach(async () => {

await TestBed.configureTestingModule({

imports: [UserCardComponent],

}).compileComponents();

fixture = TestBed.createComponent(UserCardComponent);

componentRef = fixture.componentRef;

// Define as entradas de sinal via setInput

componentRef.setInput("id", "123");
componentRef.setInput("name", "John Doe");

fixture.detectChanges();

});

it("deve exibir o nome do usuário", () => {

const el = fixture.nativeElement.querySelector("h3");

expect(el.textContent).toContain("John Doe");

});
});
```

---

## Resumo das Melhores Práticas

| Padrão | ✅ Fazer | ❌ Não fazer |
| -------------------- | ------------------------------ | ------------------------------- |
| **Estado** | Usar sinais para estado local | Usar RxJS em excesso para estado simples |
| **Componentes** | Independentes com importações diretas | Módulos compartilhados inchados |
| **Detecção de Mudanças** | OnPush + Sinais | Detecção de Mudanças padrão em todos os lugares |
| **Carregamento Preguiçoso** | `@defer` e `loadComponent` | Carregamento imediato de tudo |
| **Injeção de Dependência** | Função `inject()` | Injeção de construtor (verbose) |
| **Entradas** | Função de sinal `input()` | Decorador `@Input()` (legado) |
| **Sem Zonas** | Habilitar para novos projetos | Forçar em projetos legados sem testes |

---

## Recursos

- [Documentação do Angular.dev](https://angular.dev)
- [Guia de Sinais do Angular](https://angular.dev/guide/signals)
- [Guia de SSR do Angular](https://angular.dev/guide/ssr)
- [Guia de Atualização do Angular](https://angular.dev/update-guide)
- [Blog do Angular](https://blog.angular.dev)

---

## Solução de Problemas Comuns

| Problema | Solução |

| ------------------------------ | --------------------------------------------------- |

| Sinal não atualiza a interface do usuário | Certifique-se de usar `OnPush` e chamar o sinal como função `count()` |

| Incompatibilidade de hidratação | Verifique a consistência do conteúdo entre servidor e cliente |

| Dependência circular | Use `inject()` com `forwardRef` |

| Zoneless não detecta alterações | Acione por meio de atualizações de sinal, não mutações |
| A busca SSR falha | Use `TransferState` ou `withFetch()` |