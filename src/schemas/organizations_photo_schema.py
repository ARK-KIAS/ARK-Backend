from pydantic import BaseModel, Field, ConfigDict


class OrganizationsPhotoBase(BaseModel):
    organization_id: int = Field(..., description="ID организации, к которой относится фото")
    file_id: int = Field(..., description="ID медиафайла в хранилище")


class OrganizationsPhotoCreate(OrganizationsPhotoBase):
    pass


class OrganizationsPhotoUpdate(OrganizationsPhotoBase):
    id: int = Field(..., description="Уникальный ID связи организации и фото")


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