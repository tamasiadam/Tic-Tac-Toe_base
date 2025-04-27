def get_menu_option():
    modes = ["Human vs Human", "Human vs Bot", "Simulated play", "Human vs Hard Bot"]

    option = int(input("""
  0. Human vs Human
  1. Human vs Bot
  2. Simulated play (Bot vs Bot)
  3. Human vs Hard Bot\n
  Please select a gamemode: """))

    if option < 4 and option >= 0:
        print(f"\n  {modes[option]} mode selected!\n")
        return option
    else:
        print("\n   Error! Please select a number from 0 to 3!")
        get_menu_option()


if __name__ == "__main__":
    option = get_menu_option()

def symbol_select():
    while True:
        player_one = input("Player 1, choose your symbol (X/O): ").strip().upper()
        if player_one in ('X', 'O'):
            player_two = 'O' if player_one == 'X' else 'X'
            print(f"Player 1 is '{player_one}', Player 2 is '{player_two}'.\n")
            return player_one
        else:
            print("Invalid choice. Please enter 'X' or 'O'.\n")

if __name__ == "__main__":
    mode = get_menu_option()
    player_one = symbol_select()