from app.integrations.adapters import SimulationAdapter
from app.models import Device

class DiscoveryEngine:
    """Transport-oriented discovery coordinator.

    Production implementations should isolate each transport: mDNS/SSDP for LAN,
    Bleak for BLE, Matter SDK for Matter, and only supported Meta/platform APIs.
    """
    def __init__(self):
        self.sim = SimulationAdapter()

    async def scan(self, transports: list[str] | None = None) -> list[Device]:
        devices = await self.sim.discover()
        if not transports:
            return devices
        wanted = set(transports)
        return [d for d in devices if wanted.intersection({t.value for t in d.transports})]
