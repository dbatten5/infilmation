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

    @mock.patch("app.api.films.get_search_results", autospec=True)
    def test_success(
        self, mock_get_search_results: mock.MagicMock, client: TestClient
    ) -> None:
        """
        Given a search query,
        When the `search_films` endpoint is hit with the query,
        Then a list of search results are returned
        """
        query = "the matrix"

        mock_get_search_results.return_value = [
            {
                "id": "123",
                "title": "The Matrix",
                "release_date": "1999-01-01",
            },
            {
                "id": "456",
                "title": "The Matrix Reloaded",
                "release_date": "2003-01-01",
            },
        ]
        url = router.url_path_for("search_films")

        resp = client.get(f"{settings.api_path}{url}?query={query}")

        assert resp.json() == [
            {
                "tmdb_id": "123",
                "title": "The Matrix",
                "release_date": "1999-01-01",
                "year": 1999,
                "cover_photo": None,
                "kind": None,
                "imdb_id": None,
            },
            {
                "tmdb_id": "456",
                "title": "The Matrix Reloaded",
                "release_date": "2003-01-01",
                "year": 2003,
                "cover_photo": None,
                "kind": None,
                "imdb_id": None,
            },
        ]


class TestCreateFilm:
    """Tests for the `create_film` function."""

    @pytest.mark.skip
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
        tmdb_id = "0123213"
        year = 1999

        mock_get_or_create_film.return_value = Film(
            title=title, imdb_id=imdb_id, year=year, tmdb_id=tmdb_id
        )

        url = router.url_path_for("create_film")
        response = client.post(
            f"{settings.api_path}{url}",
            json={"title": title, "imdb_id": imdb_id, "year": year, "tmdb_id": tmdb_id},
        )

        assert response.status_code == 200

        assert response.json()["title"] == title
        assert response.json()["year"] == year
        assert response.json()["imdb_id"] == imdb_id
        assert response.json()["tmdb_id"] == tmdb_id

        mock_get_or_create_film.assert_awaited_once_with(
            title=title, imdb_id=imdb_id, year=year, tmdb_id=tmdb_id
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
