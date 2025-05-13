from fastapi import APIRouter

from .auth_routes import auth_router
from .notification_router import notification_router
from .organization_routes import organization_router
from .perm_routes import perm_router
from .region_routes import region_router
from .users_routes import user_routes
from .admin_routes import admin_router
from .horses_routes import horses_router
from .breeds_routes import breeds_router


def get_apps_router():
    router = APIRouter()
    router.include_router(auth_router)
    router.include_router(perm_router)
    router.include_router(user_routes)
    router.include_router(admin_router)
    router.include_router(organization_router)
    router.include_router(region_router)
    router.include_router(notification_router)
    router.include_router(horses_router)
    router.include_router(breeds_router)


    return router

main_router = get_apps_router()
