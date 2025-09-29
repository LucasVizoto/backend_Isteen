from .interfaces.game_finder_controller_interface import GameFinderControllerInterface
from src.models.sqlite.interfaces.games_repository_interface import GamesRepositoryInterface

class GameFinderController(GameFinderControllerInterface):
    def __init__(self, game_repository:GamesRepositoryInterface):
        self.__game_repository = game_repository

    def find(game_id: int) -> dict:
        ...