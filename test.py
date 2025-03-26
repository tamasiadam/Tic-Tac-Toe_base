from board import get_empty_board, is_board_full, get_winning_player, board_decoration
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option


def main():
# The main function
    gamemode = get_menu_option()
    board = get_empty_board()
    decoration = board_decoration(board)
    symbol_1, symbol_2 = symbol_select_human_vs_human()
    full = isFull(board, symbol_1, symbol_2) # The function that starts the game is also in here.

def symbol_select_human_vs_human():
# This function decides the players' symbols
    symbol_1 = input("\nPlayer 1 choose your symbol (X or O): ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print(f"Player 1 is {symbol_1}\nPlayer 2 is {symbol_2}")
    elif symbol_1 != "X" or symbol_1 != "O":
        ValueError
        print("Invalid symbol. Try again.")
        symbol_select_human_vs_human()

    return symbol_1, symbol_2


def startGamming(board, symbol_1, symbol_2, count):
# This function starts the game.

    # Decides the turn
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player "+ player + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))


    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))    
        
    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)



def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function check if the board is full
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = board_decoration(board)
        
        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ")

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")
        
    # This is function gives a report 
    report(count, winner, symbol_1, symbol_2)



def outOfBoard(row, column):
# This function tells the players that their selection is out of range
    print("Out of boarder. Pick another one. ")

def isWinner(board, symbol_1, symbol_2, count):
# This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")
            
            
    # Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner
    


def illegal(board, symbol_1, symbol_2, row, column):
    print("The square you picked is already filled. Pick another one.")

    
def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")


main()