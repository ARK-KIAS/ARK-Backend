from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.races_race_days_schema import RacesRaceDaysCreate, RacesRaceDaysUpdate, RacesRaceDaysResponse, \
    RacesRaceDaysQuery
from src.repositories.races_race_days_repository import races_race_days_repository

from .misc_functions import is_authorized
from .schemas.query_helper import MiscRequest

races_race_days_router = APIRouter(prefix="/races_race_days", tags=["races_race_days"])

@races_race_days_router.post('', dependencies=[Depends(is_authorized)], response_model=RacesRaceDaysResponse)
async def add_org(payload: RacesRaceDaysCreate):
    out = await races_race_days_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@races_race_days_router.get('', response_model=RacesRaceDaysResponse)
async def get_orgs_by_filter(params: RacesRaceDaysQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await races_race_days_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'races_race_days': jsonable_encoder(horses)}, status_code=200)

@races_race_days_router.get('/{id}', response_model=RacesRaceDaysResponse)
async def get_orgs(id: int):
    race_days = await races_race_days_repository.get_single(id=id)

    if race_days is None:
        return JSONResponse(content={'message': 'There is no races_race_days with that ID!'}, status_code=404)

    return JSONResponse(content={'race_days': jsonable_encoder(race_days)}, status_code=200)


@races_race_days_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=RacesRaceDaysResponse)
async def update_org(id: int, payload:RacesRaceDaysUpdate):
    updated_race_days = await races_race_days_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_race_days)}, status_code=200)

@races_race_days_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race = await races_race_days_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
