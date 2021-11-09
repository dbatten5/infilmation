"""Module to hold test fixtures etc."""
from typing import AsyncGenerator
from typing import Generator

import pytest
import sqlalchemy
from fastapi.testclient import TestClient

from app.core.config import settings
from app.db import database
from app.main import app
from app.models import metadata


@pytest.fixture(autouse=True, scope="module")
def create_test_database() -> Generator[None, None, None]:
    """Create a test database before tests and tear down afterwards."""
    engine = sqlalchemy.create_engine(settings.sqlalchemy_database_uri)
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    """Initialize a `TestClient` to be used in tests.

    Yields:
        the test client
    """
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(name="use_transaction")
async def use_transaction_fixture() -> AsyncGenerator[None, None]:
    """Wrap a test in a database transaction."""
    async with database, database.transaction(force_rollback=True):
        yield
