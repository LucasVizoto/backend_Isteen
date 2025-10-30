from .interfaces.view_interface import ViewInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.controllers.interfaces.game_deleter_controller_interface import GameDeleterControllerInterface

class GameDeleterView(ViewInterface):

    def __init__(self, controller: GameDeleterControllerInterface):
        self.__controller = controller

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        game_id = request.params["id"]
        self.__controller.delete_game(game_id)

        return HttpResponse(status_code = 204)