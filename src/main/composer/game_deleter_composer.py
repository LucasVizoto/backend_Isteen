from src.models.sqlite.repository.games_repository import GamesRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.game_deleter_controller import GameDeleterController
from src.view.game_deleter_view import GameDeleterView

def game_creator_composer():
    model = GamesRepository(db_connection_handler)
    controller = GameDeleterController(model)
    view = GameDeleterView(controller)

    return view