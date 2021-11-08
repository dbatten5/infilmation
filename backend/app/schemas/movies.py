"""Module to hold movie related schemas."""
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class MovieTypeEnum(str, Enum):
    """Enum for IMDb search result type."""

    MOVIE = "movie"


class SearchResult(BaseModel):
    """Schema for a movie search result."""

    title: str
    kind: MovieTypeEnum
    year: Optional[int] = None
    imdb_id: str
