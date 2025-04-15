from pydantic import BaseModel, Field, ConfigDict


class OrganizationsDocsBase(BaseModel):
    organization_id: int = Field(..., description="ID организации, к которой относится документ")
    file_id: int = Field(..., description="ID файла документа в медиа-хранилище")


class OrganizationsDocsCreate(OrganizationsDocsBase):
    pass


class OrganizationsDocsUpdate(OrganizationsDocsBase):
    id: int = Field(..., description="Уникальный ID связи документа с организацией")


class OrganizationsDocsResponse(OrganizationsDocsBase):
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