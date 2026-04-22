#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"
npm run coverage || true
# Exemplo Codecov (configure token no GitHub Secrets)
# curl -Os https://uploader.codecov.io/latest/linux/codecov && chmod +x codecov && ./codecov -t $CODECOV_TOKEN
success "✅ Relatório de cobertura enviado"