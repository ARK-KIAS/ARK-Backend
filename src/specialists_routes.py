from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.schemas.query_helper import MiscRequest
from src.schemas.specialists_schema import SpecialistsCreate, SpecialistsUpdate, SpecialistsResponse, SpecialistsQuery
from src.repositories.specialists_repository import specialists_repository
from src.misc_functions import is_authorized

specialists_router = APIRouter(prefix="/specialists", tags=["specialists"])

@specialists_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: SpecialistsCreate):
    out = await specialists_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@specialists_router.get('', response_model=SpecialistsResponse)
async def get_orgs_by_filter(params: SpecialistsQuery = Depends(), misc: MiscRequest = Depends()):
    params_dict = params.dict()
    filter = dict()
    for param in params_dict.keys():
        if params_dict[param] is not None:
            filter[param] = params_dict[param]

    horses = await specialists_repository.get_multi_filtered(**filter, order=misc.order, limit=misc.limit, offset=misc.offset)

    return JSONResponse(content={'specialists': jsonable_encoder(horses)}, status_code=200)

@specialists_router.get('/{id}', response_model=SpecialistsResponse)
async def get_orgs(id: int):
    specialist = await specialists_repository.get_single(id=id)

    if specialist is None:
        return JSONResponse(content={'message': 'There is no specialist with that ID!'}, status_code=404)

    return JSONResponse(content={'specialist': jsonable_encoder(specialist)}, status_code=200)


@specialists_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=SpecialistsResponse)
async def update_org(id: int, payload:SpecialistsUpdate):
    updated_specialist = await specialists_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_specialist)}, status_code=200)

@specialists_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    specialist = await specialists_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)