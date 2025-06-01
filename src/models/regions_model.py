from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class RegionsModel(Base):
    __tablename__ = "regions"
    name: Mapped[str] = mapped_column(String(50), unique=True)
