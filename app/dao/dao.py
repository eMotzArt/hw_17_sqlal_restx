from app.database.database import db
from app.dao.models import Movie

class DAO():
    def get_items(self, model):
        return model.query.all()

    def get_item(self, model, id):
        return model.query.get(id)

    def create_item(self, model, data):
        new_item = model(**data)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def update_item(self, model, id, data):
        model.query.filter_by(id=id).update(data)
        db.session.commit()
        return

    def delete_item(self, model, id):
        model.query.filter_by(id=id).delete()
        db.session.commit()
        return

class MovieDAO(DAO):
    def get_items(self, data=None):
        if not data:
            return Movie.query.all()

        query = Movie.query
        for filter_ in data:
            if value := data.get(filter_):
                query = query.filter(getattr(Movie, filter_) == value)
        return query.all()
