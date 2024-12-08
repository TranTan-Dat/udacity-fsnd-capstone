-- Insert data into movies table
INSERT INTO movies (id, title, release_year)
VALUES
(1, 'Movie 1', 2020),
(2, 'Movie 2', 2021);

-- Insert data into actors table
INSERT INTO actors (id, name, age, gender, movie_id)
VALUES
(1, 'Actor 1', 30, 'Male', 1),
(2, 'Actor 2', 25, 'Female', 2);