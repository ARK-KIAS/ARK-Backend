from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

from src.misc_functions import is_authorized

from src.schemas.bonitations_schema import BonitationsCreate, BonitationsResponse, BonitationsUpdate
from src.repositories.bonitations_repository import bonitations_repository

bonitation_router = APIRouter(prefix="/bonitations", tags=["bonitations"])

@bonitation_router.post('/', dependencies=[Depends(is_authorized)])
async def add_org(payload: BonitationsCreate):
    await bonitations_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@bonitation_router.get('/', dependencies=[Depends(is_authorized)], response_model=BonitationsCreate)
async def get_orgs():
    bonitations = await bonitations_repository.get_multi()

    return JSONResponse(content={'bonitation': jsonable_encoder(bonitations)}, status_code=200)
    #return bonitation

@bonitation_router.get('/{id}', dependencies=[Depends(is_authorized)])
async def get_orgs(id: int):
    bonitation = await bonitations_repository.get_single(id=id)

    return JSONResponse(content={'horses_photos': jsonable_encoder(bonitation)}, status_code=200)


@bonitation_router.put('/', dependencies=[Depends(is_authorized)])
async def update_org(payload:BonitationsUpdate):
    bonitation = await bonitations_repository.update(payload, id=payload.id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(bonitation)}, status_code=200)

@bonitation_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    bonitation = await bonitations_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
