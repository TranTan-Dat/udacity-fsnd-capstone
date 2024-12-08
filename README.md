# Casting Agency Project
This is my final capstone project for Udacity's FullStack Web Developer Nanodegree.
Web app can be accessed at [here](https://udacity-fsnd-capstone-srxy.onrender.com)

## Project Motivation
The Casting Agency Project simulates a company focused on producing movies and managing actors by assigning them to different film projects. As an Executive Producer within the company, you are building a system to simplify and enhance the workflow for movie creation and actor assignments.

This project serves as a platform for practicing and showcasing a range of web development skills, including data modeling, API design, authentication and authorization, and cloud deployment.


## Key Dependencies & Platforms

- **[Flask](http://flask.pocoo.org/)**: A lightweight backend microservices framework used to handle HTTP requests and responses.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: The Python SQL toolkit and ORM for interacting with the lightweight SQLite database. You'll primarily work within `app.py` and reference `models.py` for database models.
- **[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#)**: An extension to manage cross-origin requests between the backend and the frontend server.
- **[Auth0](https://auth0.com/docs/)**: The authentication and authorization system for securely managing users with various roles, simplifying user access control.
- **[PostgreSQL](https://www.postgresql.org/)**: A widely used relational database integrated into the project, with support for other relational databases available with minor adjustments.
- **[Reader](https://www.reader.com/)**: The cloud platform used for deploying the application.
- **[Postman](https://www.postman.com/)**: A collaboration platform for API development, used for testing and managing API requests, including endpoints for the project.


## Endpoints:

### Movies:
- **GET** `/movies`: Retrieve a list of all movies.
- **POST** `/movies`: Create a new movie.
- **PATCH** `/movies/{movie_id}`: Update a specific movie by ID.
- **DELETE** `/movies/{movie_id}`: Delete a specific movie by ID.

### Actors:
- **GET** `/actors`: Retrieve a list of all actors.
- **POST** `/actors`: Create a new actor.
- **PATCH** `/actors/{actor_id}`: Update a specific actor by ID.
- **DELETE** `/actors/{actor_id}`: Delete a specific actor by ID.


### Roles
* Casting Assistant
    * GET /actors and /movies

* Casting Director
    * GET /actors and /movies
    * ADD /actors and DELETE /actors
    * PATCH /actors and /movies
    
* Executive Producer
    * GET /actors and /movies
    * ADD /actors and DELETE /actors
    * PATCH /actors and /movies
    * ADD /movies and DELETE /movies


### JWT Tokens for each role:
* Casting Assistant - 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDWjczT1ZyZnNFTjl0cW1FSFBKYyJ9.eyJpc3MiOiJodHRwczovL2F6eS1jb2ZmZWVzaG9wLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJwczZjN1pmQmpZb2x5T0FZa3pUQnhCRXkzcTY0VXVmb0BjbGllbnRzIiwiYXVkIjoiZnNuZC1pbWFnZSIsImlhdCI6MTczMzY0MDE3MywiZXhwIjoxNzMzNzI2NTczLCJzY29wZSI6ImdldDphY3RvcnMgZ2V0Om1vdmllcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6InBzNmM3WmZCallvbHlPQVlrelRCeEJFeTNxNjRVdWZvIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.iaglrSxj55YNRCPbYVRO_7agDcTDxFi9fGN5YvWeX2VlGKWovHKoSihFE-tQ5qUvFney3RsVlyN4fNSiiecNwTLyJpk9BTg8Ukrl1zY_VxJcmUl1mhktmcMkIZdsu5uXUz60eBIF2F-_xLrcsohmpT5i5YlPDDMt-4uVhrCJ1d2Y6UnM7lFA3bJD_kwZZAuuAuQyOKxauWdL0lyZjRExyJYD-Ha7DOhh6a6d825my3kIJ05TRBZMrQUAxI_wjat3wIO6YSuTyte_8a1kDL-Z_hEPOW3jBotR8q66Nk1iqLvZIlx5IpHef9h8NjzyV_z3rZykFpM78xLo4PUBiLj64w

* Casting Director
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDWjczT1ZyZnNFTjl0cW1FSFBKYyJ9.eyJpc3MiOiJodHRwczovL2F6eS1jb2ZmZWVzaG9wLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJwczZjN1pmQmpZb2x5T0FZa3pUQnhCRXkzcTY0VXVmb0BjbGllbnRzIiwiYXVkIjoiZnNuZC1pbWFnZSIsImlhdCI6MTczMzY0MDI2MCwiZXhwIjoxNzMzNzI2NjYwLCJzY29wZSI6ImdldDphY3RvcnMgZ2V0OmFjdG9ycy1kZXRhaWwgcG9zdDphY3RvcnMgcGF0Y2g6YWN0b3JzIGRlbGV0ZTphY3RvcnMgZ2V0Om1vdmllcyBnZXQ6bW92aWVzLWRldGFpbCBwb3N0Om1vdmllcyBwYXRjaDptb3ZpZXMiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJhenAiOiJwczZjN1pmQmpZb2x5T0FZa3pUQnhCRXkzcTY0VXVmbyIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsInBvc3Q6YWN0b3JzIiwicGF0Y2g6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBvc3Q6bW92aWVzIiwicGF0Y2g6bW92aWVzIl19.ZkhdKiDDQFVLW8Xv7vqb_6hIuQzDXhdU7ci8gOlC6U2sf4c7LHdbUxGxLITY8KFzxr-HcUR_9pABv9nOmqsxFCfHKI06IrvrlM4AXxOUH7lP2Bn-osCXQCRSX0IkwsSM6LRXWMcRskYWXaRd-rjFn2fCN1hQc_mUG1xg293RftSk2mZ2cp7ycuRwcrnVcVGiqL2u18-e2ZMH4ivwNEnBds_Lv9-3E-X83ss_QvfeEYI3R_5uoTZbS6Q-B-dv6Vooj5-7ATX0_B22b_jg6sgmDSg1KbaIG587a6pyFVHpHaoAraAgXfnBCCf1sxO2YOownx-TWU-dEd8j7U8Js662dQ

* Executive Producer - 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDWjczT1ZyZnNFTjl0cW1FSFBKYyJ9.eyJpc3MiOiJodHRwczovL2F6eS1jb2ZmZWVzaG9wLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJwczZjN1pmQmpZb2x5T0FZa3pUQnhCRXkzcTY0VXVmb0BjbGllbnRzIiwiYXVkIjoiZnNuZC1pbWFnZSIsImlhdCI6MTczMzY0MDM4MiwiZXhwIjoxNzMzNzI2NzgyLCJzY29wZSI6ImdldDphY3RvcnMgZ2V0OmFjdG9ycy1kZXRhaWwgcG9zdDphY3RvcnMgcGF0Y2g6YWN0b3JzIGRlbGV0ZTphY3RvcnMgZ2V0Om1vdmllcyBnZXQ6bW92aWVzLWRldGFpbCBwb3N0Om1vdmllcyBwYXRjaDptb3ZpZXMgZGVsZXRlOm1vdmllcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6InBzNmM3WmZCallvbHlPQVlrelRCeEJFeTNxNjRVdWZvIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwicG9zdDphY3RvcnMiLCJwYXRjaDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIiwicG9zdDptb3ZpZXMiLCJwYXRjaDptb3ZpZXMiLCJkZWxldGU6bW92aWVzIl19.wmHhEWuetGk2j3xPitKVE1HKT6VCt-KLggBQLAtU-AafWqb0AQhaZPFqD-xL0bJKoIMimiWRmCvAVUsQnk3KUqIpqGkwteWo9_IZIZsRvT66rJfRaL1kmY3Gt53agMZzD2mj9Cc71c3z7p3ar59JXsRXhJAU8y8s4XExd86bIgNh2GVYPaW5q74vqdoke-eXVv9-4EE2gBBtvtu4rQCitNU06JtkMh02cls2geJTrrLWvD22W6UlxdCl7c2IehYKvaAuTVslHdLHUFZJ9dhfPWVjeBPJPX5R388Fy6Rc2pK2xYBLLS7fWK3XhIwFCT7HY63FoeNX59yKwOeH8zT0jA


## API Endpoints

### Movies

### GET /movies
- **Response:**
  ```
  {
      
      "movies": [
          {
              "id": 1,
              "title": "Movie 1",
              "release_year": 2020
          },
          {
              "id": 2,
              "title": "Movie 2",
              "release_year": 2021
          }
      ],
      "success": true,
  }
  ```

#### GET /movies/{movie_id}
Retrieves a specific movie by its ID.

**Sample Response:**
  ```
  {
    "movie": {
      "id": 1, 
      "release_year": 2020, 
      "title": "Movie 1"
    }, 
    "success": true
  }
  ```


#### POST /movies
Creates a new movie.

**Sample Request:**
```
{
    "title": "The Matrix",
    "release_year": 1999
}
```


#### PATCH /movies/{movie_id}
Updates a specific movie by its ID.

**Sample Request:**
```
{
    "title": "The Matrix",
    "release_year": 2000
}
```

**Sample Response**
```
{
    "movie": {
        "id": 3,
        "title": "The Matrix",
        "release_year": 2000
    },
    "success": true
}
```




#### DELETE /movies/{movie_id}
Deletes a specific movie by its ID.

**URL Parameters:**
- `movie_id` (integer): The ID of the movie to delete.

**Sample Response**
```
{
    "movie": {
        "id": 3,
        "title": "The Matrix",
        "release_year": 2000
    },
    "success": true
}
```


### Actors
#### GET /actors
Retrieves a list of actors with pagination support.

**Sample Response:**
```
{
  "actors": [
    {
      "age": 30, 
      "gender": "Male", 
      "id": 1, 
      "movie_id": 1, 
      "name": "Actor 1"
    }, 
    {
      "age": 25, 
      "gender": "Female", 
      "id": 2, 
      "movie_id": 2, 
      "name": "Actor 2"
    }
  ], 
  "success": true
}
```



#### GET /actors/{actor_id}
Retrieves a specific actor by its ID.
**Sample Response:**
```
{
  "actors":
    {
      "age": 30, 
      "gender": "Male", 
      "id": 1, 
      "movie_id": 1, 
      "name": "Actor 1"
    },
  "success": true
}
```


#### POST /actors
Creates a new actor.

**Sample Request:**
```
{
    "name": "Leonardo DiCaprio",
    "age": 45,
    "gender": "Male",
    "movie_id": 2
}
```
**Sample Response**
```
{
    "actor": {
        "id": 3,
        "name": "Leonardo DiCaprio",
        "age": 45,
        "gender": "Male",
        "movie_id": 2
    },
    "success": true
}

```

#### PATCH /actors/{actor_id}
Updates a specific actor by its ID.

**Sample Request:**
```
{
    "name": "Brad Pitt",
    "age": 56,
    "gender": "Male",
    "movie_id": 1
}
```
**Sample Response**
```
{
    "actor": {
        "id": 3,
        "name": "Brad Pitt",
        "age": 56,
        "gender": "Male",
        "movie_id": 1
    },
    "success": true
}

```


#### DELETE /actors/{actor_id}
Deletes a specific actor by its ID.

**Sample Response**
```
{
    "success": true,
    "actor": {
        "id": 3,
        "name": "Brad Pitt",
        "age": 56,
        "gender": "Male",
        "movie_id": 1
    }
}
```