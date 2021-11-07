"""Module to hold database related config."""
import databases
import sqlalchemy

import ormar

from app.core.config import settings

database = databases.Database(str(settings.sqlalchemy_database_uri))
metadata = sqlalchemy.MetaData()


class MainMeta(ormar.ModelMeta):
    """Base meta for all models."""

    database = database
    metadata = metadata
