from board import get_empty_board, board_full, get_winning_player, board_decoration
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option


def main():

    gamemode = get_menu_option()
    board = get_empty_board()
    decoration = board_decoration(board)
    symbol_1, symbol_2 = symbol_select_human_vs_human()
    full = BoardFull(board, symbol_1, symbol_2)


def symbol_select_human_vs_human():
    
    while True:
        symbol_1 = input("\nPlayer 1 choose your symbol (X or O): ").upper()
        if symbol_1 == "X":
            symbol_2 = "O"
            print(f"\nPlayer 1 is {symbol_1}\nPlayer 2 is {symbol_2}")
            break
        elif symbol_1 == "O":
            symbol_2 = "X"
            print(f"\nPlayer 1 is {symbol_1}\nPlayer 2 is {symbol_2}")
            break
        else:
            print("Invalid symbol. Please choose either 'X' or 'O'.")
    return symbol_1, symbol_2


def start(board, symbol_1, symbol_2, count):


    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("\nPlayer " + player + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "\nupper row: 0\nmiddle row 1\nbottom row: 2 \n"))
    column = int(input("Pick a column:"
                       "\nleft column: 0\nmiddle column 1\nright column: 2 \n"))


    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row:"
                    "\nupper row: 0\nmiddle row 1\nbottom row: 2 \n"))
        column = int(input("Pick a column:"
                       "\nleft column: 0\nmiddle column 1\nright column: 2 \n"))

    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row\nupper row:"
                        "0\nmiddle row: 1\nbottom row: 2 \n"))
        column = int(input("Pick a column:"
                           "\nleft column: 0\nmiddle column: 1\nright column 2 \n"))

    if player == symbol_1:
        board[row][column] = symbol_1

    else:
        board[row][column] = symbol_2

    return (board)


def BoardFull(board, symbol_1, symbol_2):
    count = 1
    winner = True

    while count < 10 and winner == True:
        gaming = start(board, symbol_1, symbol_2, count)
        pretty = board_decoration(board)

        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ")


        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")


    report(count, winner, symbol_1, symbol_2)


def outOfBoard(row, column):

    print("Out of boarder. Pick another one. ")


def isWinner(board, symbol_1, symbol_2, count):

    winner = True

    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")


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
    if (winner == False) and (count % 2 == 1):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")


main()