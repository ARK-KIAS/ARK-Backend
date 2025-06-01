from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import TEXT as PgText
from .base_model import Base


class HorseOwnersModel(Base):
    __tablename__ = "horse_owners"
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id")) #Date of creation
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) #Date of creation
    horse_id: Mapped[int] = mapped_column(ForeignKey("horses.id")) #Date of creation
    percent: Mapped[int] = mapped_column(Integer, default=0) #User email