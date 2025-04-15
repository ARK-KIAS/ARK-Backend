from fastapi import APIRouter

from .support.controllers import support_controller, admin_controller
from .config.database.db_helper import db_helper

from .repositories.sqlalchemy_repository import SqlAlchemyRepository

from .models.permissions_model import PermissionsModel

from .schemas.permissions_schema import PermissionCreate, PermissionUpdate, PermissionResponse

class PermissionRepository(SqlAlchemyRepository[PermissionsModel, PermissionCreate, PermissionUpdate]):
    pass


def get_apps_router():
    router = APIRouter()
    router.include_router(admin_controller.router)
    router.include_router(support_controller.router)
    return router

router = get_apps_router()

@router.post('/')
def add_permission(payload: PermissionCreate):
    perm_repository = PermissionRepository(PermissionsModel, db_session=db_helper.get_db_session)
    perm_repository.create(payload)

    return {'status': 'success'}

@router.get('/')
def get_permission():
    perm_repository = PermissionRepository(PermissionsModel, db_session=db_helper.get_db_session)
    perm = perm_repository.get_multi()

    return {'status': 'success', 'results': len(perm), 'notes': perm}