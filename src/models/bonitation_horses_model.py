from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class BonitationHorsesModel(Base):
    __tablename__ = "bonitation_horses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    bonitation_id: Mapped[int] = mapped_column(ForeignKey("bonitations.id")) #Bucket name
    horse_id: Mapped[int] = mapped_column(ForeignKey("horses.id")) #Bucket name