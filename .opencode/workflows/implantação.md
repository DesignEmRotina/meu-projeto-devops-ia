---
descrição: Comando de implantação para releases em produção. Executa verificações prévias e o processo de implantação.
---
```

# /implantação – Deploy em Produção

$ARGUMENTS

---

## Objetivo

Este comando gerencia o deploy em produção, incluindo **checagens prévias (pre-flight)**, execução do deploy e verificação pós-implantação.

---

## Subcomandos

```
/implantação                - Assistente interativo de deploy
/implantação checagens      - Executa apenas as verificações pré-deploy
/implantação pré-visualizar - Deploy em ambiente de preview/staging
/implantação produção       - Deploy em produção
/implantação reversão       - Retorna para a versão anterior
```

---

## Checklist Pré-Deploy

Antes de qualquer deploy:

```markdown
## 🚀 Checklist Pré-Deploy

### Qualidade de Código
- [ ] Sem erros de TypeScript (`npx tsc --noEmit`)
- [ ] ESLint passando (`npx eslint .`)
- [ ] Todos os testes passando (`npm test`)

### Segurança
- [ ] Nenhum segredo hardcoded
- [ ] Variáveis de ambiente documentadas
- [ ] Dependências auditadas (`npm audit`)

### Performance
- [ ] Tamanho do bundle aceitável
- [ ] Nenhum `console.log` esquecido
- [ ] Imagens otimizadas

### Documentação
- [ ] README atualizado
- [ ] CHANGELOG atualizado
- [ ] Documentação da API em dia

### Pronto para fazer deploy? (s/n)
```

---

## Fluxo de Deploy

```
┌─────────────────┐
│  /implantação   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Checagens      │
│  prévias        │
└────────┬────────┘
         │
   Passou? ──Não──► Corrigir problemas
         │
        Sim
         │
         ▼
┌─────────────────┐
│  Build da       │
│  aplicação      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Deploy na      │
│  plataforma     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Health check   │
│  & verificação  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ✅ Concluído   │
└─────────────────┘
```

---

## Formato de Saída

### Deploy Bem-sucedido

```markdown
## 🚀 Deploy Concluído

### Resumo
- **Versão:** v1.2.3
- **Ambiente:** produção
- **Duração:** 47 segundos
- **Plataforma:** Vercel

### URLs
- 🌐 Produção: https://app.example.com
- 📊 Dashboard: https://vercel.com/project

### O que mudou
- Adicionada funcionalidade de perfil de usuário
- Corrigido bug de login
- Dependências atualizadas

### Health Check
✅ API respondendo (200 OK)
✅ Banco de dados conectado
✅ Todos os serviços saudáveis
```

### Deploy com Falha

```markdown
## ❌ Falha no Deploy

### Erro
Build falhou na etapa: compilação TypeScript

### Detalhes
```

error TS2345: Argument of type 'string' is not assignable...

```

### Resolução
1. Corrigir erro de TypeScript em `src/services/user.ts:45`
2. Executar `npm run build` localmente para validar
3. Tentar `/implantação` novamente

### Rollback Disponível
Versão anterior (v1.2.2) ainda está ativa.
Execute `/implantação reversão` se necessário.
```

---

## Suporte a Plataformas

| Plataforma | Comando                | Observações                            |
| ---------- | ---------------------- | -------------------------------------- |
| Vercel     | `vercel --prod`        | Detectado automaticamente para Next.js |
| Railway    | `railway up`           | Requer Railway CLI                     |
| Fly.io     | `fly deploy`           | Requer flyctl                          |
| Docker     | `docker compose up -d` | Para ambientes self-hosted             |

---

## Exemplos

```
/implantação
/deploy verificação
/deploy visualização
/deploy produção --skip-tests
/deploy reversão
```
