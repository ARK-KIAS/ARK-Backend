from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class HorseHistoryBase(BaseModel):
    horse_id: int = Field(..., description="ID лошади, для которой записана история изменений")
    field_name: str = Field(..., description="Название измененного поля", max_length=255)
    new_value: str = Field(..., description="Новое значение поля", max_length=255)


class HorseHistoryCreate(HorseHistoryBase):
    updated_at: Optional[datetime] = Field(None, description="Дата и время изменения")


class HorseHistoryResponse(HorseHistoryBase):
    id: int = Field(..., description="Уникальный идентификатор записи истории")
    updated_at: datetime = Field(..., description="Дата и время изменения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "horse_id": 123,
                "field_name": "nickname",
                "new_value": "Буцефал",
                "updated_at": "2023-01-15T14:30:00"
            }
        }
    )