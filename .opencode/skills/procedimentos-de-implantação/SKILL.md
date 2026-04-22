---
name: procedimentos-de-implantação
description: "Princípios e tomada de decisão para implantação em produção. Fluxos de trabalho de implantação seguros, estratégias de reversão e verificação. Ensina a pensar, não a memorizar scripts."
risk: crítico
source: comunidade
date_add: "27/02/2026"
---

# Procedimentos de Implantação

> Princípios e tomada de decisão para implantações seguras em produção.

> **Aprenda a PENSAR, não a memorizar scripts.**

---

## ⚠️ Como usar esta habilidade

Esta habilidade ensina **princípios de implantação**, não scripts bash para copiar.

- Cada implantação é única
- Entenda o PORQUÊ por trás de cada etapa
- Adapte os procedimentos à sua plataforma

---

## 1. Seleção da Plataforma

### Árvore de Decisão

```
O que você está implantando?
│
├── Site estático / JAMstack
│ └── Vercel, Netlify, Cloudflare Pages
│
├── Aplicativo web simples
│ ├── Gerenciado → Railway, Render, Fly.io
│ └── Controle → VPS + PM2/Docker
│
├── Microsserviços
│ └── Orquestração de contêineres
│
└── Serverless
└── Funções de borda, Lambda
```

### Cada plataforma tem procedimentos diferentes

| Plataforma | Método de implantação |

|----------|------------------|

| **Vercel/Netlify** | Git push, implantação automática |

| **Railway/Render** | Git push ou CLI |

| **VPS + PM2** | SSH + etapas manuais |

| **Docker** | Envio de imagem + orquestração |

| **Kubernetes** | kubectl apply |

---

## 2. Princípios de Pré-Implantação

### As 4 Categorias de Verificação

| Categoria | O que verificar |

|----------|--------------|

| **Qualidade do Código** | Testes aprovados, linting limpo, revisado |

| **Build** | Build de produção funcionando, sem avisos |

| **Ambiente** | Variáveis ​​de ambiente definidas, segredos atualizados |

| **Segurança** | Backup realizado, plano de rollback pronto |

### Lista de Verificação de Pré-Implantação

- [ ] Todos os testes aprovados
- [ ] Código revisado e aprovado
- [ ] Build de produção concluído com sucesso
- [ ] Variáveis ​​de ambiente verificadas
- [ ] Migrações de banco de dados prontas (se houver)
- [ ] Plano de reversão documentado
- [ ] Equipe notificada
- [ ] Monitoramento pronto

---

## 3. Princípios do Fluxo de Trabalho de Implantação

### O Processo de 5 Fases

```
1. PREPARAR

└── Verificar código, build e variáveis ​​de ambiente

2. BACKUP

└── Salvar o estado atual antes de fazer alterações

3. IMPLANTAR

└── Executar com o monitoramento aberto

4. VERIFICAR

└── Verificação de integridade, logs e fluxos principais

5. CONFIRMAR ou REVERTER

└── Tudo certo? Confirme. Problemas? Reversão.

```

### Princípios da Fase

| Fase | Princípio |

|-------|-----------|

| **Preparar** | Nunca implante código não testado |

| **Backup** | Não é possível reverter sem backup |

| **Implantar** | Observe o processo, não se afaste |

| **Verificar** | Confie, mas verifique |

| **Confirmar** | Tenha o gatilho de reversão pronto |

---

## 4. Verificação Pós-Implantação

### O que Verificar

| Verificar | Por quê |

|-------|-----|

| **Endpoint de integridade** | O serviço está em execução |

| **Logs de erro** | Nenhum erro novo |

| **Fluxos de usuário principais** | Recursos críticos funcionam |

| **Desempenho** | Tempos de resposta aceitáveis ​​|

Janela de verificação

- **Primeiros 5 minutos**: Monitoramento ativo
- **15 minutos**: Confirmação de estabilidade
- **1 hora**: Verificação final
- **No dia seguinte**: Revisão das métricas

---

## 5. Princípios de Rollback

### Quando usar o Rollback

| Sintoma | Ação |

|---------|--------|

| Serviço inativo | Rollback imediato |

| Erros críticos | Rollback |

| Desempenho >50% degradado | Considerar rollback |

| Problemas menores | Corrigir rapidamente |

### Estratégia de Rollback por Plataforma

| Plataforma | Método de Rollback |

|----------|----------------|

| **Vercel/Netlify** | Reimplementar commit anterior |

| **Railway/Render** | Rollback no painel de controle |

| **VPS + PM2** | Restaurar backup, reiniciar |

| **Docker** | Tag da imagem anterior |

| **K8s** | kubectl rollout undo |

### Princípios de Rollback

1. **Velocidade acima da perfeição**: Reverter primeiro, depurar depois
2. **Não acumule erros**: Um rollback, não múltiplas alterações
3. **Comunicar**: Informar a equipe sobre o ocorrido
4. **Análise pós-incidente**: Entender o motivo após a estabilização

---

## 6. Implantação sem tempo de inatividade

### Estratégias

| Estratégia | Como funciona |

|----------|--------------|

| **Rolling** | Substituir instâncias uma a uma |

| **Blue-Green** | Alternar o tráfego entre ambientes |

| **Canary** | Mudança gradual de tráfego |

### Princípios de seleção

| Cenário | Estratégia |

|----------|----------|

| Liberação padrão | Rolling |

| Alteração de alto risco | Blue-green (rollback fácil) |

| Necessita de validação | Canary (teste com tráfego real) |

---

## 7. Procedimentos de Emergência

### Prioridade para Serviço Indisponível

1. **Avaliar**: Qual o sintoma?

2. **Solução rápida**: Reiniciar se não estiver claro
3. **Reverter**: Se a reinicialização não resolver o problema
4. **Investigar**: Após estabilização

### Ordem de Investigação

| Verificar | Problemas Comuns |

|-------|--------------|

| **Logs** | Erros, exceções |

| **Recursos** | Disco cheio, memória |

| **Rede** | DNS, firewall |

| **Dependências** | Banco de dados, APIs |

---

## 8. Antipadrões

| ❌ Não faça | ✅ Faça |

|----------|-------|

| Implantar na sexta-feira | Implantar no início da semana |

| Implantação apressada | Seguir o processo |

| Ignorar o ambiente de teste | Sempre testar primeiro | | Implantar sem backup | Fazer backup antes da implantação |

| Afastar-se após a implantação | Monitorar por mais de 15 minutos |

| Várias alterações simultâneas | Uma alteração por vez |

---

## 9. Lista de Verificação de Decisão

Antes da implantação:

- [ ] **Procedimento adequado à plataforma?**
- [ ] **Estratégia de backup pronta?**
- [ ] **Plano de reversão documentado?**
- [ ] **Monitoramento configurado?**
- [ ] **Equipe notificada?**
- [ ] **Horário para monitorar depois?**

---

## 10. Melhores Práticas

1. **Implantações pequenas e frequentes** em vez de grandes lançamentos
2. **Sinalizadores de recursos** para alterações de risco
3. **Automatize** etapas repetitivas
4. **Documente** cada implantação
5. **Revise** o que deu errado após os problemas
6. **Teste a reversão** antes de precisar dela

---

> **Lembre-se:** Toda implantação é um risco. Minimize o risco por meio da preparação, não da velocidade.

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.

## Limitações
- Use esta habilidade somente quando a tarefa corresponder claramente ao escopo descrito acima.

- Não considere a saída como um substituto para validação, testes ou revisão especializada específicos do ambiente.

- Pare e peça esclarecimentos se faltarem entradas, permissões, limites de segurança ou critérios de sucesso necessários.

