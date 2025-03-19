from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class PermissionsModel(Base):
    __tablename__ = "permissions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    name: Mapped[String] = mapped_column(String(50), unique=True) #Name of permission
    accounts_all: Mapped[bool] = mapped_column(Boolean) #Is full access to accounts
    races_full: Mapped[bool] = mapped_column(Boolean) #Is full access to races data
    bonitation_full: Mapped[bool] = mapped_column(Boolean) #Is full access to bonitation data
    specialist_full: Mapped[bool] = mapped_column(Boolean) #Is full access to specialist data
    files_full: Mapped[bool] = mapped_column(Boolean) #Is full access to files storage
    hold_horses: Mapped[bool] = mapped_column(Boolean) #May have horses and ask for bonitation
    create_bonitations: Mapped[bool] = mapped_column(Boolean) #Can recieve requests for bonitation
    create_races: Mapped[bool] = mapped_column(Boolean) #Can send races result
