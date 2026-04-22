#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "🚀 Iniciando stack local (frontend + backend + DB)..."

require_command "docker" "npm"

if [[ -f "docker-compose.yml" ]]; then
  docker compose up -d db redis
  log "INFO" "Serviços Docker iniciados"
fi

# Assume package.json com scripts: dev:frontend, dev:backend ou "dev"
if npm run | grep -q "dev:"; then
  npm run dev --if-present &
else
  npm run dev &
fi

success "✅ Stack local iniciada. Acesse http://localhost:3000 (ou porta configurada)"