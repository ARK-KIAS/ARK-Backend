from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class MediaFilesModel(Base):
    __tablename__ = "media_files"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    bucket_name: Mapped[str] = mapped_column(String(50), unique=False) #Bucket name
    file_name: Mapped[str] = mapped_column(String(50), unique=True) #File name
    extension: Mapped[str] = mapped_column(String(50), unique=False) #File extension
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True) #Date of deletion
