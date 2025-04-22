from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.horse_history_model import HorseHistoryModel

from src.schemas.horse_history_schema import HorseHistoryCreate, HorseHistoryUpdate

class HorseHistoryRepository(SqlAlchemyRepository[HorseHistoryModel, HorseHistoryCreate, HorseHistoryUpdate]):
    pass

horse_history_repository = HorseHistoryRepository(HorseHistoryModel, db_session=db_helper.get_db_session)