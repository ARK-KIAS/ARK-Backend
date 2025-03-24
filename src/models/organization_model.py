from datetime import datetime
from sqlalchemy import String, Integer, func, Boolean, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class OrganizationModel(Base):
    __tablename__ = "organization"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #Unique id
    created_at: Mapped[datetime] = mapped_column(default=func.now()) #Date of creation
    # organiztion_type #Organization type #?
    admin_id: Mapped[int] = mapped_column(ForeignKey("user.id")) #User id
    name: Mapped[String] = mapped_column(String(50), unique=False)
    short_name: Mapped[String] = mapped_column(String(50), unique=False)
    address: Mapped[String] = mapped_column(String(50), unique=False)
    mail_address: Mapped[String] = mapped_column(String(50), unique=False)
    inn: Mapped[String] = mapped_column(String(10), unique=False)
    kpp: Mapped[String] = mapped_column(String(9), unique=False)
    bik: Mapped[String] = mapped_column(String(9), unique=False)
    ogrn: Mapped[String] = mapped_column(String(13), unique=False)
    okved_code: Mapped[String] = mapped_column(String(7), unique=False)
    all_okved_code: Mapped[String] = mapped_column(String(50), unique=False)
    director_name: Mapped[String] = mapped_column(String(50), unique=False)
    chief_accountant_name: Mapped[String] = mapped_column(String(50), unique=False)
    email: Mapped[String] = mapped_column(String(50), unique=True)
    tel: Mapped[String] = mapped_column(String(50), unique=True)
    settlement_account: Mapped[String] = mapped_column(String(50), unique=True)
    corr_account: Mapped[String] = mapped_column(String(20), unique=True)
    logo_id: Mapped[int] = mapped_column(ForeignKey("media_files.id")) #Media files id
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id")) #Regions id
    #status #?
    site_link: Mapped[String] = mapped_column(String(100), unique=True)
    okved_approved: Mapped[bool] = mapped_column(Boolean)
    land_hectares: Mapped[float] = mapped_column(Float)
    land_status_ok: Mapped[bool] = mapped_column(Boolean)
