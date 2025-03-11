# 2048 Game in Python (using Tkinter)

## Challenge Overview

The challenge i have given myself is to build a small project every day to improve coding skills. On one of the days, I decided to recreate the popular 2048 game using Python and Tkinter. The game consists of a 4x4 grid where you combine tiles with matching values (2, 4, 8, etc.) to reach the ultimate tile value of 2048. The goal is to achieve the highest score possible while avoiding running out of moves.

## Project Overview

This project is a simple implementation of the 2048 game using Python's Tkinter library for the graphical user interface. The game allows players to move tiles in four directions (left, right, up, and down), merge matching tiles, and spawn new tiles after every move. The player’s score and high score are displayed at the top of the screen. The game ends when there are no more moves left to make.

### Key Features:
- A 4x4 grid where tiles can move and merge.
- Score counter that updates dynamically as the game progresses.
- High score tracking that keeps the highest score across multiple sessions.
- Game over condition when no moves are possible.

## Used Software

### Languages
- **Python 3**: The main programming language used to implement the game.

### Libraries
- **Tkinter**: Python's standard library for creating graphical user interfaces (GUIs). Used for displaying the game grid, tiles, and the score.
- **random**: Python's library for generating random numbers, used to spawn new tiles in random positions.

## Implementation Details

1. **Game Initialization**: 
   - The game board is a 4x4 grid, represented by a 2D list of integers (zeros for empty spaces).
   - The game starts with two tiles (2 or 4) placed randomly on the grid.
   
2. **Movement**:
   - The player can use the arrow keys to move tiles in four directions: left, right, up, and down.
   - The movement logic checks for possible merges between tiles of the same value (e.g., two 2s merge into one 4).
   - After every move, a new tile (either a 2 or a 4) spawns at a random empty location on the grid.

3. **Score Calculation**:
   - Each time two tiles merge, the player's score increases by the value of the newly created tile.
   - The score is displayed and updated on the GUI dynamically as moves are made.
   
4. **High Score Tracking**:
   - A high score is maintained across sessions. If the current score exceeds the high score, it is updated and displayed.

5. **Game Over**:
   - The game ends when there are no more valid moves (i.e., the grid is full, and no adjacent tiles can merge).

### Key Functions:
- `initialize_game()`: Initializes the game by creating a 4x4 grid and placing two initial tiles.
- `spawn_new_tile()`: Places a new tile (2 or 4) in a random empty spot on the board.
- `move_left()`: Handles the logic for moving tiles to the left and merging them if possible.
- `move()`: Calls `move_left()` based on the direction (right, up, or down) and modifies the board accordingly.
- `is_game_over()`: Checks if the game is over by verifying if there are no more valid moves.
- `update_display()`: Updates the visual display of the board on the Tkinter canvas.
- `on_keypress()`: Handles user input (arrow key presses) to control the game.

## Notes for Future Improvements:
- **Animation**: Adding smooth animations when tiles move and merge could enhance the user experience.
- **Undo Feature**: Implementing an undo feature to reverse the last move could make the game more enjoyable.
- **Difficulty Levels**: Adding different difficulty levels where the speed or the frequency of higher-value tiles increases as the player progresses could add more challenge.
- **Mobile Support**: Make the game responsive to different screen sizes or add support for mobile touch events.
- **Save/Load Game**: Allow the player to save the game state and load it later to continue from where they left off.

## License

This project is open-source and is licensed under the MIT License.

PS: my highscore is 932, let me know if you beat it
