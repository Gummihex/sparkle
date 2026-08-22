# HERMES LIGHT HUB — Master Plan

## 1. Core
- Unified Device / Capability / State model
- command validation
- room/group/scene graph
- persistence and migrations
- event bus + WebSocket updates

## 2. Discovery
- Wi-Fi/LAN: mDNS, SSDP and manufacturer-supported local discovery
- BLE: platform-native scanning through Flutter/native bridge; backend Bleak where appropriate on Windows
- Matter: official Matter commissioning and controller stack
- Meta: discover only supported Meta devices/interfaces; never claim generic Bluetooth visibility equals device control
- Manual IP/QR pairing fallback

## 3. Adapters
- Philips Hue: Bridge/local API integration
- Nanoleaf: supported local OpenAPI and model-specific capabilities
- Govee: official developer/local interfaces according to model
- Twinkly: supported official/current interface only
- Matter generic adapter
- BLE generic adapter

## 4. UX
- command-center dashboard
- device cards with capability badges
- room topology
- discovery center
- scene editor
- effect timeline
- LED mapping view
- diagnostics

## 5. AI pipeline
`natural language -> intent -> entity resolution -> capability check -> safe plan -> preview -> execute -> audit`

AI must never directly issue an unvalidated hardware command. A deterministic policy layer checks device capabilities, ranges and authorization first.

## 6. Local AI
Provider interface supports local models through an OpenAI-compatible local endpoint or another explicit provider. The app works fully without AI.

## 7. Screen/Music Sync
- Windows capture service
- zone extraction
- color palette / luminance analysis
- audio FFT / beat detection
- rate limiting and device batching

## 8. Graph
Nodes: device, room, group, scene, automation, LED zone, screen zone.
Edges: belongs-to, grouped-with, participates-in, mapped-to, triggers, mirrors.

## 9. Stats
- discovery duration
- command latency
- adapter errors
- reconnect count
- online ratio
- CPU/RAM/network
- per-device update rate

## 10. Release
- CI lint/test
- Windows portable/release package
- signed installer
- Android APK/AAB
- release notes + checksums
- no secrets in repository
