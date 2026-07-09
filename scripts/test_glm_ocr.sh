#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "${SCRIPT_DIR}/glm_ocr_lectures.sh" -Lecture "Lecture 3" -Page "01" -Force "$@"
