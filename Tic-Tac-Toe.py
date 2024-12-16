import random


def printgrid():
    """Displays grid when function is called."""

    for row in range(0, 13):
        print("")
        for column in range(0, 25):
            print(rowList[row][column], end = "")


def playpos(posInput = None, newValue = None):  # Function
    """
    Searches for specific and empty grid play positions.
    Updates the grid positions List with new index values corresponding to player/program moves made.
    Counts empty positions and returns True if count reaches 9 (used to indicate if game is over).

    PARAMETERS
    (Arguments are optional)
    posInput(int): The number of the chosen grid position for game move.
    newValue(str): The new value which is to be placed in the chosen grid position.

    RETURNS
    inputCount(bool): If no arguments are given, returns True if count has reached 9 (no positions are empty; grid positions are filled).
    rowList[row][column](list): Returns what value is stored in the specific List index position.

    Playable grid positions:
    1 : rowList[2][4]
    2 : rowList[2][12]
    3 : rowList[2][20]
    4 : rowList[6][4]
    5 : rowList[6][12]
    6 : rowList[6][20]
    7 : rowList[10][4]      
    8 : rowList[10][12]
    9 : rowList[10][20]
    """

    gridPos = 0
    inputCount = 0

    for row in range(2, 10 + 1, 4):
        for column in range(4, 20 + 1, 8):
            gridPos += 1  # Theoretically converts rowList[row][column] to gridPos.

            if posInput == None and newValue == None:  # If no arguments are given.
                if rowList[row][column] == "X" or rowList[row][column] == "O":
                    inputCount += 1  # If grid position is not empty, increments count.

                # If no grid positions are empty, return True.
                if inputCount == 9: return True

            # If chosen grid position has been reached in Loop.
            elif posInput == gridPos:
                if newValue == "X": rowList[row][column] = "X"  # Update chosen position with 'X'.
                elif newValue == "O": rowList[row][column] = "O"  # Update chosen position with 'O'.
                elif newValue == None: return rowList[row][column]


def gameStat(playerType):  # Function
    """
    Determines whether the user or program has won or not.

    PARAMETERS
    playerType(str): The type of player who's game status is being checked (specifically for user or program).

    RETURNS
    playerWin(bool): Returns True if any of the specified winning conditions are met, or False if none of the
    conditions are met. 
    """

    if playerType == "user": moveType = "X"  # If player type is the user.
    elif playerType == "prog": moveType = "O"  # If player type is the program.

    # Checks for 3 'X' or 'O' per row.
    # Checks for 3 'X' or 'O' per column.
    # Checks for 3 'X' or 'O' per diagonal row.
    if str(rowList[2]).count(moveType) == 3 \
        or str(rowList[6]).count(moveType) == 3 \
        or str(rowList[10]).count(moveType) == 3 \
        or [rowList[2][4], rowList[6][4], rowList[10][4]].count(moveType) == 3 \
        or [rowList[2][12], rowList[6][12], rowList[10][12]].count(moveType) == 3 \
        or [rowList[2][20], rowList[6][20], rowList[10][20]].count(moveType) == 3 \
        or [rowList[2][4], rowList[6][12], rowList[10][20]].count(moveType) == 3 \
        or [rowList[2][20], rowList[6][12], rowList[10][4]].count(moveType) == 3:
        playerWin = True
    else:
        playerWin = False
    
    return playerWin


def yesnoerror(userInput):  # Error handling Function
    """Checks that user input is either 'y' or 'n', returns user input."""

    # Keeps prompting for input until input conditions are met.
    while True:
        if userInput == "Y" or userInput == "N": break
        else: userInput = input("\nPlease only enter Y or N.\nDo you want to play again? (Y/N): ").upper()
    return userInput


rowList = []
columnList = []

# Structures the game grid.
for row in range(0, 13):
    for column in range(0, 25):
        if row == 0 or row  == 12: columnList.insert(column, " ")
        elif row == 4 or row == 8: columnList.insert(column, "-")
        else:
            if column == 8 or column == 16: columnList.insert(column, "|")
            else: columnList.insert(column, " ")
    rowList.insert(row, columnList)
    columnList = []

playerMove = 1  # Sets playerMove to True/valid.

print("""\n
-------------------------
 Welcome to Tic-Tac-Toe!""")

while True:
    if playerMove: printgrid()  # If player move is valid, prints the grid.
    
    playerMove = input("\n\nPlease select a position to enter the X between 1 to 9: ")

    try:
        playerMove = int(playerMove)  # Input must be converted to int.
        if playerMove in range(1, 9 + 1):  # Input must be number from 1 - 9.
            if playpos(playerMove) == " ": playpos(playerMove, "X")  # Grid position must be empty. Places player move at specified grid position.
            else: raise IndexError
        else: raise ValueError
    except IndexError: # If position on grid is already filled.
        playerMove = 0
        print("\nInvalid input.\nPlease select a different position for X.")
    except ValueError: # If input not in range 1 - 9, or type int.
        playerMove = 0
        print("\nInvalid input.\nPlease only enter a number from 1 to 9 to select a position for X.")

    if playerMove:  # If player move is valid.
        if not playpos():  # If game is not over.
            printgrid()
            if gameStat("user") == False:  # If user has not won.
                if gameStat("prog") == False: # If program has not won, make a move.
                    while True:
                        progMove = random.randrange(1, 9 + 1)
                        if playpos(progMove) == " ":
                            playpos(progMove, "O")
                            break
                    print(f"\nComputer placed an O on position {progMove}")

                # If program wins.
                if gameStat("prog") == True:
                    for row in range(0, 13):  # Prints grid.
                        print("")
                        for column in range(0, 25):
                            print(rowList[row][column], end = "")

                    print("\n\nYou lose!")
                    playAgain = yesnoerror(input("\nDo you want to play again? (Y/N): ").upper())

                    # If player does not want to play again.
                    if playAgain == "N":
                        print("\n\nThank you for playing tic-tac-toe.\nGame ended.")
                        break  # End loop and end game.

                    # If player wants to play again, reset grid postions to empty.
                    else:
                        for row in range(2, 10 + 1, 4):
                            for column in range(4, 20 + 1, 8): rowList[row][column] = " "

            # If user wins.
            elif gameStat("user") == True:
                print("\n\nYou win!")
                playAgain = yesnoerror(input("\nDo you want to play again? (Y/N): ").upper())
                if playAgain == "N":
                    print("\nThank you for playing tic-tac-toe.\nGame ended.")
                    break
                else:
                    for row in range(2, 10 + 1, 4):
                        for column in range(4, 20 + 1, 8): rowList[row][column] = " "
        
        #  If count in playpos() Function has reached 9 - game is over.
        else:
            # If user wins.
            if gameStat("user") == True:
                for row in range(0, 13):  # Prints grid.
                    print("")
                    for column in range(0, 25):
                        print(rowList[row][column], end = "")

                print("\n\nYou win!")
                playAgain = yesnoerror(input("\nDo you want to play again? (Y/N): ").upper())
                if playAgain == "N":
                    print("\nThank you for playing tic-tac-toe.\nGame ended.")
                    break
                else:
                    for row in range(2, 10 + 1, 4):
                        for column in range(4, 20 + 1, 8): rowList[row][column] = " "
            # If user did not win, program can't win after user's last move.
            else:
                for row in range(0, 13):  # Prints grid.
                    print("")
                    for column in range(0, 25):
                        print(rowList[row][column], end = "")

                print("\n\nNo one wins!")
                playAgain = yesnoerror(input("\nDo you want to play again? (Y/N): ").upper())
                if playAgain == "N":
                    print("\n\nThank you for playing tic-tac-toe.\nGame ended.")
                    break
                else:
                    for row in range(2, 10 + 1, 4):
                        for column in range(4, 20 + 1, 8): rowList[row][column] = " "