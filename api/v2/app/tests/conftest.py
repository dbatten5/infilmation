from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.db.session import SessionLocal
from app.db.base import Base
from app.main import app, get_db

from .utils.overrides import override_get_db
from .utils.test_db import TestingSessionLocal, engine

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def db() -> Generator:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
