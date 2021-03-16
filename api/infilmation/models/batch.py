from infilmation import db
from infilmation import ma

batch_film_table = db.Table('batch_film', db.Model.metadata,
    db.Column('batch_id', db.Integer, db.ForeignKey('batch.id')),
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'))
)

class Batch(db.Model):
    __tablename__ = 'batch'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True)
    raw = db.Column(db.Text)
    films = db.relationship('Film', secondary=batch_film_table)

    def __repr__(self):
        return '<Batch %r>' % (self.key,)
