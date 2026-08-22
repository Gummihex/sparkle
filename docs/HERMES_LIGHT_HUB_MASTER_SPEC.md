# HERMES LIGHT HUB — Master Project Specification

## Objective
Universal local-first smart-lighting control center for Windows 11 and Android. One Flutter client codebase, Python/FastAPI orchestration backend, native platform bridges where required.

## Core integrations
- Philips Hue: official local/developer mechanisms; capability-driven.
- Nanoleaf: official local OpenAPI where supported.
- Govee: official developer API where applicable; respect rate limits.
- Twinkly: adapter boundary only until a currently supported official interface is verified; never invent or bypass an API.
- Matter: architecture for discovery/commissioning/control using a supported SDK.
- Bluetooth: transport/discovery layer; only control devices with a known supported protocol.
- Meta/Home: compatibility detector based on real supported paths (e.g. Matter), never guessed.

## Modules
Dashboard, Devices, Rooms, Groups, Scenes, Effects, Automations, Discovery Center, Screen Sync, Music Sync, LED Mapping, AI, Local AI provider interface, Diagnostics, Network Graph, Stats, Compatibility Matrix, Backup/Restore, Plugin System.

## Architecture
Flutter -> REST/WebSocket -> FastAPI -> Light Engine -> Integration Adapters -> Devices.
Local-first. Backend binds to localhost by default. LAN access is explicit. No automatic router port forwarding.

## Unified model
Device(id,name,manufacturer,model,firmware,protocols,connection,room,groups,capabilities,state,metadata). Capabilities are dynamic; unsupported operations must produce structured errors.

## Discovery
Providers: LAN/mDNS/SSDP/BLE/Matter/manufacturer/manual-IP. Discovery results include IP, hostname, manufacturer, model, protocols, capabilities and confidence. Discovery is controlled and user-authorized; no aggressive scanning.

## AI pipeline
Natural-language request -> intent parser -> capability validator -> permission validator -> command plan -> adapter execution -> state/event update. Providers are abstracted so local models and cloud models can be swapped. AI cannot execute arbitrary OS commands.

## Local AI
Optional provider interface for Ollama/llama.cpp/other local runtimes. No provider is mandatory for the core app.

## Screen/Music Sync
Windows-local processing. Screen capture/audio analysis stays local by default. Zone mapping translates analyzed colors/features into light commands with rate limiting and smoothing.

## Graph
Model relations: device -> room -> group -> scene -> automation and device -> physical/LED layout -> screen zone. UI graph is diagnostic/visualization, not the source of truth.

## Stats
Collect non-secret local metrics: device latency, online/offline counts, command rate, adapter errors, discovery duration, backend CPU/memory where available. Never log credentials/tokens.

## Releases
Outputs: Windows installer (MSIX/EXE), Android release APK, debug APK, SHA256SUMS, release notes. GitHub Actions should lint/test/build both targets where runners permit.

## Documentation
README, architecture, API, integration setup, security, Windows, Android, discovery, troubleshooting, compatibility matrix, user manual and release notes.

## Delivery phases
1. architecture + simulation
2. backend + Flutter shell
3. discovery
4. Hue/Nanoleaf/Govee
5. Matter/BLE
6. scenes/groups/rooms/effects
7. automation
8. Screen/Music Sync
9. AI/local AI
10. graph/stats/diagnostics
11. installers/APK
12. hardware verification

## Quality gate
No fake hardware control. No undocumented API claims. Run formatting, lint, unit/integration tests, build verification and simulation tests before release.
