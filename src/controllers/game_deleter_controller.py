from .interfaces.game_deleter_controller_interface import GameDeleterControllerInterface
from src.models.sqlite.interfaces.games_repository_interface import GamesRepositoryInterface

class GameDeleterController(GameDeleterControllerInterface):
    
    def __init__(self, game_repository: GamesRepositoryInterface) -> None:
        self.__game_repository = game_repository

    def delete_game(self, game_id: str) -> None:
        self.__game_repository.delete_game(game_id)