from infilmation import db

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    genres = db.Column(db.String(255))
    runtime = db.Column(db.String(255))
    cast = db.Column(db.String(255))
    directors = db.Column(db.String(255))
    plot = db.Column(db.String(255))
    imdb_title = db.Column(db.String(255))
    imdb_year = db.Column(db.Integer)
    imdb_score = db.Column(db.String(255))
    imdb_low_confidence = db.Column(db.Integer)
    mtc_title = db.Column(db.String(255))
    mtc_year = db.Column(db.Integer)
    mtc_score = db.Column(db.String(255))
    mtc_low_confidence = db.Column(db.Integer)
    rt_title = db.Column(db.String(255))
    rt_year = db.Column(db.Integer)
    rt_tomato_score = db.Column(db.String(255))
    rt_audience_score = db.Column(db.String(255))
    rt_low_confidence = db.Column(db.Integer)

    def __repr__(self):
        return '<Movie %r>' % (self.key)
