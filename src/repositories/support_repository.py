from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.support_model import SupportModel

from src.schemas.support_schema import SupportCreate, SupportUpdate

class SupportRepository(SqlAlchemyRepository[SupportModel, SupportCreate, SupportUpdate]):
    pass

support_repository = SupportRepository(SupportModel, db_session=db_helper.get_db_session)