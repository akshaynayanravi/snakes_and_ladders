import random

# from utils import get_positions_dict


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        if self.position + steps <= 100:
            self.position += steps
        return self.position

    def current_position(self):
        return self.position


# TODO: For future improvement to implement Snake as an entity.
# class Snake:
#     def __init__(self, head, tail):
#         self.head = head
#         self.tail = tail
#
#     def positions(self):
#         return {self.head: self.tail}


# TODO: For future improvement to implement Ladder as an entity.
# class Ladder:
#     def __init__(self, bottom, top):
#         self.bottom = bottom
#         self.top = top
#
#     def positions(self):
#         return {self.bottom: self.top}


class Board:
    def __init__(self, board_size, snakes, ladders):
        self.size = board_size
        self.snakes = {head: tail for head, tail in snakes}
        self.ladders = {bottom: top for bottom, top in ladders}
        # self.snakes = get_positions_dict([Snake(head,tail).positions() for head, tail in snakes])
        # self.ladders = get_positions_dict([Ladder(bottom, top).positions() for bottom, top in ladders])

    def check_for_snakes_and_ladders(self, position):
        if position in self.snakes:
            print(
                f"Oops! Hit a snake at {position}, sliding down to {self.snakes[position]}."
            )
            return self.snakes[position]

        if position in self.ladders:
            print(
                f"Yay! Found a ladder at {position}, climbing up to {self.ladders[position]}."
            )
            return self.ladders[position]

        return position


class Die:
    def __init__(self, die_size):
        self.size = die_size

    def roll(self):
        return random.randint(1, self.size)


class Game:
    def __init__(self, players, board: Board, die: Die):
        self.players = [Player(name) for name in players]
        self.board = board
        self.die = die
        self.current_player = 0

    def play_turn(self):
        player = self.players[self.current_player]
        str(input(f"\n{player.name} your turn to roll... <ENTER>"))
        roll = self.die.roll()
        print(f"{player.name} rolls a {roll}.")

        player.move(roll)
        print(f"{player.name} moves to {player.current_position()}.")

        new_position = self.board.check_for_snakes_and_ladders(
            player.current_position()
        )
        player.position = new_position
        print(f"{player.name} is now on square {player.current_position()}.")

        if player.current_position() == self.board.size:
            print(f"\n{player.name} wins the game!")
            return True

        self.current_player = (self.current_player + 1) % len(self.players)
        return False

    def start_game(self):
        print("\nLet's start the game!")
        game_over = False
        while not game_over:
            game_over = self.play_turn()
