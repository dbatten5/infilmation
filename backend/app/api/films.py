"""Module to hold the `movies` router."""
from typing import List

from fastapi import APIRouter
from fastapi import Query
from phylm.tools import search_movies

from app.crud import get_or_create_film
from app.models.film import Film
from app.schemas.films import FilmIn
from app.schemas.films import SearchResult

router = APIRouter(prefix="/films")


@router.get("/search", response_model=List[SearchResult])
def search_films(query: str) -> List[SearchResult]:
    """Search for a film from a given query.
    \f
    Args:
        query: the query string

    Returns:
        a list of search results
    """
    search_results = search_movies(query=query)
    return [
        SearchResult(**result) for result in search_results if result["kind"] == "movie"
    ]


@router.post("/", response_model=Film)
async def create_film(film_request: FilmIn) -> Film:
    """Create a new film.
    \f
    Args:
        film_request: a `FilmIn` instance

    Returns:
        a `Film` object
    """
    return await get_or_create_film(
        title=film_request.title, imdb_id=film_request.imdb_id
    )


@router.get("/", response_model=List[Film])
async def get_films(imdb_ids: List[str] = Query([])) -> List[Film]:
    """Filter films by multiple `imdb_id`.
    \f
    Args:
        imdb_ids: a list of `imdb_id` queries

    Returns:
        a list of filtered `Film` objects
    """
    return await Film.objects.filter(imdb_id__in=imdb_ids).all()
