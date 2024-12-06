import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def setup_db(app, database_path=None):
    if database_path is None:
        database_path = os.getenv('DATABASE_PATH')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    release_year = Column(Integer())
    actors = db.relationship('Actor', backref='movies')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year
        }

class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    gender = Column(String())

    movie_id = db.Column(
        db.Integer,
        db.ForeignKey('movies.id'),
        nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }