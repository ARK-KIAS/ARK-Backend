from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class BonitationHorsesModel(Base):
    __tablename__ = "bonitation_horses"
    bonitation_id: Mapped[int] = mapped_column(ForeignKey("bonitations.id")) #Bucket name
    horse_id: Mapped[int] = mapped_column(ForeignKey("horses.id")) #Bucket name
    is_ready: Mapped[bool] = mapped_column(Boolean)  # Bucket name