from datetime import datetime
from sqlalchemy import String, Integer, func, ForeignKey, Enum, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base
from src.datatypes.enum_bonitation_status import BonitationStatus
from src.datatypes.enum_bonitation_type import BonitationType

class BonitationsModel(Base):
    __tablename__ = "bonitations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    inspector_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    prefers_time_min: Mapped[datetime] = mapped_column(DateTime, nullable=True, unique=False)
    prefers_time_max: Mapped[datetime] = mapped_column(DateTime, nullable=True, unique=False)
    approved_time: Mapped[datetime] = mapped_column(DateTime, nullable=True, unique=False)
    comment: Mapped[str] = mapped_column(String(500), unique=False, nullable=True)
    org_contact_name: Mapped[str] = mapped_column(String(250), unique=False)
    org_contact_tel: Mapped[str] = mapped_column(String(50), unique=False)
    org_contact_link: Mapped[str] = mapped_column(String(500), unique=False)
    status: Mapped[BonitationStatus] = mapped_column(Enum(BonitationStatus), nullable=True, unique=False)
    type: Mapped[BonitationType] = mapped_column(Enum(BonitationType), nullable=True, unique=False)