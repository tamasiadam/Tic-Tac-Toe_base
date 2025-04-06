def get_menu_option():
    option = int(input("""
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI\n
  Please select a gamemode: """))

    if option < 5 and option > 0:
        print(f"Mode {option} selected!")
        return option
    else:
        print("\nError! Please select a number from 1 to 4!")
        get_menu_option()


if __name__ == "__main__":
    option = get_menu_option()