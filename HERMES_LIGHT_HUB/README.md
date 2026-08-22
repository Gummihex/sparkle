# HERMES LIGHT HUB

Universal smart-lighting control platform for Windows 11 + Android.

## Mission
One local-first control plane for Philips Hue, Nanoleaf, Govee, Twinkly and other supported lighting ecosystems, with Wi-Fi/LAN, Bluetooth, Matter and official API paths.

## Architecture
- Flutter: Windows 11 + Android UI/client
- Python/FastAPI: local orchestration and WebSocket event bus
- Adapter SDK: manufacturer/protocol isolation
- Discovery: LAN/mDNS/SSDP + BLE + Matter
- Engine: capabilities -> normalized commands -> execution -> state verification
- AI: scene planner, voice intents, automation planner
- Local AI: optional provider with no cloud dependency
- Graph: devices/rooms/groups/LED zones/scenes/automations
- Stats: latency, availability, discovery and adapter health

## Repository modules
See `docs/` for architecture, compatibility, security, build and release plans.

## Rule
Never invent or rely on undocumented proprietary protocols. Use official/current interfaces and explicitly mark unsupported capabilities.

## Status
Foundation branch created; implementation is being built incrementally behind this module boundary.
