from flask_restx import Namespace, Resource, fields

from app.dao.dao import MovieDAO
from app.apis.movies_api.parser import movie_parser, movie_query_parser

api = Namespace('movies')

# api model
movie = api.model('Movie', {
    'id': fields.Integer(readonly=True, description='Movie unique identifier'),
    'title': fields.String(required=True, description='Movie title'),
    'description': fields.String(required=True, description='Movie description'),
    'trailer': fields.String(required=True, description='Movie trailer link'),
    'year': fields.Integer(required=True, description='Movie release year'),
    'rating': fields.Float(required=True, description='Movie rating'),
    'genre_id': fields.Integer(required=True, description='Genre id'),
    'director_id': fields.Integer(required=True, description='Director id')
})


@api.route('/')
class MoviesView(Resource):
    @api.expect(movie_query_parser)
    @api.marshal_list_with(movie)
    def get(self):
        data = movie_query_parser.parse_args()
        return MovieDAO().get_items(data)

    @api.expect(movie_parser)
    @api.marshal_with(movie, code=201)
    def post(self):
        data = movie_parser.parse_args()
        return MovieDAO().create_item(data)


@api.route('/<int:id>')
class DirectorView(Resource):
    @api.marshal_with(movie)
    @api.response(code=404, description='Item not found')
    def get(self, id):
        if result := MovieDAO().get_item(id):
            return result, 200
        return '',404

    @api.expect(movie_parser)
    @api.response(code=204, description="Successfully modified")
    def put(self, id):
        data = movie_parser.parse_args()
        return MovieDAO().update_item(id, data), 201

    @api.response(code=204, description="Successfully deleted")
    def delete(self, id):
        return MovieDAO().delete_item(id), 204


