# Build / Install / Release Plan

## Windows 11
Flutter Windows release + bundled/local FastAPI service. Package as MSIX or EXE. Provide first-run wizard, optional startup, system tray and LAN pairing. Do not require public Internet exposure.

## Android
Flutter release APK. Use Android Keystore-backed secure storage and only required Nearby Devices/network/notification permissions. Pair with the local HERMES instance using QR/temporary code.

## CI
GitHub Actions should run: Flutter format/analyze/test; Python compile/lint/test; Windows build on Windows runner; Android build on Android-capable runner. Release workflow attaches installer/APK and SHA256SUMS.

## Versioning
Semantic versioning. `main` is releasable; feature branches and PRs for changes. Tag releases as `vX.Y.Z`.

## Installer behavior
Never overwrite user configuration silently. Offer backup/migration. Never package secrets or developer API keys.
