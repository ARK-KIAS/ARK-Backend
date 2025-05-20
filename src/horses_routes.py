from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.redis_sessions_repository import redis_sessions_repository
from src.repositories.horses_repository import horses_repository
from src.schemas.horses_schema import HorsesCreate, HorsesUpdate, HorsesResponse

from .misc_functions import is_authorized

horses_router = APIRouter(prefix="/horses", tags=["horses"])

@horses_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorsesCreate):
    await horses_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@horses_router.get('', dependencies=[Depends(is_authorized)], response_model=HorsesResponse)
async def get_orgs():
    horses = await horses_repository.get_multi()

    return JSONResponse(content={'horses': jsonable_encoder(horses)}, status_code=200)
    #return horses

@horses_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesResponse)
async def get_orgs(id: int):
    horse = await horses_repository.get_single(id=id)

    return JSONResponse(content={'horse': jsonable_encoder(horse)}, status_code=200)


@horses_router.put('', dependencies=[Depends(is_authorized)], response_model=HorsesResponse)
async def update_org(payload:HorsesUpdate):
    updated_horse = await horses_repository.update(payload, id=payload.id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horse)}, status_code=200)

@horses_router.patch('', dependencies=[Depends(is_authorized)], response_model=HorsesResponse)
async def update_org(payload:HorsesUpdate):
    updated_horse = await horses_repository.update(payload, id=payload.id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horse)}, status_code=200)

@horses_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    horse = await horses_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})