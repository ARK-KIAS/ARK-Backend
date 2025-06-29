from datetime import datetime, timedelta
from sqlalchemy import String, Integer, func, ForeignKey, Uuid, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.config.project_config import settings

from .base_model import Base

class RedisSessionsModel(Base):
    __tablename__ = "redis_sessions"
    expired_at: Mapped[datetime] = mapped_column(default=func.now() + timedelta(days=settings.EXPIRED_AFTER)) #Date of expiring
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) #User id
    access_token: Mapped[Uuid] = mapped_column(Uuid, unique=True) #Unique access token
    # ip: Mapped[str] = mapped_column(String(24), unique=False) #Request ip
    browser: Mapped[str] = mapped_column(String(50), unique=False) #Broweser from request
    os: Mapped[str] = mapped_column(String(50), unique=False) #os of request
    # geolocation: Mapped[str] = mapped_column(String(50), unique=False) #geolocation of request
    # cookie_id: Mapped[str] = mapped_column(String(50), unique=True) #cookie
