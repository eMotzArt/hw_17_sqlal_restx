from flask_restx import Namespace, Resource, fields

from app.dao.models import Genre, Director, Movie
from app.dao.dao import DAO
from app.apis.directors_api.parser import director_parser

api = Namespace('directors')

# api model
director = api.model('Director', {
    'id': fields.Integer(readonly=True, description='Director unique identifier'),
    'name': fields.String(required=True, description='The director name')
})


@api.route('/')
class DirectorsView(Resource):
    @api.marshal_list_with(director)
    def get(self):
        return DAO().get_items(Director)

    @api.expect(director_parser)
    @api.marshal_with(director, code=201)
    def post(self):
        data = director_parser.parse_args()
        return DAO().create_item(Director, data)


@api.route('/<int:id>')
class DirectorView(Resource):
    @api.marshal_with(director)
    @api.response(code=404, description='Item not found')
    def get(self, id):
        if result := DAO().get_item(Director, id):
            return result, 200
        return '', 404

    @api.expect(director_parser)
    @api.response(code=204, description="Successfully modified")
    def put(self, id):
        data = director_parser.parse_args()
        return DAO().update_item(Director,id,data), 201

    @api.response(code=204, description="Successfully deleted")
    def delete(self, id):
        return DAO().delete_item(Director, id), 204


