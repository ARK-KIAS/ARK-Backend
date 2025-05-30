
from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.horse_history_schema import HorseHistoryCreate, HorseHistoryUpdate, HorseHistoryResponse, \
    HorseHistoryQuery
from src.repositories.horse_history_repository import horse_history_repository

from .misc_functions import is_authorized
from .repositories.horses_repository import horses_repository
from .schemas.query_helper import MiscRequest

history_router = APIRouter(prefix="/history", tags=["history"])

@history_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorseHistoryCreate):
    if await horses_repository.get_single(id=payload.horse_id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    out = await horse_history_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@history_router.get('', dependencies=[Depends(is_authorized)], response_model=HorseHistoryResponse)
async def get_orgs_by_filter(params: HorseHistoryQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await horse_history_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'horse_history': jsonable_encoder(horses)}, status_code=200)

@history_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorseHistoryResponse)
async def get_orgs(id: int):
    horse_history = await horse_history_repository.get_single(id=id)

    if horse_history is None:
        return JSONResponse(content={'message': 'There is no horse_history with that ID!'}, status_code=404)

    return JSONResponse(content={'race_days': jsonable_encoder(horse_history)}, status_code=200)


@history_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=HorseHistoryResponse)
async def update_org(id: int, payload:HorseHistoryUpdate):
    if await horse_history_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no horse-history with that ID!'}, status_code=404)

    if await horses_repository.get_single(id=payload.horse_id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    updated_horse_history = await horse_history_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horse_history)}, status_code=200)

@history_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race = await horse_history_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)