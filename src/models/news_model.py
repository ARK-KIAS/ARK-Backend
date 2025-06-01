from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.datatypes.enum_notification_type import NotificationType
from src.datatypes.enum_notification_status import NotificationStatus

from .base_model import Base
from ..datatypes.enum_news_type import NewsType


class NewsModel(Base):
    __tablename__ = "news"
    title: Mapped[str] = mapped_column(String(100), unique=False) #User email
    main_text: Mapped[Text] = mapped_column(Text, unique=False) #Text of the notification
    type: Mapped[NewsType] = mapped_column(Enum(NewsType), unique=False) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    file_id: Mapped[int] = mapped_column(ForeignKey("media_files.id"), nullable=True)
