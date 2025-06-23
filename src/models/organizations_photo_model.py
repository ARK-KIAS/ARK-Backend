from datetime import datetime

from sqlalchemy import String, Integer, func, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class OrganizationsPhotoModel(Base):
    __tablename__ = "organizations_photo"
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id")) #Bucket name
    file_id: Mapped[int] = mapped_column(ForeignKey("media_files.id")) #Bucket name