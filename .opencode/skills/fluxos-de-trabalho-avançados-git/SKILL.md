--- 
name: fluxos-de-trabalho-avançados-git
description: "Domine técnicas avançadas do Git para manter um histórico limpo, colaborar de forma eficaz e se recuperar de qualquer situação com confiança."
risk: crítico
source: comunidade
date_add: "27/02/2026"
---

# Fluxos de Trabalho Avançados do Git

Domine técnicas avançadas do Git para manter um histórico limpo, colaborar de forma eficaz e se recuperar de qualquer situação com confiança.

## Não use esta habilidade quando

- A tarefa não estiver relacionada a fluxos de trabalho avançados do Git
- Você precisar de um domínio ou ferramenta diferente fora deste escopo

## Instruções

- Esclareça os objetivos, restrições e entradas necessárias.

- Aplique as melhores práticas relevantes e valide os resultados.

- Forneça etapas práticas e verificação.

- Se forem necessários exemplos detalhados, abra `resources/implementation-playbook.md`.

## Use esta habilidade quando:

- Limpar o histórico de commits antes de mesclar
- Aplicar commits específicos em diferentes branches
- Encontrar commits que introduziram bugs
- Trabalhar em múltiplas funcionalidades simultaneamente
- Recuperar erros do Git ou commits perdidos
- Gerenciar fluxos de trabalho complexos de branches
- Preparar PRs limpos para revisão
- Sincronizar branches divergentes

## Conceitos Básicos

### 1. Rebase Interativo

O rebase interativo é o canivete suíço da edição do histórico do Git.

**Operações Comuns:**
- `pick`: Mantém o commit como está
- `reword`: Altera a mensagem do commit
- `edit`: Modifica o conteúdo do commit
- `squash`: Combina com o commit anterior
- `fixup`: Semelhante ao squash, mas descarta a mensagem
- `drop`: Remove o commit completamente

**Uso Básico:**
```bash
# Rebase dos últimos 5 commits
git rebase -i HEAD~5

# Rebase de todos os commits na branch atual
git rebase -i $(git merge-base HEAD main)

# Rebase em um commit específico
git rebase -i abc123
```

### 2. Cherry-Picking

Aplica commits específicos de uma branch a outra sem mesclar branches inteiras.

```bash
# Selecionar commit único
git cherry-pick abc123

# Selecionar intervalo de commits (início exclusivo)
git cherry-pick abc123..def456

# Selecionar sem commitar (apenas alterações de estágio)
git cherry-pick -n abc123

# Selecionar e editar a mensagem do commit
git cherry-pick -e abc123
```

### 3. Git Bisect

Busca binária no histórico de commits para encontrar o commit que introduziu um bug.

```bash
# Iniciar busca binária
git bisect start

# Marcar o commit atual como ruim
git bisect bad

# Marcar o commit bom conhecido
git bisect good v1.0.0

# O Git fará o checkout do commit intermediário - teste-o
# Em seguida, marque-o como bom ou ruim
git bisect good # ou: git bisect bad

# Continuar até encontrar um bug
# Ao terminar
git bisect reset
```

**Busca binária automatizada:**
```bash
# Usar script para testar automaticamente
git bisect start HEAD v1.0.0
git bisect run ./test.sh

# test.sh deve retornar 0 para bom, 1-127 (exceto 125) para ruim
```

### 4. Árvores de trabalho

Trabalhar em vários branches simultaneamente sem stashing ou troca de branches.

```bash
# Listar árvores de trabalho existentes
git worktree list

# Adicionar nova árvore de trabalho para branch de recurso
git worktree add ../project-feature feature/new-feature

# Adicionar árvore de trabalho e criar nova branch
git worktree add -b bugfix/urgent ../project-hotfix main

# Remover árvore de trabalho
git worktree remove ../project-feature

# Remover árvores de trabalho obsoletas
git worktree prune
```

### 5. Reflog

Sua rede de segurança - rastreia todas as movimentações de referências, inclusive commits excluídos.

```bash
# Visualizar reflog
git reflog

# Visualizar reflog para um branch específico
git reflog show feature/branch

# Restaurar commit excluído
git reflog
# Encontrar o hash do commit
git checkout abc123
git branch recovered-branch

# Restaurar branch excluído
git reflog
git branch deleted-branch abc123
```

## Fluxos de Trabalho Práticos

### Fluxo de Trabalho 1: Limpar o Branch de Funcionalidade Antes do PR

```bash
# Começar com o branch de funcionalidade
git checkout feature/user-auth

# Rebase interativo para limpar o histórico
git rebase -i main

# Exemplos de operações de rebase:
# - Squash commits de "correção de erro de digitação"
# - Reescrever mensagens de commit para maior clareza
# - Reordenar commits logicamente
# - Remover commits desnecessários

# Forçar push do branch limpo (seguro se ninguém mais estiver usando)
git push --force-with-lease origin feature/user-auth
```

### Fluxo de Trabalho 2: Aplicar Correção em várias versões

```bash
# Criar correção na branch principal
git checkout main
git commit -m "correção: patch de segurança crítico"

# Aplicar às branches de lançamento
git checkout release/2.0
git cherry-pick abc123

git checkout release/1.9
git cherry-pick abc123

# Lidar com conflitos, se houver
git cherry-pick --continue
# ou
git cherry-pick --abort
```

### Fluxo de Trabalho 3: Introdução à Busca de Bugs

```bash
# Iniciar busca binária
git bisect start
git bisect bad HEAD
git bisect good v2.1.0

# O Git verifica o commit intermediário - executar testes
npm test

# Se os testes falharem
git bisect bad

# Se os testes passarem
git bisect good

# O Git verificará automaticamente o próximo commit para teste
# Repita até encontrar um bug

# Versão automatizada
git bisect start HEAD v2.1.0
git bisect run npm test
```

### Fluxo de Trabalho 4: Desenvolvimento com Múltiplas Branches

```bash
# Diretório principal do projeto
cd ~/projects/myapp

# Criar árvore de trabalho para correção de bugs urgentes
git worktree add ../myapp-hotfix hotfix/critical-bug

# Trabalhar na correção em um diretório separado
cd ../myapp-hotfix
# Fazer alterações, commit
git commit -m "Correção: resolve bug crítico"
git push origin hotfix/critical-bug

# Retornar ao trabalho principal sem interrupção
cd ~/projects/myapp
git fetch origin
git cherry-pick hotfix/critical-bug

# Limpar ao terminar
git worktree remove ../myapp-hotfix
```

### Fluxo de trabalho 5: Recuperar de erros

```bash
# Reiniciou acidentalmente para o commit errado
git reset --hard HEAD~5 # Oh não!

# Use o reflog para encontrar commits perdidos
git reflog
# A saída mostra:
# abc123 HEAD@{0}: reset: movendo para HEAD~5
# def456 HEAD@{1}: commit: minhas alterações importantes

# Recupere commits perdidos
git reset --hard def456

# Ou crie um branch a partir do commit perdido
git branch recovery def456
```

## Técnicas Avançadas

### Estratégia de Rebase vs. Merge

**Quando usar Rebase:**
- Limpar commits locais antes de enviar as alterações
- Manter o branch de recurso atualizado com o principal
- Criar um histórico linear para facilitar a revisão

**Quando usar Merge:**
- Integrar recursos concluídos ao principal
- Preservar o histórico exato de colaboração
- Branches públicos usados ​​por outros

```bash
# Atualize o branch de recurso com as alterações do principal (rebase)
git checkout feature/my-feature
git fetch origin
git rebase origin/main

# Lide com conflitos
git status
# Corrija conflitos em arquivos
git add .

git rebase --continue

# Ou faça um merge em vez disso
git merge origin/main
```

### Fluxo de Trabalho de Autosquash

Combine automaticamente os commits de correção durante o rebase.

``bash
# Faça o commit inicial
git commit -m "feat: adicionar autenticação de usuário"

# Mais tarde, corrija algo nesse commit
# Prepare as alterações
git commit --fixup HEAD # ou especifique o hash do commit

# Faça mais alterações
git commit --fixup abc123

# Rebase com autosquash
git rebase -i --autosquash main

# O Git marca automaticamente os commits de correção
```

### Commit Dividido

Divida um commit em vários commits lógicos.

```bash
# Iniciar rebase interativo
git rebase -i HEAD~3

# Marcar commit para dividir com 'edit'
# O Git irá parar neste commit

# Redefinir commit, mas manter as alterações
git reset HEAD^

# Preparar e confirmar em partes lógicas
git add file1.py
git commit -m "feat: adicionar validação"

git add file2.py
git commit -m "feat: adicionar tratamento de erros"

# Continuar rebase
git rebase --continue
```

### Seleção Parcial de Arquivos

Selecionar apenas arquivos específicos de um commit.

```bash
# Exibir arquivos no commit
git show --name-only abc123

# Fazer checkout de arquivos específicos do commit
git checkout abc123 --path/to/file1.py path/to/file2.py

# Preparar e fazer commit
git commit -m "cherry-pick: aplicar alterações específicas de abc123"
```

## Boas Práticas

1. **Sempre use --force-with-lease**: Mais seguro que --force, evita sobrescrever o trabalho de outros
2. **Rebase somente commits locais**: Não faça rebase de commits que já foram enviados e compartilhados
3. **Mensagens de commit descritivas**: Seu eu do futuro agradecerá ao seu eu do presente
4. **Commits atômicos**: Cada commit deve ser uma única alteração lógica
5. **Teste antes de enviar com força**: Certifique-se de que a reescrita do histórico não quebrou nada
6. **Mantenha o Reflog em dia**: Lembre-se de que o reflog é sua rede de segurança por 90 dias
7. **Crie um branch antes de operações arriscadas**: Criar branch de backup antes de rebases complexos

```bash
# Push forçado seguro
git push --force-with-lease origin feature/branch

# Criar backup antes de operações arriscadas
git branch backup-branch
git rebase -i main
# Se algo der errado
git reset --hard backup-branch
```

## Armadilhas comuns

- **Rebase em branches públicas**: Causa conflitos de histórico para colaboradores
- **Push forçado sem lease**: Pode sobrescrever o trabalho de um colega
- **Perda de trabalho em rebase**: Resolva conflitos com cuidado, teste após o rebase
- **Esquecer a limpeza da worktree**: Worktrees órfãs consomem espaço em disco
- **Não fazer backup antes de experimentar**: Sempre crie uma branch de segurança
- **Bissecção em diretório de trabalho sujo**: Faça commit ou stash antes da bissecção

## Comandos de recuperação

```bash
# Abortar operações em andamento
git rebase --abort
git merge --abort
git cherry-pick --abortar
git bisect reset

# Restaurar arquivo para a versão de um commit específico
git restore --source=abc123 caminho/para/arquivo

# Desfazer o último commit, mas manter as alterações
git reset --soft HEAD^

# Desfazer o último commit e descartar as alterações
git reset --hard HEAD^

# Recuperar branch excluída (dentro de 90 dias)
git reflog
git branch branch-recuperada abc123
```

## Recursos

- **references/git-rebase-guide.md**: Análise detalhada do rebase interativo
- **references/git-conflict-resolution.md**: Estratégias avançadas de resolução de conflitos
- **references/git-history-rewriting.md**: Reescrevendo o histórico do Git com segurança
- **assets/git-workflow-checklist.md**: Lista de verificação para limpeza pré-PR
- **assets/git-aliases.md**: Aliases Git úteis para fluxos de trabalho avançados
- **scripts/git-clean-branches.sh**: Limpa branches mescladas e obsoletas
