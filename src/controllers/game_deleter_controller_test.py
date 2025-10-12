from .game_deleter_controller import GameDeleterController

def test_delete_game(mocker):
    # Arrange
    mock_game_repository = mocker.Mock()
    game_deleter_controller = GameDeleterController(mock_game_repository)
    game_id= "test_game_id"

    # Act
    game_deleter_controller.delete_game(game_id)

    # Assert
    mock_game_repository.delete_game.assert_called_once_with(game_id)


