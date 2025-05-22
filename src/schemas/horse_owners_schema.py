from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class HorseOwnersBase(BaseModel):
    organization_id: int = Field(..., description="ID организации-владельца")
    user_id: int = Field(..., description="ID пользователя-владельца")
    horse_id: int = Field(..., description="ID лошади")
    percent: int = Field(default=0, ge=0, le=100, description="Доля владения в процентах (0-100)")


class HorseOwnersCreate(HorseOwnersBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "organization_id": 123,
                "user_id": 456,
                "horse_id": 789,
                "percent": 50
            }
        }
    )


class HorseOwnersUpdate(HorseOwnersBase):
    id: int = Field(..., description="Уникальный идентификатор записи о владельце")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "organization_id": 123,
                "user_id": 456,
                "horse_id": 789,
                "percent": 50
            }
        }
    )


class HorseOwnersResponse(HorseOwnersBase):
    id: int = Field(..., description="Уникальный идентификатор записи о владельце")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "organization_id": 123,
                "user_id": 456,
                "horse_id": 789,
                "percent": 50
            }
        }
    )