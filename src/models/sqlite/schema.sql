CREATE TABLE IF NOT EXISTS 'games'(
    id TEXT PRIMARY KEY,
    game_name TEXT NOT NULL,
    game_description TEXT NOT NULL,
    release_date DATE NOT NULL,
    url_game TEXT NOT NULL,
    url_image_game TEXT NOT NULL,
    developer TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS 'users'(
    id TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL,
);