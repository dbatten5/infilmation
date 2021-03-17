"""Module for Film model unit tests"""

from infilmation.models.film import Film

def test_film_repr():
    """
    Given a Film object,
    When the representation is called,
    Then expect to receive the correct representation
    """
    film = Film(
        key='abc',
        title='The Movie',
        imdb_title='The Movie',
    )
    assert film.__repr__() == '<Film abc The Movie>'


def test_film_key():
    """
    Given a film title,
    When a Film object is created from it,
    Then the key is automatically populated
    """
    title = 'Film A'
    film = Film(title=title)
    assert film.key is not None
