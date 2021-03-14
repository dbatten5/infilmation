import functools
from phylm.movie import Movie as Phylm
from hashlib import sha1

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from infilmation.database import db_session
from infilmation.models import Movie

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=('GET','POST'))
def home():
    if request.method == 'POST':
        title = request.form['title']
        key = sha1(str.encode(title.lower().strip())).hexdigest()
        retrieved_movie = Movie.query.filter(Movie.key == key).first()

        if not retrieved_movie:
            m = Phylm(title)
            new_movie = Movie(
                key=key,
                title=m.title,
                year=m.year,
                genres=m.genres(),
                runtime=m.runtime(),
                cast=m.cast(),
                directors=m.directors(),
                plot=m.plot(),
                imdb_title=m.imdb_title(),
                imdb_year=m.imdb_year(),
                imdb_score=m.imdb_score(),
                imdb_low_confidence=m.imdb_low_confidence(),
                mtc_title=m.mtc_title(),
                mtc_year=m.mtc_year(),
                mtc_score=m.mtc_score(),
                mtc_low_confidence=m.mtc_low_confidence(),
                rt_title=m.rt_title(),
                rt_year=m.rt_year(),
                rt_tomato_score=m.rt_tomato_score(),
                rt_audience_score=m.rt_audience_score(),
                rt_low_confidence=m.rt_low_confidence()
            )
            db_session.add(new_movie)
            db_session.commit()

        return redirect(url_for('movie.results', film=key))

    return render_template('home.html')


@bp.route('/results', methods=('GET',))
def results():
    key = request.args.get('film')
    retrieved_movies = Movie.query.filter_by(key=key).all()
    return render_template('results.html', movies=retrieved_movies)
