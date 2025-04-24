from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.breeds_model import BreedsModel

from src.schemas.breeds_schema import BreedsCreate, BreedsUpdate

class BreedsRepository(SqlAlchemyRepository[BreedsModel, BreedsCreate, BreedsUpdate]):
    pass

breeds_repository = BreedsRepository(BreedsModel, db_session=db_helper.get_db_session)