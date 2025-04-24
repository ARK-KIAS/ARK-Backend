from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.specialist_docs_model import SpecialistDocsModel

from src.schemas.specialist_docs_schema import SpecialistDocsCreate, SpecialistDocsUpdate

class SpecialistDocsRepository(SqlAlchemyRepository[SpecialistDocsModel, SpecialistDocsCreate, SpecialistDocsUpdate]):
    pass

specialist_docs_repository = SpecialistDocsRepository(SpecialistDocsModel, db_session=db_helper.get_db_session)