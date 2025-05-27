from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.races_schema import RacesCreate, RacesUpdate, RacesResponse, RacesQuery
from src.repositories.races_repository import races_repository

from .misc_functions import is_authorized
from .schemas.query_helper import MiscRequest

race_router = APIRouter(prefix="/races", tags=["races"])

@race_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: RacesCreate):
    out = await races_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@race_router.get('', response_model=RacesResponse)
async def get_orgs_by_filter(params: RacesQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await races_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    if len(horses) == 0:
        return JSONResponse(content={'message': 'Filter is too strict!'}, status_code=404)

    return JSONResponse(content={'races': jsonable_encoder(horses)}, status_code=200)

@race_router.get('/{id}', response_model=RacesResponse)
async def get_orgs(id: int):
    race = await races_repository.get_single(id=id)

    if race is None:
        return JSONResponse(content={'message': 'There is no race with that ID!'}, status_code=404)

    return JSONResponse(content={'races': jsonable_encoder(race)}, status_code=200)


@race_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=RacesResponse)
async def update_org(id: int, payload:RacesUpdate):
    updated_race = await races_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_race)}, status_code=200)

@race_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race = await races_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
