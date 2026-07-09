#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PS_SCRIPT="${SCRIPT_DIR}/glm_ocr_lectures.ps1"

if ! command -v powershell.exe >/dev/null 2>&1; then
  echo "powershell.exe not found. GLM-OCR runs via Ollama on Windows." >&2
  exit 1
fi

if ! command -v wslpath >/dev/null 2>&1; then
  echo "wslpath not found; cannot translate paths for Windows PowerShell." >&2
  exit 1
fi

WIN_PS_SCRIPT="$(wslpath -w "${PS_SCRIPT}")"
WIN_REPO_ROOT="$(wslpath -w "${REPO_ROOT}")"

exec powershell.exe -NoProfile -ExecutionPolicy Bypass -File "${WIN_PS_SCRIPT}" -RepoRoot "${WIN_REPO_ROOT}" "$@"
