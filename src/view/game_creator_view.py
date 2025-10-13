from .interfaces.view_interface import ViewInterface

from src.controllers.game_creator_controller import GameCreatorController

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class GameCreatorView(ViewInterface):
    def __init__(self, controller: GameCreatorController):
        self.__controller = controller

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        game_data = request.body
        response = self.__controller.create(game_data)

        return HttpResponse(status_code=201, body=response)