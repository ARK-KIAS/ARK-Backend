from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from typing import Optional
from src.datatypes.enum_sex import Sex
from src.datatypes.enum_life_status import LifeStatus


class HorsesBase(BaseModel):
    birth_region_id: int = Field(..., description="ID региона рождения")
    chip_num: int = Field(default=0, description="Номер чипа")
    sex: Sex = Field(default=Sex.none, description="Пол лошади")
    passport_series: str = Field(default="", description="Серия паспорта")
    passport_number: str = Field(default="", description="Номер паспорта")
    passport_issuer: str = Field(default="", description="Кем выдан паспорт")
    passport_issued_at: datetime = Field(..., description="Дата выдачи паспорта")
    nickname: str = Field(default="", description="Кличка")
    suit: str = Field(default="", description="Масть")
    father_id: Optional[int] = Field(..., description="ID отца")
    mother_id: Optional[int] = Field(..., description="ID матери")
    organization_id: int = Field(..., description="ID организации-владельца")
    breed_id: int = Field(..., description="ID породы")
    born_at: Optional[datetime] = Field(None, description="Дата рождения")
    dead_at: Optional[datetime] = Field(None, description="Дата смерти")
    life_status: LifeStatus = Field(default=LifeStatus.none, description="Жизненный статус")
    rating: float = Field(default=0.0, description="Общий рейтинг")

    # Физические параметры
    height: Optional[int] = Field(None, description="Высота в холке (см)")
    oblique_length: Optional[int] = Field(None, description="Косая длина туловища (см)")
    torso_circumference: Optional[int] = Field(None, description="Обхват груди (см)")
    pastern_circumference: Optional[int] = Field(None, description="Обхват пясти (см)")
    weight: Optional[int] = Field(None, description="Вес (кг)")

    # Рейтинги
    rating_origin: Optional[int] = Field(None, description="Рейтинг происхождения")
    rating_soundings: Optional[int] = Field(None, description="Рейтинг промеров")
    rating_exterior: Optional[int] = Field(None, description="Рейтинг экстерьера")
    rating_offspring: Optional[int] = Field(None, description="Рейтинг потомства")
    rating_donorship: Optional[int] = Field(None, description="Рейтинг донорства")
    rating_typicality: Optional[int] = Field(None, description="Рейтинг типичности")
    rating_breed: Optional[int] = Field(None, description="Рейтинг породности")
    rating_efficiency: Optional[int] = Field(None, description="Рейтинг работоспособности")
    rating_adaptability: Optional[int] = Field(None, description="Рейтинг адаптивности")
    coolness: Optional[int] = Field(None, description="Оценка резвости")
    insemination_percent: Optional[int] = Field(None, ge=0, le=100, description="Процент успешных осеменений")


class HorsesCreate(HorsesBase):
    pass


class HorsesUpdate(HorsesBase):
    id: int = Field(..., description="Уникальный ID лошади")


class HorsesResponse(HorsesBase):
    id: int = Field(..., description="Уникальный ID лошади")
    created_at: datetime = Field(..., description="Дата создания записи")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T00:00:00",
                "birth_region_id": 1,
                "chip_num": 123456,
                "sex": "male",
                "passport_series": "AB",
                "passport_number": "123456",
                "passport_issuer": "ВНИИК",
                "passport_issued_at": "2020-05-15T00:00:00",
                "nickname": "Буцефал",
                "suit": "вороной",
                "father_id": 2,
                "mother_id": 3,
                "organization_id": 1,
                "breed_id": 1,
                "born_at": "2018-04-10T00:00:00",
                "life_status": "active",
                "rating": 4.5,
                "height": 165,
                "weight": 450
            }
        }
    )