from datetime import date, time, datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from src.schemas.query_helper import make_partial_model


class RacesRaceDaysBase(BaseModel):
    race_id: int = Field(..., description="ID скачки")
    race_day_id: int = Field(..., description="ID скакового дня")


class RacesRaceDaysCreate(RacesRaceDaysBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "race_id": "1",
                "race_day_id": "10",
            }
        }
    )


class RacesRaceDaysUpdate(RacesRaceDaysBase):
    id: int = Field(..., description="Уникальный ID")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "race_id": "1",
                "race_day_id": "10",
            }
        }
    )


class RacesRaceDaysResponse(RacesRaceDaysBase):
    id: int = Field(..., description="Уникальный ID гоночного дня")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "race_id": "1",
                "race_day_id": "10",
                "created_at": "2023-01-10T09:15:00"
            }
        }
    )

RacesRaceDaysQuery = make_partial_model(RacesRaceDaysResponse)