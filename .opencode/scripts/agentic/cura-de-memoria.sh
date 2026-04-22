#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "🧹 Curando memória dos agentes..."

# Limpa short-term
rm -rf .opencode/memory/short-term/* 2>/dev/null || true

# Compacta long-term (opcional)
cd .opencode/memory/long-term && tar -czf execucoes-historicas-$(date +%Y%m%d).tar.gz execuções-historicas/ 2>/dev/null || true

success "✅ Memória curada"