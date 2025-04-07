from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class PermissionBase(BaseModel):
    name: str = Field(..., max_length=50, description="Name of the permission", example="Admin")
    accounts_all: bool = Field(..., description="Full access to accounts", example=True)
    races_full: bool = Field(..., description="Full access to races data", example=False)
    bonitation_full: bool = Field(..., description="Full access to bonitation data", example=False)
    specialist_full: bool = Field(..., description="Full access to specialist data", example=False)
    files_full: bool = Field(..., description="Full access to files storage", example=False)
    hold_horses: bool = Field(..., description="May have horses and ask for bonitation", example=True)
    create_bonitations: bool = Field(..., description="Can receive requests for bonitation", example=False)
    create_races: bool = Field(..., description="Can send race results", example=False)


class PermissionCreate(PermissionBase):
    pass


class PermissionResponse(PermissionBase):
    id: int = Field(..., description="Unique identifier of the permission")
    created_at: datetime = Field(..., description="Date and time when permission was created")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "created_at": "2023-01-01T00:00:00",
                "name": "Admin",
                "accounts_all": False,
                "races_full": True,
                "bonitation_full": False,
                "specialist_full": False,
                "files_full": False,
                "hold_horses": False,
                "create_bonitations": False,
                "create_races": True
            }
        }
    )