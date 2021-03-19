import uuid
from sqlalchemy import Boolean, Column, Integer, String, Table, ForeignKey, Text
from sqlalchemy.orm import relationship

from .database import Base

batch_film_table = Table('batch_film', Base.metadata,
    Column('batch_id', Integer, ForeignKey('batch.id')),
    Column('film_id', Integer, ForeignKey('film.id'))
)

class Film(Base):
    __tablename__ = 'film'

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(50), unique=True)
    title = Column(String(255))
    year = Column(Integer)
    genres = Column(String(255))
    runtime = Column(String(255))
    cast = Column(String(255))
    directors = Column(String(255))
    plot = Column(String(255))
    imtitle = Column(String(255))
    imyear = Column(Integer)
    imscore = Column(String(255))
    imlow_confidence = Column(Boolean)
    mtc_title = Column(String(255))
    mtc_year = Column(Integer)
    mtc_score = Column(String(255))
    mtc_low_confidence = Column(Boolean)
    rt_title = Column(String(255))
    rt_year = Column(Integer)
    rt_tomato_score = Column(String(255))
    rt_audience_score = Column(String(255))
    rt_low_confidence = Column(Boolean)

    def __repr__(self):
        return f"<Film {self.key} {self.imdb_title}>"

class Batch(Base):
    __tablename__ = 'batch'

    id = Column(Integer, primary_key=True)
    key = Column(String(50), unique=True)
    raw = Column(Text)
    films = relationship('Film', secondary=batch_film_table)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.key = uuid.uuid4().hex

    def __repr__(self):
        return f"<Batch {self.key}>"
