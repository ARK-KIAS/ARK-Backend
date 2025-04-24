from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base
from src.datatypes.enum_usage_direction import UsageDirection

class BreedsModel(Base):
    __tablename__ = "breeds"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    name: Mapped[str] = mapped_column(String(50), unique=False)
    patient_code: Mapped[int] = mapped_column(Integer, autoincrement=False)
    usage_direction: Mapped[UsageDirection] = mapped_column(Enum(UsageDirection))
    reg_year: Mapped[int] = mapped_column(Integer, autoincrement=False)
    category: Mapped[str] = mapped_column(String(50), unique=False)
