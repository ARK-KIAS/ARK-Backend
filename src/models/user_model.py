from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    email: Mapped[String] = mapped_column(String(50), unique=True) #User email
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id")) #Permission id
    #organiztion_type #Organization type #?
    given_name: Mapped[String] = mapped_column(String(50), unique=False)
    family_name: Mapped[String] = mapped_column(String(50), unique=False)
    middle_name: Mapped[String] = mapped_column(String(50), unique=False)
