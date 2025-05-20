from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.horse_owners_schema import HorseOwnersCreate, HorseOwnersUpdate, HorseOwnersResponse
from src.repositories.horse_owners_repository import horse_owners_repository

from .misc_functions import is_authorized

owners_router = APIRouter(prefix="/owners", tags=["owners"])

@owners_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorseOwnersCreate):
    await horse_owners_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@owners_router.get('', dependencies=[Depends(is_authorized)], response_model=HorseOwnersResponse)
async def get_orgs():
    horse_owners = await horse_owners_repository.get_multi()

    return JSONResponse(content={'horse_owners': jsonable_encoder(horse_owners)}, status_code=200)
    #return horse_owners

@owners_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorseOwnersResponse)
async def get_orgs(id: int):
    horse_owners = await horse_owners_repository.get_single(id=id)

    return JSONResponse(content={'horse_owners': jsonable_encoder(horse_owners)}, status_code=200)


@owners_router.put('', dependencies=[Depends(is_authorized)], response_model=HorseOwnersResponse)
async def update_org(payload:HorseOwnersUpdate):
    updated_horses_races = await horse_owners_repository.update(payload, id=payload.id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horses_races)}, status_code=200)

@owners_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    horse_owners = await horse_owners_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
