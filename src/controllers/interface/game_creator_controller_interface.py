from abc import ABC, abstractmethod

class GameCreatorControllerInterface(ABC):

    @abstractmethod
    def create(game_info: dict) -> dict:
        ...