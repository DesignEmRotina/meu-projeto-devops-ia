#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"

log "INFO" "🔄 Resetando banco Prisma (dev only)..."

npx prisma migrate reset --force
npx prisma db push
npx prisma generate
scripts/db/seed.sh

success "✅ Banco resetado e seeded"