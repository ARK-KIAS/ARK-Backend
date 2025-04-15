from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.bonitations_model import BonitationsModel

from src.schemas.bonitations_schema import BonitationsCreate, BonitationsUpdate

class BonitationsRepository(SqlAlchemyRepository[BonitationsModel, BonitationsCreate, BonitationsUpdate]):
    pass

bonitations_repository = BonitationsRepository(BonitationsModel, db_session=db_helper.get_db_session)