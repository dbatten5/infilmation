"""Module to define crud actions."""
from typing import List
from typing import Optional

from phylm import Phylm

from app.models.film import Actor
from app.models.film import Director
from app.models.film import Film
from app.models.film import Genre


async def add_film_genres(film: Film, genres: List[str]) -> None:
    """Save genres against the film.

    Args:
        film: a `Film` instance against which to save the genres
        genres: a list of genres to be saved against the film
    """
    for genre in genres:
        db_genre = await Genre.objects.get_or_create(name=genre)
        await film.genres.add(db_genre)


async def add_film_actors(film: Film, actors: List[str]) -> None:
    """Save actors against the film.

    Args:
        film: a `Film` instance against which to save the actors
        actors: a list of actors to be saved against the film
    """
    for actor in actors:
        db_actor = await Actor.objects.get_or_create(name=actor)
        await film.cast.add(db_actor)


async def add_film_directors(film: Film, directors: List[str]) -> None:
    """Save directors against the film.

    Args:
        film: a `Film` instance against which to save the directors
        directors: a list of directors to be saved against the film
    """
    for director in directors:
        db_director = await Director.objects.get_or_create(name=director)
        await film.directors.add(db_director)


async def create_film(
    title: str,
    year: Optional[int] = None,
    imdb_id: Optional[str] = None,
) -> Film:
    """Create a new film in the database.

    Args:
        title: the title of the film
        year: the year of the film
        imdb_id: the imdb id of the film

    Returns:
        a `Film` object
    """
    phylm = Phylm(title=title, imdb_id=imdb_id, year=year).load_sources(
        ["imdb", "mtc", "rt"]
    )
    film = await Film.objects.create(
        title=title,
        year=phylm.imdb.year,
        runtime=phylm.imdb.runtime,
        plot=phylm.imdb.plot,
        imdb_id=imdb_id,
        imdb_title=phylm.imdb.title,
        imdb_year=phylm.imdb.year,
        imdb_rating=phylm.imdb.rating,
        imdb_low_confidence=phylm.imdb.low_confidence,
        mtc_title=phylm.mtc.title,
        mtc_year=phylm.mtc.year,
        mtc_rating=phylm.mtc.rating,
        mtc_low_confidence=phylm.mtc.low_confidence,
        rt_title=phylm.rt.title,
        rt_year=phylm.rt.year,
        rt_tomato_rating=phylm.rt.tomato_score,
        rt_low_confidence=phylm.rt.low_confidence,
    )
    await add_film_directors(film=film, directors=phylm.imdb.directors())
    await add_film_actors(film=film, actors=phylm.imdb.cast())
    await add_film_genres(film=film, genres=phylm.imdb.genres())
    return film


async def get_or_create_film(
    title: str,
    year: Optional[int] = None,
    imdb_id: Optional[str] = None,
) -> Film:
    """Return a film from the database or a create a new one.

    Args:
        title: the title of the film
        year: the year of the film
        imdb_id: the imdb id of the film

    Returns:
        a `Film` object
    """
    if imdb_id:
        film = await Film.objects.get_or_none(imdb_id=imdb_id)

        if film:
            return film

    return await create_film(title=title, year=year, imdb_id=imdb_id)
