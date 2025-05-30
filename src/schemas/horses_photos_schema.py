from pydantic import BaseModel, Field, ConfigDict

from src.schemas.query_helper import make_partial_model


class HorsesPhotosBase(BaseModel):
    horse_id: int = Field(..., description="ID организации, загрузившей фото")
    file_id: int = Field(..., description="ID файла в медиа-хранилище")


class HorsesPhotosCreate(HorsesPhotosBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "horse_id": 123,
                "file_id": 456
            }
        }
    )


class HorsesPhotosUpdate(HorsesPhotosBase):
    id: int = Field(..., description="Уникальный ID записи о фото лошади")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "horse_id": 123,
                "file_id": 456
            }
        }
    )


class HorsesPhotosResponse(HorsesPhotosBase):
    id: int = Field(..., description="Уникальный ID записи о фото лошади")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "horse_id": 123,
                "file_id": 456
            }
        }
    )

HorsesPhotosQuery = make_partial_model(HorsesPhotosResponse)