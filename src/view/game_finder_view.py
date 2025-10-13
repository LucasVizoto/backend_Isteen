from .interfaces.view_interface import ViewInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.controllers.game_finder_controller import GameFinderController

class GameFinderView(ViewInterface):
    def __init__(self, controller: GameFinderController):
        self.__controller = controller

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        game_id = request.params['id']
        response = self.__controller.find(game_id)

        return HttpResponse(status_code=200, body=response)