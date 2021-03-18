from flask import Blueprint, request, jsonify
from infilmation.models.batch import Batch, BatchSchema
from infilmation.utils.batch_repository import create_batch

batch_bp = Blueprint('batch', __name__)
batch_schema = BatchSchema()

@batch_bp.route('/batch', methods=('POST',))
def create():
    titles = request.json['titles']
    batch = create_batch(titles)
    return jsonify(batch_schema.dump(batch)), 201


@batch_bp.route('/batch/<key>', methods=('GET',))
def get(key):
    batch = Batch.query.filter_by(key=key).first_or_404()
    return jsonify(batch_schema.dump(batch))
