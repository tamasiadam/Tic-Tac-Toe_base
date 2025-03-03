def get_menu_option():
  
  valasztas = int(input("""
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI
  
  Válassz:"""))

  if valasztas < 5:
    print(f"{valasztas}. mód sikeresen kiválasztva! ")
    return valasztas
  else:
    ValueError
    print("Hiba! Kérlek adj meg egy számot 1-től 4-ig!")
    get_menu_option()
     
"""
  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.

  pass
"""

if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()

