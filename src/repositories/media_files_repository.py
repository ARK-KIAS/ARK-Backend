from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.media_files_model import MediaFilesModel

from src.schemas.media_files_schema import MediaFilesCreate, MediaFilesUpdate

class MediaFilesRepository(SqlAlchemyRepository[MediaFilesModel, MediaFilesCreate, MediaFilesUpdate]):
    pass

media_files_repository = MediaFilesRepository(MediaFilesModel, db_session=db_helper.get_db_session)