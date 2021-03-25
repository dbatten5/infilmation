from sqlalchemy.orm import Session

from app.crud import get_batch_by_key, create_batch
from app.schemas import BatchCreate
from app.tests.utils.create_models import create_batch as create_test_batch


def test_get_batch_by_key(db: Session):
    """
    Given a batch in the database,
    When it's retrieved by key,
    Then the batch from the database is retreived
    """
    db_batch = create_test_batch(db)
    fetched_batch = get_batch_by_key(db, db_batch.key)
    assert fetched_batch.id == db_batch.id


def test_get_batch_by_key_unrecognised(db: Session):
    """
    Given a new batch,
    When it's retrieved by key,
    Then None is returned
    """
    assert get_batch_by_key(db, 'notakey') is None


def test_create_batch(db: Session):
    """
    Given a new batch,
    When the create_batch function is called,
    Then the batch is created and returned
    """
    batch_in = BatchCreate(raw_titles="Film 1")
    batch = create_batch(db, batch=batch_in)
    assert batch.id is not None
