from datetime import datetime, date, time
from xmlrpc.client import DateTime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime, Date, Time
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class RaceDaysModel(Base):
    __tablename__ = "race_days"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    name: Mapped[str] = mapped_column(String(50), unique=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    date: Mapped[date] = mapped_column(Date, nullable=True, unique=False)
    start_time: Mapped[time] = mapped_column(Time, nullable=True, unique=False)

