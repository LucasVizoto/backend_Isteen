from abc import ABC, abstractmethod

class GameFinderControllerInterface(ABC):

    @abstractmethod
    def find(game_id:int) -> dict:
        ... 