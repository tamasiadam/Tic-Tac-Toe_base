from game import TicTacToe
from menu import get_menu_option, choose_team


def main():
    gamemode = get_menu_option()
    if gamemode == 0:
        player_one = choose_team()
    elif gamemode == 1:
        print("Hamarosan")
    elif gamemode == 2:
        print("Hamarosan...")
    elif gamemode == 3:
        print("Hamarosan..")
    game = TicTacToe()
    game.play(gamemode)
    


if __name__ == "__main__":
    main()