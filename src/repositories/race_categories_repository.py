from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.race_categories_model import RaceCategoriesModel

from src.schemas.race_categories_schema import RaceCategoriesCreate, RaceCategoriesUpdate

class RaceCategoriesRepository(SqlAlchemyRepository[RaceCategoriesModel, RaceCategoriesCreate, RaceCategoriesUpdate]):
    pass

race_categories_repository = RaceCategoriesRepository(RaceCategoriesModel, db_session=db_helper.get_db_session)