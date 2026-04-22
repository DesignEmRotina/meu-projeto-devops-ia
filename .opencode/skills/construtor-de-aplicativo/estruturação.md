# Scaffolding de Projeto

> Estrutura de diretórios e arquivos centrais para novos projetos.

---

## Estrutura Full-Stack Next.js (Otimizada para 2025)

```
project-name/
├── src/
│   ├── app/                        # Apenas rotas (camada fina)
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── globals.css
│   │   ├── (auth)/                 # Grupo de rotas – páginas de autenticação
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   ├── (dashboard)/            # Grupo de rotas – layout do dashboard
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   └── api/
│   │       └── [resource]/route.ts
│   │
│   ├── features/                   # Módulos organizados por feature
│   │   ├── auth/
│   │   │   ├── components/
│   │   │   ├── hooks/
│   │   │   ├── actions.ts          # Server Actions
│   │   │   ├── queries.ts          # Busca de dados
│   │   │   └── types.ts
│   │   ├── products/
│   │   │   ├── components/
│   │   │   ├── actions.ts
│   │   │   └── queries.ts
│   │   └── cart/
│   │       └── ...
│   │
│   ├── shared/                     # Utilitários compartilhados
│   │   ├── components/ui/          # Componentes de UI reutilizáveis
│   │   ├── lib/                    # Utils, helpers
│   │   └── hooks/                  # Hooks globais
│   │
│   └── server/                     # Código exclusivo do servidor
│       ├── db/                     # Cliente de banco de dados (Prisma)
│       ├── auth/                   # Configuração de autenticação
│       └── services/               # Integrações com APIs externas
│
├── prisma/
│   ├── schema.prisma
│   ├── migrations/
│   └── seed.ts
│
├── public/
├── .env.example
├── .env.local
├── package.json
├── tailwind.config.ts
├── tsconfig.json
└── README.md
```

---

## Princípios da Estrutura

| Princípio                   | Implementação                                                                    |
| --------------------------- | -------------------------------------------------------------------------------- |
| **Isolamento por feature**  | Cada feature em `features/` com seus próprios componentes, hooks e actions       |
| **Separação Server/Client** | Código exclusivo do servidor em `server/`, evitando imports acidentais no client |
| **Rotas enxutas**           | `app/` usado apenas para roteamento, lógica fica em `features/`                  |
| **Grupos de rotas**         | `(groupName)/` para compartilhamento de layout sem impactar a URL                |
| **Código compartilhado**    | `shared/` para UI e utilitários realmente reutilizáveis                          |

---

## Arquivos Centrais

| Arquivo                | Finalidade                                       |
| ---------------------- | ------------------------------------------------ |
| `package.json`         | Dependências do projeto                          |
| `tsconfig.json`        | TypeScript + aliases de caminho (`@/features/*`) |
| `tailwind.config.ts`   | Configuração do Tailwind                         |
| `.env.example`         | Template de variáveis de ambiente                |
| `README.md`            | Documentação do projeto                          |
| `.gitignore`           | Regras de ignorar arquivos no Git                |
| `prisma/schema.prisma` | Esquema do banco de dados                        |

---

## Aliases de Caminho (tsconfig.json)

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"],
      "@/features/*": ["./src/features/*"],
      "@/shared/*": ["./src/shared/*"],
      "@/server/*": ["./src/server/*"]
    }
  }
}
```

---

## Quando Usar Cada Local

| Necessidade              | Local                         |
| ------------------------ | ----------------------------- |
| Nova página/rota         | `app/(group)/page.tsx`        |
| Componente de feature    | `features/[name]/components/` |
| Server Action            | `features/[name]/actions.ts`  |
| Busca de dados           | `features/[name]/queries.ts`  |
| Botão/Input reutilizável | `shared/components/ui/`       |
| Query de banco de dados  | `server/db/`                  |
| Chamada para API externa | `server/services/`            |
