CREATE TABLE IF NOT EXISTS 'games'(
    id TEXT PRIMARY KEY,
    game_name TEXT NOT NULL,
    game_description TEXT NOT NULL,
    release_date DATE NOT NULL,
    url_game TEXT NOT NULL,
    url_image_game TEXT NOT NULL,
    developer TEXT NOT NULL,
);