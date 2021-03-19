from sqlalchemy.orm import Session
from phylm import Phylm

from app.utils import generate_key
from . import models, schemas


def get_film_by_title(db: Session, title: str):
    key = generate_key(title)
    return db.query(models.Film).filter(models.Film.key == key).first()


def create_film(db: Session, film: schemas.FilmCreate):
    phylm = Phylm(film.title)
    db_film = models.Film(
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
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film


def get_or_create_film(db: Session, film: schemas.FilmCreate):
    db_film = get_film_by_title(db, film.title)
    if db_film:
        return db_film
    return create_film(db, film)


def get_batch_by_key(db: Session, key: str):
    return db.query(models.Batch).filter(models.Batch.key == key).first()


def create_batch(db: Session, batch: schemas.BatchCreate):
    db_batch = models.Batch(raw_titles=batch.raw_titles)
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch
