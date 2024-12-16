README: Python Tic-Tac-Toe Game

---------- Overview ---------------------------------
This program implements a simple command-line Tic-Tac-Toe game in Python. The user plays against the computer, taking turns to place their respective marks (X for the user and O for the computer) on a 3x3 grid. The game checks for win conditions or a draw after each turn and allows the player to restart the game upon its conclusion.


---------- Features ---------------------------------

1. Interactive Gameplay: The user selects positions to place their X marks, while the computer chooses positions randomly for its O marks.

2. Win Detection: The program checks for all possible winning conditions (rows, columns, and diagonals).

3. Draw Detection: The game ends in a draw if all positions are filled without a winner.

4. Replay Option: At the end of each game, the user can choose to play again or exit.


---------- How to Play ---------------------------------

1. Run the Program: Execute the Python script in a terminal or IDE.
   
2. Select a Position: When prompted, input a number between 1 and 9 to place your X on the grid.
Positions are mapped as follows:

 1 | 2 | 3
 ---------
 4 | 5 | 6
 ---------
 7 | 8 | 9

3. Computer's Turn: The computer will automatically choose an empty position for its O.
   
4. Win/Draw: The game ends when a player gets three of their marks in a row (horizontal, vertical, or diagonal).
All positions are filled without a winner (draw).

5. Replay or Exit: After the game ends, you can choose to play again by entering Y or exit by entering N.


---------- Functions ---------------------------------

1. printgrid()
Displays the current game grid in the terminal.

2. playpos(posInput=None, newValue=None)
Manages the game grid's state, updates positions, and checks if the grid is full.
Parameters:
posInput (int): Position to update (1-9).
newValue (str): Value to place (X or O).
Returns:
True if the grid is full (game over).
Current value at a grid position if newValue is not provided.

3. gameStat(playerType)
Checks if a specific player (user or prog) has met a winning condition.
Parameters:
playerType (str): Player type (user for X, prog for O).
Returns:
True if the player has won.
False otherwise.

4. yesnoerror(userInput)
Validates user input for replaying the game.
Parameters:
userInput (str): Input string (Y/N).
Returns:
Validated input (Y/N).


---------- Code Structure ---------------------------------

1. Initialization
The grid is represented as a 2D list (rowList) that simulates a graphical board in the terminal. Positions are pre-defined to correspond with numbers 1 through 9.

2. Main Game Loop
Prints the grid.
Prompts the user for input and validates it.
Updates the grid with the user's move if valid.
Checks for game-ending conditions: User win, computer win, or draw.
If the game continues, the computer selects a random valid position for its move.
Repeats until the game ends.

3. Game Reset
After the game concludes, the grid is reset to its initial state if the user opts to replay.


---------- Error Handling ---------------------------------

1. Ensures user inputs are integers between 1 and 9.

2. Prompts the user to select another position if their chosen position is already filled.

3. Validates Y/N inputs for replaying the game.


---------- Future Improvements ---------------------------------

- Add a smarter algorithm for the computer's moves.

- Implement a graphical interface using libraries like tkinter or pygame.

- Allow users to choose their mark (X or O) and decide who goes first.


---------- Requirements ---------------------------------

- Python 3.x
  
- random Python library


---------- Running the Program ---------------------------------

1. Save the script to a file, e.g., tic_tac_toe.py.

2. Open a terminal and navigate to the file's directory.

3. Run the script using python tic_tac_toe.py


Enjoy the game!
