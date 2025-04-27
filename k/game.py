import random
from menu import get_menu_option

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A flat list representing 3x3
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

    def is_draw(self):
        return all(cell != ' ' for cell in self.board) and self.check_winner() is None

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self, gamemode):
        while True:
            self.display_board()
            print(f"Player {self.current_player}, enter your move (e.g. A0): ", end='')
            raw = input().strip().upper()
            # Expect letter A-C for column and digit 0-2 for row
            if len(raw) != 2 or raw[0] not in 'ABC' or raw[1] not in '012':
                print("Invalid input. Use format A0, B1, C2 etc. Column A-C, row 0-2.")
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

            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player()

def ai_steps():
    # Sorok és oszlopok definiálása
    rows = ['A', 'B', 'C']
    cols = ['0', '1', '2']
    # Véletlenszerű sor és oszlop kiválasztása
    row = random.choice(rows)
    col = random.choice(cols)
    coord = f"{row}{col}"
    print(coord)
    return coord

