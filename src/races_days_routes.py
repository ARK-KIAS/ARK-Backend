from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.race_days_schema import RaceDaysCreate, RaceDaysUpdate, RaceDaysResponse
from src.repositories.race_days_repository import race_days_repository

from .misc_functions import is_authorized

race_days_router = APIRouter(prefix="/races/days", tags=["race_days"])

@race_days_router.get('/')
async def add_permission():
    return JSONResponse(content={'status': 'success'}, status_code=200)

@race_days_router.post('/', dependencies=[Depends(is_authorized)])
async def add_org(payload: RaceDaysCreate):
    await race_days_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@race_days_router.get('/', dependencies=[Depends(is_authorized)], response_model=RaceDaysCreate)
async def get_orgs():
    race_days = await race_days_repository.get_multi()

    return JSONResponse(content={'race_days': jsonable_encoder(race_days)}, status_code=200)
    #return race_days

@race_days_router.get('/{id}', dependencies=[Depends(is_authorized)])
async def get_orgs(id: int):
    race_days = await race_days_repository.get_single(id=id)

    return JSONResponse(content={'race_days': jsonable_encoder(race_days)}, status_code=200)


@race_days_router.put('/', dependencies=[Depends(is_authorized)])
async def update_org(payload:RaceDaysUpdate):
    updated_race_days = await race_days_repository.update(payload, id=payload.id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_race_days)}, status_code=200)

@race_days_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race = await race_days_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
