# HERMES architecture

```text
Flutter UI (Windows / Android)
        |
        | REST + WebSocket
        v
FastAPI Control Plane
        |
        +-- Discovery Manager
        |     +-- LAN/mDNS/SSDP
        |     +-- BLE
        |     +-- Matter
        |
        +-- Light Engine
        |     +-- normalized commands
        |     +-- capability validation
        |     +-- state verification
        |     +-- scenes/effects/groups
        |
        +-- Adapter Registry
        |     +-- Philips Hue
        |     +-- Nanoleaf
        |     +-- Govee
        |     +-- Twinkly
        |     +-- Matter
        |     +-- Bluetooth
        |
        +-- AI Pipeline
        |     +-- intent parser
        |     +-- scene planner
        |     +-- automation planner
        |     +-- voice bridge
        |     +-- local model provider
        |
        +-- Graph + Stats
              +-- rooms/devices/groups/LED zones
              +-- health/latency/telemetry
```

## Design decisions
1. Local-first. The controller should work without a cloud dependency whenever the device protocol permits it.
2. Capability-driven. UI and automation logic must query capabilities instead of assuming every light supports RGB, effects, temperature, animation, or per-LED control.
3. Adapter isolation. Manufacturer-specific behavior stays behind a stable adapter interface.
4. Transport independence. Wi-Fi/LAN, Bluetooth, Matter and cloud APIs are represented as transports rather than separate application concepts.
5. Safety. Credentials are stored in OS secure storage; logs redact secrets; remote LAN access is disabled by default.
6. Testability. Every adapter gets simulation fixtures and contract tests before hardware integration.
