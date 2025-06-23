from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from src.schemas.query_helper import make_partial_model


class MediaFilesGroupsBase(BaseModel):
    name: str = Field(..., max_length=50, description="Name of the file group")


class MediaFilesGroupsCreate(MediaFilesGroupsBase):

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "photo",
            }
        }
    )


class MediaFilesGroupsUpdate(MediaFilesGroupsBase):
    id: int = Field(..., description="Group file ID")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "photo",
            }
        }
    )


class MediaFilesGroupsResponse(MediaFilesGroupsBase):
    id: int = Field(..., description="Unique file group ID")
    created_at: datetime = Field(..., description="Group creation timestamp")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "photo",
                "created_at": "2023-01-15T10:30:00",
            }
        }
    )

MediaFilesGroupsQuery = make_partial_model(MediaFilesGroupsResponse)