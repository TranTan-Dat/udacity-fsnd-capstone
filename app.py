from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth.auth import requires_auth, AuthError

QUESTIONS_PER_PAGE = 10

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
    @requires_auth('get:movies')
    def get_movies():
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        movies = Movie.query.all()
        result = len(movies)
        if start >= result:
            return jsonify({
                'success': True,
                'movies': []  # Fixed typo 'modvies'
            })
        result = movies[start:end]
        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in result]
        })
    
    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        return jsonify({
            'success': True,
            'movie': movie.format()
        })


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie():
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_year = body.get('release_year', None)
        
        if not isinstance(new_title, str) or not isinstance(new_release_year, int):
            abort(422)

        if not new_title or not new_release_year:
            abort(422)

        exist = Movie.query.filter(Movie.title == new_title, Movie.release_year == new_release_year).one_or_none()
        if exist is not None:
            abort(409)

        try:
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
    @requires_auth('patch:movies')
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
    @requires_auth('delete:movies')
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
    @requires_auth('get:actors')
    def get_actors():
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        actors = Actor.query.all()
        result = len(actors)
        if start >= result:
            return jsonify({
                'success': True,
                'actors': []  # Fixed typo 'modvies'
            })
        result = actors[start:end]
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in result]
        })
    
    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def get_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor():
        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_movie_id = body.get('movie_id', None)

        if not new_name or not new_age or not new_gender or not new_movie_id:
            abort(422)

        exist = Actor.query.filter(
            Actor.name == new_name,
            Actor.age == new_age,
            Actor.gender == new_gender,
            Actor.movie_id == new_movie_id
        ).one_or_none()
        if exist is not None:
            abort(409)
        
        try:
            new_actor = Actor(name=new_name, age=new_age, gender=new_gender, movie_id=new_movie_id)
            new_actor.insert()
            return jsonify({
                'success': True,
                'actor': new_actor.format()
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(actor_id):
        body = request.get_json()
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        movie = Movie.query.filter(Movie.id == body.get('movie_id', None)).one_or_none()
        if actor is None or movie is None:
            abort(404)

        try:
            if body.get('name', None):
                actor.name = body.get('name', None)
            if body.get('age', None):
                actor.age = body.get('age', None)
            if body.get('gender', None):
                actor.gender = body.get('gender', None)
            if body.get('movie_id', None):
                actor.movie_id = body.get('movie_id', None)
            actor.update()
            return jsonify({
                'success': True,
                'actor': actor.format()
            })
        except BaseException as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        try:
            actor.delete()
            return jsonify({
                'success': True,
                'actor': actor.format()
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

    @app.errorhandler(Exception)  # Fixed missing error code or exception type
    def handle_errors(error):
        error_code = error.code if hasattr(error, 'code') else 500
        return jsonify({
            'success': False,
            'error': error_code,
            'message': error_handlers.get(error_code, 'Unexpected error')
        }), error_code

    return app
