from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, create_model

from src.datatypes.enum_notification_status import NotificationStatus
from src.datatypes.enum_notification_type import NotificationType
from src.schemas.query_helper import make_partial_model


class NotificationsBase(BaseModel):
    title: str = Field(..., max_length=50, description="Заголовок уведомления")
    description: str = Field(..., max_length=50, description="Текст уведомления")
    status: NotificationStatus = Field(..., description="Статус уведомления")
    type: NotificationType = Field(..., description="Тип уведомления")
    user_id: int = Field(..., description="ID пользователя-получателя")


class NotificationsCreate(NotificationsBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "title": "Новое сообщение",
                "description": "У вас новое сообщение в чате",
                "status": "success",
                "type": "active",
                "user_id": 123
            }
        }
    )


class NotificationsUpdate(NotificationsBase):
    id: int = Field(..., description="Уникальный ID уведомления")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "Новое сообщение",
                "description": "У вас новое сообщение в чате",
                "status": "success",
                "type": "general",
                "user_id": 123
            }
        }
    )


class NotificationsResponse(NotificationsBase):
    id: int = Field(..., description="Уникальный ID уведомления")
    created_at: datetime = Field(..., description="Дата создания уведомления")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T12:00:00",
                "title": "Новое сообщение",
                "description": "У вас новое сообщение в чате",
                "status": "success",
                "type": "general",
                "user_id": 123
            }
        }
    )

NotificationsQuery = make_partial_model(NotificationsResponse)