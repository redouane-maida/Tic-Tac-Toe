"""# Tic-Tac-Toe
Matthieu, Franck, Redouane"""

# Création du tableau et de ses lignes.
tableau = [" " for i in range(9)]

def affichez_tableau():
    Ligne1 = f"| {tableau[0]} | {tableau[1]} | {tableau[2]} |"
    Ligne2 = f"| {tableau[3]} | {tableau[4]} | {tableau[5]} |"
    Ligne3 = f"| {tableau[6]} | {tableau[7]} | {tableau[8]} |"
    print(Ligne1)
    print(Ligne2)
    print(Ligne3)

# Création du Tour par tour et du mode de jeu

choix_mode_jeu = input("tapez 'A' pour jouer contre un bot ou 'B' pour jouer contre un joueur")

if choix_mode_jeu == 'A':
    import random
    def tour_joueur(icon): #joueur
        if icon == "X":
            nombre = 1
            choix = int(input("Fais ton choix (1-9): "))
        elif icon == "O": #Bot
            nombre = 2
            choix = random.randint(1,9)
            print(f"Le bot (joueur {nombre}) a choisi la case {choix}")
        if tableau[choix - 1] == " ":
            tableau[choix - 1] = icon
        else:
            print("Cette case est déja prise!")
            tour_joueur(icon)
elif choix_mode_jeu == 'B':
    def tour_joueur(icon):
        if icon == "X":
            nombre = 1
        elif icon == "O":
            nombre = 2
        print(f"A ton tour joueur {nombre}")
        choix = int(input("Fais ton choix (1-9): "))
        if tableau[choix - 1] == " ":
            tableau[choix - 1] = icon
        else:
            print("Cette case est déja prise!")
            tour_joueur(icon)

# Conditions de victoire
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

# En cas d'égalité
def egalite():
    if " " not in tableau:
        return True
    else:
        return False

# Message Victoire
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
