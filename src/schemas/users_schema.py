from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from src.datatypes.enum_organization_type import OrganizationType


class UsersBase(BaseModel):
    email: EmailStr = Field(..., max_length=50, description="Email пользователя (уникальный идентификатор)")
    permission_id: int = Field(..., description="ID уровня доступа пользователя")
    organization_type: OrganizationType = Field(..., description="Тип организации пользователя")
    given_name: str = Field(..., max_length=50, description="Имя пользователя")
    family_name: str = Field(..., max_length=50, description="Фамилия пользователя")
    middle_name: str = Field(..., max_length=50, description="Отчество пользователя (при наличии)")


class UsersCreate(UsersBase):
    pass


class UsersUpdate(UsersBase):
    id: int = Field(..., description="Уникальный идентификатор пользователя в системе")


class UsersResponse(UsersBase):
    id: int = Field(..., description="Уникальный идентификатор пользователя в системе")
    created_at: datetime = Field(..., description="Дата и время создания пользователя")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "email": "user@example.com",
                "permission_id": 2,
                "organization_type": "hippodrome",
                "given_name": "Иван",
                "family_name": "Иванов",
                "middle_name": "Иванович",
                "created_at": "2023-01-01T00:00:00"
            }
        }
    )