from pydantic import BaseModel, Field, ConfigDict

from src.schemas.query_helper import make_partial_model


class OrganizationsPhotoBase(BaseModel):
    organization_id: int = Field(..., description="ID организации, к которой относится фото")
    file_id: int = Field(..., description="ID медиафайла в хранилище")


class OrganizationsPhotoCreate(OrganizationsPhotoBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "organization_id": 123,
                "file_id": 456
            }
        }
    )


class OrganizationsPhotoUpdate(OrganizationsPhotoBase):
    id: int = Field(..., description="Уникальный ID связи организации и фото")

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


class OrganizationsPhotoResponse(OrganizationsPhotoBase):
    id: int = Field(..., description="Уникальный ID связи организации и фото")

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

OrganizationsPhotoQuery = make_partial_model(OrganizationsPhotoResponse)