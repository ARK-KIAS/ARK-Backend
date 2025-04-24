from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.permissions_model import PermissionsModel

from src.schemas.permissions_schema import PermissionsCreate, PermissionsUpdate

class PermissionsRepository(SqlAlchemyRepository[PermissionsModel, PermissionsCreate, PermissionsUpdate]):
    pass

permissions_repository = PermissionsRepository(PermissionsModel, db_session=db_helper.get_db_session)