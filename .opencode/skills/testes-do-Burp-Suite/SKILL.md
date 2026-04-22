--- 
name: testes-do-Burp-Suite
description: "Execute testes abrangentes de segurança em aplicações web usando o conjunto de ferramentas integradas do Burp Suite, incluindo interceptação e modificação de tráfego HTTP, análise e reprodução de requisições, varredura automatizada de vulnerabilidades e fluxos de trabalho de testes manuais."
risk: ofensivo
source: comunidade
autor: zebbern
date_add: "2026-02-27"
---

> USO AUTORIZADO APENAS: Use esta habilidade somente para avaliações de segurança autorizadas, validação defensiva ou ambientes educacionais controlados.

# Teste de Aplicações Web com Burp Suite

## Objetivo

Execute testes abrangentes de segurança em aplicações web usando o conjunto de ferramentas integradas do Burp Suite, incluindo interceptação e modificação de tráfego HTTP, análise e reprodução de requisições, varredura automatizada de vulnerabilidades e fluxos de trabalho de testes manuais. Esta habilidade permite a descoberta e exploração sistemática de vulnerabilidades em aplicações web por meio de metodologia de testes baseada em proxy.

## Entradas / Pré-requisitos

### Ferramentas Necessárias
- Burp Suite Community ou Professional Edition instalado
- Navegador integrado do Burp ou navegador externo configurado
- URL da aplicação web alvo
- Credenciais válidas para testes autenticados (se aplicável)

### Configuração do Ambiente
- Burp Suite iniciado com um projeto temporário ou nomeado
- Listener de proxy ativo em 127.0.0.1:8080 (padrão)
- Navegador configurado para usar o proxy do Burp (ou usar o navegador do Burp)
- Certificado CA instalado para interceptação HTTPS

### Comparação de Edições
| Recurso | Community | Professional |

|---------|-----------|--------------|

| Proxy | ✓ | ✓ |

| Repeater | ✓ | ✓ |

| Intruder | Limited | Full |

| Scanner | ✗ | ✓ |

| Extensions | ✓ | ✓ | ## Resultados/Entregáveis

### Resultados Principais
- Requisições/respostas HTTP interceptadas e modificadas
- Relatórios de varredura de vulnerabilidades com recomendações de correção
- Documentação do histórico HTTP e do mapa do site
- Provas de conceito para explorar vulnerabilidades identificadas

## Fluxo de Trabalho Principal

### Fase 1: Interceptação de Tráfego HTTP

#### Iniciar o Navegador do Burp
Navegue até o navegador integrado para uma integração perfeita com o proxy:

1. Abra o Burp Suite e crie/abra um projeto
2. Vá para a aba **Proxy > Intercept**
3. Clique em **Abrir Navegador** para iniciar o navegador pré-configurado
4. Posicione as janelas para visualizar o Burp e o navegador simultaneamente

#### Configurar a Interceptação
Controle quais requisições são capturadas:

```
Proxy > Intercept > Interceptar (ativar/desativar)

Quando ATIVADO: As requisições são pausadas para revisão/modificação
Quando DESATIVADO: As requisições são encaminhadas e registradas no histórico
```

#### Interceptar e Encaminhar Solicitações
Processar tráfego interceptado:

1. Ative a interceptação: **Interceptar ativado**
2. Acesse o URL de destino no navegador
3. Observe a solicitação em espera na guia Proxy > Interceptar
4. Analise o conteúdo da solicitação (cabeçalhos, parâmetros, corpo)
5. Clique em **Encaminhar** para enviar a solicitação ao servidor
6. Continue encaminhando as solicitações subsequentes até que a página seja carregada

#### Visualizar histórico HTTP
Acessar o registro completo de tráfego:

1. Acesse a guia **Proxy > Histórico HTTP**
2. Clique em qualquer entrada para visualizar a solicitação/resposta completa
3. Classifique clicando nos cabeçalhos das colunas (# para ordem cronológica)
4. Use filtros para focar no tráfego relevante

### Fase 2: Modificando solicitações

#### Interceptar e modificar
Altere os parâmetros da solicitação antes de encaminhá-la:

1. Ative a interceptação: **Interceptar ativado**
2. Acione a solicitação de destino no navegador
3. Localize o parâmetro a ser modificado na solicitação interceptada
4. Edite o valor diretamente no editor de solicitações
5. Clique em **Encaminhar** para enviar a solicitação modificada Solicitação

#### Alvos de Modificação Comuns
| Alvo | Exemplo | Finalidade |

|--------|---------|---------|

| Parâmetros de preço | `price=1` | Testar lógica de negócios |

| IDs de usuário | `userId=admin` | Testar controle de acesso |

| Valores de quantidade | `qty=-1` | Testar validação de entrada |

| Campos ocultos | `isAdmin=true` | Testar escalonamento de privilégios |

#### Exemplo: Manipulação de Preço

```http
POST /cart HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded

productId=1&quantity=1&price=100

# Modificar para:
productId=1&quantity=1&price=1
```

Resultado: Item adicionado ao carrinho com o preço modificado.

### Fase 3: Definindo o Escopo do Alvo

#### Definir Escopo
Concentre os testes em um alvo específico:

1. Acesse **Alvo > Mapa do Site**
2. Clique com o botão direito do mouse no host de destino no painel esquerdo
3. Selecione **Adicionar ao escopo**
4. Quando solicitado, clique em **Sim** para excluir o tráfego fora do escopo

#### Filtrar por Escopo
Remova o ruído do histórico HTTP:

1. Clique no filtro de exibição acima do histórico HTTP
2. Selecione **Mostrar somente itens dentro do escopo**
3. O histórico agora mostra apenas o tráfego do site de destino

#### Benefícios do Escopo
- Reduz a desordem de solicitações de terceiros
- Impede o teste acidental de sites fora do escopo
- Melhora a eficiência da varredura
- Cria relatórios mais claros

### Fase 4: Usando o Burp Repeater
### Fase 4: Usando o Burp Repeater

#### Enviar Requisição para o Repeater
Preparar a requisição para teste manual:

1. Identificar requisições interessantes no histórico HTTP
2. Clicar com o botão direito na requisição e selecionar **Enviar para o Repeater**
3. Ir para a aba **Repeater** para acessar a requisição

#### Modificar e Reenviar
Testar diferentes entradas de forma eficiente:

```
1. Visualizar a requisição na aba Repeater
2. Modificar os valores dos parâmetros
3. Clicar em Enviar para submeter a requisição
4. Revisar a resposta no painel direito
5. Usar as setas de navegação para revisar o histórico da requisição
```

#### Fluxo de Trabalho de Teste com o Repeater

```
Requisição Original:
GET /product?productId=1 HTTP/1.1

Teste 1: productId=2 → Resposta de produto válido
Teste 2: productId=999 → Resposta de produto não encontrado
Teste 3: productId=' → Resposta de erro/exceção
Teste 4: productId=1 OU 1=1 → Teste de injeção SQL
```

#### Analisar Respostas
Procure por indicadores de vulnerabilidades:

- Mensagens de erro revelando rastreamentos de pilha
- Divulgação de informações de framework/versão
- Comprimentos de resposta diferentes indicando falhas lógicas
- Diferenças de tempo sugerindo injeção cega
- Dados inesperados nas respostas

### Fase 5: Executando Varreduras Automatizadas

#### Iniciar Nova Varredura
Inicie a varredura de vulnerabilidades (somente para a versão Profissional):

1. Acesse a aba **Painel**
2. Clique em **Nova varredura**
3. Insira a URL de destino no campo **URLs para varredura**
4. Configure as opções de varredura

#### Opções de Configuração da Varredura

| Modo | Descrição | Duração |

|------|-------------|----------|

| Leve | Visão geral de alto nível | ~15 minutos |

| Rápido | Verificação rápida de vulnerabilidades | ~30 minutos |

| Equilibrado | Varredura completa padrão | ~1-2 horas |

| Testes profundos | Testes minuciosos | Várias horas |

#### Monitorar o Progresso da Varredura
Acompanhe a atividade de varredura:

1. Visualize o status da tarefa no **Painel de Controle**
2. Observe a atualização em tempo real de **Destino > Mapa do Site**
3. Verifique a aba **Problemas** para vulnerabilidades descobertas

#### Revisar os Problemas Identificados
Analise os resultados da varredura:

1. Selecione a tarefa de varredura no Painel de Controle
2. Acesse a aba **Problemas**
3. Clique no problema para visualizar:

- **Aviso**: Descrição e correção

- **Solicitação**: Solicitação HTTP que acionou a varredura

- **Resposta**: Resposta do servidor mostrando a vulnerabilidade

### Fase 6: Ataques de Intrusão

#### Configurar o Intruso
Configure o ataque automatizado:

1. Envie uma solicitação para o Intruso (clique com o botão direito > Enviar para o Intruso)
2. Acesse a aba **Intruso**
3. Defina as posições da carga útil usando os marcadores §
4. Selecione o tipo de ataque

#### Tipos de Ataque

| Tipo | Descrição | Caso de Uso |

------|-------------|----------|

| Sniper | Posição única, iteração de payloads | Fuzzing de um parâmetro |

| Aríete | Mesma carga útil em todas as posições | Teste de credenciais |

| Garfo | Iteração paralela de payloads | Pares nome de usuário:senha |

| Bomba de fragmentação | Todas as combinações de payloads | Força bruta completa |

#### Configurar Payloads

```
Aba Posições:
POST /login HTTP/1.1
...
username=§admin§&password=§password§

Aba Payloads:
Conjunto 1: admin, user, test, guest
Conjunto 2: password, 123456, admin, letmein
```

#### Analisar Resultados
Revisar a saída do ataque:

- Classificar por comprimento da resposta para encontrar anomalias
- Filtrar por código de status para tentativas bem-sucedidas
- Usar grep para buscar strings específicas
- Exportar resultados para documentação

## Referência Rápida

### Atalhos de Teclado
| Ação | Windows/Linux | macOS |

|--------|---------------|-------|

| Encaminhar solicitação | Ctrl+F | Cmd+F |

| Descartar solicitação | Ctrl+D | Cmd+D |

| Enviar para o Repetidor | Ctrl+R | Cmd+R |

| Enviar para o Intruso | Ctrl+I | Cmd+I |

| Alternar interceptação | Ctrl+T | Cmd+T |

### Payloads de Teste Comuns

```
# Injeção de SQL
' OR '1'='1
' OR '1'='1'--
1 UNION SELECT NULL--

# XSS
<script>alert(1)</script>
"><img src=x onerror=alert(1)>
javascript:alert(1)

# Path Traversal
../../../etc/passwd
..\..\..\..\windows\win.ini

# Injeção de Comando
; ls -la
| cat /etc/passwd
`whoami`
```

### Dicas para Modificação de Requisições
- Clique com o botão direito para acessar as opções do menu de contexto
- Use o decodificador para codificar/decodificar
- Compare as requisições usando a ferramenta Comparador
- Salve as requisições relevantes no projeto

## Restrições e Salvaguardas

### Limites Operacionais
- Teste apenas aplicativos autorizados
- Configure o escopo para evitar testes acidentais fora do escopo
- Limite a taxa de varreduras para evitar negação de serviço
- Documente todas as descobertas e ações

### Limitações Técnicas
- A Edição Comunitária não possui um scanner automatizado
- Alguns sites podem bloquear o tráfego de proxy
- O HSTS/certificado fixado pode exigir configuração adicional
- Varreduras intensas podem acionar bloqueios do WAF

### Melhores Práticas
- Sempre defina o escopo alvo antes de realizar testes extensivos
- Use o navegador do Burp para interceptação confiável
- Salve o projeto regularmente para preservar o trabalho
- Revise os resultados da varredura manualmente para identificar falsos positivos

## Exemplos

### Exemplo 1: Teste de Lógica de Negócios

**Cenário**: Manipulação de preços em e-commerce

1. Adicione um item ao carrinho normalmente e intercepte a requisição. Solicitação
2. Identificar o parâmetro `price=9999` no corpo da requisição POST
3. Modificar para `price=1`
4. Encaminhar a requisição
5. Concluir a compra com o preço manipulado

**Descoberta**: O servidor confia nos valores de preço fornecidos pelo cliente.

### Exemplo 2: Bypass de Autenticação

**Cenário**: Testando o formulário de login

1. Enviar credenciais válidas, capturar a requisição no Repeater
2. Enviar para o Repeater para teste
3. Tentar: `username=admin' OR '1'='1'--`
4. Observar a resposta de login bem-sucedido

**Descoberta**: Injeção de SQL na autenticação.

### Exemplo 3: Divulgação de Informações

**Cenário**: Coleta de informações baseada em erros

1. Navegue até a página do produto e observe o parâmetro `productId`.
2. Envie uma solicitação ao Repeater.
3. Altere `productId=1` para `productId=test`.
4. Observe o erro detalhado que revela a versão do framework.

**Descoberta**: Apache Struts 2.5.12 revelado no rastreamento de pilha.

## Solução de Problemas

### Navegador não conecta através do proxy
- Verifique se o ouvinte de proxy está ativo (Proxy > Opções)
- Verifique se as configurações de proxy do navegador apontam para 127.0.0.1:8080
- Certifique-se de que nenhum firewall esteja bloqueando conexões locais
- Use o navegador integrado do Burp para uma configuração confiável

### Falha na interceptação de HTTPS
- Instale o certificado CA do Burp no navegador/sistema
- Acesse http://burp para baixar o certificado
- Adicione o certificado às raízes confiáveis
- Reinicie o navegador após a instalação

### Desempenho lento
- Limite o escopo para reduzir o processamento
- Desative extensões desnecessárias
- Aumente o tamanho do heap da JVM nas opções de inicialização
- Feche as abas e recursos do Burp que não estiverem em uso

### Requisições não estão sendo interceptadas
- Verifique se a opção "Interceptar ativado" está habilitada
- Verifique se as regras de interceptação não estão filtrando o destino
- Certifique-se de que o navegador esteja usando o proxy do Burp
- Verifique se o destino não está usando um protocolo não suportado

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.