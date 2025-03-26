from datetime import datetime, time
from sqlalchemy import String, Integer, func, ForeignKey, Enum, Time, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base
from src.datatypes.enum_currency_type import CurrencyType
from src.datatypes.enum_track_cover import TrackCover
from src.datatypes.enum_track_status import TrackStatus
from src.datatypes.enum_race_type import RaceType


class RacesModel(Base):
    __tablename__ = "races"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    start_time: Mapped[time] = mapped_column(Time)
    name: Mapped[str] = mapped_column(String(100))
    race_day_id: Mapped[int] = mapped_column(ForeignKey("race_days.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("race_categories.id"))
    prize_money: Mapped[int] = mapped_column(Integer)
    prize_places: Mapped[int] = mapped_column(Integer)
    currency: Mapped[CurrencyType] = mapped_column(Enum(CurrencyType))
    capacity: Mapped[int] = mapped_column(Integer)
    distance: Mapped[int] = mapped_column(Integer)
    track_cover: Mapped[TrackCover] = mapped_column(Enum(TrackCover))
    track_status: Mapped[TrackStatus] = mapped_column(Enum(TrackStatus))
    type: Mapped[RaceType] = mapped_column(Enum(RaceType))
    with_obstacles: Mapped[bool] = mapped_column(Boolean)
