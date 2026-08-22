from fastapi import FastAPI
from app.api.devices import router as devices_router
from app.api.discovery import router as discovery_router

app = FastAPI(title='HERMES LIGHT HUB', version='0.2.0')
app.include_router(devices_router, prefix='/api/v1')
app.include_router(discovery_router, prefix='/api/v1')

@app.get('/health')
async def health():
    return {'status': 'ok', 'service': 'hermes-light-hub', 'version': app.version}
