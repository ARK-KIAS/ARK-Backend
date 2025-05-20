from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.race_categories_schema import RaceCategoriesCreate, RaceCategoriesUpdate, RaceCategoriesResponse
from src.repositories.race_categories_repository import race_categories_repository

from .misc_functions import is_authorized

race_categories_router = APIRouter(prefix="/races/categories", tags=["race_categories"])

@race_categories_router.get('/')
async def add_permission():
    return JSONResponse(content={'status': 'success'}, status_code=200)

@race_categories_router.post('/', dependencies=[Depends(is_authorized)])
async def add_org(payload: RaceCategoriesCreate):
    await race_categories_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@race_categories_router.get('/', dependencies=[Depends(is_authorized)], response_model=RaceCategoriesCreate)
async def get_orgs():
    race_categories = await race_categories_repository.get_multi()

    return JSONResponse(content={'race_categories': jsonable_encoder(race_categories)}, status_code=200)
    #return race_categories

@race_categories_router.get('/{id}', dependencies=[Depends(is_authorized)])
async def get_orgs(id: int):
    race_categories = await race_categories_repository.get_single(id=id)

    return JSONResponse(content={'race_days': jsonable_encoder(race_categories)}, status_code=200)


@race_categories_router.put('/', dependencies=[Depends(is_authorized)])
async def update_org(payload:RaceCategoriesUpdate):
    updated_race_categories = await race_categories_repository.update(payload, id=payload.id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_race_categories)}, status_code=200)

@race_categories_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race_categories = await race_categories_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
