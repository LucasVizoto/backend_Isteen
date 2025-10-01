from .interfaces.game_finder_controller_interface import GameFinderControllerInterface
from src.models.sqlite.interfaces.games_repository_interface import GamesRepositoryInterface
from src.models.sqlite.entities.game_entity import GameEntity

from src.errors.error_types.http_not_found_error import HttpNotFoundError

class GameFinderController(GameFinderControllerInterface):
    def __init__(self, game_repository:GamesRepositoryInterface):
        self.__game_repository = game_repository

    def find(self, game_id: str) -> dict:
        game = self.__get_game_from_db(game_id)
        formated_response = self.__format_response(game)
        return formated_response

    def __get_game_from_db(self, game_id: str) -> GameEntity:
        game = self.__game_repository.get_game_by_id(game_id)
        if not game:
            raise HttpNotFoundError('Game not founded on database')
        return game
    
    def __format_response(self, game: GameEntity) -> dict:
        return {
            "data": {
                "type": "Game",
                "attributes": {
                    "id": game.id,
                    "name": game.name,
                    "description": game.description,
                    "release_date": game.release_date,
                    "url_game": game.url_game,
                    "url_image_game": game.url_image_game,
                    "developer": game.developer
                }
            }
        }