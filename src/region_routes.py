from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.schemas.query_helper import MiscRequest
from src.schemas.regions_schema import RegionsCreate, RegionsUpdate, RegionsResponse, RegionsQuery

from src.repositories.regions_repository import regions_repository

region_router = APIRouter(prefix="/regions", tags=["region"])

# Organization Region Repos ############################################################################################
@region_router.post('/org/regions')
async def add_org(payload: RegionsCreate):
    out = await regions_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@region_router.get('/org/regions', response_model=RegionsResponse)
async def get_orgs_by_filter(params: RegionsQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await regions_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    if len(horses) == 0:
        return JSONResponse(content={'message': 'Filter is too strict!'}, status_code=404)

    return JSONResponse(content={'regions': jsonable_encoder(horses)}, status_code=200)

@region_router.put('/org/regions/{id}', response_model=RegionsResponse)
async def update_org(id: int, payload:RegionsUpdate):
    updated_region = await regions_repository.update(payload, id=id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_region)}, status_code=200)

@region_router.delete('/org/regions/{id}')
async def delete_org(id: int, payload:RegionsUpdate):
    perm = await regions_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})