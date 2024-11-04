# Snake and Ladder Game

```text
Question 1: Object-Oriented Design - Snake and Ladder Game

Design and implement the classic Snake and Ladder board game.
Reference: https://www.wikihow.com/Play-Snakes-and-Ladders

Requirements
1. 10x10 board (squares 1-100)
2. 2-4 players
3. Six-sided die
4. 8-10 randomly placed snakes and ladders
5. Game ends when a player reaches square 100

Tasks

Design entity classes
● Identify core entities and their attributes
● Define relationships between entities
● No UI implementation required (use simple print statements if needed)

Implement game logic
● Player movement with die rolls
● Snake and ladder mechanics
● Turn management
● Win condition checking
● Game state tracking

Note
Focus on object-oriented design and core game logic only. No graphical or terminal UI required.
```

### `constants`
Defines the game settings, including:
- `BOARD_SIZE`: The size of the board (default is 100).
- `DIE_SIZE`: Number of faces on the die (default is 6).
- `SNAKES`: List of tuples representing the heads and tails of snakes.
- `LADDERS`: List of tuples representing the start and end points of ladders.

### `entities`
Contains the following main classes:
- **`Player`**
- **`Board`**
- **`Die`**
- **`Game`**

## Instructions

### Prerequisites

- Python 3.x
- Poetry

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/akshaynayanravi/snakes_and_ladders.git
    cd snakes_and_ladders
    ```

2. Setting up virtual environment using Poetry:
   ```bash
   poetry install
   poetry shell
   ```
   
3. Run the game:
    ```bash
    python main.py
    ```

4. Run unit tests:
   ```bash
   pytest -s .
   ```
   
5. Generate coverage report:
   ```bash
   coverage run -m pytest -s . -v && coverage report -m
   ```
    Note: Current coverage stands at 94%

## Example Output
    Hi,
    Welcome to the classic Snakes And Ladders Game!!!
    
    Board set-up is complete...
    Board Size - 100,
    Die Size - 6,
    No. of Snakes - 10,
    No. of Ladders - 9
    
    No. of players? 3
    Player 1: A
    Player 2: B
    Player 3: C
    Players - ['A', 'B', 'C']
    
    Let's start the game!
    
    A your turn to roll... <ENTER>
    A rolls a 1.
    A moves to 1.
    Yay! Found a ladder at 1, climbing up to 38.
    A is now on square 38.
    .
    .
    .
    A your turn to roll... <ENTER>
    A rolls a 3.
    A moves to 47.
    Oops! Hit a snake at 47, sliding down to 26.
    A is now on square 26.
    .
    .
    .
    A your turn to roll... <ENTER>
    A rolls a 4.
    A moves to 80.
    Yay! Found a ladder at 80, climbing up to 100.
    A is now on square 100.
    
    A wins the game!

## Customization

To customize the game, edit the constants in `constants.py`:

- **Snakes** and **Ladders**: Modify `SNAKES` and `LADDERS` lists to change the positions of snakes and ladders.
- **Board Size** and **Die Size**: Adjust `BOARD_SIZE` and `DIE_SIZE` for different board sizes and dice.
