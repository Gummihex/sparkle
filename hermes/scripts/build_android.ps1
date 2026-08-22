$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '../apps/client')
flutter pub get
flutter build apk --release
flutter build appbundle --release
Write-Host 'HERMES Android APK/AAB build complete.'
