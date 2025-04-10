from pydantic import BaseModel, Field, ConfigDict
from src.datatypes.enum_usage_direction import UsageDirection


class BreedBase(BaseModel):
    name: str = Field(..., max_length=50, description="Название породы")
    patient_code: int = Field(..., description="Код породы в системе")
    usage_direction: UsageDirection = Field(..., description="Направление использования породы")
    reg_year: int = Field(..., description="Год регистрации породы")
    category: str = Field(..., max_length=50, description="Категория породы")


class BreedCreate(BreedBase):
    pass


class BreedResponse(BreedBase):
    id: int = Field(..., description="Уникальный идентификатор породы")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Арабская",
                "patient_code": 101,
                "usage_direction": "decorative",
                "reg_year": 2020,
                "category": "Верховая"
            }
        }
    )