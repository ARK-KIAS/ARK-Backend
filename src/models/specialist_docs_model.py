from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class SpecialistDocsModel(Base):
    __tablename__ = "specialists_docs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    specialist_id: Mapped[int] = mapped_column(ForeignKey("specialists.id")) #Bucket name
    file_id: Mapped[int] = mapped_column(ForeignKey("media_files.id")) #Bucket name