from fastapi import APIRouter

# from .support.controllers import support_controller, admin_controller
from .auth_routes import auth_router
from .perm_routes import perm_router
from .users_routes import user_routes
from .admin_routes import admin_router
from src.schemas.permissions_schema import PermissionsCreate, PermissionsUpdate

from src.repositories.permissions_repository import permissions_repository


def get_apps_router():
    router = APIRouter()
    router.include_router(auth_router)
    router.include_router(perm_router)
    router.include_router(user_routes)
    router.include_router(admin_router)


    return router

main_router = get_apps_router()
