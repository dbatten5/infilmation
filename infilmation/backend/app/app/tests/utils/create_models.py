from sqlalchemy.orm import Session

from app import crud
from app.schemas import BatchCreate
from app.models import Film, Batch


def create_batch(db: Session, raw_titles='Film 1\nFilm 2') -> Batch:
    batch_in = BatchCreate(raw_titles=raw_titles)
    return crud.create_batch(db, batch_in)


def create_film(db: Session, title: str = 'Film 1', **kwargs) -> Film:
    film = Film(title=title, **kwargs)
    db.add(film)
    db.commit()
    return film
