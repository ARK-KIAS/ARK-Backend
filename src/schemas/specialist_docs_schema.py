from pydantic import BaseModel, Field, ConfigDict

from src.schemas.query_helper import make_partial_model


class SpecialistDocsBase(BaseModel):
    specialist_id: int = Field(..., description="ID специалиста, к которому относится документ")
    file_id: int = Field(..., description="ID файла документа в медиа-хранилище")


class SpecialistDocsCreate(SpecialistDocsBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "specialist_id": 123,
                "file_id": 456
            }
        }
    )


class SpecialistDocsUpdate(SpecialistDocsBase):
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


class SpecialistDocsResponse(SpecialistDocsBase):
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

SpecialistDocsQuery = make_partial_model(SpecialistDocsResponse)