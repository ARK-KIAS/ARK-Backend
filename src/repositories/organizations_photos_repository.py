from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.organizations_photo_model import OrganizationsPhotoModel

from src.schemas.organizations_photo_schema import OrganizationsPhotoCreate, OrganizationsPhotoUpdate

class OrganizationsPhotoRepository(SqlAlchemyRepository[OrganizationsPhotoModel, OrganizationsPhotoCreate, OrganizationsPhotoUpdate]):
    pass

organizations_photo_repository = OrganizationsPhotoRepository(OrganizationsPhotoModel, db_session=db_helper.get_db_session)