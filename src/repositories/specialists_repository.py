from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.specialists_model import SpecialistsModel

from src.schemas.specialists_schema import SpecialistsCreate, SpecialistsUpdate

class SpecialistsRepository(SqlAlchemyRepository[SpecialistsModel, SpecialistsCreate, SpecialistsUpdate]):
    pass

specialists_repository = SpecialistsRepository(SpecialistsModel, db_session=db_helper.get_db_session)