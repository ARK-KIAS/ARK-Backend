from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.breeds_repository import breeds_repository
from src.schemas.breeds_schema import BreedsCreate, BreedsUpdate, BreedsResponse

from .misc_functions import is_authorized

breeds_router = APIRouter(prefix="/breeds", tags=["breeds"])

@breeds_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: BreedsCreate):
    await breeds_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@breeds_router.get('', dependencies=[Depends(is_authorized)], response_model=BreedsResponse)
async def get_orgs():
    breeds = await breeds_repository.get_multi()

    return JSONResponse(content={'breeds': jsonable_encoder(breeds)}, status_code=200)

@breeds_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=BreedsResponse)
async def get_orgs(id: int):
    breed = await breeds_repository.get_single(id=id)

    return JSONResponse(content={'breed': jsonable_encoder(breed)}, status_code=200)


@breeds_router.put('', dependencies=[Depends(is_authorized)], response_model=BreedsResponse)
async def update_org(payload:BreedsUpdate):
    updated_breed = await breeds_repository.update(payload, id=payload.id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_breed)}, status_code=200)

@breeds_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    breed = await breeds_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})