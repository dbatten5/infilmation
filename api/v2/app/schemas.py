from typing import List
from pydantic import BaseModel


class FilmBase(BaseModel):
    title: str


class FilmCreate(FilmBase):
    pass


class Film(FilmBase):
    id: int
    key: str
    year: int
    genres: str
    runtime: str
    cast: str
    directors: str
    plot: str
    imtitle: str
    imyear: int
    imscore: str
    imlow_confidence: bool
    mtc_title: str
    mtc_year: int
    mtc_score: str
    mtc_low_confidence: bool
    rt_title: str
    rt_year: int
    rt_tomato_score: str
    rt_audience_score: str
    rt_low_confidence: bool

    class Config:
        orm_mode = True


class BatchBase(BaseModel):
    raw_titles: str


class BatchCreate(BatchBase):
    pass


class Batch(BatchBase):
    id: int
    key: str
    films: List[Film] = []

    class Config:
        orm_mode = True
