from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from typing import Optional

from src.schemas.query_helper import make_partial_model


class RedisSessionsBase(BaseModel):
    # access_token: UUID = Field(..., description="Уникальный токен доступа")
    # ip: str = Field(..., max_length=24, description="IP адрес запроса")
    browser: str = Field(..., max_length=50, description="Браузер пользователя")
    os: str = Field(..., max_length=50, description="Операционная система")
    # geolocation: str = Field(..., max_length=50, description="Геолокация")


class RedisSessionsAuth(RedisSessionsBase):
    username: str = Field(..., max_length=50, description="Username")
    password: str = Field(..., max_length=50, description="Password")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                # "ip": "192.168.1.1",
                "browser": "Chrome 120.0",
                "os": "Windows 10",
                # "geolocation": "Moscow, Russia",
                "username": "loshadka",
                "password": "saodnoand"
            }
        }
    )

class RedisSessionsCreate(RedisSessionsBase):
    user_id: int = Field(..., description="ID пользователя")
    access_token: UUID = Field(..., description="Уникальный токен доступа")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "user_id": 123,
                "access_token": "550e8400-e29b-41d4-a716-446655440000",
                # "ip": "192.168.1.1",
                "browser": "Chrome 120.0",
                "os": "Windows 10",
                # "geolocation": "Moscow, Russia",
                "username": "loshadka",
                "password": "saodnoand"
            }
        }
    )


class RedisSessionsUpdate(RedisSessionsBase):
    id: int = Field(..., description="Уникальный ID сессии")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "access_token": "550e8400-e29b-41d4-a716-446655440000",
                # "ip": "192.168.1.1",
                "browser": "Chrome 120.0",
                "os": "Windows 10",
                # "geolocation": "Moscow, Russia",
                "username": "loshadka",
                "password": "saodnoand"
            }
        }
    )

class RedisSessionsResponse(RedisSessionsBase):
    id: int = Field(..., description="Уникальный ID сессии")
    user_id: int = Field(..., description="ID пользователя")
    created_at: datetime = Field(..., description="Дата создания сессии")
    expired_at: datetime = Field(..., description="Дата истечения сессии")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "user_id": 123,
                "access_token": "550e8400-e29b-41d4-a716-446655440000",
                # "ip": "192.168.1.1",
                "browser": "Chrome 120.0",
                "os": "Windows 10",
                # "geolocation": "Moscow, Russia",
                "created_at": "2023-12-01T12:00:00",
                "expired_at": "2023-12-31T12:00:00",
                "username": "loshadka",
                "password": "saodnoand"
            }
        }
    )

RedisSessionsQuery = make_partial_model(RedisSessionsResponse)