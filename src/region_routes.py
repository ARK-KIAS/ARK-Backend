from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.regions_schema import RegionsCreate, RegionsUpdate

from src.repositories.regions_repository import regions_repository

region_router = APIRouter(prefix="/region", tags=["region"])

# Organization Region Repos ############################################################################################
@region_router.post('/org/region')
async def add_org(payload: RegionsCreate):
    await regions_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@region_router.get('/org/region')
async def get_orgs():
    perm = await regions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@region_router.patch('/org/region')
async def update_org(payload:RegionsUpdate):
    perm = await regions_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@region_router.delete('/org/region')
async def delete_org(payload:RegionsUpdate):
    perm = await regions_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})