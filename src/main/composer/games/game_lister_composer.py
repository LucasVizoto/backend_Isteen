from src.models.sqlite.repository.games_repository import GamesRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.game_lister_controller import GameListerController
from src.view.game_lister_view import GameListerView

def game_lister_composer():
    model = GamesRepository(db_connection_handler)
    controller = GameListerController(model)
    view = GameListerView(controller)

    return view