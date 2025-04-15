from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.races_model import RacesModel

from src.schemas.races_schema import RacesCreate, RacesUpdate

class RacesRepository(SqlAlchemyRepository[RacesModel, RacesCreate, RacesUpdate]):
    pass

races_repository = RacesRepository(RacesModel, db_session=db_helper.get_db_session)