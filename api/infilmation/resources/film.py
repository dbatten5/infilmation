from flask import Blueprint, request, jsonify
from infilmation.models import Film, FilmSchema
from infilmation.utils.film_repository import get_or_create_from_title

film_bp = Blueprint('film', __name__)

film_schema = FilmSchema()

@film_bp.route('/film', methods=('POST',))
def create_film():
    title = request.json['title']
    film = get_or_create_from_title(title)
    schema = FilmSchema()
    return jsonify(schema.dump(film))


@film_bp.route('/film/<key>', methods=('GET',))
def get_film(key):
    schema = FilmSchema()
    film = Film.query.filter_by(key=key).first_or_404()
    return jsonify(schema.dump(film))
