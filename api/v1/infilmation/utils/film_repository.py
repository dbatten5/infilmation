"""Module to store some utilities based on the Film model"""
from phylm import Phylm
from infilmation.models.film import Film
from infilmation import db
from infilmation.utils.general import generate_key


def get_from_title(title):
    """Return the first film for a given title"""
    key = generate_key(title)
    return Film.query.filter(Film.key == key).first()


def store_from_title(title):
    """Store a new film based on a given title"""
    phylm = Phylm(title)
    new_film = Film(
        title=phylm.title,
        year=phylm.year,
        genres=phylm.genres(),
        runtime=phylm.runtime(),
        cast=phylm.cast(),
        directors=phylm.directors(),
        plot=phylm.plot(),
        imdb_title=phylm.imdb_title(),
        imdb_year=phylm.imdb_year(),
        imdb_score=phylm.imdb_score(),
        imdb_low_confidence=phylm.imdb_low_confidence(),
        mtc_title=phylm.mtc_title(),
        mtc_year=phylm.mtc_year(),
        mtc_score=phylm.mtc_score(),
        mtc_low_confidence=phylm.mtc_low_confidence(),
        rt_title=phylm.rt_title(),
        rt_year=phylm.rt_year(),
        rt_tomato_score=phylm.rt_tomato_score(),
        rt_audience_score=phylm.rt_audience_score(),
        rt_low_confidence=phylm.rt_low_confidence()
    )
    db.session.add(new_film)
    db.session.commit()
    return new_film


def get_or_create_from_title(title):
    """Return a film if it exists or create a new one"""
    retrieved_film = get_from_title(title)
    if retrieved_film:
        return retrieved_film
    return store_from_title(title)
