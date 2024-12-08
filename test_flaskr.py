import unittest
import os
from flask import Flask
import json
from app import create_app
from models import setup_db, Movie, Actor

class CapstoneAppTestCase(unittest.TestCase):
    """This class represents the Capstone app test case."""
        
    def setUp(self):
        """Define test variables and initialize app."""
        self.database_path = os.environ.get('DATABASE_URL')
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })
        with self.app.app_context():
            from models import db
            db.create_all()
        self.client = self.app.test_client
        self.new_movie = {'title': 'New Movie', 'release_year': 2022}
        self.new_actor = {'name': 'New Actor', 'age': 30, 'gender': 'Male', 'movie_id': 1}
        self.auth_token = f'Bearer {self.get_auth_token()}'

    def get_auth_token(self):
        # Replace this with your actual authentication logic to obtain a JWT token
        return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDWjczT1ZyZnNFTjl0cW1FSFBKYyJ9.eyJpc3MiOiJodHRwczovL2F6eS1jb2ZmZWVzaG9wLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJwczZjN1pmQmpZb2x5T0FZa3pUQnhCRXkzcTY0VXVmb0BjbGllbnRzIiwiYXVkIjoiZnNuZC1pbWFnZSIsImlhdCI6MTczMzQ4NzEyNSwiZXhwIjoxNzMzNTczNTI1LCJzY29wZSI6ImdldDphY3RvcnMgZ2V0OmFjdG9ycy1kZXRhaWwgcG9zdDphY3RvcnMgcGF0Y2g6YWN0b3JzIGRlbGV0ZTphY3RvcnMgZ2V0Om1vdmllcyBnZXQ6bW92aWVzLWRldGFpbCBwb3N0Om1vdmllcyBwYXRjaDptb3ZpZXMgZGVsZXRlOm1vdmllcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6InBzNmM3WmZCallvbHlPQVlrelRCeEJFeTNxNjRVdWZvIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwicG9zdDphY3RvcnMiLCJwYXRjaDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicG9zdDptb3ZpZXMiLCJwYXRjaDptb3ZpZXMiLCJkZWxldGU6bW92aWVzIl19.opC4q_jrUcSALPsh6f35sMBjdhWmnGnaqAWX3jlLIhYk1vWeu-q-Gkxqe-HuvwfGZ3n2y2UB8shHfmFY1mKyf6A2lZY0FkAo6xbXvvHWMltPrN0DcajDkJ2UaAzLPiT3N0Fsg9184ylC0bvdgI0FkzrjXP4AeD1xXruKiOGtXkYJfCNBjdxWIcYoT4nQmYcIZs3Usgrs3RLlKrG43iWgnEwIR9MmhBxdVqVUnhO749ltceR6fLMAVbupUcO-vG2ODPvg_AAtMOpdoTBHbwsoxhuTTNDaIRQBoDN9u4nsBseaSaRrw9jXDeXQ8_jaxTVIjhayKpN-HlimZdUeo7F5oQ'

    def tearDown(self):
        """Executed after each test."""
        with self.app.app_context():
            from models import db
            db.session.remove()
            db.drop_all()
            # Delete the database file if it exists
            if os.path.exists('your_database_file.db'):
                os.remove('your_database_file.db')

    def test_health_check(self):
        """Test health check endpoint."""
        response = self.client().get('/')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('description', data)

    def test_get_movies(self):
        """Test retrieving movies."""
        response = self.client().get('/movies', headers={'Authorization': self.auth_token})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['movies'], list)

    def test_create_movie(self):
        """Test creating a new movie."""
        response = self.client().post('/movies', json=self.new_movie)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('movie', data)
        self.assertEqual(data['movie']['title'], self.new_movie['title'])
        
    def test_create_movie_invalid_data(self):
        """Test creating a new movie with invalid data."""
        invalid_movie = {'title': 123, 'release_year': 'abd'}
        response = self.client().post('movies', json=invalid_movie)
        dara = json.loads(response.data)
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(dara['success'], False)
        self.assertIn('message', dara)

    def test_update_movie(self):
        """Test updating a movie."""
        # Create a movie first
        self.client().post('/movies', json=self.new_movie)
        updated_movie = {'title': 'Updated Movie'}
        response = self.client().patch('/movies/1', json=updated_movie)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie']['title'], 'Updated Movie')

    def test_delete_movie(self):
        """Test deleting a movie."""
        # Create a movie first
        self.client().post('/movies', json=self.new_movie)
        response = self.client().delete('/movies/1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('movie', data)

    def test_create_actor(self):
        """Test creating a new actor."""
        self.client().post('/movies', json=self.new_movie)
        response = self.client().post('/actors', json=self.new_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('actor', data)
        self.assertEqual(data['actor']['name'], self.new_actor['name'])

    def test_update_actor(self):
        """Test updating an actor."""
        self.client().post('/movies', json=self.new_movie)
        self.client().post('/actors', json=self.new_actor)
        updated_actor = {'name': 'Updated Actor'}
        response = self.client().patch('/actors/1', json=updated_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor']['name'], 'Updated Actor')

    def test_delete_actor(self):
        """Test deleting an actor."""
        self.client().post('/movies', json=self.new_movie)
        self.client().post('/actors', json=self.new_actor)
        response = self.client().delete('/actors/1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('actor', data)
        
    

if __name__ == "__main__":
    unittest.main()
