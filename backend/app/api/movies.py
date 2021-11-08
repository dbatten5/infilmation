"""Module to hold the `movies` router."""
from typing import List

from fastapi import APIRouter
from phylm.tools import search_movies

from app.schemas.movies import SearchResult

router = APIRouter(prefix="/movies")


@router.get("/search", response_model=List[SearchResult])
def search(query: str) -> List[SearchResult]:
    """Search for a movie from a given query.

    Args:
        query: the query string

    Returns:
        a list of search results
    """
    search_results = search_movies(query=query)
    return [
        SearchResult(**result) for result in search_results if result["kind"] == "movie"
    ]
