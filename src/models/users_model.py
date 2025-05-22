from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base
from src.datatypes.enum_organization_type import OrganizationType

class UsersModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    email: Mapped[str] = mapped_column(String(50), unique=True) #User email
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id")) #Permission id
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id")) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    given_name: Mapped[str] = mapped_column(String(50), unique=False)
    family_name: Mapped[str] = mapped_column(String(50), unique=False)
    middle_name: Mapped[str] = mapped_column(String(50), unique=False)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50), unique=False)
