from sqlalchemy import Column, String, DateTime

from src.models.sqlite.settings.base import Base

class GameEntity(Base):
    __tablename__ = 'games'

    id = Column(String, primary_key = True)
    game_name = Column(String, nullable= False)
    game_description = Column(String, nullable = False)
    release_date = Column(DateTime, nullable = False)
    url_game = Column(String, nullable = False)
    url_image_game = Column(String, nullable = False)
    developer = Column(String, nullable = False)


    def to_dict(self):
        """Converte a entidade GameEntity para um dicionário."""
        return {
            "id": self.id,
            "game_name": self.game_name,
            "game_description": self.game_description,
            "release_date": self.release_date,
            "url_game": self.url_game,
            "url_image_game": self.url_image_game,
            "developer": self.developer
        }
    def __repr__(self):
        return f"GameEntity [id={self.id}, name={self.game_name}, \
            description={self.game_description}, release_date={self.release_date}, \
                url_game={self.url_game}, url_image_game={self.url_image_game}, \
                    developer={self.developer}]"
