"""Tests for the schemas."""
import pytest
from pydantic import ValidationError

from app.schemas import films


class TestSearchResults:
    """Tests for the `SearchResult` schema."""

    def test_year_gets_populated_from_the_release_date(self) -> None:
        """
        Given a search result with release_date but no year,
        When a `SearchResult` schema is instantiated,
        Then the year is generated from the release_date
        """
        data = {"title": "foo", "release_date": "1999-01-01"}

        obj = films.SearchResult(**data)

        assert obj.year == 1999

    def test_no_year_and_no_release_date_throws_an_error(self) -> None:
        """
        Given a search result with no release_date and no year,
        When a `SearchResult` schema is instantiated,
        Then a validation error is raised
        """
        data = {"title": "foo"}

        with pytest.raises(ValidationError):
            films.SearchResult(**data)
