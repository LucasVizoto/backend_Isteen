from src.models.sqlite.entities.game_entity import GameEntity

from .game_lister_controller import GameListerController

class MockGameRepository:
    def list_games(self) -> list:
        return [
            GameEntity(
                id = "1",
                game_name = "Game One",
                game_description = "Description One",
                release_date = "2023-01-01T00:00:00",
                url_game = "http://example.com/game1",
                url_image_game = "http://example.com/game1.png",
                developer = "Dev One"
            ),
            GameEntity(
                id = "2",
                game_name = "Game Two",
                game_description = "Description Two",
                release_date = "2023-02-01T00:00:00",
                url_game = "http://example.com/game1",
                url_image_game = "http://example.com/game1.png",
                developer = "Dev Two"
            )
            
        ]

def test_game_lister_controller():
    mock_repository = MockGameRepository()
    controller = GameListerController(mock_repository)

    response = controller.list_games()

    expected_response = {
        "data": {
            "type": "Games",
            "count": 2,
            "games": [
                {
                    "id": "1",
                    "game_name": "Game One",
                    "game_description": "Description One",
                    "release_date": "2023-01-01T00:00:00",
                    "url_game": "http://example.com/game1",
                    "url_image_game": "http://example.com/game1.png",
                    "developer": "Dev One"
                },
                {
                    "id": "2",
                    "game_name": "Game Two",
                    "game_description": "Description Two",
                    "release_date": "2023-02-01T00:00:00",
                    "url_game": "http://example.com/game1",
                    "url_image_game": "http://example.com/game1.png",
                    "developer": "Dev Two"
                }
            ]
        }
    }

    assert response == expected_response