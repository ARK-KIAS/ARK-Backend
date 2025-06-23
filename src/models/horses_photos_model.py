from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class HorsesPhotosModel(Base):
    __tablename__ = "horses_photos"
    horse_id: Mapped[int] = mapped_column(ForeignKey("horses.id")) #Bucket name
    file_id: Mapped[int] = mapped_column(ForeignKey("media_files.id")) #Bucket name