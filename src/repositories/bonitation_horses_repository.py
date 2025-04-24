from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.bonitation_horses_model import BonitationHorsesModel

from src.schemas.bonitation_horses_schema import BonitationHorsesCreate, BonitationHorsesUpdate

class BonitationHorsesRepository(SqlAlchemyRepository[BonitationHorsesModel, BonitationHorsesCreate, BonitationHorsesUpdate]):
    pass

bonitation_horses_repository = BonitationHorsesRepository(BonitationHorsesModel, db_session=db_helper.get_db_session)