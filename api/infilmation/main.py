"""Module for defining the Main Blueprint"""

from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from infilmation.models import Movie
from infilmation.utils.movie_repository import get_or_create_from_title

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=('GET','POST'))
def home():
    """Define the home route. Renders the home screen and handles the form input post
    request to either retrieve a movie or store a new one"""
    if request.method == 'POST':
        title = request.form['title']
        movie = get_or_create_from_title(title)
        return redirect(url_for('main.results', film=movie.key))

    return render_template('home.html')


@bp.route('/results', methods=('GET',))
def results():
    """Define the results route. Looks for a film key in the params and retrieves the
    associated film from the database
    """
    key = request.args.get('film')
    retrieved_movies = Movie.query.filter_by(key=key).all()
    return render_template('results.html', movies=retrieved_movies)


@bp.route('/thing', methods=('GET',))
def thing():
    return {'thing': 'thing!'}
