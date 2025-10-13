from .interfaces.view_interface import ViewInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.controllers.interfaces.game_lister_controller_interface import GameListerControllerInterface

class GameListerView(ViewInterface):

    def __init__(self, controller: GameListerControllerInterface):
        self.__controller = controller

    def handle_request(self, request):
        response = self.__controller.list_games()
        return HttpResponse(status_code=200,body = response)