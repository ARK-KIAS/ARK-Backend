from datetime import datetime, timedelta
from sqlalchemy import String, Integer, func, ForeignKey, Uuid, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base

class RedisSessionsModel(Base):
    __tablename__ = "redis_sessions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    expired_at: Mapped[datetime] = mapped_column(default=func.now() + timedelta(days=14)) #Date of expiring TODO refactor and use config
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) #User id
    access_token: Mapped[Uuid] = mapped_column(Uuid, unique=True) #Unique access token
    ip: Mapped[String] = mapped_column(String(24), unique=False) #Request ip
    browser: Mapped[String] = mapped_column(String(50), unique=False) #Broweser from request
    os: Mapped[String] = mapped_column(String(50), unique=False) #os of request
    geolocation: Mapped[String] = mapped_column(String(50), unique=False) #geolocation of request
