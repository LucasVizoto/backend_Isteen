from abc import ABC, abstractmethod
from datetime import datetime
from src.models.sqlite.entities.game_entity import GameEntity

class GamesRepositoryInterface(ABC):

    @abstractmethod
    def get_game_by_id(self, game_id: str) -> GameEntity:
        ...

    @abstractmethod
    def create_game(self, game_name: str, game_description: str,
                     release_date: datetime, url_game: str, url_image_game:str, developer:str ) -> None:
        ...

    @abstractmethod
    def delete_game(self, game_id: str) -> None:
        ...
    
    @abstractmethod
    def list_games(self) -> list[GameEntity]:
        ...