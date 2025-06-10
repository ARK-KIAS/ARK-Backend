from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper
from ..models.media_files_groups_model import MediaFilesGroupsModel
from ..schemas.media_files_groups_schema import MediaFilesGroupsCreate, MediaFilesGroupsUpdate


class MediaFilesGroupsRepository(SqlAlchemyRepository[MediaFilesGroupsModel, MediaFilesGroupsCreate, MediaFilesGroupsUpdate]):
    pass

media_files_groups_repository = MediaFilesGroupsRepository(MediaFilesGroupsModel, db_session=db_helper.get_db_session)