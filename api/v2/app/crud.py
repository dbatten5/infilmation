from typing import Any, Optional, TypeVar, Generic, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from pydantic import BaseModel
from phylm import Phylm

from app.utils import generate_key
from app.db.base_class import Base
from . import models, schemas


def get_film_by_title(db: Session, title: str):
    key = generate_key(title)
    return db.query(models.Film).filter(models.Film.key == key).first()


def create_film(db: Session, film: schemas.FilmCreate):
    phylm = Phylm(film.title)
    db_film = models.Film(
        title=phylm.title,
        year=phylm.year,
        runtime=phylm.runtime(),
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
    add_film_genres(db, db_film, phylm.genres())
    add_film_cast(db, db_film, phylm.cast())
    add_film_directors(db, db_film, phylm.directors())
    return db_film


def add_film_genres(db: Session, film: schemas.Film, genres: List[str]):
    for genre_name in genres:
        db_genre = genre.get_or_create_by_name(
            db,
            schemas.SimpleCreate(name=genre_name),
        )
        film.genres.append(db_genre)
    db.commit()


def add_film_cast(db: Session, film: schemas.Film, actors: List[str]):
    for actor_name in actors:
        db_actor = actor.get_or_create_by_name(
            db,
            schemas.SimpleCreate(name=actor_name),
        )
        film.cast.append(db_actor)
    db.commit()


def add_film_directors(db: Session, film: schemas.Film, directors: List[str]):
    for director_name in directors:
        db_director = director.get_or_create_by_name(
            db,
            schemas.SimpleCreate(name=director_name),
        )
        film.directors.append(db_director)
    db.commit()


def get_or_create_film(db: Session, film: schemas.FilmCreate):
    db_film = get_film_by_title(db, film.title)
    if db_film:
        return db_film
    return create_film(db, film)


def get_batch_by_key(db: Session, key: str):
    batches = db.query(models.Batch).all()
    return db.query(models.Batch).filter(models.Batch.key == key).first()


def create_batch(db: Session, batch: schemas.BatchCreate):
    db_batch = models.Batch(raw_titles=batch.raw_titles)
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDSimpleModel(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_or_create_by_name(self, db: Session, obj_in: CreateSchemaType) -> Optional[ModelType]:
        db_record = db.query(self.model).filter(self.model.name == obj_in.name).first()
        if db_record:
            return db_record
        return self.create(db, obj_in=obj_in)


class CRUDGenre(CRUDSimpleModel[models.Genre, schemas.SimpleCreate]):
    pass

genre = CRUDGenre(models.Genre)


class CRUDActor(CRUDSimpleModel[models.Actor, schemas.SimpleCreate]):
    pass

actor = CRUDActor(models.Actor)


class CRUDDirector(CRUDSimpleModel[models.Director, schemas.SimpleCreate]):
    pass

director = CRUDDirector(models.Director)
