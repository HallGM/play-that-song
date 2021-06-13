DROP TABLE IF EXISTS requests;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;



CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE songs (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  artist_id INT REFERENCES artists(id),
  last_played TIMESTAMP
);  

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  bio TEXT
);

CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    song_id INT REFERENCES songs(id),
    user_id INT REFERENCES users(id),
    time TIMESTAMP,
    played BOOLEAN
)
