from fastapi import APIRouter

#from .support.controllers import support_controller, admin_controller

from src.schemas.users_schema import UsersCreate, UsersUpdate
from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate
from src.schemas.media_files_schema import MediaFilesCreate, MediaFilesUpdate
from src.schemas.regions_schema import RegionsCreate, RegionsUpdate

from src.repositories.users_repository import users_repository
from src.repositories.organizations_repository import organizations_repository
from src.repositories.media_files_repository import media_files_repository
from src.repositories.regions_repository import regions_repository


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

    return {'status': 'success'}

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

    return {'status': 'success'}

# Organization Repos ##########################################################################################################
@auth_router.post('/org')
async def add_org(payload: OrganizationsCreate):
    await organizations_repository.create(payload)

    return {'status': 'success'}

@auth_router.get('/org')
async def get_orgs():
    perm = await organizations_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@auth_router.patch('/org')
async def update_org(payload:OrganizationsUpdate):
    perm = await organizations_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@auth_router.delete('/org')
async def delete_org(payload:OrganizationsUpdate):
    perm = await organizations_repository.delete(id=payload.id)

    return {'status': 'success'}

# Organization Media Repos ##########################################################################################################
@auth_router.post('/org/media')
async def add_org(payload: MediaFilesCreate):
    await media_files_repository.create(payload)

    return {'status': 'success'}

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

    return {'status': 'success'}

# Organization Region Repos ##########################################################################################################
@auth_router.post('/org/region')
async def add_org(payload: RegionsCreate):
    await regions_repository.create(payload)

    return {'status': 'success'}

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

    return {'status': 'success'}