from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr, HttpUrl
from typing import Optional
from src.datatypes.enum_organization_type import OrganizationType
from src.datatypes.enum_organization_status import OrganizationStatus


class OrganizationsBase(BaseModel):
    organization_type: OrganizationType = Field(..., description="Тип организации")
    admin_id: int = Field(..., description="ID администратора организации")
    name: str = Field(..., max_length=50, description="Полное название организации")
    short_name: str = Field(..., max_length=50, description="Краткое название")
    address: str = Field(..., max_length=50, description="Юридический адрес")
    mail_address: str = Field(..., max_length=50, description="Почтовый адрес")
    inn: str = Field(..., max_length=10, description="ИНН")
    kpp: str = Field(..., max_length=9, description="КПП")
    bik: str = Field(..., max_length=9, description="БИК")
    ogrn: str = Field(..., max_length=13, description="ОГРН")
    okved_code: str = Field(..., max_length=7, description="Основной ОКВЭД")
    all_okved_code: str = Field(..., max_length=50, description="Все ОКВЭДы")
    director_name: str = Field(..., max_length=50, description="ФИО директора")
    chief_accountant_name: str = Field(..., max_length=50, description="ФИО главного бухгалтера")
    email: EmailStr = Field(..., max_length=50, description="Контактный email")
    tel: str = Field(..., max_length=50, description="Контактный телефон")
    settlement_account: str = Field(..., max_length=50, description="Расчетный счет")
    corr_account: str = Field(..., max_length=20, description="Корреспондентский счет")
    logo_id: Optional[int] = Field(None, description="ID логотипа в медиа-хранилище")
    region_id: int = Field(..., description="ID региона")
    status: OrganizationStatus = Field(..., description="Статус организации")
    site_link: Optional[str] = Field(None, max_length=100, description="Ссылка на сайт")
    okved_approved: bool = Field(..., description="Подтверждены ли коды ОКВЭД")
    land_hectares: float = Field(..., description="Площадь земель в гектарах")
    land_status_ok: bool = Field(..., description="Статус земельного участка")


class OrganizationsCreate(OrganizationsBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "organization_type": "breeder",
                "admin_id": 123,
                "name": "ООО 'Конный завод'",
                "short_name": "Конный завод",
                "address": "г. Москва, ул. Лошадиная, 1",
                "mail_address": "г. Москва, ул. Лошадиная, 1",
                "inn": "1234567890",
                "kpp": "123456789",
                "bik": "123456789",
                "ogrn": "1234567890123",
                "okved_code": "01.49",
                "all_okved_code": "01.49, 01.50",
                "director_name": "Иванов Иван Иванович",
                "chief_accountant_name": "Петрова Мария Сергеевна",
                "email": "info@horsefarm.ru",
                "tel": "+79991234567",
                "settlement_account": "40702810123450123456",
                "corr_account": "30101810100000000123",
                "logo_id": 1,
                "region_id": 77,
                "status": "active",
                "site_link": "https://horsefarm.ru",
                "okved_approved": True,
                "land_hectares": 150.5,
                "land_status_ok": True
            }
        }
    )


class OrganizationsUpdate(OrganizationsBase):
    id: int = Field(..., description="Уникальный ID организации")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "organization_type": "breeder",
                "admin_id": 123,
                "name": "ООО 'Конный завод'",
                "short_name": "Конный завод",
                "address": "г. Москва, ул. Лошадиная, 1",
                "mail_address": "г. Москва, ул. Лошадиная, 1",
                "inn": "1234567890",
                "kpp": "123456789",
                "bik": "123456789",
                "ogrn": "1234567890123",
                "okved_code": "01.49",
                "all_okved_code": "01.49, 01.50",
                "director_name": "Иванов Иван Иванович",
                "chief_accountant_name": "Петрова Мария Сергеевна",
                "email": "info@horsefarm.ru",
                "tel": "+79991234567",
                "settlement_account": "40702810123450123456",
                "corr_account": "30101810100000000123",
                "logo_id": 1,
                "region_id": 77,
                "status": "active",
                "site_link": "https://horsefarm.ru",
                "okved_approved": True,
                "land_hectares": 150.5,
                "land_status_ok": True
            }
        }
    )


class OrganizationsResponse(OrganizationsBase):
    id: int = Field(..., description="Уникальный ID организации")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T00:00:00",
                "organization_type": "breeder",
                "admin_id": 123,
                "name": "ООО 'Конный завод'",
                "short_name": "Конный завод",
                "address": "г. Москва, ул. Лошадиная, 1",
                "mail_address": "г. Москва, ул. Лошадиная, 1",
                "inn": "1234567890",
                "kpp": "123456789",
                "bik": "123456789",
                "ogrn": "1234567890123",
                "okved_code": "01.49",
                "all_okved_code": "01.49, 01.50",
                "director_name": "Иванов Иван Иванович",
                "chief_accountant_name": "Петрова Мария Сергеевна",
                "email": "info@horsefarm.ru",
                "tel": "+79991234567",
                "settlement_account": "40702810123450123456",
                "corr_account": "30101810100000000123",
                "logo_id": 1,
                "region_id": 77,
                "status": "active",
                "site_link": "https://horsefarm.ru",
                "okved_approved": True,
                "land_hectares": 150.5,
                "land_status_ok": True
            }
        }
    )