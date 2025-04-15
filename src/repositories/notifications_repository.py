from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.notifications_model import NotificationsModel

from src.schemas.notifications_schema import NotificationsCreate, NotificationsUpdate

class NotificationsRepository(SqlAlchemyRepository[NotificationsModel, NotificationsCreate, NotificationsUpdate]):
    pass

notifications_repository = NotificationsRepository(NotificationsModel, db_session=db_helper.get_db_session)