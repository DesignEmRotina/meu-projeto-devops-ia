--- 
name: ffuf-web-fuzzing
description: Guia especializado para fuzzing web com ffuf durante testes de penetração, incluindo fuzzing autenticado com requisições brutas, autocalibração e análise de resultados.
risk: desconhecido
source: comunidade
---

# Skill FFUF (Fuzz Faster U Fool)

## Quando usar

- Você está realizando fuzzing em alvos web com `ffuf` durante testes de segurança autorizados ou testes de penetração.

- A tarefa envolve descoberta de conteúdo, enumeração de subdomínios, fuzzing de parâmetros ou fuzzing de requisições autenticadas.

- Você precisa de orientação sobre wordlists, filtragem, calibração e interpretação eficiente dos resultados do ffuf.

## Visão geral
FFUF é um fuzzer web rápido escrito em Go, projetado para descobrir conteúdo oculto, diretórios, arquivos, subdomínios e testar vulnerabilidades durante testes de penetração. É significativamente mais rápido do que ferramentas tradicionais como dirb ou dirbuster.

## Instalação
```bash
# Usando Go
go install github.com/ffuf/ffuf/v2@latest

# Usando Homebrew (macOS)
brew install ffuf

# Download do binário
# Baixe em: https://github.com/ffuf/ffuf/releases/latest
```

## Conceitos Básicos

### A Palavra-chave `FUZZ`
A palavra-chave `FUZZ` é usada como um marcador que é substituído por entradas da sua lista de palavras. Você pode colocá-lo em qualquer lugar:
- URLs: `https://target.com/FUZZ`
- Cabeçalhos: `-H "Host: FUZZ"`
- Dados POST: `-d "username=admin&password=FUZZ"`
- Vários locais com palavras-chave personalizadas: `-w wordlist.txt:CUSTOM` e use `CUSTOM` em vez de `FUZZ`

### Modos de múltiplas listas de palavras
- **clusterbomb**: Testa todas as combinações (padrão) - produto cartesiano
- **pitchfork**: Itera pelas listas de palavras em paralelo (correspondência 1 para 1)
- **sniper**: Testa uma posição por vez (para múltiplas posições FUZZ)

## Casos de uso comuns

### 1. Descoberta de diretórios e arquivos
```bash
# Fuzzing básico de diretórios
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ

# Com extensões de arquivo
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -e .php,.html,.txt,.pdf

# Saída colorida e detalhada
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -c -v

# Com recursão (encontra diretórios aninhados)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -recursion -recursion-depth 2
```

### 2. Enumeração de Subdomínios
```bash
# Descoberta de hosts virtuais
ffuf -w /caminho/para/subdomínios.txt -u https://target.com -H "Host: FUZZ.target.com" -fs 4242

# Observação: -fs 4242 filtra respostas de tamanho 4242 (ajuste com base no tamanho de resposta padrão)
```

### 3. Parâmetro Fuzzing
```bash
# Nomes de parâmetros GET
ffuf -w /caminho/para/params.txt -u https://target.com/script.php?FUZZ=test_value -fs 4242

# Valores de parâmetros GET
ffuf -w /caminho/para/values.txt -u https://target.com/script.php?id=FUZZ -fc 401

# Múltiplos parâmetros
ffuf -w params.txt:PARAM -w values.txt:VAL -u https://target.com/?PARAM=VAL -mode clusterbomb
```

### 4. Fuzzing de dados POST
```bash
# Fuzzing básico de POST
ffuf -w /caminho/para/passwords.txt -X POST -d "username=admin&password=FUZZ" -u https://target.com/login.php -fc 401

# Dados JSON POST
ffuf -w entries.txt -u https://target.com/api -X POST -H "Content-Type: application/json" -d '{"name": "FUZZ", "key": "value"}' -fr "error"

# Fuzzing de múltiplos campos POST
ffuf -w users.txt:USER -w passes.txt:PASS -X POST -d "username=USER&password=PASS" -u https://target.com/login -mode pitchfork
```

### 5. Fuzzing de Cabeçalhos
```bash
# Cabeçalhos personalizados
ffuf -w /caminho/para/wordlist.txt -u https://target.com -H "X-Custom-Header: FUZZ"

# Múltiplos cabeçalhos
ffuf -w /caminho/para/wordlist.txt -u https://target.com -H "User-Agent: FUZZ" -H "X-Forwarded-For: 127.0.0.1"
```

## Filtragem e Correspondência

### Correspondências (Incluir Resultados)
- `-mc`: Corresponder a códigos de status (padrão: 200-299, 301, 302, 307, 401, 403, 405, 500)
- `-ml`: Corresponder à contagem de linhas
- `-mr`: Corresponder a expressões regulares
- `-ms`: Corresponder ao tamanho da resposta
- `-mt`: Corresponder ao tempo de resposta (por exemplo, `>100` ou `<100` milissegundos)
- `-mw`: Corresponder à contagem de palavras

### Filtros (Excluir Resultados)
- `-fc`: Filtrar códigos de status (por exemplo, `-fc 404, 403, 401`)
- `-fl`: Filtrar à contagem de linhas
- `-fr`: Filtrar a expressão regular (por exemplo, `-fr "erro"`)
- `-fs`: Filtrar a resposta tamanho (ex.: `-fs 42,4242`)
- `-ft`: Tempo de resposta do filtro
- `-fw`: Contagem de palavras do filtro

### Autocalibração (USAR POR PADRÃO!)
**CRÍTICO:** Sempre use `-ac`, a menos que tenha um motivo específico para não usar. Isso é especialmente importante ao usar o Claude para analisar os resultados, pois reduz drasticamente o ruído e os falsos positivos.

```bash
# Autocalibração - SEMPRE USE ESTA
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -ac

# Autocalibração por host (útil para múltiplos hosts)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -ach

# String de autocalibração personalizada (para padrões específicos)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -acc "404NotFound"
```

**Por que `-ac` é essencial:**
- Detecta e filtra automaticamente respostas falsas positivas repetitivas
- Remove ruídos de sites dinâmicos com conteúdo aleatório
- Facilita muito a análise dos resultados, tanto para humanos quanto para o Claude
- Impede que milhares de respostas 404/403 idênticas poluam a saída
- Adapta-se ao comportamento específico do alvo

**Quando o Claude analisa seus resultados do ffuf, `-ac` É OBRIGATÓRIO** - sem ele, Claude perderá tempo analisando milhares de falsos positivos em vez de encontrar as anomalias interessantes.

## Limitação de Taxa e Temporização

### Controle de Taxa
```bash
# Limitar a 2 requisições por segundo (modo furtivo)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -rate 2

# Adicionar atraso entre as requisições (0,1 a 2 segundos aleatórios)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -p 0.1-2.0

# Definir o número de threads simultâneas (padrão: 40)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -t 10
```

### Limites de Tempo
```bash
# Tempo máximo total de execução (60 segundos)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -maxtime 60

# Tempo máximo por tarefa (útil com recursão)
ffuf -w `ffuf -w /caminho/para/lista/de/palavras.txt -u https://target.com/FUZZ -maxtime-job 60 -recursion`

## Opções de Saída

### Formatos de Saída
```bash
# Saída JSON
ffuf -w /caminho/para/lista/de/palavras.txt -u https://target.com/FUZZ -o results.json

# Saída HTML
ffuf -w /caminho/para/lista/de/palavras.txt -u https://target.com/FUZZ -of html -o results.html

# Saída CSV
ffuf -w /caminho/para/lista/de/palavras.txt -u https://target.com/FUZZ -of csv -o results.csv

# Todos os formatos
ffuf -w /caminho/para/lista/de/palavras.txt -u https://target.com/FUZZ -of all -o results

# Modo silencioso (sem progresso, apenas resultados)
ffuf -w /caminho/para/lista/de/palavras.txt -u https://target.com/FUZZ -s

# Redirecionar para arquivo com tee
ffuf -w /caminho/para/lista/de/palavras.txt -u https://target.com/FUZZ -s | tee results.txt
```

## Técnicas Avançadas

### Usando Requisições HTTP Brutas (Crítico para Fuzzing Autenticado)
Este é um dos recursos mais poderosos do ffuf, especialmente para requisições autenticadas com cabeçalhos, cookies ou tokens complexos.

**Fluxo de trabalho:**
1. Capture uma requisição autenticada completa (do Burp Suite, DevTools do navegador, etc.)
2. Salve-a em um arquivo (por exemplo, `req.txt`)
3. Substitua o valor que você deseja testar com a palavra-chave `FUZZ`
4. Use a flag `--request`

```bash
# A partir de um arquivo contendo a requisição HTTP bruta
ffuf --request req.txt -w /caminho/para/wordlist.txt -ac
```
**Exemplo de arquivo req.txt:**
```http
POST /api/v1/users/FUZZ HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Cookie: session=abc123xyz; csrftoken=def456
Content-Type: application/json
Content-Length: 27

{"action":"view","id":"1"}
```

**Casos de Uso:**
- Fuzzing de endpoints autenticados com cabeçalhos de autenticação complexos
- Teste de endpoints de API com tokens JWT
- Fuzzing com tokens CSRF, cookies de sessão e cabeçalhos personalizados
- Teste de endpoints que exigem User-Agents ou cabeçalhos Accept específicos
- Requisições POST/PUT/DELETE com autenticação

**Dicas Profissionais:**
- Você pode inserir o FUZZ em vários locais: caminho da URL, cabeçalhos, corpo
- Use `-request-proto https` se necessário (o padrão é https)
- Sempre use `-ac` para filtrar respostas autenticadas de "não encontrado" ou erro
- Ótimo para testes IDOR: fuzzing de IDs de usuário, IDs de documento, etc. em contextos autenticados

```bash
# Padrões comuns de fuzzing autenticado
ffuf --request req.txt -w user_ids.txt -ac -mc 200 -o results.json

# Com múltiplas posições de FUZZ usando palavras-chave personalizadas
ffuf --request req.txt -w endpoints.txt:ENDPOINT -w ids.txt:ID -mode pitchfork -ac
```

### Uso de Proxy
```bash
# Proxy HTTP (útil para o Burp Suite)
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -x http://127.0.0.1:8080

# Proxy SOCKS5
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -x socks5://127.0.0.1:1080

# Reproduzir requisições correspondentes através do proxy
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -replay-proxy http://127.0.0.1:8080
```

### Cookies e Autenticação
```bash
# Usando cookies
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -b "sessionid=abc123; token=xyz789"

# Autenticação de certificado do cliente
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -cc client.crt -ck client.key
```

### Codificação
```bash
# Codificação de URL
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -enc 'FUZZ:urlencode'

# Múltiplas codificações
ffuf -w /caminho/para/wordlist.txt -u https://target.com/FUZZ -enc 'FUZZ:urlencode b64encode'
```

### Testando Vulnerabilidades
```bash
# Teste de injeção SQL
ffuf -w sqli_payloads.txt -u https://target.com/page.php?id=FUZZ -fs 1234

# Teste de XSS
ffuf -w xss_payloads.txt -u https://target.com/search?q=FUZZ -mr "<script>"

# Injeção de comando
ffuf -w cmdi_payloads.txt -u https://target.com/execute?cmd=FUZZ -fr "error"
```

### Processamento em Lote de Múltiplos Alvos
```bash
# Processar múltiplas URLs
cat targets.txt | xargs -I@ sh -c 'ffuf -w wordlist.txt -u @/FUZZ -ac'

# Percorrer múltiplos alvos com resultados
for url in $(cat targets.txt); do

ffuf -w wordlist.txt -u $url/FUZZ -ac -o "results_$(echo $url | md5sum | cut -d' ' -f1).json"
done
```

## Melhores Práticas

### 1. SEMPRE Use Autocalibração
Use `-ac` por padrão para cada varredura. Isso é imprescindível para testes de intrusão produtivos:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -ac
```
### 2. Use Requisições Brutas para Autenticação
Não se preocupe com parâmetros de linha de comando para autenticação complexa. Capture a requisição completa e use `--request`:
```bash
# 1. Capture a requisição autenticada do Burp/DevTools
# 2. Salve em req.txt com a palavra-chave FUZZ
# 3. Execute com -ac
ffuf --request req.txt -w wordlist.txt -ac -o results.json
```

### 3. Use as listas de palavras apropriadas
- **Descoberta de diretórios**: SecLists Discovery/Web-Content (raft-large-directories.txt, directory-list-2.3-medium.txt)
- **Subdomínios**: SecLists Discovery/DNS (subdomains-top1million-5000.txt)
- **Parâmetros**: SecLists Discovery/Web-Content (burp-parameter-names.txt)
- **Nomes de usuário**: SecLists Usernames
- **Senhas**: SecLists Passwords
- Origem: https://github.com/danielmiessler/SecLists

### 3. Limitação de Taxa para Discreção
Use `-rate` para evitar acionar WAFs/IDSs ou sobrecarregar o servidor:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -rate 2 -t 10
```

### 4. Filtragem Estratégica
- Verifique primeiro a resposta padrão para identificar tamanhos de resposta, códigos de status ou padrões comuns
- Use `-fs` para filtrar por tamanho ou `-fc` para filtrar por código de status
- Combine filtros: `-fc 403,404 -fs 1234`

### 5. Salvar Resultados Adequadamente
Sempre salve os resultados em um arquivo para análise posterior:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -o results.json -of json
```

### 6. Uso Interativo Modo
Pressione ENTER durante a execução para entrar no modo interativo, onde você pode:
- Ajustar os filtros em tempo real
- Salvar os resultados atuais
- Reiniciar a verificação
- Gerenciar a fila

### 7. Profundidade de Recursão
Tenha cuidado com a profundidade de recursão para evitar ficar preso em loops infinitos ou sobrecarregar o servidor:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -recursion -recursion-depth 2 -maxtime-job 120
```

## Padrões Comuns e Comandos Simples

### Varredura Rápida de Diretórios
```bash
ffuf -w ~/wordlists/common.txt -u https://target.com/FUZZ -mc 200,301,302,403 -ac -c -v
```
### Varredura Abrangente com Extensões
```bash
ffuf -w ~/wordlists/raft-large-directories.txt -u https://target.com/FUZZ -e .php,.html,.txt,.bak,.old -ac -c -v -o results.json
```

### Fuzzing Autenticado (Requisição Bruta)
```bash
# 1. Salve sua requisição autenticada em req.txt com a palavra-chave FUZZ
# 2. Execute:
ffuf --request req.txt -w ~/wordlists/api-endpoints.txt -ac -o results.json -of json
```

### Descoberta de Endpoints da API
```bash
ffuf -w ~/wordlists/api-endpoints.txt -u https://api.target.com/v1/FUZZ -H "Authorization: Bearer TOKEN" -mc 200,201 -ac -c
```

### Descoberta de Subdomínios com Autocalibração
```bash
ffuf -w ~/wordlists/subdomains-top5000.txt -u https://FUZZ.target.com -ac -c -v
```

### Teste de Força Bruta de Login POST
```bash
ffuf -w ~/wordlists/passwords.txt -X POST -d "username=admin&password=FUZZ" -u https://target.com/login -fc 401 -rate 5 -ac
```

### Teste IDOR com Autenticação
```bash
# Use req.txt com cabeçalhos autenticados e FUZZ no parâmetro ID
ffuf --request req.txt -w numbers.txt -ac -mc 200 -fw 100-200
```

## Arquivo de Configuração
Crie `~/.config/ffuf/ffufrc` para as configurações padrão:
```
[http]
headers = ["User-Agent: Mozilla/5.0"]
timeout = 10

[general]
colors = true
threads = 40

[matcher]
status = "200-299,301,302,307,401,403,405,500"
```

## Solução de Problemas

### Muitos Falsos Positivos
- Use `-ac` para autocalibração
- Verifique a resposta padrão e filtre por tamanho com `-fs`
- Use filtragem por expressão regular com `-fr`

### Muito Lento
- Aumente o número de threads: `-t 100`
- Reduza o tamanho da lista de palavras
- Use `-ignore-body` se não precisar do conteúdo da resposta

### Bloqueio
- Reduza a taxa: `-rate 2`
- Adicione atrasos: `-p 0.5-1.5`
- Reduza o número de threads: `-t 10`
- Randomize o User-Agent
- Use rotação de proxy

### Resultados Ausentes
- Verifique se você está filtrando de forma muito agressiva
- Use `-mc all` para ver todas as respostas
- Desative a autocalibração temporariamente
- Use o modo detalhado `-v` para ver o que está acontecendo

## Recursos
- GitHub oficial: https://github.com/ffuf/ffuf
- Wiki: https://github.com/ffuf/ffuf/wiki
- Guia do Codingo: https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html
- Laboratório Prático: http://ffuf.me
- Listas de palavras do SecLists: https://github.com/danielmiessler/SecLists

## Cartão de Referência Rápida

| Tarefa | Modelo de Comando |

|------|------------------|

| Descoberta de Diretório | `ffuf -w wordlist.txt -u https://target.com/FUZZ -ac` |

| Descoberta de Subdomínio | `ffuf -w subdomains.txt -u https://FUZZ.target.com -ac` |

| Fuzzing de Parâmetros | `ffuf -w params.txt -u https://target.com/page?FUZZ=value -ac` |
| Fuzzing de Dados POST | `ffuf -w wordlist.txt -X POST -d "param=FUZZ" -u https://target.com/endpoint` |

| Com Extensões | Adicione `-e .php,.html,.txt` |
| Filtrar Status | Adicione `-fc 404,403` |
| Filtrar Tamanho | Adicione `-fs 1234` |
| Limite de Taxa | Adicione `-rate 2` |

| Salvar Saída | Adicione `-o results.json` |

| Detalhado | Adicione `-c -v` |

| Recursão | Adicione `-recursion -recursion-depth 2` |

| Através de Proxy | Adicione `-x http://127.0.0.1:8080` |

## Recursos Adicionais

Esta habilidade inclui materiais suplementares no diretório `resources/`:

### Arquivos de Recursos
- **WORDLISTS.md**: Guia completo para listas de palavras do SecLists, listas recomendadas para diferentes cenários, extensões de arquivo e padrões de referência rápida
- **REQUEST_TEMPLATES.md**: Modelos req.txt pré-construídos para cenários comuns de autenticação (JWT, OAuth, cookies de sessão, chaves de API, etc.) com exemplos de uso

### Script Auxiliar
- **ffuf_helper.py**: Script Python para auxiliar em:

- Análise dos resultados JSON do ffuf em busca de anomalias e descobertas interessantes
- Criação de arquivos de modelo req.txt a partir de argumentos da linha de comando

- Geração de listas de palavras baseadas em números para testes IDOR

**Uso do Script Auxiliar:**

```bash
# Analisar resultados para encontrar anomalias interessantes
python3 ffuf_helper.py analyze results.json

# Criar requisição autenticada template
python3 ffuf_helper.py create-req -o req.txt -m POST -u "https://api.target.com/users" \

-H "Authorization: Bearer TOKEN" -d '{"action":"FUZZ"}'

# Gerar lista de palavras para teste IDOR
python3 ffuf_helper.py wordlist -o ids.txt -t numbers -s 1 -e 10000
```

**Quando usar recursos:**
- Usuários precisam de recomendações de listas de palavras → Consulte WORDLISTS.md
- Usuários precisam de ajuda com solicitações autenticadas → Consulte REQUEST_TEMPLATES.md
- Usuários desejam analisar resultados → Use ffuf_helper.py analyze
- Usuários precisam gerar req.txt → Use ffuf_helper.py create-req
- Usuários precisam de intervalos de números para IDOR → Use ffuf_helper.py wordlist

## Notas para Claude
Ao auxiliar usuários com o ffuf:
1. **SEMPRE inclua `-ac` em todos os comandos** - Isso é obrigatório para testes de penetração em produção e análise de resultados
2. Quando os usuários mencionarem fuzzing autenticado ou fornecerem tokens/cookies de autenticação:

- Sugira a criação de um arquivo `req.txt` com a requisição HTTP completa
- Mostre a eles como inserir o FUZZ onde desejam realizar o fuzzing
- Use `ffuf --request req.txt -w wordlist.txt -ac`
3. Sempre recomende começar com `-ac` para autocalibração
4. Sugira wordlists apropriadas do SecLists com base na tarefa
5. Lembre os usuários de usar limitação de taxa (`-rate`) para alvos de produção
6. Incentive o salvamento da saída em arquivos para documentação: `-o results.json`
7. Sugira estratégias de filtragem com base no reconhecimento inicial
8. Sempre use a palavra-chave FUZZ (diferencia maiúsculas de minúsculas)
9. Considere Stealth: menos threads, limitação de taxa e atrasos para alvos sensíveis
10. Para relatórios de pentest, use `-of html` ou `-of csv` para formatos amigáveis ​​ao cliente
11. **Ao analisar os resultados do ffuf para usuários:**

- Presuma que eles usaram `-ac` (caso contrário, os resultados serão muito ruidosos)
- Concentre-se em anomalias: códigos de status diferentes, tamanhos de resposta, tempo
- Procure endpoints interessantes: admin, api, backup, config, .git, etc.

- Sinalize vulnerabilidades potenciais: mensagens de erro, rastreamentos de pilha, informações de versão
- Sugira fuzzing de acompanhamento em descobertas interessantes