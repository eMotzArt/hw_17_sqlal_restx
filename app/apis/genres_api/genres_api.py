from flask_restx import Namespace, Resource, fields

from app.dao.models import Genre
from app.dao.dao import DAO
from app.apis.genres_api.parser import genre_parser

api = Namespace('genres')

# api model
genre = api.model('Genre', {
    'id': fields.Integer(readonly=True, description='The genre unique identifier'),
    'name': fields.String(required=True, description='The genre name')
})


@api.route('/')
class GenresView(Resource):
    @api.marshal_list_with(genre)
    def get(self):
        return DAO().get_items(Genre)

    @api.expect(genre_parser, validate=True)
    @api.marshal_with(genre, code=201)
    def post(self):
        data = genre_parser.parse_args()
        return DAO().create_item(Genre, data)


@api.route('/<int:id>')
class GenreView(Resource):
    @api.marshal_with(genre)
    @api.response(code=404, description='Item not found')
    def get(self, id):
        if result := DAO().get_item(Genre, id):
            return result, 200
        return '',404

    @api.expect(genre_parser, validate=True)
    @api.response(code=204, description="Successfully modified")
    def put(self, id):
        data = genre_parser.parse_args()
        return DAO().update_item(Genre, id, data), 204

    @api.response(code=204, description="Successfully deleted")
    def delete(self, id):
        return DAO().delete_item(Genre, id), 204


