from flask_restx import Namespace, Resource, fields

from app.dao.dao import DirectorDAO
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
        return DirectorDAO().get_items()

    @api.expect(director_parser)
    @api.marshal_with(director, code=201)
    def post(self):
        data = director_parser.parse_args()
        return DirectorDAO().create_item(data)


@api.route('/<int:id>')
class DirectorView(Resource):
    @api.marshal_with(director)
    @api.response(code=404, description='Item not found')
    def get(self, id):
        if result := DirectorDAO().get_item(id):
            return result, 200
        return '', 404

    @api.expect(director_parser)
    @api.response(code=204, description="Successfully modified")
    def put(self, id):
        data = director_parser.parse_args()
        return DirectorDAO().update_item(id, data), 201

    @api.response(code=204, description="Successfully deleted")
    def delete(self, id):
        return DirectorDAO().delete_item(id), 204


