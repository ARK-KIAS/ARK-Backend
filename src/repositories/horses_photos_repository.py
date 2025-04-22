from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.horses_photos_model import HorsesPhotosModel

from src.schemas.horses_photos_schema import HorsesPhotosCreate, HorsesPhotosUpdate

class HorsesPhotosRepository(SqlAlchemyRepository[HorsesPhotosModel, HorsesPhotosCreate, HorsesPhotosUpdate]):
    pass

horses_photos_repository = HorsesPhotosRepository(HorsesPhotosModel, db_session=db_helper.get_db_session)