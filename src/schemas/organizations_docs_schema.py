from pydantic import BaseModel, Field, ConfigDict


class OrganizationDocBase(BaseModel):
    organization_id: int = Field(..., description="ID организации, к которой относится документ")
    file_id: int = Field(..., description="ID файла документа в медиа-хранилище")


class OrganizationDocCreate(OrganizationDocBase):
    pass


class OrganizationDocResponse(OrganizationDocBase):
    id: int = Field(..., description="Уникальный ID связи документа с организацией")

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