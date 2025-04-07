from datetime import date, time, datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class RaceDayBase(BaseModel):
    name: str = Field(..., max_length=50, description="Название гоночного дня")
    date: Optional[date] = Field(None, description="Дата проведения")
    start_time: Optional[time] = Field(None, description="Время начала")


class RaceDayCreate(RaceDayBase):
    pass


class RaceDayResponse(RaceDayBase):
    id: int = Field(..., description="Уникальный ID гоночного дня")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Приз Антона Павленко",
                "date": "2023-05-15",
                "start_time": "14:30:00",
                "created_at": "2023-01-10T09:15:00"
            }
        }
    )