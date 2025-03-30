from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from src.datatypes.enum_notification_type import NotificationType


class NotificationBase(BaseModel):
    title: str = Field(..., max_length=50, description="Заголовок уведомления")
    description: str = Field(..., max_length=50, description="Текст уведомления")
    type: NotificationType = Field(..., description="Тип уведомления")
    user_id: int = Field(..., description="ID пользователя-получателя")


class NotificationCreate(NotificationBase):
    pass


class NotificationResponse(NotificationBase):
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
                "type": "general",
                "user_id": 123
            }
        }
    )