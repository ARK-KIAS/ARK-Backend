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

RANDOM_COOKIE_ID = "isaugdiuadushadoisahn"


def get_apps_router():
    router = APIRouter(prefix="/auth")
    #router.include_router(admin_controller.router)
    #router.include_router(support_controller.router)
    return router

auth_router = get_apps_router()

# Users Repos ##########################################################################################################
@auth_router.post('/users')
async def add_user(payload: UsersCreate):
    await users_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@auth_router.get('/users')
async def get_users():
    perm = await users_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@auth_router.patch('/users')
async def update_user(payload:UsersUpdate):
    perm = await users_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@auth_router.delete('/users')
async def delete_user(payload:UsersUpdate):
    perm = await users_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})

# Auth Session #########################################################################################################

@auth_router.post('/login')
async def check_auth(payload: RedisSessionsAuth):
    password = payload.password
    username = payload.username

    auth = await users_repository.get_single(username=username, password=password)

    if auth is None:
        return JSONResponse(content={"message": "Auth failure, check login/password"}, status_code=401)

    response = RedirectResponse("/", status_code=302)

    response.set_cookie(key="Authorization", value=RANDOM_COOKIE_ID)

    payload_dict = payload.dict()
    payload_dict["user_id"] = auth.id
    payload_dict["cookie_id"] = RANDOM_COOKIE_ID
    create_model = RedisSessionsCreate(**payload_dict)

    await redis_sessions_repository.create(create_model)

    return response

@auth_router.get('/login')
async def get_session():
    perm = await redis_sessions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@auth_router.delete('/login')
async def delete_session(payload:RedisSessionsUpdate):
    perm = await redis_sessions_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})

@auth_router.get('/logout')
async def logout(response: Response):

    response.delete_cookie(key="Authorization")
    perm = await redis_sessions_repository.delete(cookie_id=RANDOM_COOKIE_ID)

    return {'status': 'success'}

async def get_auth_user(request: Request):
    """verify that user has a valid session"""
    session_id = request.cookies.get("Authorization")
    if not session_id:
        raise HTTPException(status_code=401)

    auth = await redis_sessions_repository.get_single(cookie_id=session_id)

    if auth is None:
        raise HTTPException(status_code=403)
    return True

# Organization Repos ###################################################################################################
@auth_router.post('/org')
async def add_org(payload: OrganizationsCreate):
    await organizations_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@auth_router.get('/org', dependencies=[Depends(get_auth_user)])
async def get_orgs():
    perm = await organizations_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@auth_router.patch('/org', dependencies=[Depends(get_auth_user)])
async def update_org(payload:OrganizationsUpdate):
    perm = await organizations_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@auth_router.delete('/org', dependencies=[Depends(get_auth_user)])
async def delete_org(payload:OrganizationsUpdate):
    perm = await organizations_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})

# Organization Media Repos #############################################################################################
@auth_router.post('/org/media')
async def add_org(payload: MediaFilesCreate):
    await media_files_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@auth_router.get('/org/media')
async def get_orgs():
    perm = await media_files_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@auth_router.patch('/org/media')
async def update_org(payload:MediaFilesUpdate):
    perm = await media_files_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@auth_router.delete('/org/media')
async def delete_org(payload:MediaFilesUpdate):
    perm = await media_files_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})

# Organization Region Repos ############################################################################################
@auth_router.post('/org/region')
async def add_org(payload: RegionsCreate):
    await regions_repository.create(payload)

    return JSONResponse(content={'status': 'success'})

@auth_router.get('/org/region')
async def get_orgs():
    perm = await regions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@auth_router.patch('/org/region')
async def update_org(payload:RegionsUpdate):
    perm = await regions_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@auth_router.delete('/org/region')
async def delete_org(payload:RegionsUpdate):
    perm = await regions_repository.delete(id=payload.id)

    return JSONResponse(content={'status': 'success'})