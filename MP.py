"""# Tic-Tac-Toe
Matthieu, Franck, Redouane"""

#Création du tableau et de ses lignes.
tableau = [" " for i in range(9)]

def affichez_tableau():
    Ligne1 = f"| {tableau[0]} | {tableau[1]} | {tableau[2]} |"
    Ligne2 = f"| {tableau[3]} | {tableau[4]} | {tableau[5]} |"
    Ligne3 = f"| {tableau[6]} | {tableau[7]} | {tableau[8]} |"

    print()
    print(Ligne1)
    print(Ligne2)
    print(Ligne3)
    print()

def tour_joueur(icon):
    if icon == "X":
        nombre = 1
    elif icon == "O":
        nombre = 2
    print(f"A ton tour joueur{nombre}")
    choix = int(input("Fais ton choix (1-9): "))
    if tableau[choix - 1] == " ":
        tableau[choix - 1] = icon
    else:
        print("Cette case est déja prise!")
        tour_joueur(icon)

def victoire(icon):
    if (tableau[0] == icon and tableau[1] == icon and tableau[2] == icon) or \
       (tableau[3] == icon and tableau[4] == icon and tableau[5] == icon) or \
       (tableau[6] == icon and tableau[7] == icon and tableau[8] == icon) or \
       (tableau[0] == icon and tableau[3] == icon and tableau[6] == icon) or \
       (tableau[1] == icon and tableau[4] == icon and tableau[7] == icon) or \
       (tableau[2] == icon and tableau[5] == icon and tableau[8] == icon) or \
       (tableau[0] == icon and tableau[4] == icon and tableau[8] == icon) or \
       (tableau[2] == icon and tableau[4] == icon and tableau[6] == icon):
        return True
    else:
        return False

def egalite():
    if " " not in tableau:
        return True
    else:
        return False

# Boucle principale du jeu
while True:
    affichez_tableau()
    tour_joueur("X")
    
    if victoire("X"):
        affichez_tableau()
        print("X gagne! Félicitation!")
        break
    elif egalite():
        affichez_tableau()
        print("C'est un match nul!")
        break

    tour_joueur("O")
    
    if victoire("O"):
        affichez_tableau()
        print("O gagne! Félicitation!")
        break
    elif egalite():
        affichez_tableau()
        print("C'est un match nul!")
        break
