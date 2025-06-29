from pydantic import BaseModel, Field, ConfigDict

from src.schemas.query_helper import make_partial_model


class RegionsBase(BaseModel):
    name: str = Field(..., max_length=50, description="Название региона")


class RegionsCreate(RegionsBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "Московская область"
            }
        }
    )


class RegionsUpdate(RegionsBase):
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


class RegionsResponse(RegionsBase):
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

RegionsQuery = make_partial_model(RegionsResponse)