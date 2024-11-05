# Knucklebones Game

This is a Python implementation of the dice game **Knucklebones** from *Cult of the Lamb*. The goal of the game is to roll dice and place them strategically on a 3x3 grid to outscore your opponent. Each player takes turns placing dice, with points calculated based on matching dice values.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd knucklebones


Game Rules
    Objective: The player with the highest score at the end of the game wins.
    Gameplay:
    Players take turns rolling a 6-sided die.
    After each roll, the player must place the die in one of three columns on their 3x3 grid.
    Dice in the same column with matching values multiply the score for that column (e.g., two 4's would multiply 4 by 2).
    You can also remove an opponent's die by placing a matching die in the same column on your grid.
    The game ends when all spaces on both players' grids are filled.

File Structure
    knucklebones.py: Main game loop and execution logic.
    player.py: Defines the Player class, which manages rolling and placing dice.
    board.py: Contains the Board class, handling the 3x3 grid and score calculations.
    utils.py: Helper functions like input validation and board display.
    tests.py: Unit tests to ensure the game logic works as expected.
    requirements.txt: Lists any external libraries (if necessary).
    Contributing
    Feel free to submit pull requests or issues to improve the game! Contributions are welcome, whether it's fixing bugs, improving the logic, or adding new features.