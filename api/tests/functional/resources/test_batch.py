"""Module for testing Batch Blueprint routes"""

from infilmation import db
from infilmation.models.film import Film

def test_get_batch(client, batch):
    """
    Given a batch in the database,
    When the batch/<key> route is requested,
    Then assert that the batch is returned as a json response
    """
    response = client.get(f"/batch/{batch.key}")
    assert response.status_code == 200
    assert response.get_json()['key'] == batch.key

def test_get_batch_with_films(client, batch, film):
    """
    Given a batch with an associated film,
    When a request is made to get the batch,
    Then the film data is returned in the response
    """
    batch.films.append(film)
    db.session.commit()
    response = client.get(f"/batch/{batch.key}")
    assert response.status_code == 200
    response_json = response.get_json()
    assert len(response_json['films']) == 1
    assert response_json['films'][0]['title'] == film.title

def test_get_batch_not_found(client):
    """
    Given a nonexistent batch key,
    When the batch/<key> route is requested,
    Then assert that a 404 is returned
    """
    response = client.get('/batch/a')
    assert response.status_code == 404

def test_create_batch(client):
    """
    Given a collection of film titles,
    When a request is made to the post batch endpoint,
    Then the batch is created and returned
    """
    film1 = Film(title='Film 1')
    film2 = Film(title='Film 2')
    db.session.add_all([film1, film2])
    db.session.commit()
    response = client.post('/batch', json={'titles': 'Film 1\nFilm 2'})
    assert response.status_code == 201
    response_json = response.get_json()
    assert response_json['key']
    assert len(response_json['films']) == 2
    assert response_json['films'][0]['title'] == 'Film 1'
    assert response_json['films'][1]['title'] == 'Film 2'
