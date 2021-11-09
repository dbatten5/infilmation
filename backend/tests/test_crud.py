"""Tests for the `crud` module."""
from unittest import mock

import pytest

from app import crud
from app.models.film import Actor
from app.models.film import Director
from app.models.film import Film
from app.models.film import Genre

database = Film.Meta.database

pytestmark = [pytest.mark.usefixtures("use_transaction"), pytest.mark.asyncio]


class TestAddFilmGenres:
    """Tests for the `add_film_genres` function."""

    async def test_success(self) -> None:
        """
        Given a list of genres, one pre-existing and one not, and a film instance,
        When the `add_film_genres` function is invoked,
        Then the missing genres are added and all are saved against the film
        """
        genres = ["Action", "Sci-fi"]

        # setup, create the existing genre and the film
        sci_fi_genre = await Genre.objects.create(name="Sci-fi")
        film = await Film.objects.create(title="The Matrix")

        # function under test
        await crud.add_film_genres(film=film, genres=genres)

        # assert that the new genre was added
        action_genre = await Genre.objects.get(name="Action")
        assert action_genre

        await film.load()

        # assert that the actors were saved against the film
        assert await film.genres.values_list(fields=["id"], flatten=True) == [
            sci_fi_genre.id,
            action_genre.id,
        ]


class TestAddFilmActors:
    """Tests for the `add_film_actors` function."""

    async def test_success(self) -> None:
        """
        Given a list of actors, one pre-existing and one not, and a film instance,
        When the `add_film_actors` function is invoked,
        Then the missing actors are added and all are saved against the film
        """
        actors = ["John", "Jane"]

        # setup, create the existing actor and the film
        jane_actor = await Actor.objects.create(name="Jane")
        film = await Film.objects.create(title="The Matrix")

        # function under test
        await crud.add_film_actors(film=film, actors=actors)

        # assert that the new actor was added
        john_actor = await Actor.objects.get(name="John")
        assert john_actor

        await film.load()

        # assert that the actors were saved against the film
        assert await film.cast.values_list(fields=["id"], flatten=True) == [
            jane_actor.id,
            john_actor.id,
        ]


class TestAddFilmDirectors:
    """Tests for the `add_film_directors` function."""

    async def test_success(self) -> None:
        """
        Given a list of directors, one pre-existing and one not, and a film instance,
        When the `add_film_directors` function is invoked,
        Then the missing directors are added and all are saved against the film
        """
        directors = ["John", "Jane"]

        # setup, create the existing director and the film
        jane_director = await Director.objects.create(name="Jane")
        film = await Film.objects.create(title="The Matrix")

        # function under test
        await crud.add_film_directors(film=film, directors=directors)

        # assert that the new director was added
        john_director = await Director.objects.get(name="John")
        assert john_director

        await film.load()

        # assert that the directors were saved against the film
        assert await film.directors.values_list(fields=["id"], flatten=True) == [
            jane_director.id,
            john_director.id,
        ]


@pytest.mark.integration
class TestCreateFilm:
    """Tests for the `create_film` function."""

    async def test_create_film(self) -> None:
        """
        Given a title and a `imdb_id`,
        When the `create_film` function is invoked,
        Then the film is added along with its directors, cast and genres
        """
        await crud.create_film(title="The Matrix", imdb_id="0133093")

        film = await Film.objects.get(imdb_id="0133093")

        assert film.dict() == {
            "title": "The Matrix",
            "cast": [],
            "directors": [],
            "genres": [],
            "id": 1,
            "imdb_id": "0133093",
            "imdb_low_confidence": False,
            "imdb_rating": 8.7,
            "imdb_title": "The Matrix",
            "imdb_year": 1999,
            "mtc_low_confidence": False,
            "mtc_rating": 73,
            "mtc_title": "The Matrix",
            "mtc_year": 1999,
            "plot": "When a beautiful stranger leads computer hacker Neo to a "
            "forbidding underworld, he discovers the shocking truth--the life he knows "
            "is the elaborate deception of an evil cyber-intelligence.",
            "rt_low_confidence": False,
            "rt_title": "The Matrix",
            "rt_tomato_rating": 88,
            "rt_year": 1999,
            "runtime": 136,
            "year": 1999,
        }


class TestGetOrCreateFilm:
    """Tests for the `get_or_create_film` function."""

    async def test_film_already_exists(self) -> None:
        """
        Given a film already existent in the database,
        When the `get_or_create_film` function is invoked,
        Then the existent film is returned
        """
        existing_film = await Film.objects.create(title="The Matrix", imdb_id="0133093")

        film = await crud.get_or_create_film(title="The Matrix", imdb_id="0133093")

        assert film == existing_film

    @mock.patch("app.crud.create_film", autospec=True)
    async def test_film_doesnt_already_exist(
        self, mock_create_film: mock.MagicMock
    ) -> None:
        """
        Given a new film,
        When the `get_or_create_film` function is invoked,
        Then a new film is created
        """
        mock_create_film.return_value = mock.Mock()

        film = await crud.get_or_create_film(title="The Matrix", imdb_id="0133093")

        assert film == mock_create_film.return_value

        mock_create_film.assert_called_once_with(title="The Matrix", imdb_id="0133093")

    @mock.patch("app.crud.create_film", autospec=True)
    async def test_only_title_provided(self, mock_create_film: mock.MagicMock) -> None:
        """
        Given a new film where only the title is provided,
        When the `get_or_create_film` function is invoked,
        Then a new film is created
        """
        mock_create_film.return_value = mock.Mock()

        film = await crud.get_or_create_film(title="The Matrix")

        assert film == mock_create_film.return_value

        mock_create_film.assert_called_once_with(title="The Matrix", imdb_id=None)
