from sqlalchemy.exc import NoResultFound
from datetime import datetime
from uuid import uuid4

from src.models.sqlite.interfaces.games_repository_interface import GamesRepositoryInterface
from src.models.sqlite.entities.game_entity import GameEntity

class GamesRepository(GamesRepositoryInterface):

    def __init__(self, db_connection)->None:
        self.__db_connection = db_connection

    def get_game_by_id(self, game_id: str) -> GameEntity:
         with self.__db_connection as database:
            try:
                game = (
                    database.session
                    .query(GameEntity)
                    .filter(GameEntity.id == game_id)
                    .with_entities(
                        GameEntity.game_name,
                        GameEntity.game_description,
                        GameEntity.release_date,
                        GameEntity.url_game,
                        GameEntity.url_image_game,
                        GameEntity.developer
                    )
                    .one()
                )
                return game
            except NoResultFound:
                return None
            
    def create_game(self, game_name: str, game_description: str,
                     release_date: datetime, url_game: str, url_image_game:str, developer:str ) -> None:
         with self.__db_connection as database:
            try:
                id = uuid4()
                person_data = GameEntity(
                    id = str(id),
                    game_name=game_name,
                    game_description = game_description,
                    release_date = release_date,
                    url_game = url_game,
                    url_image_game = url_image_game,
                    developer = developer
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def delete_game(self, game_id: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(GameEntity)
                    .filter(GameEntity.id == game_id)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def list_games(self) -> list[GameEntity]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(GameEntity).all()
                return pets
            except NoResultFound:
                return []