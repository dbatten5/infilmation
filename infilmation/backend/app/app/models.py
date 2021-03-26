from typing import List

import uuid
from enum import Enum

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Table,
    ForeignKey,
    Text,
    Float,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.orm import Session

from app.utils import generate_key
from app.db.base_class import Base


batch_film_table = Table('batch_film', Base.metadata,
    Column('batch_id', Integer, ForeignKey('batch.id')),
    Column('film_id', Integer, ForeignKey('film.id'))
)


film_genre_table = Table('film_genre', Base.metadata,
    Column('film_id', Integer, ForeignKey('film.id')),
    Column('genre_id', Integer, ForeignKey('genre.id'))
)


director_film_table = Table('director_film', Base.metadata,
    Column('director_id', Integer, ForeignKey('director.id')),
    Column('film_id', Integer, ForeignKey('film.id'))
)


actor_film_table = Table('actor_film', Base.metadata,
    Column('actor_id', Integer, ForeignKey('actor.id')),
    Column('film_id', Integer, ForeignKey('film.id'))
)


class Film(Base):
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(50), unique=True)
    title = Column(String(255))
    year = Column(Integer)
    runtime = Column(String(255))
    plot = Column(Text)
    imdb_title = Column(String(255))
    imdb_year = Column(Integer)
    imdb_score = Column(String(255))
    imdb_low_confidence = Column(Boolean)
    mtc_title = Column(String(255))
    mtc_year = Column(Integer)
    mtc_score = Column(String(255))
    mtc_low_confidence = Column(Boolean)
    rt_title = Column(String(255))
    rt_year = Column(Integer)
    rt_tomato_score = Column(String(255))
    rt_audience_score = Column(String(255))
    rt_low_confidence = Column(Boolean)

    cast = relationship('Actor', secondary=actor_film_table)
    directors = relationship('Director', secondary=director_film_table)
    genres = relationship('Genre', secondary=film_genre_table)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.key = kwargs.get('key', generate_key(self.title))

    def __repr__(self):
        return f"<Film {self.key} {self.imdb_title or self.title}>"


class BatchStatus(str, Enum):
    pending = 'pending'
    started = 'started'
    finished = 'finished'


class Batch(Base):
    id = Column(Integer, primary_key=True)
    key = Column(String(50), unique=True)
    raw_titles = Column(Text)
    completion = Column(Float, default=0.0, nullable=False)
    status = Column(pgEnum(BatchStatus), nullable=False, default='pending')
    films = relationship('Film', secondary=batch_film_table)
    current_film = Column(Text)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.key = uuid.uuid4().hex

    def __repr__(self):
        return f"<Batch {self.key}>"

    @property
    def initial_count(self):
        stripped_titles = self.raw_titles.rstrip('\n')
        if not stripped_titles:
            return 0
        return stripped_titles.count('\n') + 1


class Genre(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)


class Actor(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Director(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
