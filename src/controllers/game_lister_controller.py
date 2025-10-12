from .interfaces.game_lister_controller_interface import GameListerControllerInterface
from src.models.sqlite.interfaces.games_repository_interface import GamesRepositoryInterface

from src.models.sqlite.entities.game_entity import GameEntity

class GameListerController(GameListerControllerInterface): 
    def __init__ (self, game_repository: GamesRepositoryInterface):
        self.__game_repository = game_repository

    def list_games(self):
        list_games_response =  self.__game_repository.list_games()
        formated_response = self.__format_response(list_games_response)
        return formated_response

    def __format_response(self, games: list[GameEntity]) -> dict:
       games_as_dict = [entity.to_dict() for entity in games]
       
       return {
            "data": {
                "type": "Games",
                "count": len(games_as_dict),
                "games": games_as_dict
            }
        }