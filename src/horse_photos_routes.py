from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.horses_photos_schema import HorsesPhotosCreate, HorsesPhotosUpdate, HorsesPhotosResponse
from src.repositories.horses_photos_repository import horses_photos_repository

from .misc_functions import is_authorized

horse_photos_router = APIRouter(prefix="/horses/photos", tags=["horses_photos"])

@horse_photos_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: HorsesPhotosCreate):
    await horses_photos_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@horse_photos_router.get('', dependencies=[Depends(is_authorized)], response_model=HorsesPhotosResponse)
async def get_orgs():
    horses_photos = await horses_photos_repository.get_multi()

    return JSONResponse(content={'horses_photos': jsonable_encoder(horses_photos)}, status_code=200)
    #return horses_photos

@horse_photos_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesPhotosResponse)
async def get_orgs(id: int):
    horses_photos = await horses_photos_repository.get_single(id=id)

    return JSONResponse(content={'horses_photos': jsonable_encoder(horses_photos)}, status_code=200)


@horse_photos_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=HorsesPhotosResponse)
async def update_org(id: int, payload:HorsesPhotosUpdate):
    updated_horses_photos = await horses_photos_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_horses_photos)}, status_code=200)

@horse_photos_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    horses_races = await horses_photos_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
