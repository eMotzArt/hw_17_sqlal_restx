from app.database.database import db
from app.dao.models import Movie, Genre, Director

class BaseDAO():
    model: db.Model
    def get_items(self):
        return self.model.query.all()

    def get_item(self, id):
        return self.model.query.get(id)

    def create_item(self, data):
        new_item = self.model(**data)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def update_item(self, id, data):
        self.model.query.filter_by(id=id).update(data)
        db.session.commit()
        return

    def delete_item(self, id):
        self.model.query.filter_by(id=id).delete()
        db.session.commit()
        return

class MovieDAO(BaseDAO):
    model = Movie
    def get_items(self, data=None):
        if not data:
            return self.model.query.all()

        query = self.model.query
        for filter_ in data:
            if value := data.get(filter_):
                query = query.filter(getattr(self.model, filter_) == value)
        return query.all()

class GenreDAO(BaseDAO):
    model = Genre
    pass

class DirectorDAO(BaseDAO):
    model = Director
    pass