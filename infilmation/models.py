from sqlalchemy import Column, Integer, String
from infilmation.database import Base

class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    key = Column(String(50), unique=True)
    title = Column(String(255))
    year = Column(Integer)
    genres = Column(String(255))
    runtime = Column(String(255))
    cast = Column(String(255))
    directors = Column(String(255))
    plot = Column(String(255))
    imdb_title = Column(String(255))
    imdb_year = Column(Integer)
    imdb_score = Column(String(255))
    imdb_low_confidence = Column(Integer)
    mtc_title = Column(String(255))
    mtc_year = Column(Integer)
    mtc_score = Column(String(255))
    mtc_low_confidence = Column(Integer)
    rt_title = Column(String(255))
    rt_year = Column(Integer)
    rt_tomato_score = Column(String(255))
    rt_audience_score = Column(String(255))
    rt_low_confidence = Column(Integer)

    def __repr__(self):
        return '<Movie %r>' % (self.key)
