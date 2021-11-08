"""Tests for the `movies` router."""
from unittest import mock

from fastapi.testclient import TestClient

from app.api.movies import router
from app.core.config import settings


class TestSearch:
    """Tests for the `search` route."""

    @mock.patch("app.api.movies.search_movies", autospec=True)
    def test_success(
        self, mock_search_movies: mock.MagicMock, client: TestClient
    ) -> None:
        """
        Given a search query,
        When the `search` endpoint is hit with the query,
        Then a list of search results are returned
        """
        query = "the matrix"

        mock_search_movies.return_value = [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "cover url": "https://some-url.com",
                "imdb_id": "0133093",
            },
            {
                "title": "The Matrix Reloaded",
                "kind": "movie",
                "year": 2003,
                "cover url": "https://some-url.com",
                "imdb_id": "0234215",
            },
        ]
        url = router.url_path_for("search")

        resp = client.get(f"{settings.api_path}{url}?query={query}")

        assert resp.json() == [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "imdb_id": "0133093",
            },
            {
                "title": "The Matrix Reloaded",
                "kind": "movie",
                "year": 2003,
                "imdb_id": "0234215",
            },
        ]

    @mock.patch("app.api.movies.search_movies", autospec=True)
    def test_only_movies_are_returned(
        self, mock_search_movies: mock.MagicMock, client: TestClient
    ) -> None:
        """
        Given a search query,
        When the `search` endpoint is hit with the query,
        Then only a list of movie search results are returned
        """
        query = "the matrix"

        mock_search_movies.return_value = [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "cover url": "https://some-url.com",
                "imdb_id": "0133093",
            },
            {
                "title": "The Matrix Tv Show",
                "kind": "episode",
                "year": 2003,
                "cover url": "https://some-url.com",
                "imdb_id": "0234215",
            },
        ]
        url = router.url_path_for("search")

        resp = client.get(f"{settings.api_path}{url}?query={query}")

        assert resp.json() == [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "imdb_id": "0133093",
            },
        ]
