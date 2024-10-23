# Choix du joueur

def player_move(icon):
    if icon == "X":
        nombre = 1
    elif icon == "O":
        nombre = 2
    print("A ton tour {}".format(nombre))
    choix = int(input("Fais ton choix (A1-C3): ").strip())
    if tableau[choix - 1] == " ":
        tableau[choix - 1] = icon
    else:
        print()
        print("Cette case est déja prise!")