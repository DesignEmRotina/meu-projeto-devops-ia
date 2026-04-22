#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "📋 Validando contratos OpenAPI + JSON Schema..."

npx @redocly/cli lint .opencode/contracts/contratos-de-api.yaml || error "Contrato inválido"
success "✅ Contratos validados"