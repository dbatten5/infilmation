from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import models

def test_get_batch(client: TestClient, db: Session):
    """
    Given a batch in the database,
    When the batch is retreived,
    Then the necessary data is returned
    """
    batch = models.Batch(raw_titles='Film 1\nFilm 2')
    db.add(batch)
    db.commit()
    response = client.get(f"/batches/{batch.key}")
    assert response.status_code == 200
    content = response.json()
    assert content['key'] == batch.key
    assert content['completion'] == 0.0


def test_get_batch_with_extras(client: TestClient, db: Session):
    """
    Given a batch in the with related genres, cast and directors,
    When the batch is retreived,
    Then the full data set is returned
    """
    # create models
    batch = models.Batch(raw_titles='Film 1')
    film = models.Film(title='Film 1')
    genre = models.Genre(name='Comedy')
    actor = models.Actor(name='Steve Martin')
    director = models.Director(name='Greta Gerwig')
    db.add_all([batch, film, genre, director])

    # add extra information to flim
    film.genres.append(genre)
    film.cast.append(actor)
    film.directors.append(director)

    # add film to batch
    batch.films.append(film)
    db.commit()

    response = client.get(f"/batches/{batch.key}")
    assert response.status_code == 200
    content = response.json()
    assert len(content['films']) == 1
    assert len(content['films'][0]['genres']) == 1
    assert content['films'][0]['genres'][0]['name'] == 'Comedy'
    assert len(content['films'][0]['cast']) == 1
    assert content['films'][0]['cast'][0]['name'] == 'Steve Martin'
    assert len(content['films'][0]['directors']) == 1
    assert content['films'][0]['directors'][0]['name'] == 'Greta Gerwig'
