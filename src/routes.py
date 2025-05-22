from fastapi import APIRouter

from .auth_routes import auth_router
from .bonitations_routes import bonitation_router
from .horse_history_routes import history_router
from .notification_routes import notification_router
from .organizations_routes import organization_router
from .owners_routes import owners_router
from .permissions_routes import perm_router
from .races_routes import race_router
from .region_routes import region_router
from .specialists_routes import specialists_router
from .tasks_routes import tasks_router
from .users_routes import user_router
from .admin_routes import admin_router
from .horses_routes import horses_router
from .breeds_routes import breeds_router
from .specialists_docs_routes import specialist_docs_router
from .races_days_routes import race_days_router
from .race_categories_routes import race_categories_router
from .organization_docs_routes import organization_docs_router
from .horses_races_routes import horses_races_router
from .horse_photos_routes import horse_photos_router
from .bonitation_horses_routes import bonitation_horses_router

def get_apps_router():
    router = APIRouter()
    router.include_router(auth_router)
    router.include_router(perm_router)
    router.include_router(user_router)
    router.include_router(admin_router)
    router.include_router(organization_router)
    router.include_router(region_router)
    router.include_router(notification_router)
    router.include_router(horses_router)
    router.include_router(breeds_router)

    router.include_router(bonitation_router)
    router.include_router(history_router)
    router.include_router(owners_router)
    router.include_router(race_router)
    router.include_router(specialists_router)
    router.include_router(specialist_docs_router)
    router.include_router(race_days_router)
    router.include_router(race_categories_router)
    router.include_router(organization_docs_router)
    router.include_router(horses_races_router)
    router.include_router(horse_photos_router)
    router.include_router(bonitation_horses_router)
    router.include_router(tasks_router)


    return router

main_router = get_apps_router()
