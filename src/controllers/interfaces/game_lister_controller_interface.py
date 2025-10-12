from abc import ABC, abstractmethod

from src.models.sqlite.entities.game_entity import GameEntity

class GameListerControllerInterface(ABC):
    @abstractmethod
    def list_games(self) -> list[GameEntity]:
        pass