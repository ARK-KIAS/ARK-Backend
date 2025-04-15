from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.horses_races_model import HorsesRacesModel

from src.schemas.horses_races_schema import HorsesRacesCreate, HorsesRacesUpdate

class HorsesRacesRepository(SqlAlchemyRepository[HorsesRacesModel, HorsesRacesCreate, HorsesRacesUpdate]):
    pass

horses_races_repository = HorsesRacesRepository(HorsesRacesModel, db_session=db_helper.get_db_session)