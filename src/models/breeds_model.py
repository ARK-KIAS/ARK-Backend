from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class BreedsModel(Base):
    __tablename__ = "breeds"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    name: Mapped[String] = mapped_column(String(50), unique=False)
    patient_code: Mapped[int] = mapped_column(Integer, autoincrement=False)
    #usage_direction #?
    reg_year: Mapped[int] = mapped_column(Integer, autoincrement=False)
    category: Mapped[String] = mapped_column(String(50), unique=False)
