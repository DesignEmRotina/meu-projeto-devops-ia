# Manual de Orquestração de Sagas

## Quando escolher orquestração versus coreografia

- Escolha orquestração quando a visibilidade do fluxo de negócios e o controle centralizado forem necessários.

- Escolha coreografia quando a autonomia for alta e o acoplamento for baixo.

## Lista de verificação para design de sagas

- Defina uma máquina de estados explícita para a saga.

- Defina uma política de tempo limite por etapa.

- Defina uma ação de compensação para cada etapa irreversível.

- Use chaves de idempotência para o tratamento de comandos.

- Armazene IDs de correlação em todos os eventos e logs.

## Tratamento de falhas

- Tente novamente falhas transitórias com recuo exponencial limitado.

- Eleve falhas irrecuperáveis ​​para o estado de compensação.

- Capture o motivo da falha visível ao operador e a etapa atual.

## Verificação

- Simule a falha em cada etapa e confirme o caminho de compensação.

- Valide o tratamento de mensagens duplicadas.

- Valide a recuperação após a reinicialização do orquestrador.