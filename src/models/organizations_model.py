from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base
from src.datatypes.enum_organization_type import OrganizationType
from src.datatypes.enum_organization_status import OrganizationStatus

class OrganizationsModel(Base):
    __tablename__ = "organizations"
    organization_type: Mapped[OrganizationType] = mapped_column(Enum(OrganizationType)) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    admin_id: Mapped[int] = mapped_column(Integer, unique=False) #User id
    name: Mapped[str] = mapped_column(String(250), unique=False)
    short_name: Mapped[str] = mapped_column(String(50), unique=False)
    address: Mapped[str] = mapped_column(String(250), unique=False)
    mail_address: Mapped[str] = mapped_column(String(250), unique=False)
    inn: Mapped[str] = mapped_column(String(10), unique=False)
    kpp: Mapped[str] = mapped_column(String(9), unique=False)
    bik: Mapped[str] = mapped_column(String(9), unique=False)
    ogrn: Mapped[str] = mapped_column(String(13), unique=False)
    okved_code: Mapped[str] = mapped_column(String(7), unique=False)
    all_okved_code: Mapped[str] = mapped_column(String(50), unique=False)
    director_name: Mapped[str] = mapped_column(String(50), unique=False)
    chief_accountant_name: Mapped[str] = mapped_column(String(50), unique=False)
    email: Mapped[str] = mapped_column(String(250), unique=True)
    tel: Mapped[str] = mapped_column(String(50), unique=True)
    settlement_account: Mapped[str] = mapped_column(String(50), unique=True)
    corr_account: Mapped[str] = mapped_column(String(20), unique=True)
    logo_id: Mapped[int] = mapped_column(ForeignKey("media_files.id")) #Media files id
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id")) #Regions id
    status: Mapped[OrganizationStatus] = mapped_column(Enum(OrganizationStatus)) # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.Enum
    site_link: Mapped[str] = mapped_column(String(100), unique=True)
    okved_approved: Mapped[bool] = mapped_column(Boolean)
    land_hectares: Mapped[float] = mapped_column(Float)
    land_status_ok: Mapped[bool] = mapped_column(Boolean)
