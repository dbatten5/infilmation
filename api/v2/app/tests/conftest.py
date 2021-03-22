from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.db.session import SessionLocal
from app.db.base import Base
from app.main import app, get_db


def get_test_db_session() -> Session:
    sqlalchemy_database_url = "sqlite:////tmp/test.db"
    engine = create_engine(
        sqlalchemy_database_url, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal()


def override_get_db():
    try:
        db = get_test_db_session()
        yield db
    finally:
        db.close()


@pytest.fixture()
def db() -> Generator:
    yield get_test_db_session()


@pytest.fixture(scope="module")
def client() -> Generator:
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
