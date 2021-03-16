import uuid
from infilmation import db
from infilmation import ma
from infilmation.models.film import FilmSchema

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

    def __init__(self, **kwargs):
        super(Batch, self).__init__(**kwargs)
        self.key = uuid.uuid4().hex

    def __repr__(self):
        return f"<Batch {self.key}>"


class BatchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Batch

    films = ma.List(ma.Nested(FilmSchema))
