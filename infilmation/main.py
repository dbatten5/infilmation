import functools
from phylm.movie import Movie as Phylm
from hashlib import sha1

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from infilmation.database import db_session
from infilmation.models import Movie
from infilmation.utils.movie_repository import get_or_create_from_title

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=('GET','POST'))
def home():
    if request.method == 'POST':
        title = request.form['title']
        movie = get_or_create_from_title(title)
        return redirect(url_for('main.results', film=movie.key))

    return render_template('home.html')


@bp.route('/results', methods=('GET',))
def results():
    key = request.args.get('film')
    retrieved_movies = Movie.query.filter_by(key=key).all()
    return render_template('results.html', movies=retrieved_movies)
