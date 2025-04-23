def get_menu_option():
    modes = ["Human vs Human", "Human vs Bot", "Simulated play", "Human vs Hard Bot"]

    option = int(input("""
  0. Human vs Human
  1. Random AI vs Random AI
  2. Human vs Random AI
  3. Human vs Unbeatable AI\n
  Please select a gamemode: """))

    if option < 5 and option > 0:
        print(f"\n  {modes[option]} mode selected!\n")
        return option
    else:
        print("\n   Error! Please select a number from 0 to 3!")
        get_menu_option()


if __name__ == "__main__":
    option = get_menu_option()