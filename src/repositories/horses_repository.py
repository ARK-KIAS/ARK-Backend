from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.horses_model import HorsesModel

from src.schemas.horses_schema import HorsesCreate, HorsesUpdate

class HorsesRepository(SqlAlchemyRepository[HorsesModel, HorsesCreate, HorsesUpdate]):
    pass

horses_repository = HorsesRepository(HorsesModel, db_session=db_helper.get_db_session)