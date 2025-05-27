from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.horses_races_schema import HorsesRacesCreate, HorsesRacesUpdate, HorsesRacesResponse, HorsesRacesQuery
from src.repositories.horses_races_repository import horses_races_repository

from .misc_functions import is_authorized
from .repositories.horses_repository import horses_repository
from .repositories.races_repository import races_repository
from .repositories.specialists_repository import specialists_repository
from .schemas.query_helper import MiscRequest

horses_races_router = APIRouter(prefix="/horses_races", tags=["horses_races"])

@horses_races_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorsesRacesCreate):
    if await races_repository.get_single(id=payload.race_id) is None:
        return JSONResponse(content={'message': 'There is no race with that ID!'}, status_code=404)

    if await horses_repository.get_single(id=payload.horse_id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    if await specialists_repository.get_single(id=payload.rider_id) is None:
        return JSONResponse(content={'message': 'There is no rider with that ID!'}, status_code=404)

    if await specialists_repository.get_single(id=payload.trainer_id) is None:
        return JSONResponse(content={'message': 'There is no trainer with that ID!'}, status_code=404)

    out = await horses_races_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@horses_races_router.get('', dependencies=[Depends(is_authorized)], response_model=HorsesRacesResponse)
async def get_orgs_by_filter(params: HorsesRacesQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await horses_races_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    if len(horses) == 0:
        return JSONResponse(content={'message': 'Filter is too strict!'}, status_code=404)

    return JSONResponse(content={'horses_races': jsonable_encoder(horses)}, status_code=200)

@horses_races_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesRacesResponse)
async def get_orgs(id: int):
    horses_races = await horses_races_repository.get_single(id=id)

    if horses_races is None:
        return JSONResponse(content={'message': 'There is no horses_races with that ID!'}, status_code=404)

    return JSONResponse(content={'horses_races': jsonable_encoder(horses_races)}, status_code=200)


@horses_races_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesRacesResponse)
async def update_org(id: int, payload:HorsesRacesUpdate):
    if await horses_races_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no horses-races with that ID!'}, status_code=404)

    if await races_repository.get_single(id=payload.race_id) is None:
        return JSONResponse(content={'message': 'There is no race with that ID!'}, status_code=404)

    if await horses_repository.get_single(id=payload.horse_id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    if await specialists_repository.get_single(id=payload.rider_id) is None:
        return JSONResponse(content={'message': 'There is no rider with that ID!'}, status_code=404)

    if await specialists_repository.get_single(id=payload.trainer_id) is None:
        return JSONResponse(content={'message': 'There is no trainer with that ID!'}, status_code=404)

    updated_horses_races = await horses_races_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horses_races)}, status_code=200)

@horses_races_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    horses_races = await horses_races_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
