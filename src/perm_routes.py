from fastapi import APIRouter

# from .support.controllers import support_controller, admin_controller
from .auth_routes import auth_router
from src.schemas.permissions_schema import PermissionsCreate, PermissionsUpdate

from src.repositories.permissions_repository import permissions_repository


RANDOM_COOKIE_ID = "isaugdiuadushadoisahn"

perm_router = APIRouter(prefix="/permission", tags=["permission"])


@perm_router.post('/')
async def add_permission(payload: PermissionsCreate):
    await permissions_repository.create(payload)

    return {'status': 'success'}

@perm_router.get('/')
async def get_permission():
    perm = await permissions_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'out': perm}

@perm_router.patch('/')
async def update_permission(payload:PermissionsUpdate):
    perm = await permissions_repository.update(payload, id=payload.id)

    return {'status': 'success', 'perm': perm}

@perm_router.delete('/')
async def delete_permission(payload:PermissionsUpdate):
    perm = await permissions_repository.delete(id=payload.id)

    return {'status': 'success', 'perm': perm}

