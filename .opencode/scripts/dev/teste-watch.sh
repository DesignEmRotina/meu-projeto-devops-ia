#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "🧪 Iniciando testes em watch mode + coverage..."

npm test -- --watchAll --coverage || error "Testes falharam"