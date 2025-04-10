from pydantic import BaseModel, Field, ConfigDict


class BonitationHorsesBase(BaseModel):
    bonitation_id: int = Field(..., description="ID связанной бонитировки", example=1)
    horse_id: int = Field(..., description="ID связанной лошади", example=5)


class BonitationHorsesCreate(BonitationHorsesBase):
    pass


class BonitationHorsesResponse(BonitationHorsesBase):
    id: int = Field(..., description="Уникальный идентификатор связи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 123,
                "bonitation_id": 1,
                "horse_id": 5
            }
        }
    )