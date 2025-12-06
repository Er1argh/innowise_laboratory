"""Pydantic schemas (Pydantic v2) for Book endpoints."""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


# Output schema.
class BookOut(BaseModel):
    """
    Schema for returning Book objects from endpoints.
    Uses `from_attributes=True` to support returning SQLAlchemy models directly.
    """
    id: int
    title: str
    author: str
    year: Optional[int]

    model_config = ConfigDict(from_attributes=True)


# Create schema.
class BookCreate(BaseModel):
    """Schema for creating a book. 'Title' and 'Author' fields are required."""
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: Optional[int] = None


# Update schema.
class BookUpdate(BaseModel):
    """Schema for partial updates. Fields are optional."""
    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    year: Optional[int] = None
