from datetime import datetime, timedelta
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from src.schemas.query_helper import make_partial_model


class HorsesRacesBase(BaseModel):
    race_id: int = Field(..., description="ID забега/соревнования")
    horse_id: int = Field(..., description="ID лошади-участницы")
    rider_id: Optional[int] = Field(None, description="ID жокея/наездника")
    trainer_id: Optional[int] = Field(None, description="ID тренера")
    time: Optional[timedelta] = Field(None, description="Зафиксированное время прохождения дистанции")
    result_place: Optional[int] = Field(None, ge=1, description="Занятое место в забеге")
    start_place: Optional[int] = Field(None, ge=1, description="Стартовый номер/позиция")
    prize_money: Optional[int] = Field(None, ge=0, description="Сумма выигрыша")
    handicap: Optional[int] = Field(None, description="Гандикап (вес и т.д.)")
    doping_control_ok: Optional[bool] = Field(None, description="Прошел ли допинг-контроль")


class HorsesRacesCreate(HorsesRacesBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "race_id": 123,
                "horse_id": 456,
                "rider_id": 789,
                "trainer_id": 101,
                "time": "00:01:30.500",
                "result_place": 2,
                "start_place": 5,
                "prize_money": 50000,
                "handicap": 3,
                "doping_control_ok": True
            }
        }
    )


class HorsesRacesUpdate(HorsesRacesBase):
    id: int = Field(..., description="Уникальный ID записи о забеге")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "race_id": 123,
                "horse_id": 456,
                "rider_id": 789,
                "trainer_id": 101,
                "time": "00:01:30.500",
                "result_place": 2,
                "start_place": 5,
                "prize_money": 50000,
                "handicap": 3,
                "doping_control_ok": True
            }
        }
    )


class HorsesRacesResponse(HorsesRacesBase):
    id: int = Field(..., description="Уникальный ID записи о забеге")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-05-15T14:30:00",
                "race_id": 123,
                "horse_id": 456,
                "rider_id": 789,
                "trainer_id": 101,
                "time": "00:01:30.500",
                "result_place": 2,
                "start_place": 5,
                "prize_money": 50000,
                "handicap": 3,
                "doping_control_ok": True
            }
        }
    )

HorsesRacesQuery = make_partial_model(HorsesRacesResponse)