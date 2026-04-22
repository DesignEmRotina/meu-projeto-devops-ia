#!/bin/bash
source "$(dirname "$0")/../utils/comum.sh"
npx prisma migrate dev --name "$1" && npx prisma generate
success "✅ Migration aplicada"