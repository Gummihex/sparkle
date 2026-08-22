from abc import ABC, abstractmethod
from app.models import Device

class LightAdapter(ABC):
    manufacturer = 'generic'

    @abstractmethod
    async def discover(self) -> list[Device]: ...

    @abstractmethod
    async def connect(self, device: Device) -> bool: ...

    @abstractmethod
    async def disconnect(self, device: Device) -> bool: ...

    @abstractmethod
    async def get_state(self, device: Device): ...

    @abstractmethod
    async def set_state(self, device: Device, patch: dict): ...

    async def health(self, device: Device) -> dict:
        return {'ok': True, 'adapter': self.manufacturer}
