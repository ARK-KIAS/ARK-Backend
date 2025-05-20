from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.horses_races_schema import HorsesRacesCreate, HorsesRacesUpdate, HorsesRacesResponse
from src.repositories.horses_races_repository import horses_races_repository

from .misc_functions import is_authorized

horses_races_router = APIRouter(prefix="/horses/races", tags=["horses_races"])

@horses_races_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorsesRacesCreate):
    await horses_races_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@horses_races_router.get('', dependencies=[Depends(is_authorized)], response_model=HorsesRacesResponse)
async def get_orgs():
    horses_races = await horses_races_repository.get_multi()

    return JSONResponse(content={'horses_races': jsonable_encoder(horses_races)}, status_code=200)
    #return horses_races

@horses_races_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesRacesResponse)
async def get_orgs(id: int):
    horses_races = await horses_races_repository.get_single(id=id)

    return JSONResponse(content={'horses_races': jsonable_encoder(horses_races)}, status_code=200)


@horses_races_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesRacesResponse)
async def update_org(id: int, payload:HorsesRacesUpdate):
    updated_horses_races = await horses_races_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horses_races)}, status_code=200)

@horses_races_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    horses_races = await horses_races_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
