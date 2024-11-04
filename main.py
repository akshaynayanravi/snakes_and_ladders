from snakes_and_ladders.constants import BOARD_SIZE, DIE_SIZE, SNAKES, LADDERS
from snakes_and_ladders.entities import Board, Die, Game


def main():
    print("Hi,\nWelcome to the classic Snakes And Ladders Game!!!")
    board = Board(board_size=BOARD_SIZE, snakes=SNAKES, ladders=LADDERS)
    die = Die(die_size=DIE_SIZE)
    print(
        f"\nBoard set-up is complete...\nBoard Size - {BOARD_SIZE},\nDie Size - {DIE_SIZE},\nNo. of Snakes - {len(SNAKES)},\nNo. of Ladders - {len(LADDERS)}"
    )
    no_of_players = int(input("\nNo. of players? "))
    players = [str(input(f"Player {idx}: ")) for idx in range(1, no_of_players + 1)]
    print(f"Players - {players}")
    game = Game(players=players, board=board, die=die)
    game.start_game()


if __name__ == "__main__":
    main()
