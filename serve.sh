#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PORT="${1:-8080}"
echo "Serving production-ready site at http://127.0.0.1:${PORT}"
python3 -m http.server "$PORT"
