from pydantic import BaseModel, Field, ConfigDict

from src.schemas.query_helper import make_partial_model


class SupportBase(BaseModel):
    category_id: int = Field(..., description="ID категории обращения")
    username: str = Field(..., description="Имя пользователя")
    text: str = Field(..., description="Текст обращения")


class SupportCreate(SupportBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "category_id": 2,
                "username": "user123",
                "text": "Помогите с проблемой в личном кабинете"
            }
        }
    )


class SupportUpdate(SupportBase):
    id: int = Field(..., description="Уникальный ID обращения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "category_id": 2,
                "username": "user123",
                "text": "Помогите с проблемой в личном кабинете"
            }
        }
    )


class SupportResponse(SupportBase):
    id: int = Field(..., description="Уникальный ID обращения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "category_id": 2,
                "username": "user123",
                "text": "Помогите с проблемой в личном кабинете"
            }
        }
    )

SupportQuery = make_partial_model(SupportResponse)