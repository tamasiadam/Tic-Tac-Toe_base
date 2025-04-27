def get_menu_option():
    mode = int(input("""
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI\n
  Please select a gamemode: """))

    if mode < 5 and mode > 0:
        print(f"Mode {mode} selected!")
        return mode
    else:
        print("\nError! Please select a number from 1 to 4!")
        get_menu_option()

def choose_team():
    while True:
        player_one = input("Player 1, choose your symbol (X/O): ").strip().upper()
        if player_one in ('X', 'O'):
            player_two = 'O' if player_one == 'X' else 'X'
            print(f"Player 1 is '{player_one}', Player 2 is '{player_two}'.\n")
            return player_one
        else:
            print("Invalid choice. Please enter 'X' or 'O'.\n")

if __name__ == "__main__":
    option = get_menu_option()
