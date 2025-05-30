from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.race_categories_schema import RaceCategoriesCreate, RaceCategoriesUpdate, RaceCategoriesResponse, \
    RaceCategoriesQuery
from src.repositories.race_categories_repository import race_categories_repository

from .misc_functions import is_authorized
from .repositories.breeds_repository import breeds_repository
from .repositories.regions_repository import regions_repository
from .schemas.query_helper import MiscRequest

race_categories_router = APIRouter(prefix="/races_categories", tags=["race_categories"])

@race_categories_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: RaceCategoriesCreate):
    if payload.region_id is not None:
        if await regions_repository.get_single(id=payload.region_id) is None:
            return JSONResponse(content={'message': 'There is no region with that ID!'}, status_code=404)

    if payload.breed_id is not None:
        if await breeds_repository.get_single(id=payload.breed_id) is None:
            return JSONResponse(content={'message': 'There is no breed with that ID!'}, status_code=404)

    out = await race_categories_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@race_categories_router.get('', dependencies=[Depends(is_authorized)], response_model=RaceCategoriesResponse)
async def get_orgs_by_filter(params: RaceCategoriesQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await race_categories_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'race_categories': jsonable_encoder(horses)}, status_code=200)

@race_categories_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=RaceCategoriesResponse)
async def get_orgs(id: int):
    race_categories = await race_categories_repository.get_single(id=id)

    if race_categories is None:
        return JSONResponse(content={'message': 'There is no race_category with that ID!'}, status_code=404)

    return JSONResponse(content={'race_days': jsonable_encoder(race_categories)}, status_code=200)


@race_categories_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=RaceCategoriesResponse)
async def update_org(id: int, payload:RaceCategoriesUpdate):
    if await race_categories_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no race_category with that ID!'}, status_code=404)

    if await regions_repository.get_single(id=payload.region_id) is None:
        return JSONResponse(content={'message': 'There is no region with that ID!'}, status_code=404)

    if await breeds_repository.get_single(id=payload.breed_id) is None:
        return JSONResponse(content={'message': 'There is no breed with that ID!'}, status_code=404)

    updated_race_categories = await race_categories_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_race_categories)}, status_code=200)

@race_categories_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    race_categories = await race_categories_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
