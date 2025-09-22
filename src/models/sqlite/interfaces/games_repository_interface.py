from abc import ABC, abstractmethod

class GamesRepositoryInterface(ABC):

    @abstractmethod
    def create_game(data: dict) -> None:
        ...