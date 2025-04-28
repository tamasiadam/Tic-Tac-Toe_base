from game import TicTacToe
from menu import get_menu_option, symbol_select


def main():
    game = TicTacToe()
    mode = get_menu_option()
    if mode == 0:
        player_one = symbol_select()
        game.play(mode)
    elif mode == 1:
        game.humanvsbot()
    elif mode == 2:
        game.Simulation(mode)

if __name__ == "__main__":
    main()