from fastapi import APIRouter

#from .support.controllers import support_controller, admin_controller

from src.schemas.permissions_schema import PermissionsCreate

from src.repositories.permissions_repository import permissions_repository


def get_apps_router():
    router = APIRouter()
    #router.include_router(admin_controller.router)
    #router.include_router(support_controller.router)
    return router

router = get_apps_router()

@router.post('/')
def add_permission(payload: PermissionsCreate):
    permissions_repository.create(payload)

    return {'status': 'success'}

@router.get('/')
def get_permission():
    perm = permissions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'notes': perm}