from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.datatypes.enum_notification_type import NotificationType

from .base_model import Base


class NotificationsModel(Base):
    __tablename__ = "notifications"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    title: Mapped[str] = mapped_column(String(50), unique=True) #User email
    description: Mapped[str] = mapped_column(String(50), unique=False) #Text of the notification
    type: Mapped[NotificationType] = mapped_column(Enum(NotificationType), unique=False) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
