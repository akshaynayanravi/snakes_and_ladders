from constants import BOARD_SIZE, DIE_SIZE, SNAKES, LADDERS, PLAYERS
from snakes_and_ladders.entities import Board, Die, Game


def main():
    board = Board(board_size=BOARD_SIZE, snakes=SNAKES, ladders=LADDERS)
    die = Die(die_size=DIE_SIZE)
    game = Game(players=PLAYERS, board=board, die=die)

    game.start_game()

if __name__ == "__main__":
    main()