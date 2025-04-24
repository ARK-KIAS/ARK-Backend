from fastapi import APIRouter

#from .support.controllers import support_controller, admin_controller

from src.schemas.permissions_schema import PermissionsCreate, PermissionsUpdate

from src.repositories.permissions_repository import permissions_repository


def get_apps_router():
    router = APIRouter()
    #router.include_router(admin_controller.router)
    #router.include_router(support_controller.router)
    return router

main_router = get_apps_router()

@main_router.post('/')
async def add_permission(payload: PermissionsCreate):
    await permissions_repository.create(payload)

    return {'status': 'success'}

@main_router.get('/')
async def get_permission():
    perm = await permissions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@main_router.patch('/')
async def update_permission(payload:PermissionsUpdate):
    perm = await permissions_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@main_router.delete('/')
async def delete_permission(payload:PermissionsUpdate):
    perm = await permissions_repository.delete(id=payload.id)

    return {'status': 'success', 'perm': perm}

