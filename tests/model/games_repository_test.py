import pytest
from datetime import datetime
from src.models.sqlite.settings.connection import db_connection_handler

from src.models.sqlite.repository.games_repository import GamesRepository


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="integração com o banco")
def test_list_games():
    repo = GamesRepository(db_connection_handler)
    response = repo.list_games()

    print(response)


@pytest.mark.skip(reason="integração com o banco - DELETE")
def test_delete_game():
    game_id = 'e3af3b9b-5237-4aed-9526-ce41a2c4b7e8'
    repo = GamesRepository(db_connection_handler)
    repo.delete_game(game_id)


@pytest.mark.skip(reason="integração com o banco - CREATE")
def test_create_game():
    game_name = 'Silksong'
    game_description = 'Joguinho pancada'
    release_date = datetime.now()
    url_game = 'https://www.construct.net/en/free-online-games/combat-71002/play'
    url_image_game = "https://assets-prd.ignimgs.com/2022/02/07/combat-sq1-1644263038605.jpg"
    developer = "Camilo Veríssimo Garcia Prado"

    repo = GamesRepository(db_connection_handler)
    repo.create_game(game_name, game_description, release_date, url_game, url_image_game, developer)


@pytest.mark.skip(reason="integração com o banco")
def test_get_game_by_id():
    game_id = "7b3e01a4-5d0f-48ab-8f27-fb1ed4a799af"

    repo = GamesRepository(db_connection_handler)
    response = repo.get_game_by_id(game_id)

    print()
    print(response)
    release_date = response.release_date
    print(release_date.strftime('%Y-%m-%d'))