from datetime import datetime
from .interfaces.game_creator_controller_interface import GameCreatorControllerInterface
from src.models.sqlite.interfaces.games_repository_interface import GamesRepositoryInterface

class GameCreatorController(GameCreatorControllerInterface):
    
    def __init__(self, games_repository: GamesRepositoryInterface) -> None:
        self.__games_repository = games_repository
    
    def create(self, game_info: dict) -> dict:
        game_name = game_info["name"]
        game_description = game_info["description"]
        release_date = game_info["release_date"]
        url_game = game_info["url_game"]
        url_image_game = game_info["url_image_game"]
        developer = game_info["developer"]

        self.__insert_on_db(game_name, game_description, release_date, url_game, url_image_game,developer)
        formated_response = self.__formated_response(game_info)
        return formated_response
    
    
    def __insert_on_db(self, game_name: str, game_description: str,
                     release_date: datetime, url_game: str, url_image_game:str, developer:str ) -> None:
        self.__games_repository.create_game(game_name, game_description, release_date, url_game, url_image_game, developer)


    def __formated_response(self, game_info:dict) -> dict:
        return {
            "data": {
                "type": "Game",
                "count": 1,
                "attributes": game_info
            }
        }