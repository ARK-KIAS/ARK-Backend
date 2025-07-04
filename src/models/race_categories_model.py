from datetime import datetime, date, time

from sqlalchemy import String, Integer, func, ForeignKey, DateTime, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.datatypes.enum_race_category_type import RaceCategoryType

from .base_model import Base


class RaceCategoriesModel(Base):
    __tablename__ = "race_categories"
    name: Mapped[str] = mapped_column(String(50), unique=False)
    type: Mapped[RaceCategoryType] = mapped_column(Enum(RaceCategoryType), nullable=True, unique=False)
    male_allowed: Mapped[bool] = mapped_column(Boolean)
    female_allowed: Mapped[bool] = mapped_column(Boolean)
    age_min: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    age_max: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"), nullable=True)
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"), nullable=True)
    jockey_weight_min: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    jockey_weight_max: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)

