from pytest_mock import MockerFixture
from sqlalchemy.orm import Session

from app.tasks import process_films
from app.tests.utils.create_models import create_batch, create_film
from app.schemas import FilmCreate
from app.models import Film


class TestProcessFilms:
    def test_no_raw_titles(self, db: Session):
        """
        Given a batch with no raw_titles,
        When the process films task is run,
        Then no films are created and the task is set to finished
        """
        batch = create_batch(db, raw_titles='')
        assert batch.status == 'pending'
        processed_batch = process_films(db, batch)
        assert processed_batch.id == batch.id
        assert batch.status == 'finished'
        assert batch.films == []

    def test_processing_with_film_already_in_the_database(self, db: Session):
        """
        Given a film already processed to the database,
        When a batch is processed referencing that film,
        Then the film is retrieved from the database and added to the batch
        """
        film = create_film(db, title='Film 1')
        batch = create_batch(db, raw_titles='Film 1')
        assert batch.films == []
        process_films(db, batch)
        assert len(batch.films) == 1
        assert batch.films[0].id == film.id
        assert batch.completion == 100.0
        assert batch.status == 'finished'

    def test_processing_film_not_already_in_the_database(
        self,
        db: Session,
        mocker: MockerFixture,
    ):
        """
        Given a new film,
        When a batch is processed,
        Then the film is added to the database and the batch
        """
        batch = create_batch(db, raw_titles='Film 1')
        dummy_film = create_film(db, title='Dummy Title')
        mocker.patch('app.tasks.create_film', return_value=dummy_film)
        batch = create_batch(db, raw_titles='Film 1')
        process_films(db, batch)
        assert len(batch.films) == 1
        assert batch.films[0].title == dummy_film.title

    def test_delay_between_processing_two_films(
        self,
        db: Session,
        mocker: MockerFixture,
    ):
        """
        Given two or more new films,
        When a batch is processed,
        Then tasks sleeps between creating films
        """
        import time
        spy = mocker.spy(time, "sleep")
        mocker.patch('random.randint', return_value=1)
        batch = create_batch(db, raw_titles='Film 1\nFilm 2')
        dummy_film_1 = create_film(db, title='Dummy Title 1')
        dummy_film_2 = create_film(db, title='Dummy Title 2')
        mocker.patch('app.tasks.create_film', side_effect=(dummy_film_1, dummy_film_2))
        process_films(db, batch)
        assert len(batch.films) == 2
        assert batch.films[0].title == dummy_film_1.title
        assert batch.films[1].title == dummy_film_2.title
        assert spy.call_count == 1
        spy.assert_called_once_with(1)

    def test_no_delay_for_films_retrieved_from_the_database(
        self,
        db: Session,
        mocker: MockerFixture,
    ):
        """
        Given two films with the second film already existing in the database,
        When a batch is processed,
        Then tasks sleeps between creating films
        """
        import time
        spy_time = mocker.spy(time, "sleep")
        import random
        spy_random = mocker.spy(random, "randint")

        batch = create_batch(db, raw_titles='Film 1\nFilm 2')
        db_film = create_film(db, title='Film 1')
        dummy_film = create_film(db, title='Dummy Title 1')
        mocker.patch('app.tasks.create_film', return_value=dummy_film)
        process_films(db, batch)
        assert len(batch.films) == 2
        assert batch.films[0].title == db_film.title
        assert batch.films[1].title == dummy_film.title
        assert spy_random.call_count == 1
        assert spy_time.call_count == 0
