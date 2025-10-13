from src.models.sqlite.repository.games_repository import GamesRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.game_finder_controller import GameFinderController
from src.view.game_finder_view import GameFinderView

def game_finder_composer():
    model = GamesRepository(db_connection_handler)
    controller = GameFinderController(model)
    view = GameFinderView(controller)

    return view