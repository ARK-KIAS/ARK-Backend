from datetime import datetime
from typing import Optional, Text

from pydantic import BaseModel, Field, ConfigDict, create_model

from src.datatypes.enum_news_type import NewsType
from src.schemas.query_helper import make_partial_model


class NewsBase(BaseModel):
    title: str = Field(..., max_length=100, description="Заголовок новости")
    main_text: Text = Field(..., description="Текст новости")
    type: NewsType = Field(..., description="Тип новости")
    file_id: Optional[int] = Field(..., description="ID файла")


class NewsCreate(NewsBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "title": "Новое сообщение",
                "main_text": "Родилась кобыла!",
                "type": "international",
                "file_id": 123
            }
        }
    )


class NewsUpdate(NewsBase):
    id: int = Field(..., description="Уникальный ID уведомления")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "Новое сообщение",
                "main_text": "Родилась кобыла!",
                "type": "international",
                "file_id": 123
            }
        }
    )


class NewsResponse(NewsBase):
    id: int = Field(..., description="Уникальный ID новости")
    created_at: datetime = Field(..., description="Дата создания новости")
    updated_at: datetime = Field(..., description="Дата и время изменения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T12:00:00",
                "updated_at": "2023-01-01T12:00:00",
                "title": "Новое сообщение",
                "main_text": "Родилась кобыла!",
                "type": "international",
                "file_id": 123
            }
        }
    )

NewsQuery = make_partial_model(NewsResponse)