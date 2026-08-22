# Compatibility Matrix

| Platform / Family | Discovery | Local | Matter | BLE | AI/Sync | Implementation state |
|---|---:|---:|---:|---:|---:|---|
| Philips Hue | Bridge/LAN | Yes | Model dependent | Model dependent | Yes | adapter scaffold |
| Nanoleaf | LAN/mDNS/model dependent | Supported models | Model dependent | Model dependent | Yes | adapter scaffold |
| Govee | LAN/API/model dependent | Model dependent | Model dependent | Model dependent | Yes | adapter scaffold |
| Twinkly | LAN/model dependent | Official interface required | Model dependent | Model dependent | Yes | adapter boundary |
| Generic Matter | Commissioning | Yes | Yes | Transport dependent | Yes | protocol adapter scaffold |
| Generic BLE | BLE scan | GATT dependent | No | Yes | Yes | native bridge required |
| Meta ecosystem | Platform/API dependent | Model dependent | Model dependent | Model dependent | Yes | discovery policy boundary |

Capabilities are detected per model. HERMES must show unavailable capabilities rather than presenting a false universal control surface.
