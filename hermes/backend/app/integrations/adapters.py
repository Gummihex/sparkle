from app.models import Device
from .base import LightAdapter

class SimulationAdapter(LightAdapter):
    manufacturer = 'simulation'
    def __init__(self):
        self.devices = [
            Device(id='sim-hue-1', name='Hue Demo', manufacturer='Philips Hue', model='Simulation', transports=['wifi'], online=True, capabilities={'power': True, 'brightness': True, 'rgb': True, 'color_temperature': True}),
            Device(id='sim-nanoleaf-1', name='Nanoleaf Demo', manufacturer='Nanoleaf', model='Simulation', transports=['wifi', 'matter', 'bluetooth'], online=True, capabilities={'power': True, 'brightness': True, 'rgb': True, 'effects': True, 'animation': True}),
            Device(id='sim-govee-1', name='Govee Demo', manufacturer='Govee', model='Simulation', transports=['wifi', 'bluetooth'], online=True, capabilities={'power': True, 'brightness': True, 'rgb': True, 'effects': True}),
            Device(id='sim-twinkly-1', name='Twinkly Demo', manufacturer='Twinkly', model='Simulation', transports=['wifi'], online=True, capabilities={'power': True, 'brightness': True, 'rgb': True, 'effects': True, 'animation': True, 'individual_led': True}),
        ]
    async def discover(self): return self.devices
    async def connect(self, device): return True
    async def disconnect(self, device): return True
    async def get_state(self, device): return device.state.model_dump()
    async def set_state(self, device, patch):
        for k, v in patch.items():
            if hasattr(device.state, k): setattr(device.state, k, v)
        return device.state.model_dump()

class PhilipsHueAdapter(SimulationAdapter):
    manufacturer = 'Philips Hue'
class NanoleafAdapter(SimulationAdapter):
    manufacturer = 'Nanoleaf'
class GoveeAdapter(SimulationAdapter):
    manufacturer = 'Govee'
class TwinklyAdapter(SimulationAdapter):
    manufacturer = 'Twinkly'
class MatterAdapter(SimulationAdapter):
    manufacturer = 'Matter'
class BluetoothAdapter(SimulationAdapter):
    manufacturer = 'Bluetooth'
class MetaDeviceAdapter(SimulationAdapter):
    manufacturer = 'Meta'
