from pydantic import BaseModel, Field, ConfigDict


class HorsesPhotosBase(BaseModel):
    organization_id: int = Field(..., description="ID организации, загрузившей фото")
    file_id: int = Field(..., description="ID файла в медиа-хранилище")


class HorsesPhotosCreate(HorsesPhotosBase):
    pass


class HorsesPhotosUpdate(HorsesPhotosBase):
    id: int = Field(..., description="Уникальный ID записи о фото лошади")


class HorsesPhotosResponse(HorsesPhotosBase):
    id: int = Field(..., description="Уникальный ID записи о фото лошади")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "organization_id": 123,
                "file_id": 456
            }
        }
    )