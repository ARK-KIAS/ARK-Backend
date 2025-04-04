from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey, Float, Enum, DateTime
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.dialects.postgresql import TEXT as Pgtext
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class HorseModel(Base):
    __tablename__ = "horses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    # organiztion_type #Organization type #?
    birth_region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"))
    chip_num: Mapped[int] = mapped_column(Integer, unique=False, default=0)
    sex: Mapped[Enum] = mapped_column(PgEnum("male", "female", "None", name="sex_enum"), unique=False, default="None") #todo use https://github.com/Pogchamp-company/alembic-postgresql-enum
    passport_series: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    passport_number: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    passport_issuer: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    passport_issued_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=False)
    nickname: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    suit: Mapped[String] = mapped_column(Pgtext, unique=False, default="")
    father_id: Mapped[int] = mapped_column(ForeignKey("horses.id"))
    mother_id: Mapped[int] = mapped_column(ForeignKey("horses.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"))
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"))
    born_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=True)
    dead_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=True)
    life_status: Mapped[Enum] = mapped_column(PgEnum("born", "foal", "active", "grand", "semen", "dead", name="sex_enum"), unique=False, default="None") #todo use https://github.com/Pogchamp-company/alembic-postgresql-enum
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

