from sqlalchemy import Column, String

from src.models.sqlite.settings.base import Base

class GameEntity(Base):
    __tablename__ = 'games'

    id = Column(String, primary_key = True)
    name = Column(String, nullable= False)
    description = Column(String, nullable = False)
    release_date = Column(String, nullable = False)
    url_game = Column(String, nullable = False)
    url_image_game = Column(String, nullable = False)
    developer = Column(String, nullable = False)

    def __repr__(self):
        return f'Game '
    