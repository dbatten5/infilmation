from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import Batch

def test_get_batch(client: TestClient, db: Session):
    """
    Given a batch in the database,
    When the batch is retreived,
    Then the necessary data is returned
    """
    batch = Batch(raw_titles='Film 1\nFilm 2')
    db.add(batch)
    db.commit()
    response = client.get(f"/batches/{batch.key}")
    assert response.status_code == 200
    content = response.json()
    assert content['key'] == batch.key
    assert content['completion'] == 0.0
