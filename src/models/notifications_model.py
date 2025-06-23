from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.datatypes.enum_notification_type import NotificationType
from src.datatypes.enum_notification_status import NotificationStatus

from .base_model import Base


class NotificationsModel(Base):
    __tablename__ = "notifications"
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now()) #Date of creation
    title: Mapped[str] = mapped_column(String(100), unique=False) #User email
    description: Mapped[str] = mapped_column(String(100), unique=False) #Text of the notification
    type: Mapped[NotificationType] = mapped_column(Enum(NotificationType), unique=False) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    status: Mapped[NotificationStatus] = mapped_column(Enum(NotificationStatus), unique=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
