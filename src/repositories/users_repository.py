from .sqlalchemy_repository import SqlAlchemyRepository

from src.config.database.db_helper import db_helper

from src.models.users_model import UsersModel

from src.schemas.users_schema import UsersCreate, UsersUpdate

class UsersRepository(SqlAlchemyRepository[UsersModel, UsersCreate, UsersUpdate]):
    pass

users_repository = UsersRepository(UsersModel, db_session=db_helper.get_db_session)