from pytest_mock import MockerFixture
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app import models
from app.tests.utils.create_models import create_film
from app.tests.utils.phylm import Phylm


def test_get_film_by_title(db: Session):
    """
    Given a film in the database,
    When it's retrieved by title,
    Then the film from the database is retreived
    """
    db_film = create_film(db)
    fetched_film = crud.get_film_by_title(db, db_film.title)
    assert fetched_film.id == db_film.id


def test_get_film_by_title_unrecognised(db: Session):
    """
    Given a new film,
    When it's retrieved by title,
    Then None is returned
    """
    assert crud.get_film_by_title(db, 'Nothing') is None


def test_create_film(db: Session, mocker: MockerFixture):
    """
    Given a film title,
    When create film is run,
    Then a film is added to the database
    """
    dummy_phylm = Phylm()
    mocker.patch('app.crud.Phylm', return_value=dummy_phylm)
    film_in = schemas.FilmCreate(title='Film')
    db_film = crud.create_film(db, film_in)
    assert db_film.imdb_score == str(dummy_phylm.imdb_score())
    assert len(db_film.genres) == len(dummy_phylm.genres())
    assert db_film.genres[0].name == dummy_phylm.genres()[0]
    assert len(db_film.cast) == len(dummy_phylm.cast())
    assert db_film.cast[0].name == dummy_phylm.cast()[0]
    assert len(db_film.directors) == len(dummy_phylm.directors())
    assert db_film.directors[0].name == dummy_phylm.directors()[0]


def test_add_genres(db: Session):
    """
    Given a film and some new and existing genres,
    When the genres are added to the film,
    Then the database associations are added
    """
    db_film = create_film(db)
    db_genre = models.Genre(name="Comedy")
    db.add(db_genre)
    db.commit()
    assert len(db_film.genres) == 0
    crud.add_film_genres(db, film=db_film, genres=[db_genre.name, "Action"])
    assert len(db_film.genres) == 2
    assert db_film.genres[0].name == "Comedy"
    assert db_film.genres[1].name == "Action"


def test_add_cast(db: Session):
    """
    Given a film and some new and existing cast,
    When the cast are added to the film,
    Then the database associations are added
    """
    db_film = create_film(db)
    db_actor = models.Actor(name="Steve Martin")
    db.add(db_actor)
    db.commit()
    assert len(db_film.cast) == 0
    crud.add_film_cast(db, film=db_film, actors=[db_actor.name, "Toni Collette"])
    assert len(db_film.cast) == 2
    assert db_film.cast[0].name == "Steve Martin"
    assert db_film.cast[1].name == "Toni Collette"


def test_add_directors(db: Session):
    """
    Given a film and some new and existing directors,
    When the directors are added to the film,
    Then the database associations are added
    """
    db_film = create_film(db)
    db_director = models.Director(name="Ron Howard")
    db.add(db_director)
    db.commit()
    assert len(db_film.directors) == 0
    crud.add_film_directors(db, film=db_film, directors=[db_director.name, "Sofia Coppola"])
    assert len(db_film.directors) == 2
    assert db_film.directors[0].name == "Ron Howard"
    assert db_film.directors[1].name == "Sofia Coppola"


def test_get_or_create_film_new(db: Session, mocker: MockerFixture):
    """
    Given a new film,
    When the get_or_create function is called,
    Then the film is persisted and returned
    """
    film_in = schemas.FilmCreate(title="The Film")
    film_out = models.Film(id=99, title="The Film")
    mocker.patch('app.crud.create_film', return_value=film_out)
    film = crud.get_or_create_film(db, film=film_in)
    assert film.title == "The Film"
    assert film.id == 99


def test_get_or_create_film_existing(db: Session):
    """
    Given an existing film,
    When the get_or_create function is called,
    Then the film is retrieved and returned
    """
    db_film = create_film(db, title="The Film")
    film_in = schemas.FilmCreate(title="The Film")
    film = crud.get_or_create_film(db, film=film_in)
    assert film.id == db_film.id
