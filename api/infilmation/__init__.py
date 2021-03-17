import os

from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import click

from redis import Redis
import rq

from instance.config import app_config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    db.session.commit()
    click.echo('Initialized the database.')


def create_app(config_name=os.getenv('APP_SETTINGS')):
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

    from infilmation.models.task import Task
    from infilmation.models.film import Film
    from infilmation.models.batch import Batch

    db.init_app(app)
    app.cli.add_command(init_db_command)

    ma.init_app(app)

    migrate.init_app(app, db)

    from .resources import film, batch
    app.register_blueprint(film.film_bp)
    app.register_blueprint(batch.batch_bp)

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('infilmation-tasks', connection=app.redis)

    return app
