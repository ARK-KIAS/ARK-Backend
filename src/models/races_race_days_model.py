from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class RacesRaceDaysModel(Base):
    __tablename__ = "races_race_days"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    race_id: Mapped[int] = mapped_column(ForeignKey("races.id")) #Bucket name
    race_day_id: Mapped[int] = mapped_column(ForeignKey("race_days.id")) #Bucket name