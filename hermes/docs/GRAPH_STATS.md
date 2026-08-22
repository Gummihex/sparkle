# Graph + Stats

## Graph
Core entities: Device, Room, Group, Scene, Automation, LEDZone, ScreenZone.
Relationships: `belongs_to`, `member_of`, `uses`, `triggers`, `maps_to`, `mirrors`.

This supports a visual topology such as:
`Room -> Group -> Devices -> LED Zones` and `Scene -> Effects -> Devices`.

## Stats
Collect timestamped metrics for discovery duration, command round-trip latency, online ratio, reconnect count, adapter error count, update frequency, CPU/RAM and network traffic. Device names and credentials must not be written into raw telemetry unless explicitly configured.
