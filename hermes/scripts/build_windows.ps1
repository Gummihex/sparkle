$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '../apps/client')
flutter pub get
flutter build windows --release
Write-Host 'HERMES Windows build complete.'
