from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime, Interval, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class HorsesRacesModel(Base):
    __tablename__ = "horses_races"
    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"))
    horse_id: Mapped[int] = mapped_column(ForeignKey("horses.id"))
    rider_id: Mapped[int] = mapped_column(ForeignKey("specialists.id"), nullable=True, default=None)
    trainer_id: Mapped[int] = mapped_column(ForeignKey("specialists.id"), nullable=True, default=None)
    time: Mapped[Interval] = mapped_column(Interval, nullable=True, unique=False, default=None)
    result_place: Mapped[int] = mapped_column(Integer, nullable=True, unique=False, default=None)
    start_place: Mapped[int] = mapped_column(Integer, nullable=True, unique=False, default=None)
    prize_money: Mapped[int] = mapped_column(Integer, nullable=True, unique=False, default=None)
    handicap: Mapped[int] = mapped_column(Integer, nullable=True, unique=False, default=None)
    doping_control_ok: Mapped[bool] = mapped_column(Boolean, nullable=True, unique=False, default=None)