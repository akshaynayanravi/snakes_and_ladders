# Snake and Ladder Game

A simple, object-oriented Python implementation of the classic Snake and Ladder game. This game is played on a 10x10 board with players, snakes, and ladders. Players roll a die, move forward based on the roll result, and encounter snakes (moving them down) or ladders (moving them up). The first player to reach square 100 wins the game.

## Features

- **10x10 board** with squares numbered from 1 to 100.
- **2-4 players** support with customizable player names.
- **6-sided die** to determine movement.
- **Randomly placed snakes and ladders** that modify player positions.
- **Win condition**: the first player to reach square 100 wins.
- Modular structure for easy modification and customization.

## Project Structure

### `constants.py`
Defines the game settings, including:
- `BOARD_SIZE`: The size of the board (default is 100).
- `DIE_SIZE`: Number of faces on the die (default is 6).
- `SNAKES`: List of tuples representing the heads and tails of snakes.
- `LADDERS`: List of tuples representing the start and end points of ladders.
- `PLAYERS`: List of player names participating in the game.

### `entities.py`
Contains the following main classes:

- **`Player`**: Represents a player with a name and position on the board.
- **`Board`**: Represents the game board, holding the positions of snakes and ladders.
- **`Die`**: Simulates a die roll, with configurable number of sides.
- **`Game`**: Manages the game flow, turn-taking, and checks for the win condition.

### `main.py`
Initializes the game with constants and starts the game loop.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/akshaynayanravi/snakes_and_ladders.git
    cd snakes_and_ladders
    ```

2. Run the game:

    ```bash
    python main.py
    ```

## How to Play

1. Each player takes turns rolling the die, moving forward by the number rolled.
2. If a player lands on the head of a snake, they move down to the snake's tail.
3. If a player lands on the bottom of a ladder, they climb up to the top of the ladder.
4. The first player to reach square 100 wins the game!

## Example Output
    Starting the Snake and Ladder Game!
    Amar rolls a 4.
    Amar moves to 4.
    Yay! Found a ladder at 4, climbing up to 14.
    Amar is now on square 14.
    Bharath rolls a 5.
    Bharath moves to 5.
    Bharath is now on square 5.
    .
    .
    .
    Amar rolls a 4.
    Amar moves to 93.
    Oops! Hit a snake at 93, sliding down to 73.
    .
    .
    .
    Amar rolls a 5.
    Amar moves to 80.
    Yay! Found a ladder at 80, climbing up to 100.
    Amar is now on square 100.
    Amar wins the game!

## Testing

### Run Tests:
- To run unit and integration tests, use the following command:
  ```bash
  pytest tests/
  ```

## Customization

To customize the game, edit the constants in `constants.py`:

- **Snakes** and **Ladders**: Modify `SNAKES` and `LADDERS` lists to change the positions of snakes and ladders.
- **Board Size** and **Die Size**: Adjust `BOARD_SIZE` and `DIE_SIZE` for different board sizes and dice.
- **Players**: Add or remove names from `PLAYERS` to change the list of participants.

## Code Overview

This project follows object-oriented principles with a modular design, separating core entities from game logic. The code is organized for readability, ease of modification, and reuse.

## Acknowledgments

- Classic board game "Snakes and Ladders" for the concept.

