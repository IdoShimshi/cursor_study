#Requires -Version 5.1

param (
    [Parameter()]
    [string]
    $RepoRoot,

    [Parameter()]
    [string]
    $ConfigPath,

    [Parameter()]
    [string]
    $CourseRoot,

    [Parameter()]
    [Alias('List')]
    [switch]
    $ShowCatalog,

    [Parameter()]
    [switch]
    $DryRun,

    [Parameter()]
    [switch]
    $ReexportAll
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$Script:HierarchyScopePages = 4
$Script:PublishFormatPdf = 'pfPDF'

function Get-NormalPath {
    param([string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) {
        return $Path
    }

    if (Test-Path -LiteralPath $Path) {
        $resolved = (Resolve-Path -LiteralPath $Path).Path
    }
    else {
        $parent = [System.IO.Path]::GetDirectoryName($Path)
        $leaf = [System.IO.Path]::GetFileName($Path)
        if ($parent -and (Test-Path -LiteralPath $parent)) {
            $resolved = Join-Path (Resolve-Path -LiteralPath $parent).Path $leaf
        }
        else {
            $resolved = $Path
        }
    }

    if ($resolved -match '::(.+)$') {
        return $Matches[1]
    }

    return $resolved
}

function Write-Info {
    param([string]$Message)
    Write-Host $Message
}

function Write-Warn {
    param([string]$Message)
    Write-Warning $Message
}

function Get-RepoRoot {
    param([string]$ProvidedRoot)

    if ($ProvidedRoot) {
        return (Resolve-Path -LiteralPath $ProvidedRoot).Path
    }

    return (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
}

function Get-ConfigPath {
    param(
        [string]$ProvidedConfigPath,
        [string]$Root
    )

    if ($ProvidedConfigPath) {
        return (Resolve-Path -LiteralPath $ProvidedConfigPath).Path
    }

    return (Join-Path $Root 'courses/dynamical-systems/onenote_export_config.json')
}

function Read-ExportConfig {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Config file not found: $Path"
    }

    $raw = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    return ($raw | ConvertFrom-Json)
}

function Connect-OneNote {
    try {
        return New-Object -ComObject OneNote.Application
    }
    catch {
        throw "Could not connect to OneNote. Install OneNote desktop for Windows and open your notebook at least once. $($_.Exception.Message)"
    }
}

function Get-OneNoteHierarchyXml {
    param([object]$OneNoteConnection)

    $xml = ''
    $OneNoteConnection.GetHierarchy('', $Script:HierarchyScopePages, [ref]$xml) | Out-Null
    return ([xml]$xml)
}

function Get-XmlChildElements {
    param(
        [object]$Parent,
        [string]$LocalName
    )

    if ($null -eq $Parent) {
        return @()
    }

    return @(
        $Parent.ChildNodes |
            Where-Object { $_.NodeType -eq 'Element' -and $_.LocalName -ieq $LocalName }
    )
}

function Get-XmlAttributeValue {
    param(
        [object]$Node,
        [string]$Name
    )

    if ($null -eq $Node) {
        return ''
    }

    $attribute = $Node.Attributes | Where-Object { $_.LocalName -ieq $Name } | Select-Object -First 1
    if ($attribute) {
        return [string]$attribute.Value
    }

    return ''
}

function Test-NameMatch {
    param(
        [string]$Candidate,
        [string]$Pattern,
        [string]$Mode
    )

    if ([string]::IsNullOrWhiteSpace($Candidate) -or [string]::IsNullOrWhiteSpace($Pattern)) {
        return $false
    }

    switch ($Mode) {
        'exact' { return ($Candidate -eq $Pattern) }
        'ignorecase' { return ($Candidate -ieq $Pattern) }
        default { return ($Candidate -like "*$Pattern*") }
    }
}

function Add-SectionsFromNode {
    param(
        [object]$Node,
        [string[]]$GroupPath,
        [System.Collections.Generic.List[object]]$Accumulator
    )

    if ($null -eq $Node) {
        return
    }

    foreach ($section in Get-XmlChildElements -Parent $Node -LocalName 'Section') {
        $Accumulator.Add([pscustomobject]@{
                Section = $section
                GroupPath = ($GroupPath -join ' / ')
            }) | Out-Null
    }

    foreach ($sectionGroup in Get-XmlChildElements -Parent $Node -LocalName 'SectionGroup') {
        $groupName = Get-XmlAttributeValue -Node $sectionGroup -Name 'name'
        $nestedPath = @($GroupPath) + @($groupName)
        Add-SectionsFromNode -Node $sectionGroup -GroupPath $nestedPath -Accumulator $Accumulator
    }
}

function Get-NotebookNodes {
    param([xml]$Hierarchy)

    $root = $Hierarchy.DocumentElement
    if ($root.LocalName -ieq 'oneNote') {
        $notebooksContainer = Get-XmlChildElements -Parent $root -LocalName 'notebooks' | Select-Object -First 1
        return @(Get-XmlChildElements -Parent $notebooksContainer -LocalName 'notebook')
    }

    if ($root.LocalName -ieq 'Notebooks') {
        return @(Get-XmlChildElements -Parent $root -LocalName 'Notebook')
    }

    return @($Hierarchy.SelectNodes("//*[local-name()='Notebook' or local-name()='notebook']"))
}

function Get-SectionsForNotebook {
    param([object]$Notebook)

    $sections = [System.Collections.Generic.List[object]]::new()
    Add-SectionsFromNode -Node $Notebook -GroupPath @() -Accumulator $sections
    return $sections
}

function Test-SectionGroupMatch {
    param(
        [string]$GroupPath,
        [string]$Pattern,
        [string]$Mode
    )

    if ([string]::IsNullOrWhiteSpace($Pattern)) {
        return $true
    }

    return (Test-NameMatch -Candidate $GroupPath -Pattern $Pattern -Mode $Mode)
}

function Get-PageNodes {
    param(
        [object]$Section,
        [bool]$IncludeSubpages
    )

    $pages = @(Get-XmlChildElements -Parent $Section -LocalName 'Page')
    if ($IncludeSubpages) {
        return $pages
    }

    return @(
        $pages | Where-Object {
            (Get-XmlAttributeValue -Node $_ -Name 'isSubpage') -ne 'true'
        }
    )
}

function Convert-OneNoteTimestamp {
    param([string]$Timestamp)

    if ([string]::IsNullOrWhiteSpace($Timestamp)) {
        return $null
    }

    return [datetime]::ParseExact(
        $Timestamp,
        'yyyy-MM-ddTHH:mm:ss.fffZ',
        [System.Globalization.CultureInfo]::InvariantCulture,
        [System.Globalization.DateTimeStyles]::AssumeUniversal -bor [System.Globalization.DateTimeStyles]::AdjustToUniversal
    )
}

function Get-SafeFileStem {
    param(
        [string]$PageTitle,
        [datetime]$LastModifiedUtc
    )

    $datePrefix = $LastModifiedUtc.ToString('yyyy-MM-dd')
    $title = if ([string]::IsNullOrWhiteSpace($PageTitle)) { 'untitled' } else { $PageTitle.Trim() }
    $invalidChars = [IO.Path]::GetInvalidFileNameChars()
    $pattern = '[{0}]+' -f [Regex]::Escape(-join $invalidChars)
    $safeTitle = [Regex]::Replace($title, $pattern, '_').Trim('_')

    if ([string]::IsNullOrWhiteSpace($safeTitle)) {
        $safeTitle = 'untitled'
    }

    if ($safeTitle.Length -gt 80) {
        $safeTitle = $safeTitle.Substring(0, 80).Trim('_')
    }

    return "${datePrefix}_${safeTitle}"
}

function Get-UniquePdfPath {
    param(
        [string]$OutputDirectory,
        [string]$FileStem
    )

    $candidate = Join-Path $OutputDirectory "$FileStem.pdf"
    if (-not (Test-Path -LiteralPath $candidate)) {
        return $candidate
    }

    $suffix = 2
    while ($true) {
        $candidate = Join-Path $OutputDirectory "${FileStem}_${suffix}.pdf"
        if (-not (Test-Path -LiteralPath $candidate)) {
            return $candidate
        }
        $suffix++
    }
}

function Read-ExportState {
    param([string]$StatePath)

    if (-not (Test-Path -LiteralPath $StatePath)) {
        return [ordered]@{
            version = 1
            sectionId = ''
            pages = @{}
        }
    }

    $raw = Get-Content -LiteralPath $StatePath -Raw -Encoding UTF8
    $parsed = $raw | ConvertFrom-Json

    $pages = @{}
    if ($parsed.pages) {
        foreach ($property in $parsed.pages.PSObject.Properties) {
            $pages[$property.Name] = $property.Value
        }
    }

    return [ordered]@{
        version = 1
        sectionId = [string]$parsed.sectionId
        pages = $pages
    }
}

function Write-ExportState {
    param(
        [string]$StatePath,
        [hashtable]$State
    )

    $pagesObject = [ordered]@{}
    foreach ($entry in ($State.pages.GetEnumerator() | Sort-Object Name)) {
        $pagesObject[$entry.Key] = $entry.Value
    }

    $payload = [ordered]@{
        version = 1
        sectionId = $State.sectionId
        pages = $pagesObject
    }

    $json = $payload | ConvertTo-Json -Depth 6
    Set-Content -LiteralPath $StatePath -Value $json -Encoding UTF8
}

function Remove-FileIfExists {
    param([string]$Path)

    if ([System.IO.File]::Exists($Path)) {
        [System.IO.File]::Delete($Path)
    }
}

function Remove-DirectoryIfExists {
    param([string]$Path)

    if ([System.IO.Directory]::Exists($Path)) {
        [System.IO.Directory]::Delete($Path, $true)
    }
}

function Remove-LectureArtifacts {
    param(
        [string]$OutputDirectory,
        [string]$PdfFileName
    )

    if ([string]::IsNullOrWhiteSpace($PdfFileName)) {
        return
    }

    $pdfPath = Join-Path $OutputDirectory $PdfFileName
    Remove-FileIfExists -Path $pdfPath

    $assetDir = Join-Path $OutputDirectory ([System.IO.Path]::GetFileNameWithoutExtension($PdfFileName))
    Remove-DirectoryIfExists -Path $assetDir
}

function Remove-OrphanLectureFolders {
    param([string]$OutputDirectory)

    $pdfStems = @{}
    foreach ($pdfPath in [System.IO.Directory]::GetFiles($OutputDirectory, '*.pdf')) {
        $stem = [System.IO.Path]::GetFileNameWithoutExtension($pdfPath)
        $pdfStems[$stem] = $true
    }

    foreach ($dirPath in [System.IO.Directory]::GetDirectories($OutputDirectory)) {
        $dirName = [System.IO.Path]::GetFileName($dirPath)
        if ($dirName.StartsWith('.')) {
            continue
        }
        if ($pdfStems.ContainsKey($dirName)) {
            continue
        }

        $hasManifest = Test-Path -LiteralPath (Join-Path $dirPath 'manifest.json')
        $hasPages = ([System.IO.Directory]::GetFiles($dirPath, 'page-*.png')).Count -gt 0
        if (-not $hasManifest -and -not $hasPages) {
            continue
        }

        Remove-DirectoryIfExists -Path $dirPath
        Write-Info ("  remove  {0}/ (orphan)" -f $dirName)
    }
}

function Ensure-Directory {
    param([string]$Path)

    if (-not [System.IO.Directory]::Exists($Path)) {
        [void][System.IO.Directory]::CreateDirectory($Path)
    }
}

function Move-FileForce {
    param(
        [string]$Source,
        [string]$Destination
    )

    Remove-FileIfExists -Path $Destination
    [System.IO.File]::Move($Source, $Destination)
}

function Show-OneNoteCatalog {
    param([xml]$Hierarchy)

    Write-Info 'Open OneNote notebooks and sections:'
    foreach ($notebook in Get-NotebookNodes -Hierarchy $Hierarchy) {
        Write-Info ("  Notebook: {0}" -f (Get-XmlAttributeValue -Node $notebook -Name 'name'))
        foreach ($entry in Get-SectionsForNotebook -Notebook $notebook) {
            $pageCount = (@(Get-PageNodes -Section $entry.Section -IncludeSubpages:$true)).Count
            $sectionName = Get-XmlAttributeValue -Node $entry.Section -Name 'name'
            $location = if ($entry.GroupPath) { "$($entry.GroupPath) / $sectionName" } else { $sectionName }
            Write-Info ("    {0} ({1} pages)" -f $location, $pageCount)
        }
    }
}

function Find-TargetSection {
    param(
        [xml]$Hierarchy,
        [object]$Config
    )

    $matches = @()
    foreach ($notebook in Get-NotebookNodes -Hierarchy $Hierarchy) {
        $notebookName = Get-XmlAttributeValue -Node $notebook -Name 'name'
        if (-not (Test-NameMatch -Candidate $notebookName -Pattern $Config.notebookName -Mode $Config.matchMode)) {
            continue
        }

        foreach ($entry in Get-SectionsForNotebook -Notebook $notebook) {
            $section = $entry.Section
            $sectionName = Get-XmlAttributeValue -Node $section -Name 'name'
            if (-not (Test-NameMatch -Candidate $sectionName -Pattern $Config.sectionName -Mode $Config.matchMode)) {
                continue
            }

            if (-not (Test-SectionGroupMatch -GroupPath $entry.GroupPath -Pattern $Config.sectionGroupName -Mode $Config.matchMode)) {
                continue
            }

            $matches += [pscustomobject]@{
                NotebookName = $notebookName
                SectionGroupPath = [string]$entry.GroupPath
                SectionName = $sectionName
                Section = $section
            }
        }
    }

    return $matches
}

function Sync-OneNoteLectures {
    param(
        [object]$Config,
        [string]$Root,
        [string]$CourseRoot,
        [switch]$DryRun,
        [switch]$ReexportAll
    )

    $outputDirectory = if ($CourseRoot) {
        Get-NormalPath -Path (Join-Path $CourseRoot 'materials/lectures')
    } else {
        Get-NormalPath -Path (Join-Path $Root 'courses/dynamical-systems/materials/lectures')
    }
    $statePath = Join-Path $outputDirectory '.export_state.json'
    $oneNote = Connect-OneNote

    try {
        $hierarchy = Get-OneNoteHierarchyXml -OneNoteConnection $oneNote
        $targets = @(Find-TargetSection -Hierarchy $hierarchy -Config $Config)

        if ($targets.Count -eq 0) {
            $groupHint = if ($Config.sectionGroupName) { " / group '$($Config.sectionGroupName)'" } else { '' }
            throw "No section matched notebook '$($Config.notebookName)'$groupHint / section '$($Config.sectionName)'. Run with -ShowCatalog to see available names."
        }

        if ($targets.Count -gt 1) {
            $names = ($targets | ForEach-Object {
                    if ($_.SectionGroupPath) { "$($_.NotebookName) / $($_.SectionGroupPath) / $($_.SectionName)" }
                    else { "$($_.NotebookName) / $($_.SectionName)" }
                }) -join '; '
            throw "Multiple sections matched. Narrow notebookName, sectionGroupName, or sectionName in config. Matches: $names"
        }

        $target = $targets[0]
        $section = $target.Section
        $includeSubpages = [bool]$Config.includeSubpages
        $pages = @(Get-PageNodes -Section $section -IncludeSubpages:$includeSubpages)

        if ($pages.Count -eq 0) {
            Write-Warn "Section '$($target.SectionName)' has no pages to export."
            return
        }

        if (-not (Test-Path -LiteralPath $outputDirectory)) {
            if ($DryRun) {
                Write-Info "Would create output directory: $outputDirectory"
            }
            else {
                Ensure-Directory -Path $outputDirectory
            }
        }

        $state = Read-ExportState -StatePath $statePath
        $state.sectionId = Get-XmlAttributeValue -Node $section -Name 'ID'
        $exportedCount = 0
        $skippedCount = 0

        Write-Info ("Notebook: {0}" -f $target.NotebookName)
        if ($target.SectionGroupPath) {
            Write-Info ("Group:    {0}" -f $target.SectionGroupPath)
        }
        Write-Info ("Section:  {0}" -f $target.SectionName)
        Write-Info ("Pages:    {0}" -f $pages.Count)
        Write-Info ("Output:   {0}" -f $outputDirectory)

        foreach ($page in $pages) {
            $pageId = Get-XmlAttributeValue -Node $page -Name 'ID'
            $pageTitle = Get-XmlAttributeValue -Node $page -Name 'name'
            $lastModifiedUtc = Convert-OneNoteTimestamp -Timestamp (Get-XmlAttributeValue -Node $page -Name 'lastModifiedTime')
            if (-not $lastModifiedUtc) {
                throw "Page '$pageTitle' is missing lastModifiedTime."
            }

            $lastModifiedIso = $lastModifiedUtc.ToString('o')
            $previous = $state.pages[$pageId]
            $needsExport = $ReexportAll -or (-not $previous) -or ($previous.lastModifiedTime -ne $lastModifiedIso)

            if (-not $needsExport) {
                $skippedCount++
                Write-Info ("  skip  {0}" -f $pageTitle)
                continue
            }

            $fileStem = Get-SafeFileStem -PageTitle $pageTitle -LastModifiedUtc $lastModifiedUtc
            $pdfPath = Get-UniquePdfPath -OutputDirectory $outputDirectory -FileStem $fileStem
            $pdfName = [System.IO.Path]::GetFileName($pdfPath)

            if ($DryRun) {
                $action = if ($previous) { 'update' } else { 'export' }
                Write-Info ("  {0}  {1} -> {2}" -f $action, $pageTitle, $pdfName)
                $exportedCount++
                continue
            }

            Write-Info ("  export  {0} -> {1}" -f $pageTitle, $pdfName)
            $destinationPath = Get-NormalPath -Path $pdfPath
            $parentDir = [System.IO.Path]::GetDirectoryName($destinationPath)
            Ensure-Directory -Path $parentDir
            Remove-FileIfExists -Path $destinationPath
            $tempPdfPath = Join-Path $env:TEMP ("onenote_export_{0}.pdf" -f [Guid]::NewGuid().ToString('N'))
            try {
                [void]$oneNote.Publish([string]$pageId, [string]$tempPdfPath, [string]'pfPDF', [string]::Empty)
                if (-not (Test-Path -LiteralPath $tempPdfPath)) {
                    throw "OneNote did not create PDF at $tempPdfPath"
                }
                Move-FileForce -Source $tempPdfPath -Destination $destinationPath
            }
            catch {
                throw "Failed to export '$pageTitle' to PDF: $($_.Exception.Message)"
            }
            finally {
                Remove-FileIfExists -Path $tempPdfPath
            }

            if ($previous -and $previous.pdfFile -and $previous.pdfFile -ne $pdfName) {
                Remove-LectureArtifacts -OutputDirectory $outputDirectory -PdfFileName $previous.pdfFile
                Write-Info ("  remove  {0}" -f $previous.pdfFile)
            }

            $state.pages[$pageId] = [ordered]@{
                title = $pageTitle
                lastModifiedTime = $lastModifiedIso
                pdfFile = $pdfName
                exportedAt = (Get-Date).ToUniversalTime().ToString('o')
            }
            $exportedCount++
        }

        $knownPageIds = @($pages | ForEach-Object { Get-XmlAttributeValue -Node $_ -Name 'ID' })
        foreach ($existingId in @($state.pages.Keys)) {
            if ($existingId -notin $knownPageIds) {
                $removed = $state.pages[$existingId]
                if ($removed.pdfFile) {
                    if (-not $DryRun) {
                        Remove-LectureArtifacts -OutputDirectory $outputDirectory -PdfFileName $removed.pdfFile
                    }
                    Write-Info ("  remove  {0}" -f $removed.pdfFile)
                }
                $state.pages.Remove($existingId) | Out-Null
            }
        }

        if (-not $DryRun) {
            Remove-OrphanLectureFolders -OutputDirectory $outputDirectory
            Write-ExportState -StatePath $statePath -State $state
        }

        Write-Info ("Done. Exported: {0}, skipped (unchanged): {1}." -f $exportedCount, $skippedCount)
    }
    finally {
        if ($oneNote) {
            [System.Runtime.InteropServices.Marshal]::ReleaseComObject($oneNote) | Out-Null
        }
    }
}

$resolvedRoot = Get-RepoRoot -ProvidedRoot $RepoRoot
$resolvedConfigPath = Get-ConfigPath -ProvidedConfigPath $ConfigPath -Root $resolvedRoot
$config = Read-ExportConfig -Path $resolvedConfigPath

if (-not $config.matchMode) {
    $config | Add-Member -NotePropertyName matchMode -NotePropertyValue 'contains' -Force
}

if ($null -eq $config.includeSubpages) {
    $config | Add-Member -NotePropertyName includeSubpages -NotePropertyValue $false -Force
}

if (-not ($config.PSObject.Properties.Name -contains 'sectionGroupName')) {
    $config | Add-Member -NotePropertyName sectionGroupName -NotePropertyValue '' -Force
}

if ($ShowCatalog) {
    $oneNote = Connect-OneNote
    try {
        $hierarchy = Get-OneNoteHierarchyXml -OneNoteConnection $oneNote
        Show-OneNoteCatalog -Hierarchy $hierarchy
    }
    finally {
        if ($oneNote) {
            [System.Runtime.InteropServices.Marshal]::ReleaseComObject($oneNote) | Out-Null
        }
    }
    exit 0
}

Sync-OneNoteLectures -Config $config -Root $resolvedRoot -CourseRoot $CourseRoot -DryRun:$DryRun -ReexportAll:$ReexportAll
