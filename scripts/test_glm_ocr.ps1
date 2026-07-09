# Single-page GLM-OCR smoke test (Lecture 3 page 1).
param(
    [string]$RepoRoot = "",
    [switch]$DryRun
)

$batchScript = Join-Path $PSScriptRoot "glm_ocr_lectures.ps1"
$params = @{
    RepoRoot = $RepoRoot
    Lecture  = "Lecture 3"
    Page     = "01"
    Force    = $true
}
if ($DryRun) {
    $params.DryRun = $true
}
& $batchScript @params
