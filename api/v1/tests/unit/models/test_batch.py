"""Module for Batch model unit tests"""

from infilmation.models.batch import Batch

def test_batch_key():
    """
    Given the Batch model,
    When a new Batch is instantiated,
    Then the batch has a uuid for a key
    """
    batch = Batch(raw='Film A\nFilm B')
    assert batch.key is not None

def test_batch_repr():
    """
    Given a Batch object,
    When the representation is called,
    Then expect to receive the correct representation
    """
    batch = Batch(raw='Film A\nFilm B')
    assert batch.__repr__() == f"<Batch {batch.key}>"
