from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base
from src.datatypes.enum_organization_type import OrganizationType

class UserModel(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    email: Mapped[str] = mapped_column(String(50), unique=True) #User email
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id")) #Permission id
    organization_type: Mapped[OrganizationType] = mapped_column(Enum(OrganizationType))
    given_name: Mapped[str] = mapped_column(String(50), unique=False)
    family_name: Mapped[str] = mapped_column(String(50), unique=False)
    middle_name: Mapped[str] = mapped_column(String(50), unique=False)
