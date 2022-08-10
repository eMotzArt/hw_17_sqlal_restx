from app.database.database import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Genre(name={self.name!r})>".format(self=self)

    def get_available_attrs(self):
        return 'name',

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Director(name={self.name!r})>".format(self=self)

    def get_available_attrs(self):
        return 'name',

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genre", backref=db.backref("used_in_movies"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)
    director = db.relationship("Director", backref=db.backref("used_in_movies"))

    def __repr__(self):
        return "<Movie(title={self.title!r})>".format(self=self)

    def get_available_attrs(self):
        return 'title', 'description', 'trailer', 'year', 'rating', 'genre_id', 'director_id'