from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)
    CORS(app, resources={r'/api/': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization, True')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, DELETE, PATCH, OPTIONS')
        return response
    
    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({
            'success': True,
            'description': 'Capstone App is running successfully!!!'
        })
    
    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        })
    
    @app.route('/movies/<int:movie_id>', methods=['GET'])
    def get_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        return jsonify({
            'success': True,
            'movie': movie.format()
        })
    
    @app.route('/movies', methods=['POST'])
    def create_movie():
        body = request.get_json()
        if not body.get('title', None)  or not body.get('release_year', None):
            abort(422)
        
        # check exist
        exist = Movie.query.filter(Movie.title == new_title and Movie.release_year == new_release_year).one_or_none()
        if exist is not None:
            abort(409)
        
        try:
            new_title = body.get('title', None)
            new_release_year = body.get('release_year', None)
            new_movie = Movie(title=new_title, release_year=new_release_year)
            new_movie.insert()
            return jsonify({
                'success': True,
                'movie': new_movie.format()
            })
        except BaseException as e:
            print(e)
            abort(422)
    
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def update_movie(movie_id):
        body = request.get_json()
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        try:
            if body.get('title', None):
                movie.title = body.get('title', None)
            if body.get('release_year', None):
                movie.release_year = body.get('release_year', None)
            movie.update()
            return jsonify({
                'success': True,
                'movie': movie.format()
            })
        except BaseException as e:
            print(e)
            abort(422)
    
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        try:
            movie.delete()
            return jsonify({
                'success': True,
                'movie': movie.format()
            })
        except BaseException as e:
            print(e)
            abort(422)
    
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.all()
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        })
    
    @app.route('/actors/<int:actor_id>', methods=['GET'])
    def get_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        return jsonify({
            'success': True,
            'actor': actor.format()
        })
    
    @app.route('/actors', methods=['POST'])
    def create_actor():
        body = request.get_json()
        if not body.get('name', None)  or not body.get('age', None) or not body.get('gender', None) or not body.get('movie_id', None):
            abort(422)
        
        # check exist
        exist = Actor.query.filter(Actor.name == new_name and Actor.age == new_age and Actor.gender == new_gender and Actor.movie_id == new_movie_id).one_or_none()
        if exist is not None:
            abort(409)
        
        try:
            new_name = body.get('name', None)
            new_age = body.get('age', None)
            new_gender = body.get('gender', None)
            new_movie_id = body.get('movie_id', None)
            new_actor = Actor(name=new_name, age=new_age, gender=new_gender, movie_id=new_movie_id)
            new_actor.insert()
            return jsonify({
                'success': True,
                'actor': new_actor.format()
            })
        except BaseException as e:
            print(e)
            abort(422)
            
            

    
    
        
    error_handlers = {
        404: 'Resource not found',
        422: 'Unprocessable entity',
        400: 'Bad request',
        500: 'Internal server error',
        409: 'Conflict with existing resource'
    }
    
    @app.errorhandler((404, 422, 400, 500))
    def handle_errors(error):
        error_code = error.code
        return jsonify({
            'success': False,
            'error': error_code,
            'message': error_handlers[error_code]
        }), error_code
        
    return app