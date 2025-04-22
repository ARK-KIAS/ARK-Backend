from fastapi import APIRouter

#from .support.controllers import support_controller, admin_controller

from src.schemas.permissions_schema import PermissionsCreate

from src.repositories.permissions_repository import permissions_repository


def get_apps_router():
    router = APIRouter(prefix="/perm")
    #router.include_router(admin_controller.router)
    #router.include_router(support_controller.router)
    return router

perm_router = get_apps_router()

@perm_router.post('/')
async def add_permission(payload: PermissionsCreate):
    await permissions_repository.create(payload)

    return {'status': 'success'}

@perm_router.get('/')
async def get_permission():
    perm = await permissions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'perm': perm}