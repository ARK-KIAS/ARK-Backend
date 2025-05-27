from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from typing import Optional
from src.datatypes.enum_bonitation_status import BonitationStatus
from src.datatypes.enum_bonitation_type import BonitationType
from src.schemas.query_helper import make_partial_model


class BonitationsBase(BaseModel):
    organization_id: int = Field(..., description="ID организации-заказчика")
    inspector_id: int = Field(..., description="ID инспектора, взявшего бонитировку")
    prefers_time_min: Optional[datetime] = Field(None, description="Предпочитаемое время начала (от)")
    prefers_time_max: Optional[datetime] = Field(None, description="Предпочитаемое время окончания (до)")
    comment: Optional[str] = Field(None, max_length=500, description="Комментарий от организации")
    org_contact_name: str = Field(..., max_length=250, description="Контактное лицо организации")
    org_contact_tel: str = Field(..., max_length=50, description="Телефон связи")
    org_contact_link: str = Field(..., max_length=500, description="Ссылка на соцсеть связи")
    status: Optional[BonitationStatus] = Field(None, description="Статус бонитировки")
    type: Optional[BonitationType] = Field(None, description="Тип бонитировки")
    is_finished: bool = Field(..., description="Выполнена ли бонитировка")


class BonitationsCreate(BonitationsBase):
    approved_time: Optional[datetime] = Field(None, description="Утверждённое время проведения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "organization_id": 123,
                "inspector_id": 456,
                "prefers_time_min": "2023-02-01T09:00:00",
                "prefers_time_max": "2023-02-01T18:00:00",
                "approved_time": "2023-02-01T10:00:00",
                "comment": "Дополнительные пожелания",
                "org_contact_name": "Иванов Иван",
                "org_contact_tel": "+79991234567",
                "org_contact_link": "t.me/Tyapkin_S",
                "status": "pending",
                "type": "chipization",
                "is_finished": "True"
            }
        }
    )


class BonitationsUpdate(BonitationsBase):
    id: int = Field(..., description="Уникальный ID бонитировки")
    approved_time: Optional[datetime] = Field(None, description="Утверждённое время проведения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "organization_id": 123,
                "inspector_id": 456,
                "prefers_time_min": "2023-02-01T09:00:00",
                "prefers_time_max": "2023-02-01T18:00:00",
                "approved_time": "2023-02-01T10:00:00",
                "comment": "Дополнительные пожелания",
                "org_contact_name": "Иванов Иван",
                "org_contact_tel": "+79991234567",
                "org_contact_link": "t.me/Tyapkin_S",
                "status": "pending",
                "type": "chipization",
                "is_finished": "True"
            }
        }
    )


class BonitationsResponse(BonitationsBase):
    id: int = Field(..., description="Уникальный ID бонитировки")
    created_at: datetime = Field(..., description="Дата создания записи")
    approved_time: Optional[datetime] = Field(None, description="Утверждённое время проведения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T00:00:00",
                "organization_id": 123,
                "inspector_id": 456,
                "prefers_time_min": "2023-02-01T09:00:00",
                "prefers_time_max": "2023-02-01T18:00:00",
                "approved_time": "2023-02-01T10:00:00",
                "comment": "Дополнительные пожелания",
                "org_contact_name": "Иванов Иван",
                "org_contact_tel": "+79991234567",
                "org_contact_link": "t.me/Tyapkin_S",
                "status": "pending",
                "type": "chipization",
                "is_finished": "True"
            }
        }
    )

BonitationsQuery = make_partial_model(BonitationsResponse)