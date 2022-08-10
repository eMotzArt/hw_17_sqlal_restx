from flask_restx import Namespace, Resource, fields

from app.dao.dao import GenreDAO
from app.apis.genres_api.parser import genre_parser

api = Namespace('genres')

# api model
genre = api.model('Genre', {
    'id': fields.Integer(readonly=True, description='The genre unique pkentifier'),
    'name': fields.String(required=True, description='The genre name')
})


@api.route('/')
class GenresView(Resource):
    @api.marshal_list_with(genre)
    def get(self):
        return GenreDAO().get_items()

    @api.expect(genre_parser, valpkate=True)
    @api.marshal_with(genre, code=201)
    def post(self):
        data = genre_parser.parse_args()
        return GenreDAO().create_item(data)


@api.route('/<int:pk>')
class GenreView(Resource):
    @api.marshal_with(genre)
    @api.response(code=404, description='Item not found')
    def get(self, pk):
        if result := GenreDAO().get_item(pk):
            return result, 200
        return '',404

    @api.expect(genre_parser, valpkate=True)
    @api.response(code=204, description="Successfully modified")
    def put(self, pk):
        data = genre_parser.parse_args()
        return GenreDAO().update_item(pk, data), 204

    @api.response(code=204, description="Successfully deleted")
    def delete(self, pk):
        return GenreDAO().delete_item(pk), 204


