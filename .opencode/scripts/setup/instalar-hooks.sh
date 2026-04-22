#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "Instalando Git hooks..."

mkdir -p .git/hooks

cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
source scripts/utils/comum.sh
log "INFO" "🔍 Executando lint e testes antes do commit..."
scripts/dev/correçao-lint.sh --fix
success "Pre-commit concluído"
EOF

chmod +x .git/hooks/pre-commit
success "✅ Git hooks instalados (pre-commit)"