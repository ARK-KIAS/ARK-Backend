from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.repositories.breeds_repository import breeds_repository
from src.schemas.breeds_schema import BreedsCreate, BreedsUpdate, BreedsResponse, BreedsQuery

from .misc_functions import is_authorized
from .schemas.query_helper import MiscRequest

breeds_router = APIRouter(prefix="/breeds", tags=["breeds"])

@breeds_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: BreedsCreate):
    out = await breeds_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@breeds_router.get('', dependencies=[Depends(is_authorized)], response_model=BreedsResponse)
async def get_orgs_by_filter(params: BreedsQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await breeds_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'breeds_repository': jsonable_encoder(horses)}, status_code=200)

@breeds_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=BreedsResponse)
async def get_orgs(id: int):
    breed = await breeds_repository.get_single(id=id)

    if breed is None:
        return JSONResponse(content={'message': 'There is no breed with that ID!'}, status_code=404)

    return JSONResponse(content={'breed': jsonable_encoder(breed)}, status_code=200)


@breeds_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=BreedsResponse)
async def update_org(id: int, payload:BreedsUpdate):
    updated_breed = await breeds_repository.update(payload, id=id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_breed)}, status_code=200)

@breeds_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    breed = await breeds_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'})
