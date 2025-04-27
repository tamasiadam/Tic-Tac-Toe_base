import random

def tic_tac_toe(grid=None):
    if grid is None:
        grid = [" "] * 9  # 9 üres mező :contentReference[oaicite:6]{index=6}

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

    def minimax(player_mark, opponent_mark, depth, is_maximizing):
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
        # lépés és tábla kiírása
        grid[best_move] = mark
        print_grid()

    # Játékosok jelölése
    Alex, Sam = "X", "O"
    # Véletlenszerű első lépő :contentReference[oaicite:7]{index=7}
    current = random.choice([Alex, Sam])

    print(f"Első lép: {current}\n")
    print_grid()

    # AI vs AI főciklus :contentReference[oaicite:8]{index=8}
    while True:
        if current == Alex:
            ai_move(Alex, Sam)
            if check_win(Alex):
                print("Alex (X) nyert!") 
                break
            current = Sam
        else:
            ai_move(Sam, Alex)
            if check_win(Sam):
                print("Sam (O) nyert!")
                break
            current = Alex

        if check_draw():
            print("Döntetlen!")
            break

if __name__ == "__main__":
    tic_tac_toe()
