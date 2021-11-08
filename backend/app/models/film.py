"""Module to hold `Film` model definitions."""
import ormar

from app.db import MainMeta


class Genre(ormar.Model):
    """Schema for the `Genre` model."""

    class Meta(MainMeta):
        """Extend the BaseMeta."""

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=255, unique=True)


class Actor(ormar.Model):
    """Schema for the `Actor` model."""

    class Meta(MainMeta):
        """Extend the BaseMeta."""

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=255, unique=True)


class Director(ormar.Model):
    """Schema for the `Director` model."""

    class Meta(MainMeta):
        """Extend the BaseMeta."""

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=255, unique=True)


class Film(ormar.Model):
    """Schema for the `Film` model."""

    class Meta(MainMeta):
        """Extend the BaseMeta."""

    id = ormar.Integer(primary_key=True)
    key = ormar.String(max_length=50, unique=True)
    title = ormar.String(max_length=255)
    year = ormar.Integer(nullable=True)
    runtime = ormar.Integer()
    plot = ormar.Text()
    imdb_id = ormar.String(max_length=255)
    imdb_title = ormar.String(max_length=255)
    imdb_year = ormar.Integer()
    imdb_rating = ormar.Float()
    imdb_low_confidence = ormar.Boolean(default=False)
    mtc_title = ormar.String(max_length=255)
    mtc_year = ormar.Integer()
    mtc_rating = ormar.Integer()
    mtc_low_confidence = ormar.Boolean(default=False)
    rt_title = ormar.String(max_length=255)
    rt_year = ormar.Integer()
    rt_tomato_rating = ormar.Integer()
    rt_low_confidence = ormar.Boolean(default=False)
    cast = ormar.ManyToMany(to=Actor)
    directors = ormar.ManyToMany(to=Director)
    genres = ormar.ManyToMany(to=Genre)
