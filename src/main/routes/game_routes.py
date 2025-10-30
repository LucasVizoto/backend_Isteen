from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_error

from src.main.composer.game_finder_composer import game_finder_composer
from src.main.composer.game_lister_composer import game_lister_composer
from src.main.composer.game_creator_composer import game_creator_composer
from src.main.composer.game_deleter_composer import game_deleter_composer

game_routes_bp = Blueprint('games_routes', __name__)



@game_routes_bp.route('/game/<game_id>', methods=['GET'])
def find_game(game_id):
    try:
        http_request = HttpRequest(params={"id": game_id})
        view = game_finder_composer()

        response = view.handle_request(http_request)

        return jsonify(response.body), response.status_code
    except Exception as e:
        http_response = handle_error(e)
        return jsonify(http_response.body), http_response.status_code




@game_routes_bp.route('/games', methods=['GET'])
def list_games():
    try:
        http_request = HttpRequest(params=request.json)
        view = game_lister_composer()

        http_response = view.handle_request(http_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as e:
        http_response = handle_error(e)
        return jsonify(http_response.body), http_response.status_code
    


@game_routes_bp.route('/games/create', methods=['POST'])
def create_game():
    try:
        http_request = HttpRequest(body=request.json)
        view = game_creator_composer()

        http_response = view.handle_request(http_request)
        return jsonify(http_response.body), http_response.status_code
    
    except Exception as e:
        http_response = handle_error(e)
        return jsonify(http_response.body), http_response.status_code
    


@game_routes_bp.route('/games/delete', methods=['DELETE'])
def delete_game():
    try:
        http_request = HttpRequest(body=request.json)
        view = game_deleter_composer()

        http_response = view.handle_request(http_request)
        return jsonify(http_response.body), http_response.status_code
    
    except Exception as e:
        http_response = handle_error(e)
        return jsonify(http_response.body), http_response.status_code