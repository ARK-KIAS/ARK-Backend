from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import TEXT as PgText
from .base_model import Base


class HorseHistoryModel(Base):
    __tablename__ = "horses_history"
    horse_id: Mapped[datetime] = mapped_column(ForeignKey("horses.id")) #Date of creation

    height: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    oblique_length: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    torso_circumference: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    pastern_circumference: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    weight: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_origin: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_soundings: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_exterior: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_offspring: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_donorship: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_typicality: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_breed: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_efficiency: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    rating_adaptability: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    coolness: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    insemination_percent: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
