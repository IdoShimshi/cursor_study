#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "${SCRIPT_DIR}/gemini_ocr_lectures.sh" --lecture "Lecture 8" --page "03" --force "$@"
