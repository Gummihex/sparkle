# Compatibility matrix — initial target

| Ecosystem | Discovery targets | Control path | Capability model | Implementation state |
|---|---|---|---|---|
| Philips Hue | Bridge/LAN, supported local mechanisms | Official local API / supported bridge | power, brightness, RGB, CCT, scenes | adapter planned |
| Nanoleaf | LAN/mDNS/model-dependent | Official local/OpenAPI where supported | panels, strips, effects, brightness, color | adapter planned |
| Govee | LAN/model/API-dependent | Official/current developer interfaces | model-dependent | adapter planned |
| Twinkly | LAN/model-dependent | Official/current supported interface only | model-dependent, including LED effects where supported | verification required |
| Matter | IP/mDNS + commissioning | Matter clusters | standardized capabilities | generic adapter planned |
| Bluetooth | BLE scan + GATT | vendor/service-specific | model-dependent | native bridge planned |
| Meta-supported devices | discovery only when an official supported integration/protocol is available | integration-specific | capability-derived | research/adapter gate |

## Important
Compatibility is model-specific. The UI must show exactly which capabilities were discovered. Unsupported functions must be disabled instead of emulated incorrectly.
