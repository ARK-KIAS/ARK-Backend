from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime, Interval, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class HorsesRacesModel(Base):
    __tablename__ = "horses_races"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"))
    horse_id: Mapped[int] = mapped_column(ForeignKey("horses.id"))
    rider_id: Mapped[int] = mapped_column(ForeignKey("specialists.id"))
    trainer_id: Mapped[int] = mapped_column(ForeignKey("specialists.id"))
    time: Mapped[Interval] = mapped_column(Interval)
    result_place: Mapped[int] = mapped_column(Integer)
    start_place: Mapped[int] = mapped_column(Integer)
    prize_money: Mapped[int] = mapped_column(Integer)
    handicap: Mapped[int] = mapped_column(Integer)
    doping_control_ok: Mapped[bool] = mapped_column(Boolean)