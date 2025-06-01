from datetime import datetime, date, time
from xmlrpc.client import DateTime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime, Date, Time
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class RaceDaysModel(Base):
    __tablename__ = "race_days"
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    name: Mapped[str] = mapped_column(String(50), unique=False)
    date: Mapped[date] = mapped_column(Date, nullable=True, unique=False)
    start_time: Mapped[time] = mapped_column(Time, nullable=True, unique=False)

