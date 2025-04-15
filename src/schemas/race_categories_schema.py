from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from src.datatypes.enum_race_category_type import RaceCategoryType


class RaceCategoriesBase(BaseModel):
    name: str = Field(..., max_length=50, description="Название категории скачек")
    type: Optional[RaceCategoryType] = Field(None, description="Тип категории скачек")
    male_allowed: bool = Field(..., description="Разрешено участие жеребцов")
    female_allowed: bool = Field(..., description="Разрешено участие кобыл")
    age_min: Optional[int] = Field(None, ge=0, description="Минимальный возраст лошади (лет)")
    age_max: Optional[int] = Field(None, ge=0, description="Максимальный возраст лошади (лет)")
    breed_id: int = Field(..., description="ID породы, разрешенной к участию")
    region_id: int = Field(..., description="ID региона проведения")
    jockey_weight_min: Optional[int] = Field(None, ge=0, description="Минимальный вес жокея (кг)")
    jockey_weight_max: Optional[int] = Field(None, ge=0, description="Максимальный вес жокея (кг)")


class RaceCategoriesCreate(RaceCategoriesBase):
    pass


class RaceCategoriesUpdate(RaceCategoriesBase):
    id: int = Field(..., description="Уникальный ID категории скачек")
    created_at: datetime = Field(..., description="Дата создания записи")


class RaceCategoriesResponse(RaceCategoriesBase):
    id: int = Field(..., description="Уникальный ID категории скачек")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Скачки для 3-летних чистокровных",
                "type": "commerce",
                "male_allowed": True,
                "female_allowed": True,
                "age_min": 3,
                "age_max": 3,
                "breed_id": 1,
                "region_id": 1,
                "jockey_weight_min": 50,
                "jockey_weight_max": 70,
                "created_at": "2023-01-01T00:00:00"
            }
        }
    )