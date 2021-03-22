from typing import List, Optional, Any
from pydantic import BaseModel


class FilmBase(BaseModel):
    title: str


class FilmCreate(FilmBase):
    pass


class Film(FilmBase):
    id: int
    key: str
    year: Optional[int]
    genres: Optional[str]
    runtime: Optional[str]
    cast: Optional[str]
    directors: Optional[str]
    plot: Optional[str]
    imdb_title: Optional[str]
    imdb_year: Optional[int]
    imdb_score: Optional[str]
    imdb_low_confidence: Optional[bool]
    mtc_title: Optional[str]
    mtc_year: Optional[int]
    mtc_score: Optional[str]
    mtc_low_confidence: Optional[bool]
    rt_title: Optional[str]
    rt_year: Optional[int]
    rt_tomato_score: Optional[str]
    rt_audience_score: Optional[str]
    rt_low_confidence: Optional[bool]

    class Config:
        orm_mode = True


class BatchBase(BaseModel):
    pass


class BatchCreate(BatchBase):
    raw_titles: str


class BatchCreateOut(BatchBase):
    key: str


class Batch(BatchBase):
    id: int
    key: str
    films: List[Film] = []
    completion: int
    status: str

    class Config:
        orm_mode = True
