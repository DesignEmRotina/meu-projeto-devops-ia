--- 
name: auditoria-de-código-pré-push
description: "Auditoria completa antes do push no GitHub: remove arquivos inúteis, código morto, falhas de segurança e problemas de otimização. Verifica cada arquivo linha por linha para garantir a prontidão para produção."
category: desenvolvimento
risk: seguro
source: comunidade
date_add: "05/03/2026"
---

# Auditoria de Código-Fonte Pré-Push

Como engenheiro sênior, você está realizando a revisão final antes de enviar este código para o GitHub. Verifique tudo cuidadosamente e corrija os problemas à medida que os encontrar.

## Quando usar esta habilidade

- O usuário solicita "auditar o código-fonte" ou "revisar antes do push"
- Antes de fazer o primeiro push para o GitHub
- Antes de tornar um repositório público
- Revisão de implantação em pré-produção
- O usuário pede para "limpar o código" ou "otimizar tudo"

## Sua tarefa

Revise todo o código-fonte arquivo por arquivo. Leia o código com atenção. Corrija os problemas imediatamente. Não se limite a observar os problemas — faça as alterações necessárias.

## Processo de Auditoria

### 1. Limpeza de Arquivos Indesejados

Comece procurando por arquivos que não deveriam estar no GitHub:

**Exclua-os imediatamente:**

- Arquivos do sistema operacional: `.DS_Store`, `Thumbs.db`, ​​`desktop.ini`

- Logs: `*.log`, `npm-debug.log*`, `yarn-error.log*`

- Arquivos temporários: `*.tmp`, `*.temp`, `*.cache`, `*.swp`

- Saída de compilação: `dist/`, `build/`, `.next/`, `out/`, `.cache/`

- Dependências: `node_modules/`, `vendor/`, `__pycache__/`, `*.pyc`

- Arquivos da IDE: `.idea/`, `.vscode/` (pergunte ao usuário primeiro), Arquivos `*.iml`, `.project`
- Arquivos de backup: `*.bak`, `*_old.*`, `*_backup.*`, `*_copy.*`
- Artefatos de teste: `coverage/`, `.nyc_output/`, `test-results/`
- Arquivos pessoais: `TODO.txt`, `NOTES.txt`, `scratch.*`, `test123.*`

**Crítico - Verificar segredos:**
- Arquivos `.env` (nunca devem ser incluídos no commit)
- Arquivos contendo: `password`, `api_key`, `token`, `secret`, `private_key`
- Arquivos `*.pem`, `*.key`, `*.cert`, `credentials.json`, `serviceAccountKey.json`

Se encontrar segredos no código, marque-o como um BLOQUEADOR CRÍTICO.

### 2. Corrigir .gitignore

Verifique se o arquivo `.gitignore` existe e está completo. Se estiver faltando ou incompleto, atualize-o para incluir todos os padrões de arquivos indesejados mencionados acima. Certifique-se de que `.env.example` exista com chaves, mas sem valores.

### 3. Audite Cada Arquivo Fonte

Analise cada arquivo de código e verifique:

**Código Morto (remova imediatamente):**

- Blocos de código comentados
- Importações/requisições não utilizadas
- Variáveis ​​não utilizadas (declaradas, mas nunca usadas)
- Funções não utilizadas (definidas, mas nunca chamadas)
- Código inacessível (após `return`, dentro de `if (false)`)
- Lógica duplicada (mesmo código em vários lugares — combine)

**Qualidade do Código (corrija os problemas conforme necessário):**
- Nomes vagos: `data`, `info`, `temp`, `thing` → renomeie para nomes descritivos
- Números mágicos: `if (status === 3)` → extraia para uma constante nomeada
- Instruções de depuração: remova `console.log`, `print()`, `debugger`
- Comentários TODO/FIXME: resolva-os ou exclua-os
- TypeScript `any`: adicione tipos apropriados ou explique por que `any` é usado
- Use `===` em vez de `==` em JavaScript
- Funções com mais de 50 linhas: considere dividi-las
- Código aninhado com mais de 3 níveis: refatore com retornos antecipados

**Problemas de lógica (críticos):**
- Ausência de verificações de nulo/indefinido
- Operações com arrays potencialmente vazios
- Funções assíncronas sem `await`
- Promises sem `.catch()` ou `try/catch`
- Possibilidade de loops infinitos
- Ausência de `default` em instruções `switch`

### 4. Verificação de segurança (tolerância zero)

**Segredos:** Procure por senhas, chaves de API e tokens embutidos no código. Eles devem estar em variáveis ​​de ambiente.

**Vulnerabilidades de Injeção:**
- SQL: Proibida a concatenação de strings em consultas — utilize apenas consultas parametrizadas.
- Injeção de comando: Proibido o uso de `exec()` com entrada fornecida pelo usuário.
- Path traversal: Proibido o uso de caminhos de arquivo a partir da entrada do usuário sem validação.
- XSS: Proibido o uso de `innerHTML` ou `dangerouslySetInnerHTML` com dados do usuário.

**Autenticação:**
- Senhas criptografadas com bcrypt/argon2 (nunca MD5 ou texto simples).
- Rotas protegidas verificam a autenticação.
- Verificações de autorização no servidor, não apenas na interface do usuário.
- Proibido o IDOR: verifique se os usuários são proprietários dos recursos que estão acessando.

**Exposição de Dados:**
- Respostas da API não vazam informações desnecessárias.
- Mensagens de erro não expõem rastreamentos de pilha ou detalhes do banco de dados.
- Paginação presente nos endpoints de lista.

**Dependências:**
- Execute `npm audit` ou uma ferramenta equivalente.
- Sinalize recursos criticamente desatualizados ou Pacotes vulneráveis

### 5. Verificação de Escalabilidade

**Banco de Dados:**
- Consultas N+1: loops com chamadas ao banco de dados → use JOINs ou consultas em lote

- Índices ausentes nas colunas WHERE/ORDER BY

- Consultas ilimitadas: adicione LIMIT ou paginação

- Evite `SELECT *`: especifique as colunas

**Design da API:**
- Operações pesadas (como e-mail, relatórios, processamento de arquivos) → mova para uma fila em segundo plano
- Limitação de taxa em endpoints públicos
- Cache para dados lidos com frequência
- Tempo limite em chamadas externas

**Código:**
- Sem estado global mutável
- Limpe os listeners de eventos (para evitar vazamentos de memória)
- Transmita arquivos grandes em vez de carregá-los em um inteiro

**Organização:**
- Estrutura de pastas clara
- Arquivos em locais lógicos
- Sem pastas "diversos" ou "coisas diversas"

**Separação de responsabilidades:**
- Camada de interface do usuário: responsável apenas pela renderização
- Lógica de negócios: funções puras
- Camada de dados: consultas isoladas ao banco de dados
- Sem arquivos "deus" com mais de 500 linhas

**Reutilização:**
- Código duplicado → extrair para utilitários compartilhados
- Constantes definidas uma única vez e importadas
- Tipos/interfaces reutilizados, não redefinidos

### 7. Desempenho

**Backend:**
- Operações custosas não bloqueiam requisições
- Agrupar chamadas ao banco de dados quando possível
- Configurar cabeçalhos de cache corretamente

**Frontend (se aplicável):**
- Implementar divisão de código
- Otimizar imagens
- Evitar dependências massivas para utilitários pequenos
- Usar carregamento lento (lazy loading) para componentes pesados ​​

### 8. Documentação **O arquivo README.md deve incluir:**

- Descrição do que o projeto faz
- Instruções para instalação e execução
- Variáveis ​​de ambiente necessárias
- Orientações sobre como executar os testes

**Comentários no código:**
- Explique o PORQUÊ, não o QUE
- Forneça explicações para lógicas complexas
- Evite comentários que simplesmente repetem o código

### 9. Testes

- Os caminhos críticos devem ter testes (autenticação, pagamentos, funcionalidades principais)
- Nenhum `test.only` ou `fdescribe` deve permanecer no código
- Evite `test.skip` sem uma explicação
- Os testes devem verificar o comportamento, não os detalhes de implementação

### 10. Verificação Final

Após fazer todas as alterações, execute o aplicativo. Certifique-se de que nada esteja quebrado. Verifique se:
- O aplicativo inicia sem erros
- As principais funcionalidades funcionam
- Os testes são aprovados (se existirem)
- Não foram introduzidas regressões

## Formato de Saída

Após a auditoria, forneça um relatório:

```
AUDITORIA DO CÓDIGO CONCLUÍDA

ARQUIVOS REMOVIDOS:
- node_modules/ (artefato de build)
- .env (continha segredos)
- old_backup.js (duplicado não utilizado)

ALTERAÇÕES NO CÓDIGO:
[src/api/users.js]

✂ Importação não utilizada removida: lodash

✂ Função obsoleta removida: formatOldWay()

🔧 Renomeado 'data' → 'userData' para maior clareza

🛡 Adicionado bloco try/catch em torno da chamada da API (linha 47)

[src/db/queries.js]

⚡ Consulta N+1 corrigida: agora usa JOIN em vez de loop

PROBLEMAS DE SEGURANÇA:

🚨 CRÍTICO: Chave da API codificada em config.js (linha 12) → movida para .env

⚠️ ALTO: Risco de injeção de SQL em search.js (linha 34) → corrigido com consulta parametrizada

ESCALABILIDADE:
⚡ Adicionada paginação ao endpoint /api/users
⚡ Adicionado índice na coluna users.email

STATUS FINAL:

✅ LIMPO - Pronto para enviar para o GitHub

Notas:
Segurança: 9/10 (um cabeçalho menor ausente)
Qualidade do Código: 10/10
Escalabilidade: 9/10
Geral: 9/10

```

## Princípios-chave

- Leia o código atentamente, não superficialmente
- Corrija Identifique os problemas imediatamente, não apenas os documente.
- Em caso de dúvida sobre a remoção de algo, pergunte ao usuário.
- Teste após fazer as alterações.
- Seja minucioso, mas prático — concentre-se em problemas reais.
- Problemas de segurança são impeditivos — nada deve ser lançado com vulnerabilidades críticas.

## Habilidades Relacionadas

- `@security-auditor` - Revisão de segurança mais aprofundada.
- `@systematic-debugging` - Investigar problemas específicos.
- `@git-pushing` - Enviar código após a auditoria.