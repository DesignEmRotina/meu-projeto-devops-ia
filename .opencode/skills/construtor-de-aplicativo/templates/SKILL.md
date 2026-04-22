nome: templates
descrição: Templates de scaffolding de projetos para novas aplicações. Use ao criar novos projetos do zero. Contém 12 templates para diferentes stacks tecnológicas.
ferramentas-permitidas: Ler, Glob, Grep
---
```

# Templates de Projeto

> Templates de início rápido para estruturar novos projetos.

---

## 🎯 Regra de Leitura Seletiva

**Leia APENAS o template correspondente ao tipo de projeto do usuário!**

| Template                                             | Stack Tecnológica   | Quando Usar              |
| ---------------------------------------------------- | ------------------- | ------------------------ |
| [nextjs-fullstack](nextjs-fullstack/TEMPLATE.md)     | Next.js + Prisma    | Aplicação web full-stack |
| [nextjs-saas](nextjs-saas/TEMPLATE.md)               | Next.js + Stripe    | Produto SaaS             |
| [nextjs-static](nextjs-static/TEMPLATE.md)           | Next.js + Framer    | Landing page             |
| [express-api](express-api/TEMPLATE.md)               | Express + JWT       | API REST                 |
| [python-fastapi](python-fastapi/TEMPLATE.md)         | FastAPI             | API em Python            |
| [react-native-app](react-native-app/TEMPLATE.md)     | Expo + Zustand      | App mobile               |
| [flutter-app](flutter-app/TEMPLATE.md)               | Flutter + Riverpod  | Multiplataforma          |
| [electron-desktop](electron-desktop/TEMPLATE.md)     | Electron + React    | App desktop              |
| [chrome-extension](chrome-extension/TEMPLATE.md)     | Chrome MV3          | Extensão de navegador    |
| [cli-tool](cli-tool/TEMPLATE.md)                     | Node.js + Commander | Ferramenta CLI           |
| [monorepo-turborepo](monorepo-turborepo/TEMPLATE.md) | Turborepo + pnpm    | Monorepo                 |
| [astro-static](astro-static/TEMPLATE.md)             | Astro + MDX         | Blog / Documentação      |

---

## Uso

1. O usuário diz: **"criar app do tipo [X]"**
2. Associar ao template apropriado
3. Ler **APENAS** o arquivo `TEMPLATE.md` desse template
4. Seguir rigorosamente a stack e a estrutura definidas

