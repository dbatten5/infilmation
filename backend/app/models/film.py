"""Module to hold `Film` model definitions."""
from datetime import timedelta
from typing import Optional

import ormar
from ormar import property_field

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
    title = ormar.String(max_length=255)
    year = ormar.Integer(nullable=True)
    runtime = ormar.Integer(nullable=True)
    plot = ormar.Text(nullable=True)
    imdb_id = ormar.String(max_length=255, nullable=True)
    imdb_title = ormar.String(max_length=255, nullable=True)
    imdb_year = ormar.Integer(nullable=True)
    imdb_rating = ormar.Float(nullable=True)
    imdb_low_confidence = ormar.Boolean(default=False)
    mtc_title = ormar.String(max_length=255, nullable=True)
    mtc_year = ormar.Integer(nullable=True)
    mtc_rating = ormar.String(max_length=255, nullable=True)
    mtc_low_confidence = ormar.Boolean(default=False)
    rt_title = ormar.String(max_length=255, nullable=True)
    rt_year = ormar.Integer(nullable=True)
    rt_tomato_rating = ormar.String(max_length=255, nullable=True)
    rt_low_confidence = ormar.Boolean(default=False, nullable=True)
    cast = ormar.ManyToMany(to=Actor, skip_reverse=True)
    directors = ormar.ManyToMany(to=Director, skip_reverse=True)
    genres = ormar.ManyToMany(to=Genre, skip_reverse=True)
    tmdb_id = ormar.String(max_length=255, nullable=True)

    @property_field
    def human_readable_runtime(self) -> Optional[str]:
        """Return the runtime in human readable form.

        Returns:
            Optional[str]: the runtime
        """
        if self.runtime:
            return str(timedelta(minutes=self.runtime))[:-3]

        return None
