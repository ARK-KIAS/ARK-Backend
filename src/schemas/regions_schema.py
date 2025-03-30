from pydantic import BaseModel, Field, ConfigDict


class RegionBase(BaseModel):
    name: str = Field(..., max_length=50, description="Название региона")


class RegionCreate(RegionBase):
    pass


class RegionResponse(RegionBase):
    id: int = Field(..., description="Уникальный идентификатор региона")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Московская область"
            }
        }
    )