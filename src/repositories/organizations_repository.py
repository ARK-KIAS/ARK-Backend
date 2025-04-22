from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.organizations_model import OrganizationsModel

from src.schemas.organizations_schema import OrganizationsCreate, OrganizationsUpdate

class OrganizationsRepository(SqlAlchemyRepository[OrganizationsModel, OrganizationsCreate, OrganizationsUpdate]):
    pass

organizations_repository = OrganizationsRepository(OrganizationsModel, db_session=db_helper.get_db_session)