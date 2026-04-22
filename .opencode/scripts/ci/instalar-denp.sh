#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"
npm ci --cache .npm --prefer-offline --no-audit
success "✅ Dependências instaladas com cache"