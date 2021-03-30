import pytest

from app.models import Batch, Film
from sqlalchemy.orm import Session

class TestBatch:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ("",  0),
            ("\n", 0),
            ("Film 1", 1),
            ("Film 1\nFilm 2", 2),
            ("Film 1\nFilm 2\n", 2),
        ],
    )
    def test_batch_initial_film_count(self, test_input: str, expected: str):
        """
        Given a batch of multiple flims,
        When the initial count is retrieved,
        Then the correct value is returned
        """
        batch = Batch(raw_titles=test_input)
        assert batch.initial_count() == expected

    def test_batch_full_completion(self, db: Session):
        """
        Given a batch with all films added,
        When the completion is retrieved,
        Then expect to see full completion
        """
        batch = Batch(raw_titles='Film 1\nFilm 2')
        film_1 = Film(title='Film 1')
        film_2 = Film(title='Film 2')
        db.add_all([film_1, film_2])
        batch.films.extend([film_1, film_2])
        db.commit()
        assert batch.completion() == 100

    def test_batch_partial_completion(self, db: Session):
        """
        Given a batch with all films added,
        When the completion is retrieved,
        Then expect to see full completion
        """
        batch = Batch(raw_titles='Film 1\nFilm 2')
        film_1 = Film(title='Film 1')
        db.add(film_1)
        batch.films.append(film_1)
        db.commit()
        assert batch.completion() == 50

    def test_batch_no_completion(self, db: Session):
        """
        Given a batch with all films added,
        When the completion is retrieved,
        Then expect to see full completion
        """
        batch = Batch(raw_titles='Film 1\nFilm 2')
        assert batch.completion() == 0
