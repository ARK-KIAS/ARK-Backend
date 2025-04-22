from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.race_days_model import RaceDaysModel

from src.schemas.race_days_schema import RaceDaysCreate, RaceDaysUpdate

class RaceDaysRepository(SqlAlchemyRepository[RaceDaysModel, RaceDaysCreate, RaceDaysUpdate]):
    pass

race_days_repository = RaceDaysRepository(RaceDaysModel, db_session=db_helper.get_db_session)