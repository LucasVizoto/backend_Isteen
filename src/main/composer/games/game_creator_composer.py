from src.models.sqlite.repository.games_repository import GamesRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.game_creator_controller import GameCreatorController
from src.view.game_creator_view import GameCreatorView

def game_creator_composer():
    model = GamesRepository(db_connection_handler)
    controller = GameCreatorController(model)
    view = GameCreatorView(controller)

    return view