from datetime import datetime, time
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from src.datatypes.enum_currency_type import CurrencyType
from src.datatypes.enum_track_cover import TrackCover
from src.datatypes.enum_track_status import TrackStatus
from src.datatypes.enum_race_type import RaceType


class RacesBase(BaseModel):
    start_time: Optional[time] = Field(None, description="Время начала забега")
    name: Optional[str] = Field(None, max_length=100, description="Название забега")
    race_day_id: int = Field(..., description="ID гоночного дня")
    category_id: int = Field(..., description="ID категории забега")
    prize_money: Optional[int] = Field(None, description="Призовой фонд")
    prize_places: Optional[int] = Field(None, description="Количество призовых мест")
    currency: Optional[CurrencyType] = Field(None, description="Валюта призового фонда")
    capacity: Optional[int] = Field(None, description="Вместимость забега")
    distance: Optional[int] = Field(None, description="Дистанция забега (метры)")
    track_cover: Optional[TrackCover] = Field(None, description="Покрытие трека")
    track_status: Optional[TrackStatus] = Field(None, description="Статус трека")
    type: Optional[RaceType] = Field(None, description="Тип забега")
    with_obstacles: bool = Field(False, description="Есть ли препятствия")


class RacesCreate(RacesBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "start_time": "14:30:00",
                "name": "Гран-при Москвы",
                "race_day_id": 5,
                "category_id": 2,
                "prize_money": 500000,
                "prize_places": 3,
                "currency": "RUB",
                "capacity": 12,
                "distance": 1600,
                "track_cover": "grass",
                "track_status": "wet",
                "type": "gallop",
                "with_obstacles": False
            }
        }
    )


class RacesUpdate(RacesBase):
    id: int = Field(..., description="Уникальный ID забега")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "start_time": "14:30:00",
                "name": "Гран-при Москвы",
                "race_day_id": 5,
                "category_id": 2,
                "prize_money": 500000,
                "prize_places": 3,
                "currency": "RUB",
                "capacity": 12,
                "distance": 1600,
                "track_cover": "grass",
                "track_status": "wet",
                "type": "gallop",
                "with_obstacles": False
            }
        }
    )


class RacesResponse(RacesBase):
    id: int = Field(..., description="Уникальный ID забега")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T00:00:00",
                "start_time": "14:30:00",
                "name": "Гран-при Москвы",
                "race_day_id": 5,
                "category_id": 2,
                "prize_money": 500000,
                "prize_places": 3,
                "currency": "RUB",
                "capacity": 12,
                "distance": 1600,
                "track_cover": "grass",
                "track_status": "wet",
                "type": "gallop",
                "with_obstacles": False
            }
        }
    )