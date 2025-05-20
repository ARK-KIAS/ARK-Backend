from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.permissions_schema import PermissionsCreate, PermissionsUpdate, PermissionsResponse

from src.repositories.permissions_repository import permissions_repository

perm_router = APIRouter(prefix="/permission", tags=["permission"])


@perm_router.post('')
async def add_permission(payload: PermissionsCreate):
    await permissions_repository.create(payload)

    return JSONResponse(content={'status': 'success'}, status_code=201)

@perm_router.get('', response_model=PermissionsResponse)
async def get_permission():
    perm = await permissions_repository.get_multi()

    return JSONResponse(content={'permission': jsonable_encoder(perm)}, status_code=200)

@perm_router.put('', response_model=PermissionsResponse)
async def update_permission(payload:PermissionsUpdate):
    updated_perm = await permissions_repository.update(payload, id=payload.id)

    return JSONResponse(content={'status': 'success', 'update': jsonable_encoder(updated_perm)}, status_code=200)

@perm_router.delete('')
async def delete_permission(payload:PermissionsUpdate):
    perm = await permissions_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'}, status_code=200)

