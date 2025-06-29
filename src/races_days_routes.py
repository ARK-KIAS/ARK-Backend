from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.race_days_schema import RaceDaysCreate, RaceDaysUpdate, RaceDaysResponse, RaceDaysQuery
from src.repositories.race_days_repository import race_days_repository

from .misc_functions import is_authorized
from .repositories.organizations_repository import organizations_repository
from .repositories.races_race_days_repository import races_race_days_repository
from .repositories.races_repository import races_repository
from .schemas.query_helper import MiscRequest

race_days_router = APIRouter(prefix="/races_days", tags=["race_days"])

@race_days_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: RaceDaysCreate):
    test = await race_days_repository.get_single(date=payload.date, organization_id=payload.organization_id)

    if test is not None:
        return JSONResponse(content={'message': 'This organization already has race on that day!'}, status_code=409)

    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    out = await race_days_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@race_days_router.get('', response_model=RaceDaysResponse)
async def get_orgs_by_filter(params: RaceDaysQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await race_days_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'race_days': jsonable_encoder(horses)}, status_code=200)

@race_days_router.get('/{id}', response_model=RaceDaysResponse)
async def get_orgs(id: int):
    race_days = await race_days_repository.get_single(id=id)

    if race_days is None:
        return JSONResponse(content={'message': 'There is no race day with that ID!'}, status_code=404)

    races_race_days = await races_race_days_repository.get_multi_filtered(race_days_id=race_days.id)

    if len(races_race_days) == 0:
        return JSONResponse(content={'message': 'There is no races on that day!'}, status_code=404)

    races = []
    for race in races_race_days:
        race_dict = (await races_repository.get_single(id=race.race_id)).__dict__
        races.append(race_dict)

    race_day_dict = race_days.__dict__
    race_day_dict["races"] = races

    return JSONResponse(content={'race_day': jsonable_encoder(race_day_dict)}, status_code=200)


@race_days_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=RaceDaysResponse)
async def update_org(id: int, payload:RaceDaysUpdate):
    if await race_days_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no race_days with that ID!'}, status_code=404)

    if await organizations_repository.get_single(id=payload.organization_id) is None:
        return JSONResponse(content={'message': 'There is no organization with that ID!'}, status_code=404)

    updated_race_days = await race_days_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_race_days)}, status_code=200)

@race_days_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race = await race_days_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
