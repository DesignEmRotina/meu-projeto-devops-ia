---
nome: depuração_sistemática
descrição: Metodologia sistemática de depuração em 4 fases, com análise de causa raiz e verificação baseada em evidências. Use ao depurar problemas complexos.
ferramentas-permitidas: Ler, Glob, Grep
---

# Depuração Sistemática

> Fonte: obra/superpowers

## Visão Geral
Esta habilidade fornece uma abordagem estruturada para depuração que evita tentativas aleatórias e garante que os problemas sejam corretamente compreendidos antes de serem resolvidos.

## Processo de Depuração em 4 Fases

### Fase 1: Reproduzir
Antes de corrigir, reproduza o problema de forma confiável.

## Etapas de Reprodução
1. [Passo exato para reproduzir]
2. [Próximo passo]
3. [Resultado esperado vs resultado atual]

## Taxa de Reprodução
- [ ] Sempre (100%)
- [ ] Frequentemente (50–90%)
- [ ] Às vezes (10–50%)
- [ ] Raramente (<10%)


### Fase 2: Isolar

Reduza o escopo para identificar a origem do problema.


## Perguntas de Isolamento
- Quando isso começou a acontecer?
- O que mudou recentemente?
- Acontece em todos os ambientes?
- Conseguimos reproduzir com código mínimo?
- Qual é a menor mudança que dispara o problema?


### Fase 3: Entender

Encontre a causa raiz, não apenas os sintomas.


## Análise de Causa Raiz
### Os 5 Porquês
1. Por quê: [Primeira observação]
2. Por quê: [Motivo mais profundo]
3. Por quê: [Ainda mais profundo]
4. Por quê: [Chegando perto]
5. Por quê: [Causa raiz]


### Fase 4: Corrigir e Verificar

Corrija o problema e verifique se ele foi realmente resolvido.

## Verificação da Correção
- [ ] O bug não ocorre mais
- [ ] Funcionalidades relacionadas continuam funcionando
- [ ] Nenhum novo problema foi introduzido
- [ ] Teste adicionado para evitar regressão


## Checklist de Depuração


## Antes de Começar
- [ ] Consegue reproduzir de forma consistente
- [ ] Possui um caso mínimo de reprodução
- [ ] Entende o comportamento esperado

## Durante a Investigação
- [ ] Verificar mudanças recentes (git log)
- [ ] Verificar logs em busca de erros
- [ ] Adicionar logs se necessário
- [ ] Usar debugger / breakpoints

## Após a Correção
- [ ] Causa raiz documentada
- [ ] Correção verificada
- [ ] Teste de regressão adicionado
- [ ] Código similar revisado


## Comandos Comuns de Depuração


# Mudanças recentes
git log --oneline -20
git diff HEAD~5

# Buscar por padrão específico
grep -r "errorPattern" --include="*.ts"

# Verificar logs
pm2 logs app-name --err --lines 100


## Anti-Padrões

❌ **Mudanças aleatórias** – "Talvez se eu mudar isso..."
❌ **Ignorar evidências** – "Isso não pode ser a causa"
❌ **Suposições** – "Deve ser X" sem prova
❌ **Não reproduzir antes** – Corrigir no escuro
❌ **Parar nos sintomas** – Não encontrar a causa raiz

