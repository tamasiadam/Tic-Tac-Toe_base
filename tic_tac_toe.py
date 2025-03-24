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
        if game_mode == HUMAN_VS_HUMAN:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_unbeatable_ai_coordinates or get_human_coordinates
        if game_mode == HUMAN_VS_HUMAN or current_player == 'X':
            x, y = get_human_coordinates(board, current_player)
        elif game_mode == HUMAN_VS_RANDOM_AI and current_player == 'O':
            x, y = get_random_ai_coordinates(board, current_player)
        elif game_mode == HUMAN_VS_UNBEATABLE_AI and current_player == 'O':
            x, y = get_unbeatable_ai_coordinates(board, current_player)
        elif game_mode == RANDOM_AI_VS_RANDOM_AI:
            if current_player == 'X':
                x, y = get_random_ai_coordinates(board, current_player)
            else:
                x, y = get_random_ai_coordinates(board, current_player)
        
        board[x][y] = current_player
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)


if __name__ == "__main__":
    main()