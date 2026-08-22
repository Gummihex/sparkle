# HERMES roadmap

## Phase 0 — Foundation
- [x] repository branch
- [x] architecture specification
- [x] normalized device/capability model
- [x] adapter contract
- [x] simulation mode

## Phase 1 — Core
- [ ] persistent SQLite database + migrations
- [ ] device registry
- [ ] room/group/scene model
- [ ] command queue
- [ ] event bus
- [ ] reconnect/backoff

## Phase 2 — Discovery
- [ ] LAN/mDNS/SSDP discovery
- [ ] native Android BLE discovery
- [ ] Windows BLE discovery
- [ ] Matter commissioning/discovery
- [ ] pairing wizard + QR where supported
- [ ] duplicate-device reconciliation

## Phase 3 — Vendor adapters
- [ ] Philips Hue official/local integration
- [ ] Nanoleaf official/local integration
- [ ] Govee official/current API integration
- [ ] Twinkly official/current interface verification and adapter
- [ ] generic Matter adapter

## Phase 4 — Light Engine
- [ ] normalized power/brightness/RGB/CCT/effect commands
- [ ] scenes
- [ ] transitions
- [ ] groups
- [ ] per-device capability filtering
- [ ] effect timeline
- [ ] LED-zone abstraction

## Phase 5 — Experience
- [ ] dashboard
- [ ] room visualization
- [ ] device topology graph
- [ ] LED mapping editor
- [ ] screen sync
- [ ] music sync

## Phase 6 — AI
- [ ] voice intent parser
- [ ] natural-language scene builder
- [ ] automation planner
- [ ] capability-aware action validator
- [ ] optional local model provider
- [ ] privacy controls

## Phase 7 — Production
- [ ] Windows installer
- [ ] signed Android APK/AAB
- [ ] GitHub Actions build matrix
- [ ] release artifacts + SHA-256
- [ ] diagnostics export
- [ ] complete PDF manual
