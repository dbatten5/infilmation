import time
import random
from infilmation.models.batch import Batch
from infilmation.utils.film_repository import get_from_title, store_from_title
from infilmation import db


def create_batch(titles_str):
    batch = Batch(raw=titles_str)
    db.session.add(batch)
    titles = titles_str.splitlines()
    delay = 0
    for title in titles:
        if delay:
            time.sleep(delay)
            delay = 0
        film = get_from_title(title)
        if not film:
            film = store_from_title(title)
            delay = random.randint(3,30)
        batch.films.append(film)
    db.session.commit()
    return batch
