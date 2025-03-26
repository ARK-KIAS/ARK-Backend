from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, Enum, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.datatypes.enum_specialist_qualification import SpecialistQualification

from .base_model import Base

class SpecialistsModel(Base):
    __tablename__ = "specialists"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    given_name: Mapped[str] = mapped_column(String(50), unique=False)
    family_name: Mapped[str] = mapped_column(String(50), unique=False)
    middle_name: Mapped[str] = mapped_column(String(50), unique=False)
    qualification: Mapped[SpecialistQualification] = mapped_column(Enum(SpecialistQualification))
    age: Mapped[int] = mapped_column(Integer)
    experience_years: Mapped[float] = mapped_column(Float, nullable=True, unique=False, default=0.0)
    license_id: Mapped[int] = mapped_column(ForeignKey("media_files.id"), nullable=True, unique=False)
    license_expired_at: Mapped[datetime] = mapped_column(DateTime)
    weight: Mapped[int] = mapped_column(Integer, nullable=True, unique=False)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    created_by_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))