from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.regions_schema import RegionsCreate, RegionsUpdate, RegionsResponse

from src.repositories.regions_repository import regions_repository

region_router = APIRouter(prefix="/region", tags=["region"])

# Organization Region Repos ############################################################################################
@region_router.post('/org/region')
async def add_org(payload: RegionsCreate):
    await regions_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@region_router.get('/org/region', response_model=RegionsResponse)
async def get_orgs():
    region = await regions_repository.get_multi()

    return JSONResponse(content={'regions': jsonable_encoder(region)}, status_code=200)

@region_router.put('/org/region/{id}', response_model=RegionsResponse)
async def update_org(id: int, payload:RegionsUpdate):
    updated_region = await regions_repository.update(payload, id=id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_region)}, status_code=200)

@region_router.delete('/org/region/{id}')
async def delete_org(id: int, payload:RegionsUpdate):
    perm = await regions_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})