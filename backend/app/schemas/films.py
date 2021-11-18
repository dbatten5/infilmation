"""Module to hold film related schemas."""
from datetime import date
from enum import Enum
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import BaseModel
from pydantic import validator


class MovieTypeEnum(str, Enum):
    """Enum for IMDb search result type."""

    MOVIE = "movie"


class SearchResult(BaseModel):
    """Schema for a film search result."""

    title: str
    kind: Optional[MovieTypeEnum] = None
    imdb_id: Optional[str] = None
    cover_photo: Optional[str] = None
    release_date: Optional[date] = None
    year: Optional[int] = None

    @validator("year", pre=True, always=True)
    def assemble_year(
        cls, value: Optional[date], values: Dict[str, Any]  # noqa: N805,B902
    ) -> Any:
        """Assemble the year.

        If year is blank but there is a `release_date` field, then extract the year from
        the release date and set the year to it

        Args:
            value: the value to be validated
            values: a dict of the other values in this config

        Raises:
            AssertionError: if neither year nor release_date is set

        Returns:
            the year
        """
        if not value and not values["release_date"]:
            raise AssertionError(
                "At least one of `year` and `release_date` must be given"
            )

        if not value and values["release_date"]:
            return values["release_date"].year


class FilmIn(BaseModel):
    """Schema for create film requests."""

    title: str
    imdb_id: Optional[str] = None
    year: Optional[int] = None
