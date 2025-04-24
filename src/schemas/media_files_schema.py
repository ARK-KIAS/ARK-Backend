from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class MediaFilesBase(BaseModel):
    bucket_name: str = Field(..., max_length=50, description="Name of the storage bucket")
    file_name: str = Field(..., max_length=50, description="Original file name", unique=True)
    extension: str = Field(..., max_length=50, description="File extension")


class MediaFilesCreate(MediaFilesBase):
    pass


class MediaFilesUpdate(MediaFilesBase):
    id: int = Field(..., description="Unique file ID")
    deleted_at: Optional[datetime] = Field(None, description="File deletion timestamp (if deleted)")


class MediaFilesResponse(MediaFilesBase):
    id: int = Field(..., description="Unique file ID")
    created_at: datetime = Field(..., description="File creation timestamp")
    deleted_at: Optional[datetime] = Field(None, description="File deletion timestamp (if deleted)")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "bucket_name": "user-uploads",
                "file_name": "profile_123",
                "extension": "jpg",
                "created_at": "2023-01-15T10:30:00",
                "deleted_at": None
            }
        }
    )