from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.bonitation_horses_schema import BonitationHorsesCreate, BonitationHorsesUpdate, BonitationHorsesResponse
from src.repositories.bonitation_horses_repository import bonitation_horses_repository

from .misc_functions import is_authorized
from .repositories.bonitations_repository import bonitations_repository
from .repositories.horses_repository import horses_repository

bonitation_horses_router = APIRouter(prefix="/bonitations_horses", tags=["bonitations_horses"])

@bonitation_horses_router.post('', dependencies=[Depends(is_authorized)])
async def add_org(payload: BonitationHorsesCreate):
    if await horses_repository.get_single(id=payload.horse_id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    if await bonitations_repository.get_single(id=payload.bonitation_id) is None:
        return JSONResponse(content={'message': 'There is no bonitation with that ID!'}, status_code=404)

    out = await bonitation_horses_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)

@bonitation_horses_router.get('', dependencies=[Depends(is_authorized)], response_model=BonitationHorsesResponse)
async def get_orgs():
    bonitation_horses = await bonitation_horses_repository.get_multi()

    return JSONResponse(content={'bonitation_horses': jsonable_encoder(bonitation_horses)}, status_code=200)
    #return bonitation_horses

@bonitation_horses_router.get('/{id}', dependencies=[Depends(is_authorized)], response_model=BonitationHorsesResponse)
async def get_orgs(id: int):
    bonitation_horses = await bonitation_horses_repository.get_single(id=id)

    if bonitation_horses is None:
        return JSONResponse(content={'message': 'There is no bonitation_horses with that ID!'}, status_code=404)

    return JSONResponse(content={'horses_photos': jsonable_encoder(bonitation_horses)}, status_code=200)


@bonitation_horses_router.put('/{id}', dependencies=[Depends(is_authorized)], response_model=BonitationHorsesResponse)
async def update_org(id: int, payload:BonitationHorsesUpdate):
    if await bonitation_horses_repository.get_single(id=id) is None:
        return JSONResponse(content={'message': 'There is no such bonitation-horse found!'}, status_code=404)

    if await horses_repository.get_single(id=payload.horse_id) is None:
        return JSONResponse(content={'message': 'There is no horse with that ID!'}, status_code=404)

    if await bonitations_repository.get_single(id=payload.bonitation_id) is None:
        return JSONResponse(content={'message': 'There is no bonitation with that ID!'}, status_code=404)

    bonitation_horses_photos = await bonitation_horses_repository.update(payload, id=id, status_code=200)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(bonitation_horses_photos)}, status_code=200)

@bonitation_horses_router.delete('/{id}', dependencies=[Depends(is_authorized)])
async def delete_org(id: int):
    bonitation_horses = await bonitation_horses_repository.delete(id=id)

    return JSONResponse(content={'status': 'success'}, status_code=200)
