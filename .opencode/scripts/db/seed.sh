#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"
npx prisma db seed
success "✅ Seed executado (idempotente)"