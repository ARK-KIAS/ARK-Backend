from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.specialists_schema import SpecialistsCreate, SpecialistsUpdate, SpecialistsResponse
from src.repositories.specialists_repository import specialists_repository
from src.misc_functions import is_authorized

specialists_router = APIRouter(prefix="/specialists", tags=["specialists"])

@specialists_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: SpecialistsCreate):
    await specialists_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@specialists_router.get('', dependencies=[Depends(is_authorized)], response_model=SpecialistsResponse)
async def get_orgs():
    specialists = await specialists_repository.get_multi()

    return JSONResponse(content={'specialists': jsonable_encoder(specialists)}, status_code=200)
    #return specialists

@specialists_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=SpecialistsResponse)
async def get_orgs(id: int):
    specialist = await specialists_repository.get_single(id=id)

    return JSONResponse(content={'specialist': jsonable_encoder(specialist)}, status_code=200)


@specialists_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=SpecialistsResponse)
async def update_org(id: int, payload:SpecialistsUpdate):
    updated_specialist = await specialists_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_specialist)}, status_code=200)

@specialists_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    specialist = await specialists_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)