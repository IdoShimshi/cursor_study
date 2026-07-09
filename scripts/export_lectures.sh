#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PS_SCRIPT="${SCRIPT_DIR}/export_onenote_lectures.ps1"

if ! command -v powershell.exe >/dev/null 2>&1; then
  echo "powershell.exe not found."
  echo "This exporter runs OneNote's Windows desktop API. From WSL, install/use Windows PowerShell and OneNote desktop."
  echo "You can also run scripts/export_onenote_lectures.ps1 directly in Windows PowerShell 5.1+."
  exit 1
fi

if ! command -v wslpath >/dev/null 2>&1; then
  echo "wslpath not found; cannot translate paths for Windows PowerShell."
  exit 1
fi

WIN_PS_SCRIPT="$(wslpath -w "${PS_SCRIPT}")"
WIN_REPO_ROOT="$(wslpath -w "${REPO_ROOT}")"

should_process=true
for arg in "$@"; do
  case "${arg}" in
    -DryRun|-Preview|-ShowCatalog|-List)
      should_process=false
      ;;
  esac
done

# Auto-detect course: if onenote_export_config.json exists in CWD, use it.
# This makes the script work from any course folder without extra params.
COURSE_CONFIG="${PWD}/onenote_export_config.json"

if [[ -f "${COURSE_CONFIG}" ]]; then
  WIN_CONFIG_PATH="$(wslpath -w "${COURSE_CONFIG}")"
  WIN_COURSE_ROOT="$(wslpath -w "${PWD}")"
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File "${WIN_PS_SCRIPT}" \
    -RepoRoot "${WIN_REPO_ROOT}" \
    -ConfigPath "${WIN_CONFIG_PATH}" \
    -CourseRoot "${WIN_COURSE_ROOT}" \
    "$@"
  if [[ "${should_process}" == true ]]; then
    chmod +x "${SCRIPT_DIR}/process_lectures.sh" 2>/dev/null || true
    "${SCRIPT_DIR}/process_lectures.sh" --lectures-dir "${PWD}/materials/lectures"
    chmod +x "${SCRIPT_DIR}/gemini_ocr_lectures.sh" 2>/dev/null || true
    "${SCRIPT_DIR}/gemini_ocr_lectures.sh" --lectures-dir "${PWD}/materials/lectures" --sync
  fi
else
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File "${WIN_PS_SCRIPT}" \
    -RepoRoot "${WIN_REPO_ROOT}" \
    "$@"
  if [[ "${should_process}" == true ]]; then
    chmod +x "${SCRIPT_DIR}/process_lectures.sh" 2>/dev/null || true
    "${SCRIPT_DIR}/process_lectures.sh"
    chmod +x "${SCRIPT_DIR}/gemini_ocr_lectures.sh" 2>/dev/null || true
    "${SCRIPT_DIR}/gemini_ocr_lectures.sh" --sync
  fi
fi
