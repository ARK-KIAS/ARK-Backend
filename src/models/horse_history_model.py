from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import TEXT as PgText
from .base_model import Base


class HorseHistoryModel(Base):
    __tablename__ = "horses_history"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    horse_id: Mapped[datetime] = mapped_column(ForeignKey("horses.id")) #Date of creation
    field_name: Mapped[String] = mapped_column(PgText, unique=True) #User email
    new_value: Mapped[String] = mapped_column(PgText, unique=True) #User email
