from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class HorseHistoryBase(BaseModel):
    horse_id: int = Field(..., description="ID лошади, для которой записана история изменений")

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


class HorseHistoryCreate(HorseHistoryBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "horse_id": 12345,
                "height": 165,
                "oblique_length": 160,
                "torso_circumference": 190,
                "pastern_circumference": 20,
                "weight": 550,
                "rating_origin": 85,
                "rating_soundings": 78,
                "rating_exterior": 92,
                "rating_offspring": 65,
                "rating_donorship": 70,
                "rating_typicality": 88,
                "rating_breed": 90,
                "rating_efficiency": 75,
                "rating_adaptability": 82,
                "coolness": 95,
                "insemination_percent": 80
            }
        }
    )

class HorseHistoryUpdate(HorseHistoryBase):
    id: int = Field(..., description="Уникальный идентификатор записи истории")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "horse_id": 123,
                "height": 165,
                "oblique_length": 160,
                "torso_circumference": 190,
                "pastern_circumference": 20,
                "weight": 550,
                "rating_origin": 85,
                "rating_soundings": 78,
                "rating_exterior": 92,
                "rating_offspring": 65,
                "rating_donorship": 70,
                "rating_typicality": 88,
                "rating_breed": 90,
                "rating_efficiency": 75,
                "rating_adaptability": 82,
                "coolness": 95,
                "insemination_percent": 80
            }
        }
    )


class HorseHistoryResponse(HorseHistoryBase):
    id: int = Field(..., description="Уникальный идентификатор записи истории")
    updated_at: datetime = Field(..., description="Дата и время изменения")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "horse_id": 123,
                "updated_at": "2023-01-15T14:30:00",
                "height": 165,
                "oblique_length": 160,
                "torso_circumference": 190,
                "pastern_circumference": 20,
                "weight": 550,
                "rating_origin": 85,
                "rating_soundings": 78,
                "rating_exterior": 92,
                "rating_offspring": 65,
                "rating_donorship": 70,
                "rating_typicality": 88,
                "rating_breed": 90,
                "rating_efficiency": 75,
                "rating_adaptability": 82,
                "coolness": 95,
                "insemination_percent": 80
            }
        }
    )