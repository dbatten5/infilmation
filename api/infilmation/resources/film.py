from flask import Blueprint, request, jsonify
from infilmation.models.film import Film, FilmSchema
from infilmation.utils.film_repository import get_or_create_from_title

film_bp = Blueprint('film', __name__)
film_schema = FilmSchema()

@film_bp.route('/film', methods=('POST',))
def create_film():
    title = request.json['title']
    film = get_or_create_from_title(title)
    return jsonify(film_schema.dump(film))


@film_bp.route('/film/<key>', methods=('GET',))
def get_film(key):
    film = Film.query.filter_by(key=key).first_or_404()
    return jsonify(film_schema.dump(film))
