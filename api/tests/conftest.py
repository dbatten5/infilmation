import pytest
from infilmation import create_app
from infilmation import db
from infilmation.models.batch import Batch
from infilmation.models.film import Film


@pytest.fixture(scope='module')
def standalone_client():
    flask_app = create_app('testing')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def client():
    flask_app = create_app('testing')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()


@pytest.fixture(scope='module')
def batch(client):
    new_batch = Batch(raw='Film A\nFilm B')
    db.session.add(new_batch)
    db.session.commit()
    return new_batch


@pytest.fixture(scope='module')
def film(client):
    new_film = Film(title='Film A')
    db.session.add(new_film)
    db.session.commit()
    return new_film
