from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class NotificationsModel(Base):
    __tablename__ = "notifications"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    title: Mapped[String] = mapped_column(String(50), unique=True) #User email
    description: Mapped[String] = mapped_column(String(50), unique=False) #Text of the notification
    ##type: Mapped[String] = mapped_column(String(50), unique=False) #?
    ##user_id: Mapped[int] = mapped_column(String(50), unique=False) #?
