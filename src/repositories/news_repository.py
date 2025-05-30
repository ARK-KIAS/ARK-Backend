from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper
from ..models.news_model import NewsModel
from ..schemas.news_schema import NewsCreate, NewsUpdate


class NewsRepository(SqlAlchemyRepository[NewsModel, NewsCreate, NewsUpdate]):
    pass

news_repository = NewsRepository(NewsModel, db_session=db_helper.get_db_session)