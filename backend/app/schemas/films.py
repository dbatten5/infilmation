"""Module to hold film related schemas."""
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class MovieTypeEnum(str, Enum):
    """Enum for IMDb search result type."""

    MOVIE = "movie"


class SearchResult(BaseModel):
    """Schema for a film search result."""

    title: str
    kind: MovieTypeEnum
    year: Optional[int] = None
    imdb_id: str


class FilmIn(BaseModel):
    """Schema for create film requests."""
