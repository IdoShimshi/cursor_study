#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="${SCRIPT_DIR}/.venv-lectures"
PYTHON="${VENV}/bin/python"
PIP="${VENV}/bin/pip"

if [[ ! -x "${PYTHON}" ]]; then
  python3 -m venv "${VENV}"
  "${PIP}" install -r "${SCRIPT_DIR}/requirements-lectures.txt"
fi

exec "${PYTHON}" "${SCRIPT_DIR}/process_lecture_pdfs.py" "$@"
