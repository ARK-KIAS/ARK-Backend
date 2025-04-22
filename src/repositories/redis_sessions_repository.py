from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.redis_sessions_model import RedisSessionsModel

from src.schemas.redis_sessions_schema import RedisSessionsCreate, RedisSessionsUpdate

class RedisSessionsRepository(SqlAlchemyRepository[RedisSessionsModel, RedisSessionsCreate, RedisSessionsUpdate]):
    pass

redis_sessions_repository = RedisSessionsRepository(RedisSessionsModel, db_session=db_helper.get_db_session)