#!/bin/bash
# iniciar.sh – Inicialização completa do projeto (uma vez só)
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "🚀 Iniciando setup do projeto Design Em Rotina..."

require_command "node" "npm"

# 1. Instala dependências
log "INFO" "Instalando dependências (npm ci)..."
npm ci --no-audit --prefer-offline

# 2. Cria .env
check_env_file

# 3. Instala hooks
"$SCRIPT_DIR/../setup/instalar-hooks.sh"

# 4. Prisma (se existir)
if [[ -f "prisma/schema.prisma" ]] || [[ -f "src/database/schema.prisma" ]]; then
  npx prisma generate
  success "Prisma gerado com sucesso"
fi

success "✅ Projeto inicializado com sucesso! Rode 'scripts/dev/start-local.sh' para iniciar."