from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.horse_owners_schema import HorseOwnersCreate, HorseOwnersUpdate, HorseOwnersResponse, HorseOwnersQuery
from src.repositories.horse_owners_repository import horse_owners_repository

from .misc_functions import is_authorized
from .schemas.query_helper import MiscRequest

owners_router = APIRouter(prefix="/owners", tags=["owners"])

@owners_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorseOwnersCreate):
    out = await horse_owners_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@owners_router.get('', dependencies=[Depends(is_authorized)], response_model=HorseOwnersResponse)
async def get_orgs_by_filter(params: HorseOwnersQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await horse_owners_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'horse_owners': jsonable_encoder(horses)}, status_code=200)

@owners_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorseOwnersResponse)
async def get_orgs(id: int):
    horse_owners = await horse_owners_repository.get_single(id=id)

    if horse_owners is None:
        return JSONResponse(content={'message': 'There is no horse_owner with that ID!'}, status_code=404)

    return JSONResponse(content={'horse_owners': jsonable_encoder(horse_owners)}, status_code=200)


@owners_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=HorseOwnersResponse)
async def update_org(id: int, payload:HorseOwnersUpdate):
    updated_horses_races = await horse_owners_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horses_races)}, status_code=200)

@owners_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    horse_owners = await horse_owners_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
