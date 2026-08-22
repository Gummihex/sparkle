# HERMES LIGHT HUB

Universal local-first smart-lighting control platform for Windows 11 + Android.

## Scope
- Philips Hue
- Nanoleaf
- Govee
- Twinkly
- Matter-capable devices
- Bluetooth Low Energy discovery
- Wi-Fi/LAN discovery
- Optional Meta-device discovery through supported platform/network interfaces
- Scenes, rooms, groups, automations, screen sync and music sync
- AI scene generation with optional local model

## Architecture
`Flutter` client -> `FastAPI` orchestration service -> `Discovery + Adapter` layer -> physical devices.

The adapter layer is capability-driven. Unsupported operations are rejected explicitly rather than guessed. Manufacturer APIs and protocols must be verified against current official documentation before production integration.

## Repository map
- `backend/` FastAPI core, models, discovery and adapters
- `apps/client/` Flutter Windows/Android client
- `docs/` architecture, security, compatibility and user documentation
- `scripts/` build/install/release helpers
- `.github/workflows/` CI/CD

## Development
Python 3.12+, Flutter 3.x, Android SDK, Windows desktop tooling.

```powershell
cd hermes/backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8765
```

```powershell
cd hermes/apps/client
flutter pub get
flutter run -d windows
# Android: flutter run -d <android-device>
```
