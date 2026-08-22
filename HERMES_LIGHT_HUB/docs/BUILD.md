# Build matrix

## Windows 11
Flutter Windows desktop client + FastAPI local service. Package with a Windows installer after integration tests pass. Native Windows components handle local networking/BLE as required.

## Android
Flutter Android app. Native Android bridge handles BLE permissions/scanning and Matter commissioning where supported. Android should be able to discover/control locally while a Windows controller is available.

## CI
Required jobs:
- lint/test backend
- Flutter analyze/test
- Windows build
- Android APK/AAB build
- artifact checksums
- release notes

Secrets must never be committed. Production signing keys remain in GitHub Actions secrets or an external signing service.
