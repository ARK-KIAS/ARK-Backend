from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.permissions_schema import PermissionsCreate, PermissionsUpdate, PermissionsResponse, PermissionsQuery

from src.repositories.permissions_repository import permissions_repository
from src.schemas.query_helper import MiscRequest

perm_router = APIRouter(prefix="/permissions", tags=["permission"])


@perm_router.post('')
async def add_permission(payload: PermissionsCreate):
    out = await permissions_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@perm_router.get('', response_model=PermissionsResponse)
async def get_orgs_by_filter(params: PermissionsQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await permissions_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    if len(horses) == 0:
        return JSONResponse(content={'message': 'Filter is too strict!'}, status_code=404)

    return JSONResponse(content={'permissions': jsonable_encoder(horses)}, status_code=200)

@perm_router.put('/{id}', response_model=PermissionsResponse)
async def update_permission(id: int, payload:PermissionsUpdate):
    updated_perm = await permissions_repository.update(payload, id=id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_perm)}, status_code=200)

@perm_router.delete('/{id}')
async def delete_permission(id: int, payload:PermissionsUpdate):
    perm = await permissions_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)

