def man_coordinates(board, symbol_1, symbol_2, count):

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



def get_human_coordinates(board, current_player):

  human_coordinate = input("Your turn! (write a position eg. A2) ")
  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """
  pass


def get_random_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass

def get_unbeatable_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3))

  board_4 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should always be (0, 0)")
  print(get_unbeatable_ai_coordinates(board_4, "X")) 

  board_5 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print("The printed coordinate should always be (1, 1)")
  print(get_unbeatable_ai_coordinates(board_5, "O")) 

  board_6 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print("The printed coordinate should either (0, 2) or (2, 0)")
  print(get_unbeatable_ai_coordinates(board_6)) 