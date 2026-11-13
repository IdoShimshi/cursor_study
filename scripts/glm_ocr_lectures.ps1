# Transcribe lecture page PNGs with GLM-OCR via Ollama on Windows.
param(
    [string]$RepoRoot = "",
    [string]$Lecture = "",
    [string]$Page = "",
    [switch]$Force,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$OcrModel = "glm-ocr"
$OcrPrompt = "Text Recognition:"
$RequestTimeoutSec = 600

function Get-RepoRoot {
    param([string]$Root)
    if ($Root) {
        return (Resolve-Path $Root).Path
    }
    return (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
}

function Get-OcrSidecarPath {
    param([string]$ImagePath)
    return [System.IO.Path]::ChangeExtension($ImagePath, ".ocr.md")
}

function Get-OllamaExe {
    $ollama = Join-Path $env:LOCALAPPDATA "Programs\Ollama\ollama.exe"
    if (-not (Test-Path $ollama)) {
        throw "Ollama not found at $ollama"
    }
    return $ollama
}

function Ensure-OllamaModel {
    Write-Host "Checking Ollama server..."
    $tags = Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags" -TimeoutSec 10
    if ($tags.models.name -notcontains "${OcrModel}:latest") {
        Write-Host "Pulling ${OcrModel} model..."
        & (Get-OllamaExe) pull $OcrModel
    }
}

function Invoke-GlmOcr {
    param([string]$ImagePath)

    $bytes = [Convert]::ToBase64String([IO.File]::ReadAllBytes($ImagePath))
    $body = @{
        model  = $OcrModel
        prompt = $OcrPrompt
        images = @($bytes)
        stream = $false
    } | ConvertTo-Json -Depth 3

    $response = Invoke-RestMethod `
        -Uri "http://127.0.0.1:11434/api/generate" `
        -Method Post `
        -Body $body `
        -ContentType "application/json" `
        -TimeoutSec $RequestTimeoutSec

    return (($response.response | Out-String).Trim())
}

function Write-TranscriptionSidecar {
    param(
        [string]$ImagePath,
        [string]$Text
    )

    $outputPath = Get-OcrSidecarPath $ImagePath
    $pageName = [System.IO.Path]::GetFileNameWithoutExtension($ImagePath)
    $lectureName = Split-Path (Split-Path $ImagePath -Parent) -Leaf
    $body = if ($Text) { $Text } else { "*(empty response)*" }

    $markdown = @(
        "# $lectureName - $pageName",
        "",
        "> Ollama glm-ocr, Text Recognition mode.",
        "",
        $body,
        ""
    ) -join [Environment]::NewLine

    Set-Content -Path $outputPath -Value $markdown -Encoding utf8
    return $outputPath
}

function Test-PageMatchesFilter {
    param(
        [string]$FileName,
        [string]$PageFilter
    )

    if (-not $PageFilter) {
        return $true
    }
    if ($PageFilter -match '^\d+$') {
        return $FileName -eq "page-$PageFilter.png" -or $FileName -eq "page-$($PageFilter.PadLeft(2, '0')).png"
    }
    if ($PageFilter -notlike "page-*") {
        return $FileName -like "*$PageFilter*"
    }
    return $FileName -like $PageFilter -or $FileName -like "$PageFilter.png"
}

function Find-LecturePageImages {
    param(
        [string]$LecturesDir,
        [string]$LectureFilter,
        [string]$PageFilter
    )

    $images = @()
    foreach ($assetDir in Get-ChildItem -Path $LecturesDir -Directory | Sort-Object Name) {
        if ($LectureFilter -and $assetDir.Name -notlike "*$LectureFilter*") {
            continue
        }
        foreach ($png in Get-ChildItem -Path $assetDir.FullName -Filter "page-*.png" | Sort-Object Name) {
            if (-not (Test-PageMatchesFilter -FileName $png.Name -PageFilter $PageFilter)) {
                continue
            }
            $images += $png.FullName
        }
    }
    return $images
}

$repoRoot = Get-RepoRoot $RepoRoot
$lecturesDir = Join-Path $repoRoot "courses\semester-2\dynamical-systems\materials\lectures"
if (-not (Test-Path $lecturesDir)) {
    throw "Lectures directory not found: $lecturesDir"
}

$allImages = Find-LecturePageImages -LecturesDir $lecturesDir -LectureFilter $Lecture -PageFilter $Page
if ($allImages.Count -eq 0) {
    Write-Host "No page images found."
    exit 0
}

$pending = @()
$skipped = 0
foreach ($imagePath in $allImages) {
    $sidecar = Get-OcrSidecarPath $imagePath
    if (-not $Force -and (Test-Path $sidecar)) {
        $skipped++
        Write-Host "skip  $sidecar"
        continue
    }
    $pending += $imagePath
}

if ($pending.Count -eq 0) {
    Write-Host "All $($allImages.Count) page(s) already have transcriptions."
    exit 0
}

Write-Host "Found $($pending.Count) page(s) to transcribe ($skipped skipped)."
if ($DryRun) {
    foreach ($imagePath in $pending) {
        Write-Host "pending  $imagePath"
    }
    exit 0
}

Ensure-OllamaModel

$failures = 0
$index = 0
foreach ($imagePath in $pending) {
    $index++
    $relative = $imagePath.Substring($repoRoot.Length).TrimStart('\')
    Write-Host ""
    Write-Host "[$index/$($pending.Count)] $relative"
    $started = Get-Date
    try {
        $text = Invoke-GlmOcr -ImagePath $imagePath
        $outputPath = Write-TranscriptionSidecar -ImagePath $imagePath -Text $text
        $elapsed = (Get-Date) - $started
        Write-Host ("ocr  {0} ({1} chars, {2:mm\:ss})" -f $outputPath, $text.Length, $elapsed)
    } catch {
        $failures++
        Write-Host "fail  $imagePath"
        Write-Host $_.Exception.Message
    }
}

if ($failures -gt 0) {
    Write-Host ""
    Write-Host "$failures page(s) failed."
    exit 1
}

Write-Host ""
Write-Host "Done. Transcribed $($pending.Count) page(s)."
