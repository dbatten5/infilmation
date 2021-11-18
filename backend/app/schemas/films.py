"""Module to hold film related schemas."""
from datetime import date
from datetime import timedelta
from enum import Enum
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import validator

from app.models.film import Actor
from app.models.film import Director
from app.models.film import Genre


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
    tmdb_id: Optional[str] = None

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
        if value:
            return value

        if not value and "release_date" in values and values["release_date"]:
            return values["release_date"].year

        raise AssertionError("At least one of `year` and `release_date` must be given")


class FilmIn(BaseModel):
    """Schema for create film requests."""

    title: str
    imdb_id: Optional[str] = None
    year: Optional[int] = None
    tmdb_id: Optional[str] = None


class FilmOut(BaseModel):
    """Schema for create film requests."""

    id: int
    title: str
    year: Optional[int] = None
    runtime: Optional[int] = None
    plot: Optional[str] = None
    imdb_id: Optional[str] = None
    imdb: Optional[str] = None
    imdb_year: Optional[int] = None
    imdb_rating: Optional[float] = None
    imdb_low_confidence: bool = False
    mtc_title: Optional[str] = None
    mtc_year: Optional[int] = None
    mtc_rating: Optional[str] = None
    mtc_low_confidence: bool = False
    rt_title: Optional[str] = None
    rt_year: Optional[int] = None
    rt_tomato_rating: Optional[str] = None
    rt_low_confidence: bool = False
    cast: List[Actor]
    directors: List[Director]
    genres: List[Genre]

    @property
    def human_readable_runtime(self) -> Optional[str]:
        """Runtime the runtime in human readable form.

        Returns:
            Optional[str]: the runtime
        """
        if self.runtime:
            return str(timedelta(minutes=self.runtime))[:-3]

        return None
