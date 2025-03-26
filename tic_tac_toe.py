from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():

    game_mode = get_menu_option() # játékmód kiválasztása
    board = get_empty_board() # üres játéktabla 
    is_game_running = True # játék folyamatban
    while is_game_running: # amíg játék folyamatban
        display_board(board) # játéktabla megjelenítés
        
        # TO DO
        # in each new iteration of the while loop the program should 
        # alternate the value of `current_player` from `X` to `O`
        current_player = 'X'

        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_unbeatable_ai_coordinates or get_human_coordinates

        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop

if __name__ == "__main__":
    main()