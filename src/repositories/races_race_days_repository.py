from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.races_race_days_model import RacesRaceDaysModel

from src.schemas.races_race_days_schema import RacesRaceDaysCreate, RacesRaceDaysUpdate

class RaceDaysRepository(SqlAlchemyRepository[RacesRaceDaysModel, RacesRaceDaysCreate, RacesRaceDaysUpdate]):
    pass

races_race_days_repository = RaceDaysRepository(RacesRaceDaysModel, db_session=db_helper.get_db_session)