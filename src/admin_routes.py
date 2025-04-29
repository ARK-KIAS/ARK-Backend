import uuid

from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response

#from .support.controllers import support_controller, admin_controller

from src.schemas.users_schema import UsersCreate, UsersUpdate
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate
from src.schemas.media_files_schema import MediaFilesCreate, MediaFilesUpdate
from src.schemas.regions_schema import RegionsCreate, RegionsUpdate
from src.schemas.redis_sessions_schema import RedisSessionsCreate, RedisSessionsUpdate, RedisSessionsAuth, RedisSessionsBase

from src.repositories.users_repository import users_repository
from src.repositories.organizations_repository import organizations_repository
from src.repositories.media_files_repository import media_files_repository
from src.repositories.regions_repository import regions_repository
from src.repositories.redis_sessions_repository import redis_sessions_repository

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


async def is_authorized(request: Request):
    """verify that user has a valid session"""
    session_id = request.cookies.get("session_cookie")
    if not session_id:
        raise HTTPException(status_code=401)

    auth = await redis_sessions_repository.get_single(cookie_id=session_id)

    if auth is None:
        raise HTTPException(status_code=403)
    return True

# Organization Repos ###################################################################################################
@admin_router.post('/org')
async def add_org(payload: OrganizationsCreate):
    await organizations_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@admin_router.get('/org', dependencies=[Depends(is_authorized)])
async def get_orgs():
    perm = await organizations_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@admin_router.patch('/org', dependencies=[Depends(is_authorized)])
async def update_org(payload:OrganizationsUpdate):
    perm = await organizations_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@admin_router.delete('/org', dependencies=[Depends(is_authorized)])
async def delete_org(payload:OrganizationsUpdate):
    perm = await organizations_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})

# Organization Media Repos #############################################################################################
@admin_router.post('/org/media')
async def add_org(payload: MediaFilesCreate):
    await media_files_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@admin_router.get('/org/media')
async def get_orgs():
    perm = await media_files_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@admin_router.patch('/org/media')
async def update_org(payload:MediaFilesUpdate):
    perm = await media_files_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@admin_router.delete('/org/media')
async def delete_org(payload:MediaFilesUpdate):
    perm = await media_files_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})

# Organization Region Repos ############################################################################################
@admin_router.post('/org/region')
async def add_org(payload: RegionsCreate):
    await regions_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@admin_router.get('/org/region')
async def get_orgs():
    perm = await regions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@admin_router.patch('/org/region')
async def update_org(payload:RegionsUpdate):
    perm = await regions_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@admin_router.delete('/org/region')
async def delete_org(payload:RegionsUpdate):
    perm = await regions_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})