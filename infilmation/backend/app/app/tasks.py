import random
import time

from sqlalchemy.orm import Session

from .crud import get_film_by_title, create_film
from .schemas import BatchCreate, FilmCreate
from .models import Batch


def process_films(db: Session, batch: BatchCreate) -> Batch:
    batch.status = 'started'
    total_films = batch.initial_count
    titles = batch.raw_titles.splitlines()
    delay = 0
    for idx, title in enumerate(titles):
        batch.current_film = title
        db.commit()
        film = get_film_by_title(db, title)
        if not film:
            if delay:
                time.sleep(delay)
            film_create = FilmCreate(title=title)
            film = create_film(db, film_create)
            delay = random.randint(3,15)
        batch.films.append(film)
        batch.completion = ((idx + 1) / total_films) * 100
        db.commit()
    batch.status = 'finished'
    db.commit()
    return batch
