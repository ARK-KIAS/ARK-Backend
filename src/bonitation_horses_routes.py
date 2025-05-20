from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.bonitation_horses_schema import BonitationHorsesCreate, BonitationHorsesUpdate, BonitationHorsesResponse
from src.repositories.bonitation_horses_repository import bonitation_horses_repository

from .misc_functions import is_authorized

bonitation_horses_router = APIRouter(prefix="/bonitations/horses", tags=["bonitations_horses"])

@bonitation_horses_router.get('/')
async def add_permission():
    return JSONResponse(content={'status': 'success'}, status_code=200)

@bonitation_horses_router.post('/', dependencies=[Depends(is_authorized)])
async def add_org(payload: BonitationHorsesCreate):
    await bonitation_horses_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@bonitation_horses_router.get('/', dependencies=[Depends(is_authorized)], response_model=BonitationHorsesCreate)
async def get_orgs():
    bonitation_horses = await bonitation_horses_repository.get_multi()

    return JSONResponse(content={'bonitation_horses': jsonable_encoder(bonitation_horses)}, status_code=200)
    #return bonitation_horses

@bonitation_horses_router.get('/{id}', dependencies=[Depends(is_authorized)])
async def get_orgs(id: int):
    bonitation_horses = await bonitation_horses_repository.get_single(id=id)

    return JSONResponse(content={'horses_photos': jsonable_encoder(bonitation_horses)}, status_code=200)


@bonitation_horses_router.put('/', dependencies=[Depends(is_authorized)])
async def update_org(payload:BonitationHorsesUpdate):
    bonitation_horses_photos = await bonitation_horses_repository.update(payload, id=payload.id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(bonitation_horses_photos)}, status_code=200)

@bonitation_horses_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    bonitation_horses = await bonitation_horses_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
