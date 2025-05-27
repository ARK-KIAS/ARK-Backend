import uuid

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse, Response
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate
from src.schemas.media_files_schema import MediaFilesCreate, MediaFilesUpdate, MediaFilesResponse
from src.schemas.regions_schema import RegionsCreate, RegionsUpdate
from src.repositories.organizations_repository import organizations_repository
from src.repositories.media_files_repository import media_files_repository
from src.repositories.regions_repository import regions_repository


admin_router = APIRouter(prefix="/admin", tags=["admin"])

# @auth_router.get('/login')
# async def get_session():
#     perm = await redis_sessions_repository.get_multi()
#
#     return {'status': 'success', 'results': len(perm), 'out': perm}

# @admin_router.delete('/login')
# async def delete_session(payload:RedisSessionsUpdate):
#     perm = await redis_sessions_repository.delete(id=payload.id)
#
#     return JSONResponse(content={'status': 'success'})

# Organization Media Repos #############################################################################################
@admin_router.post('/org/media')
async def add_org(payload: MediaFilesCreate):
    if await media_files_repository.get_single(file_name=payload.file_name):
        return JSONResponse(content={'message': 'File with this name already exists!'}, status_code=409)

    out = await media_files_repository.create(payload)
    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=200)

@admin_router.get('/org/media', response_model=MediaFilesResponse)
async def get_orgs():
    perm = await media_files_repository.get_multi()

    return JSONResponse(content={'media_files': jsonable_encoder(perm)}, status_code=200)

@admin_router.put('/org/media/{id}', response_model=MediaFilesResponse)
async def update_org(id: int, payload:MediaFilesUpdate):
    if await media_files_repository.get_single(file_name=payload.file_name):
        return JSONResponse(content={'message': 'File with this name already exists!'}, status_code=409)

    perm = await media_files_repository.update(payload, id=id)

    return JSONResponse(content={'media_file': jsonable_encoder(perm)}, status_code=200)

@admin_router.delete('/org/media')
async def delete_org(payload:MediaFilesUpdate):
    perm = await media_files_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'}, status_code=200)

@admin_router.post('/org')
async def add_org(payload: OrganizationsCreate):
    if await organizations_repository.get_single(corr_account=payload.corr_account):
        return JSONResponse(content={'message': 'Organization with this corr account already exists!'}, status_code=409)

    if await organizations_repository.get_single(email=payload.email):
        return JSONResponse(content={'message': 'Organization with this email already exists!'}, status_code=409)

    if await organizations_repository.get_single(settlement_account=payload.settlement_account):
        return JSONResponse(content={'message': 'Organization with this settlement account already exists!'}, status_code=409)

    if await organizations_repository.get_single(site_link=payload.site_link):
        return JSONResponse(content={'message': 'Organization with this site link already exists!'}, status_code=409)

    if await organizations_repository.get_single(tel=payload.tel):
        return JSONResponse(content={'message': 'Organization with this telephone number already exists!'}, status_code=409)


    out = await organizations_repository.create(payload)

    return JSONResponse(content={'status': 'success', 'output': jsonable_encoder(out)}, status_code=201)