from pydantic import BaseModel, Field, ConfigDict


class SpecialistDocBase(BaseModel):
    specialist_id: int = Field(..., description="ID специалиста, к которому относится документ")
    file_id: int = Field(..., description="ID файла документа в медиа-хранилище")


class SpecialistDocCreate(SpecialistDocBase):
    pass


class SpecialistDocResponse(SpecialistDocBase):
    id: int = Field(..., description="Уникальный ID записи документа специалиста")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "specialist_id": 123,
                "file_id": 456
            }
        }
    )