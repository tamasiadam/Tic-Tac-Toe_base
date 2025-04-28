def get_menu_option():
    modes = ["Human vs Human", "Human vs Bot", "Simulated play"]

    option = int(input("""
  0. Human vs Human
  1. Human vs Bot
  2. Simulated play (Bot vs Bot)\n
  Please select a gamemode: """))

    if option < 3 and option >= 0:
        print(f"\n  {modes[option]} mode selected!\n")
        return option
    else:
        print("\n   Error! Please select a number from 0 to 2!")
        get_menu_option()


if __name__ == "__main__":
    option = get_menu_option()

if __name__ == "__main__":
    mode = get_menu_option()