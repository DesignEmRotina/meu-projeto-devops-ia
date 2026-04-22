# Scripts Utilitários e Automações – Design Em Rotina

## Visão Geral
Scripts bash para desenvolvimento local, CI/CD, agentes IA e manutenção.  
Todos os scripts **sourcam `utils/comum.sh`** para consistência, logging e segurança.

## Pré-requisitos
- Bash 4+ (macOS/Linux) ou Git Bash (Windows)
- Node.js 20+ + npm
- Docker + Docker Compose (recomendado para `start-local.sh`)
- Prisma CLI (instalado via `npm install -D prisma`)
- Husky (opcional – `instalar-hooks.sh` instala hooks nativos)

## Como usar
```bash
chmod +x scripts/**/*.sh
scripts/setup/iniciar.sh          # primeira vez
scripts/dev/start-local.sh        # dev loop

Lista Completa

setup/ → Inicialização única
dev/ → Ciclo diário de desenvolvimento
db/ → Banco de dados (Prisma)
agentic/ → Interação com .opencode/ (memória, contracts, logs)
ci/ → Chamados por GitHub Actions (idempotentes)
utils/ → Funções reutilizáveis
