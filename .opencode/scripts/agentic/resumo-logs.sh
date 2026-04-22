#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "📊 Gerando resumo semanal de logs..."

find .opencode/logs/diario -name "*.jsonl" -exec cat {} + | jq -r '.level + " " + .message' > .opencode/logs/arquivado/sumarios/sumario-semanal-$(date +%Y-W%V).md
success "✅ Resumo gerado em .opencode/logs/arquivado/sumarios/"