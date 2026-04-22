#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "🔧 Executando lint + auto-fix..."

npx eslint . --fix --max-warnings=0 || warn "ESLint encontrou warnings"
npx prettier --write "**/*.{js,ts,jsx,tsx,md}" 2>/dev/null || true
npx stylelint "**/*.css" --fix 2>/dev/null || true

success "✅ Lint e formatação concluídos"