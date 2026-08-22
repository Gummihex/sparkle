from enum import Enum
from pydantic import BaseModel, Field
from typing import Any

class Transport(str, Enum):
    wifi = 'wifi'
    ethernet = 'ethernet'
    bluetooth = 'bluetooth'
    matter = 'matter'
    cloud = 'cloud'
    usb = 'usb'

class Capability(BaseModel):
    power: bool = False
    brightness: bool = False
    rgb: bool = False
    color_temperature: bool = False
    effects: bool = False
    animation: bool = False
    individual_led: bool = False
    screen_sync: bool = False
    music_sync: bool = False

class DeviceState(BaseModel):
    power: bool = False
    brightness: int = Field(0, ge=0, le=100)
    rgb: tuple[int, int, int] | None = None
    color_temperature: int | None = None
    effect: str | None = None

class Device(BaseModel):
    id: str
    name: str
    manufacturer: str
    model: str | None = None
    address: str | None = None
    transports: list[Transport] = []
    room_id: str | None = None
    online: bool = False
    capabilities: Capability = Capability()
    state: DeviceState = DeviceState()
    metadata: dict[str, Any] = {}
