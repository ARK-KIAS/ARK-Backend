from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.organizations_docs_model import OrganizationsDocsModel

from src.schemas.organizations_docs_schema import OrganizationsDocsCreate, OrganizationsDocsUpdate

class OrganizationsDocsRepository(SqlAlchemyRepository[OrganizationsDocsModel, OrganizationsDocsCreate, OrganizationsDocsUpdate]):
    pass

organizations_docs_repository = OrganizationsDocsRepository(OrganizationsDocsModel, db_session=db_helper.get_db_session)