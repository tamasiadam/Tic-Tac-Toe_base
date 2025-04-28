import random
from menu import get_menu_option

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A 3x3 empty grid
        self.current_player = 'X'

    def display_board(self):
        print("\n  A   B   C")
        for i in range(3):
            row = self.board[i * 3:(i + 1) * 3]
            print(f"{i} " + ' | '.join(row))
            if i < 2:
                print(" ---+---+---")
        print("\n")

    def make_move(self, x, y):
        position = x * 3 + y
        if 0 <= position < 9 and self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

    def draw(self):
        return all(cell != ' ' for cell in self.board) and self.check_winner() is None

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self, mode):
        while True:
            self.display_board()
            print(f"Player {self.current_player}, enter your move (e.g. A0): ", end='')
            raw = input().strip().upper()
      
            if len(raw) != 2 or raw[0] not in 'ABC' or raw[1] not in '012':
                print("Invalid input. Use format A0, B1, C2 etc.")
                continue
            y = ord(raw[0]) - ord('A')  # column
            x = int(raw[1])             # row

            if not self.make_move(x, y):
                print("Cell already taken or invalid. Try again.")
                continue

            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"Congratulations! Player {winner} wins!")
                break

            if self.draw():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player()

    def Simulation(self, mode, grid=None):
        if grid is None:
            grid = [" "] * 9  

        def print_grid():
            print(f"{grid[0]}|{grid[1]}|{grid[2]}")
            print("-+-+-")
            print(f"{grid[3]}|{grid[4]}|{grid[5]}")
            print("-+-+-")
            print(f"{grid[6]}|{grid[7]}|{grid[8]}\n")

        def check_win(mark):
            wins = [(0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6)]
            return any(grid[a]==grid[b]==grid[c]==mark for a,b,c in wins)

        def check_draw():
            return all(cell != " " for cell in grid)

        def minimax(player_mark, opponent_mark, depth, is_maximizing): #legjobb lépés
            if check_win(player_mark):
                return 1
            if check_win(opponent_mark):
                return -1
            if check_draw():
                return 0

            if is_maximizing:
                best_score = -float("inf")
                for i in range(9):
                    if grid[i] == " ":
                        grid[i] = player_mark
                        score = minimax(player_mark, opponent_mark, depth+1, False)
                        grid[i] = " "
                        best_score = max(best_score, score)
                return best_score
            else:
                best_score = float("inf")
                for i in range(9):
                    if grid[i] == " ":
                        grid[i] = opponent_mark
                        score = minimax(player_mark, opponent_mark, depth+1, True)
                        grid[i] = " "
                        best_score = min(best_score, score)
                return best_score

        def ai_move(mark, opponent_mark):
            best_score = -float("inf")
            best_move = None
            for i in range(9):
                if grid[i] == " ":
                    grid[i] = mark
                    score = minimax(mark, opponent_mark, 0, False)
                    grid[i] = " "
                    if score > best_score:
                        best_score, best_move = score, i
  
            grid[best_move] = mark
            print_grid()


        AI_one, AI_two = "X", "O"

        current = random.choice([AI_one, AI_two])

        print(f"First to move: {current}\n")
        print_grid()


        while True:
            if current == AI_one:
                ai_move(AI_one, AI_two)
                if check_win(AI_one):
                    print("X won!") 
                    break
                current = AI_two
            else:
                ai_move(AI_two, AI_one)
                if check_win(AI_two):
                    print("O won!")
                    break
                current = AI_one

            if check_draw():
                print("It's a Draw!")
                break
