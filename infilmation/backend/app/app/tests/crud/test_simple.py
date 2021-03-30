from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app import models


def test_creating_a_genre(db: Session) -> None:
    """
    Given a name of a genre,
    When the genre is created,
    Then the genre from the database is returned
    """
    genre_in = schemas.SimpleCreate(name='Comedy')
    genre = crud.genre.create(db, obj_in=genre_in)
    assert genre.name == 'Comedy'


def test_creating_a_director(db: Session) -> None:
    """
    Given a name of a director,
    When the director is created,
    Then the director from the database is returned
    """
    director_in = schemas.SimpleCreate(name='Barry Jenkins')
    director = crud.director.create(db, obj_in=director_in)
    assert director.name == 'Barry Jenkins'


def test_creating_an_actor(db: Session) -> None:
    """
    Given a name of an actor,
    When the actor is created,
    Then the actor from the database is returned
    """
    actor_in = schemas.SimpleCreate(name='Kate Winslet')
    actor = crud.actor.create(db, obj_in=actor_in)
    assert actor.name == 'Kate Winslet'


def test_get_or_create_a_existing_genre(db: Session) -> None:
    """
    Given a genre matching an existing record,
    When the genre is get_or_created,
    Then the genre from the database is returned
    """
    db_genre = models.Genre(name='Comedy')
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    genre_in = schemas.SimpleCreate(name='Comedy')
    genre = crud.genre.get_or_create_by_name(db, obj_in=genre_in)
    assert genre.id == db_genre.id


def test_get_or_create_a_new_genre(db: Session) -> None:
    """
    Given a new genre,
    When the genre is get_or_created,
    Then the genre is created in the database and returned
    """
    genre_in = schemas.SimpleCreate(name='Action')
    genre = crud.genre.get_or_create_by_name(db, obj_in=genre_in)
    assert genre.id is not None
