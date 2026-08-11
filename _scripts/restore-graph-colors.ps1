<#
Applies the Molecular Notes color groups (atoms / molecules / topics /
sources) to .obsidian/graph.json.

.obsidian/graph.json is gitignored (it also stores per-session state like
zoom/pan/search, which would otherwise create noise on every commit). So
a fresh clone has no graph.json, and Obsidian creates a colorless default
on first open. This script applies the color groups from
_scripts/graph-colors.json on top of whatever graph.json currently exists
(or creates it if missing), without touching other settings.

Usage:
  1. Fully quit Obsidian (not just close the window/vault).
  2. Run this script:  pwsh ./restore-graph-colors.ps1
  3. (Re)open the vault in Obsidian.

If colors ever look grey again (e.g. after Obsidian resets the file on
some future "first open"), just re-run this script the same way.
#>

$seedPath  = Join-Path $PSScriptRoot "graph-colors.json"
$graphPath = Join-Path $PSScriptRoot "..\.obsidian\graph.json"

$seed = Get-Content -LiteralPath $seedPath -Raw | ConvertFrom-Json

if (Test-Path -LiteralPath $graphPath) {
    $json = Get-Content -LiteralPath $graphPath -Raw | ConvertFrom-Json
} else {
    $json = [pscustomobject]@{}
}

$json | Add-Member -NotePropertyName 'collapse-color-groups' -NotePropertyValue $seed.'collapse-color-groups' -Force
$json | Add-Member -NotePropertyName 'colorGroups' -NotePropertyValue $seed.colorGroups -Force

$graphDir = Split-Path -Parent $graphPath
if (-not (Test-Path -LiteralPath $graphDir)) {
    New-Item -ItemType Directory -Path $graphDir -Force | Out-Null
}

$json | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $graphPath -Encoding UTF8

Write-Host "Graph color groups applied ($graphPath)."
Write-Host "Make sure Obsidian is fully closed, then (re)open the vault."
