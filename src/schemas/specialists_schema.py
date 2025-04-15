from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from src.datatypes.enum_specialist_qualification import SpecialistQualification


class SpecialistsBase(BaseModel):
    given_name: str = Field(..., max_length=50, description="Имя специалиста")
    family_name: str = Field(..., max_length=50, description="Фамилия специалиста")
    middle_name: str = Field(..., max_length=50, description="Отчество специалиста")
    qualification: SpecialistQualification = Field(..., description="Квалификация специалиста")
    age: int = Field(..., ge=18, le=100, description="Возраст специалиста")
    experience_years: Optional[float] = Field(0.0, ge=0, description="Опыт работы в годах")
    license_id: Optional[int] = Field(None, description="ID лицензии в медиафайлах")
    license_expired_at: datetime = Field(..., description="Дата окончания действия лицензии")
    weight: Optional[int] = Field(None, ge=30, le=300, description="Вес специалиста (кг)")
    organization_id: int = Field(..., description="ID организации специалиста")
    created_by_id: int = Field(..., description="ID организации, создавшей запись")


class SpecialistsCreate(SpecialistsBase):
    pass


class SpecialistsUpdate(SpecialistsBase):
    id: int = Field(..., description="Уникальный ID специалиста")
    created_at: datetime = Field(..., description="Дата создания записи")


class SpecialistsResponse(SpecialistsBase):
    id: int = Field(..., description="Уникальный ID специалиста")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T00:00:00",
                "given_name": "Иван",
                "family_name": "Петров",
                "middle_name": "Сергеевич",
                "qualification": "trainer",
                "age": 35,
                "experience_years": 10.5,
                "license_id": 123,
                "license_expired_at": "2025-12-31T00:00:00",
                "weight": 75,
                "organization_id": 1,
                "created_by_id": 1
            }
        }
    )