#pylint: disable=unused-argument
from src.controllers.game_finder_controller import GameFinderController

class MockGame():
    def __init__(self)-> None:
        self.id = '123'
        self.name = "John"
        self.description = "Doe"
        self.release_date = "Rex"
        self.url_game = "Dog"
        self.url_image_game = "Dog"
        self.developer = "Dog"

class MockGameRepository():
    def get_game_by_id(self) -> MockGame:
        return MockGame()

def test_find():
    controller = GameFinderController(MockGameRepository)
    response = controller.find('123')

    expected_response = {
        "data": {
                "type": "Game",
                "attributes": {
                    "id": '123',
                    "name": "John",
                    "description": "Doe",
                    "release_date": "Rex",
                    "url_game": "Dog",
                    "url_image_game": "Dog",
                    "developer": "Dog"
                }
            }
    }

    assert response == expected_response