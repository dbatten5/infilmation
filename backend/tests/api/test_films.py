"""Tests for the `movies` router."""
from unittest import mock

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.api.films import router
from app.core.config import settings
from app.models.film import Film

database = Film.Meta.database


class TestSearchFilms:
    """Tests for the `search_films` route."""

    @mock.patch("app.api.films.search_movies", autospec=True)
    def test_success(
        self, mock_search_movies: mock.MagicMock, client: TestClient
    ) -> None:
        """
        Given a search query,
        When the `search_films` endpoint is hit with the query,
        Then a list of search results are returned
        """
        query = "the matrix"

        mock_search_movies.return_value = [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "cover_photo": "https://some-url.com",
                "imdb_id": "0133093",
            },
            {
                "title": "The Matrix Reloaded",
                "kind": "movie",
                "year": 2003,
                "cover_photo": "https://some-url.com",
                "imdb_id": "0234215",
            },
        ]
        url = router.url_path_for("search_films")

        resp = client.get(f"{settings.api_path}{url}?query={query}")

        assert resp.json() == [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "imdb_id": "0133093",
                "cover_photo": "https://some-url.com",
            },
            {
                "title": "The Matrix Reloaded",
                "kind": "movie",
                "year": 2003,
                "imdb_id": "0234215",
                "cover_photo": "https://some-url.com",
            },
        ]

    @mock.patch("app.api.films.search_movies", autospec=True)
    def test_only_films_are_returned(
        self, mock_search_movies: mock.MagicMock, client: TestClient
    ) -> None:
        """
        Given a search query,
        When the `search_films` endpoint is hit with the query,
        Then only a list of movie search results are returned
        """
        query = "the matrix"

        mock_search_movies.return_value = [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "cover_photo": "https://some-url.com",
                "imdb_id": "0133093",
            },
            {
                "title": "The Matrix Tv Show",
                "kind": "episode",
                "year": 2003,
                "cover_photo": "https://some-url.com",
                "imdb_id": "0234215",
            },
        ]
        url = router.url_path_for("search_films")

        resp = client.get(f"{settings.api_path}{url}?query={query}")

        assert resp.json() == [
            {
                "title": "The Matrix",
                "kind": "movie",
                "year": 1999,
                "cover_photo": "https://some-url.com",
                "imdb_id": "0133093",
            },
        ]


class TestCreateFilm:
    """Tests for the `create_film` function."""

    @mock.patch("app.api.films.get_or_create_film", autospec=True)
    @pytest.mark.asyncio
    async def test_success(
        self, mock_get_or_create_film: mock.AsyncMock, client: TestClient
    ) -> None:
        """
        Given a title and imdb_id,
        When the `/films/` endpoint is hit with the query,
        Then the `get_or_create_film` crud function is run
        """
        title = "The Matrix"
        imdb_id = "0133093"
        year = 1999

        mock_get_or_create_film.return_value = Film(
            title=title, imdb_id=imdb_id, year=year
        )

        url = router.url_path_for("create_film")
        response = client.post(
            f"{settings.api_path}{url}",
            json={"title": title, "imdb_id": imdb_id, "year": year},
        )

        assert response.status_code == 200

        assert response.json()["title"] == title
        assert response.json()["year"] == year
        assert response.json()["imdb_id"] == imdb_id

        mock_get_or_create_film.assert_awaited_once_with(
            title=title, imdb_id=imdb_id, year=year
        )


@pytest.mark.skip
class TestGetFilms:
    """Tests for the `get_films` function."""

    @pytest.mark.asyncio
    async def test_success(self, async_client: AsyncClient) -> None:
        """
        Given some films already in the database,
        When the `/films/` endpoint is hit with a list of `imdb_ids`,
        Then the filtered films are returned
        """
        film_1 = await Film.objects.create(title="film 1", imdb_id="1")
        film_2 = await Film.objects.create(title="film 2", imdb_id="2")

        url = router.url_path_for("get_films")

        response = await async_client.get(
            f"{settings.api_path}{url}?imdb_ids=1&imdb_ids=2&imdb_ids=3",
        )

        assert response.status_code == 200

        data = response.json()

        assert len(data) == 2
        assert data[0]["id"] == film_1.id
        assert data[1]["id"] == film_2.id
