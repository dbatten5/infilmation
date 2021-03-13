import functools
from phylm.movie import Movie
from hashlib import sha1

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from infilmation.db import get_db

bp = Blueprint('movie', __name__, url_prefix='/')

@bp.route('/', methods=('GET','POST'))
def home():
    if request.method == 'POST':
        title = request.form['title']
        key = sha1(str.encode(title.lower().strip())).hexdigest()
        db = get_db()
        retrieved_movie = db.execute(
            'SELECT m.id'
            ' FROM movie m'
            ' WHERE m.key = ?',
            (key,)
        ).fetchone()

        if not retrieved_movie:
            m = Movie(title)
            db.execute(
                """INSERT INTO movie (
                    key,
                    title,
                    year,
                    genres,
                    runtime,
                    cast,
                    directors,
                    plot,
                    imdb_title,
                    imdb_year,
                    imdb_score,
                    imdb_low_confidence,
                    mtc_title,
                    mtc_year,
                    mtc_score,
                    mtc_low_confidence,
                    rt_title,
                    rt_year,
                    rt_tomato_score,
                    rt_audience_score,
                    rt_low_confidence
                )"""
                'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (
                    key,
                    m.title,
                    m.year,
                    m.genres(),
                    m.runtime(),
                    m.cast(),
                    m.directors(),
                    m.plot(),
                    m.imdb_title(),
                    m.imdb_year(),
                    m.imdb_score(),
                    m.imdb_low_confidence(),
                    m.mtc_title(),
                    m.mtc_year(),
                    m.mtc_score(),
                    m.mtc_low_confidence(),
                    m.rt_title(),
                    m.rt_year(),
                    m.rt_tomato_score(),
                    m.rt_audience_score(),
                    m.rt_low_confidence()
                )
            )
            db.commit()

        return redirect(url_for('movie.results', film=key))

    return render_template('home.html')


@bp.route('/results', methods=('GET',))
def results():
    key = request.args.get('film')
    db = get_db()
    retrieved_movies = db.execute(
        'SELECT m.imdb_title, m.runtime, m.genres, m.cast, m.imdb_score, m.imdb_year'
        ' FROM movie m'
        ' WHERE m.key = ?',
        (key,)
    ).fetchall()
    return render_template('results.html', movies=retrieved_movies)
