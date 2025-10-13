from src.errors.error_types.unprocessable_entity_error import UnprocessableEntityError

from cerberus import Validator


def create_game_validator(body: any):
    body_validator = Validator({
        "type": "dict",
        "schema": {
            "game_name": {"type": "string", "minlength": 1, "maxlength": 100, "required": True},
            "description": {"type": "string", "minlength": 1, "maxlength": 1000, "required": True},
            "release_date": {"type": "string", "minlength": 10, "maxlength": 10, "required": True},
            "url_game": {"type": "string", "minlength": 1, "maxlength": 255, "required": True},
            "url_game_image": {"type": "string", "minlength": 1, "maxlength": 255, "required": True},
            "developer": {"type": "string", "minlength": 1, "maxlength": 100, "required": True},
        }
    })

    response = body_validator.validate(body)
    if response is False:
        raise UnprocessableEntityError(f"Invalid body: {body_validator.errors}")