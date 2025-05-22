from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey, Float, Enum, DateTime
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.dialects.postgresql import TEXT as Pgtext
from sqlalchemy.orm import Mapped, mapped_column

from src.datatypes.enum_sex import Sex
from src.datatypes.enum_life_status import LifeStatus

from .base_model import Base


class HorsesModel(Base):
    __tablename__ = "horses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    birth_region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"))
    chip_num: Mapped[int] = mapped_column(Integer, unique=False, default=0)
    sex: Mapped[Sex] = mapped_column(Enum(Sex), unique=False, default=Sex.none) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    passport_series: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    passport_number: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    passport_issuer: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    passport_issued_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=False)
    nickname: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    suit: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    father_id: Mapped[int] = mapped_column(ForeignKey("horses.id"), nullable=True)
    mother_id: Mapped[int] = mapped_column(ForeignKey("horses.id"), nullable=True)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"))
    born_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=True)
    dead_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=True)
    life_status: Mapped[LifeStatus] = mapped_column(Enum(LifeStatus), unique=False, default=LifeStatus.none) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    rating: Mapped[float] = mapped_column(Float, default=0.0, unique=False)

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
