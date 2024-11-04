import pytest
from snakes_and_ladders.entities import Player, Board, Die, Game


# Test the Player class
def test_player_initial_position():
    player = Player("Alice")
    assert player.current_position() == 0


def test_player_move_within_bounds():
    player = Player("Bob")
    player.move(3)
    assert player.current_position() == 3


def test_player_move_exceeding_bounds():
    player = Player("Charlie")
    player.move(100)  # Move to 100
    player.move(5)  # Attempt to move beyond 100
    assert player.current_position() == 100


# Test the Board class
@pytest.fixture
def setup_board():
    snakes = [(16, 6), (47, 26)]
    ladders = [(1, 38), (4, 14)]
    return Board(board_size=100, snakes=snakes, ladders=ladders)


def test_apply_snake(setup_board):
    new_position = setup_board.check_for_snakes_and_ladders(16)
    assert new_position == 6  # Should slide down to 6


def test_apply_ladder(setup_board):
    new_position = setup_board.check_for_snakes_and_ladders(1)
    assert new_position == 38  # Should climb up to 38


def test_apply_no_effect(setup_board):
    new_position = setup_board.check_for_snakes_and_ladders(10)
    assert new_position == 10  # No snakes or ladders


# Test the Die class
def test_die_roll():
    die = Die(die_size=6)
    result = die.roll()
    assert result in range(1, 7)  # Should roll a number between 1 and 6


# Test the Game class
@pytest.fixture
def setup_game():
    snakes = [(16, 6), (47, 26)]
    ladders = [(1, 38), (4, 14)]
    players = ["Alice", "Bob"]
    board = Board(board_size=100, snakes=snakes, ladders=ladders)
    die = Die(die_size=6)
    return Game(players=players, board=board, die=die)


def test_game_win_condition(setup_game):
    # Simulate a player reaching 100
    setup_game.players[0].position = 100
    assert setup_game.players[0].current_position() == setup_game.board.size


def test_game_turn_management(setup_game):
    initial_position = setup_game.players[0].current_position()
    setup_game.play_turn()  # Alice's turn
    assert (
        initial_position != setup_game.players[0].current_position()
    )  # Position should change


if __name__ == "__main__":
    pytest.main()
