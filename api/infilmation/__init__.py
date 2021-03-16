import os

from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import click

db = SQLAlchemy()
ma = Marshmallow()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    db.session.commit()
    click.echo('Initialized the database.')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    sqlite_db_path=os.path.join(app.instance_path, 'infilmation.db')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'infilmation.sqlite'),
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{sqlite_db_path}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.cli.add_command(init_db_command)

    ma.init_app(app)

    from .resources import film, batch
    app.register_blueprint(film.film_bp)
    app.register_blueprint(batch.batch_bp)

    return app
