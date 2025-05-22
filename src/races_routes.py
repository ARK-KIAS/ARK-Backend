from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.races_schema import RacesCreate, RacesUpdate, RacesResponse
from src.repositories.races_repository import races_repository

from .misc_functions import is_authorized

race_router = APIRouter(prefix="/races", tags=["races"])

@race_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: RacesCreate):
    await races_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@race_router.get('', dependencies=[Depends(is_authorized)], response_model=RacesResponse)
async def get_orgs():
    races = await races_repository.get_multi()

    return JSONResponse(content={'races': jsonable_encoder(races)}, status_code=200)
    #return races

@race_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=RacesResponse)
async def get_orgs(id: int):
    race = await races_repository.get_single(id=id)

    return JSONResponse(content={'race': jsonable_encoder(race)}, status_code=200)


@race_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=RacesResponse)
async def update_org(id: int, payload:RacesUpdate):
    updated_race = await races_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_race)}, status_code=200)

@race_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race = await races_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
