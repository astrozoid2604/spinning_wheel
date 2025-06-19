[CmdletBinding()]
param(
    [Parameter(Mandatory=$true, HelpMessage='How many hours should the jiggle run?')]
    [ValidateRange(0.01, 1000)]
    [double]$Hours
)

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$period = 5
$endTime = (Get-Date).AddHours($Hours)
$moveRight = $true

Write-Host "Starting KeepAwake. Will run until $endTime.`n"

while ((Get-Date) -lt $endTime) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] Mouse jiggle performed."

    $p = [System.Windows.Forms.Cursor]::Position
    $delta = if ($moveRight) { 1 } else { -1 }
    [System.Windows.Forms.Cursor]::Position = `
        New-Object System.Drawing.Point ($p.X + $delta), $p.Y
    $moveRight = -not $moveRight

    Start-Sleep -Seconds $period
}

Write-Host "`nKeepAwake session completed at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')."


# powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Desktop\spinning_wheel\keep_awake\keep_awake.ps1 -Hours 24
