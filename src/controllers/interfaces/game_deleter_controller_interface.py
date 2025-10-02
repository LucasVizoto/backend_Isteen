from abc import ABC, abstractmethod

class GameDeleterControllerInterface(ABC):

    @abstractmethod
    def delete_game(self, game_id: int) -> None:
        pass