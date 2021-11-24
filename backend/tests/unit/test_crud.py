"""Tests for `crud` module."""
import vcr

from app import crud
from tests.conftest import FIXTURES_DIR

VCR_FIXTURES_DIR = f"{FIXTURES_DIR}/crud"


class TestGetFilmStreamingProviders:
    """Tests for the `get_film_streaming_providers` function."""

    @vcr.use_cassette(
        f"{VCR_FIXTURES_DIR}/the_revenant.yaml", filter_query_parameters=["api_key"]
    )
    def test_flatrate_and_rental(self) -> None:
        """
        Given a film with flatrate and rental values,
        When the results are returned,
        Then the appropriate dict is returned
        """
        providers = crud.get_film_streaming_providers(tmdb_id="281957")

        assert providers == {
            "netflix": True,
            "amazon_prime": True,
            "amazon_video": True,
        }

    @vcr.use_cassette(
        f"{VCR_FIXTURES_DIR}/dune.yaml", filter_query_parameters=["api_key"]
    )
    def test_no_flatrate_or_rental(self) -> None:
        """
        Given a film with no flatrate and unrecognised rental values,
        When the results are returned,
        Then the appropriate dict is returned
        """
        providers = crud.get_film_streaming_providers(tmdb_id="438631")

        assert providers == {
            "netflix": False,
            "amazon_prime": False,
            "amazon_video": False,
        }
