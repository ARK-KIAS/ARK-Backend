from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.horse_owners_model import HorseOwnersModel

from src.schemas.horse_owners_schema import HorseOwnersCreate, HorseOwnersUpdate

class HorseOwnersRepository(SqlAlchemyRepository[HorseOwnersModel, HorseOwnersCreate, HorseOwnersUpdate]):
    pass

horse_owners_repository = HorseOwnersRepository(HorseOwnersModel, db_session=db_helper.get_db_session)