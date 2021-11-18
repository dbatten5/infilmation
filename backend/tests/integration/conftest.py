"""Module to hold test fixtures etc."""
from typing import AsyncGenerator
from typing import Generator

import pytest
import sqlalchemy
from asgi_lifespan import LifespanManager
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.core.config import settings
from app.main import app
from app.models import metadata


@pytest.fixture(autouse=True, scope="module")
def create_test_database() -> Generator[None, None, None]:
    """Create a test database before tests and tear down afterwards.

    Ensures the test database is being used before doing any operations

    Yields:
        a generator
    """
    assert "test" in str(settings.sqlalchemy_database_uri)

    engine = sqlalchemy.create_engine(settings.sqlalchemy_database_uri)
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


@pytest.fixture(scope="module", name="client")
def client_fixture() -> Generator[TestClient, None, None]:
    """Initialize a `TestClient` to be used in tests.

    Yields:
        the test client
    """
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(name="async_client", scope="package")
async def async_client_fixture() -> AsyncGenerator[AsyncClient, None]:
    """Initialize an `AsyncClient` to be used in tests.

    Yields:
        the async test client
    """
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as test_client:
            yield test_client
