from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref

from .base_model import Base


class MediaFilesGroupsModel(Base):
    __tablename__ = "media_files_groups"
    name: Mapped[str] = mapped_column(String(50), unique=True) #Bucket name

    media_files = relationship(
        'MediaFilesModel',
        back_populates='media_files_groups',
        cascade="all, delete, delete-orphan"
    )
