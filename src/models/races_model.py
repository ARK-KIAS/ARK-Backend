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
    start_time: Mapped[time] = mapped_column(Time, nullable=True, unique=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True, unique=False)
    race_day_id: Mapped[int] = mapped_column(ForeignKey("race_days.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("race_categories.id"))
    prize_money: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    prize_places: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    currency: Mapped[CurrencyType] = mapped_column(Enum(CurrencyType), nullable=True, unique=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    distance: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    track_cover: Mapped[TrackCover] = mapped_column(Enum(TrackCover), nullable=True, unique=False)
    track_status: Mapped[TrackStatus] = mapped_column(Enum(TrackStatus), nullable=True, unique=False)
    type: Mapped[RaceType] = mapped_column(Enum(RaceType), nullable=True, unique=False)
    with_obstacles: Mapped[bool] = mapped_column(Boolean)
