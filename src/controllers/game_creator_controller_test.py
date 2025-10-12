import pytest
from datetime import datetime

from src.controllers.game_creator_controller import GameCreatorController

class MockGameRepository:
    def create_game(self, game_name: str, game_description: str,
                     release_date: datetime, url_game: str, url_image_game:str, developer:str ) -> None:
        ...



def test_create():
    game_info = {
        "name": "John",
        "description": "joguinho pancada",
        "release_date": datetime.now(),
        "url_game": 'https://www.construct.net/en/free-online-games/combat-71002/play',
        "url_image_game": "https://assets-prd.ignimgs.com/2022/02/07/combat-sq1-1644263038605.jpg",
        "developer": "Camilo Veríssimo Garcia Prado"
    }

    controller = GameCreatorController(MockGameRepository())
    response = controller.create(game_info)

    assert response['data']["type"] == 'Game'
    assert response['data']["count"] == 1
    assert response['data']["attributes"] == game_info

@pytest.mark.skip('Teste de validação, ainda não implementado')
def test_create_error():
    game_info_without_url_game = {
        "name": "John",
        "description": "joguinho pancada",
        "release_date": datetime.now(),
        "url_image_game": "https://assets-prd.ignimgs.com/2022/02/07/combat-sq1-1644263038605.jpg",
        "developer": "Camilo Veríssimo Garcia Prado"
    }
    controller = GameCreatorController(MockGameRepository())

    with pytest.raises(Exception) as exc_info:
        controller.create(game_info_without_url_game)

    assert str(exc_info.value) == ...