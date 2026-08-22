from fastapi import APIRouter, HTTPException, Query
from app.discovery import DiscoveryEngine
from app.models import Device

router = APIRouter(prefix='/api/v1', tags=['hermes'])
engine = DiscoveryEngine()

@router.get('/devices', response_model=list[Device])
async def devices():
    return await engine.scan()

@router.get('/discovery/scan', response_model=list[Device])
async def scan(transports: list[str] | None = Query(default=None)):
    return await engine.scan(transports)

@router.post('/devices/{device_id}/command')
async def command(device_id: str, patch: dict):
    devices = await engine.scan()
    device = next((d for d in devices if d.id == device_id), None)
    if not device:
        raise HTTPException(404, 'DEVICE_NOT_FOUND')
    return {'ok': True, 'device_id': device_id, 'patch': patch}
