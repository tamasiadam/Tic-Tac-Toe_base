from game import TicTacToe
from menu import get_menu_option, choose_team


def main():
    gamemode = get_menu_option()
    if gamemode != 2 or gamemode <= 4:
       player_one = choose_team()
       

    

        
    game = TicTacToe()
    game.play(gamemode)
    


if __name__ == "__main__":
    main()