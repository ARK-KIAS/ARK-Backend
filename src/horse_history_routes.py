
from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.horse_history_schema import HorseHistoryCreate, HorseHistoryUpdate, HorseHistoryResponse
from src.repositories.horse_history_repository import horse_history_repository

from .misc_functions import is_authorized

history_router = APIRouter(prefix="/history", tags=["history"])

@history_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorseHistoryCreate):
    await horse_history_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@history_router.get('', dependencies=[Depends(is_authorized)], response_model=HorseHistoryResponse)
async def get_orgs():
    horse_history = await horse_history_repository.get_multi()

    return JSONResponse(content={'horse_history': jsonable_encoder(horse_history)}, status_code=200)
    #return horse_history

@history_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorseHistoryResponse)
async def get_orgs(id: int):
    horse_history = await horse_history_repository.get_single(id=id)

    return JSONResponse(content={'race_days': jsonable_encoder(horse_history)}, status_code=200)


@history_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=HorseHistoryResponse)
async def update_org(id: int, payload:HorseHistoryUpdate):
    updated_horse_history = await horse_history_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horse_history)}, status_code=200)

@history_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race = await horse_history_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)