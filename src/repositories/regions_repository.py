from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.regions_model import RegionsModel

from src.schemas.regions_schema import RegionsCreate, RegionsUpdate

class RegionsRepository(SqlAlchemyRepository[RegionsModel, RegionsCreate, RegionsUpdate]):
    pass

regions_repository = RegionsRepository(RegionsModel, db_session=db_helper.get_db_session)