import os

from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import click

from instance.config import app_config

db = SQLAlchemy()
ma = Marshmallow()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    db.session.commit()
    click.echo('Initialized the database.')


def create_app(config_name):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
