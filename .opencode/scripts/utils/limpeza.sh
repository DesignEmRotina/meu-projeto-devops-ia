
---

### 2. `scripts/utils/comum.sh` (base de tudo)

```bash
#!/bin/bash
# comum.sh – Funções comuns, logging e error handling (Design Em Rotina)
set -euo pipefail

# ==================== CONFIGURAÇÃO ====================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
export PROJECT_ROOT

LOG_LEVEL="${LOG_LEVEL:-INFO}"  # DEBUG, INFO, WARN, ERROR
LOG_FILE="${PROJECT_ROOT}/logs/atual/sessao-atual.log"

# Cores
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

# ==================== LOGGING ====================
log() {
  local level=$1; shift
  local msg="$*"
  local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
  echo -e "${timestamp} [${level}] ${msg}" | tee -a "$LOG_FILE"
  
  case $level in
    DEBUG) [[ "$LOG_LEVEL" == "DEBUG" ]] && echo -e "${YELLOW}[DEBUG]${NC} $msg" ;;
    INFO)  echo -e "${GREEN}[INFO]${NC} $msg" ;;
    WARN)  echo -e "${YELLOW}[WARN]${NC} $msg" ;;
    ERROR) echo -e "${RED}[ERROR]${NC} $msg" >&2 ;;
  esac
}

error() { log "ERROR" "$*"; exit 1; }
success() { log "INFO" "✅ $1"; }
warn() { log "WARN" "$1"; }

# ==================== UTILITÁRIOS ====================
require_command() {
  command -v "$1" >/dev/null 2>&1 || error "Comando '$1' não encontrado. Instale antes de continuar."
}

check_env_file() {
  if [[ ! -f "${PROJECT_ROOT}/.env" ]]; then
    cp "${PROJECT_ROOT}/.env.example" "${PROJECT_ROOT}/.env" 2>/dev/null || warn ".env.example não encontrado. Crie manualmente."
    success ".env criado a partir de .env.example"
  fi
}