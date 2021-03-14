"""Module to store some utilities based on the Movie model"""
from hashlib import sha1
from phylm.movie import Movie as Phylm
from infilmation.models import Movie
from infilmation import db


def generate_movie_key(title):
    """Generate a sha1 from the title to be stored as the Movie key"""
    return sha1(str.encode(title.lower().strip())).hexdigest()


def get_from_title(title):
    """Return the first movie for a given title"""
    key = generate_movie_key(title)
    return Movie.query.filter(Movie.key == key).first()


def store_from_title(title):
    """Store a new movie based on a given title"""
    key = generate_movie_key(title)
    m = Phylm(title)
    new_movie = Movie(
        key=key,
        title=m.title,
        year=m.year,
        genres=m.genres(),
        runtime=m.runtime(),
        cast=m.cast(),
        directors=m.directors(),
        plot=m.plot(),
        imdb_title=m.imdb_title(),
        imdb_year=m.imdb_year(),
        imdb_score=m.imdb_score(),
        imdb_low_confidence=m.imdb_low_confidence(),
        mtc_title=m.mtc_title(),
        mtc_year=m.mtc_year(),
        mtc_score=m.mtc_score(),
        mtc_low_confidence=m.mtc_low_confidence(),
        rt_title=m.rt_title(),
        rt_year=m.rt_year(),
        rt_tomato_score=m.rt_tomato_score(),
        rt_audience_score=m.rt_audience_score(),
        rt_low_confidence=m.rt_low_confidence()
    )
    db.session.add(new_movie)
    db.session.commit()
    return new_movie


def get_or_create_from_title(title):
    """Return a movie if it exists or create a new one"""
    retrieved_movie = get_from_title(title)
    if retrieved_movie:
        return retrieved_movie
    return store_from_title(title)
