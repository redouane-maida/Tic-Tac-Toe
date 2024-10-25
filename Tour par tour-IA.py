#Création du Tour par tour 
import random
def tour_joueur(icon): #joueur
    if icon == "X":
        nombre = 1
        choix = int(input("Fais ton choix (1-9): ").strip())
    elif icon == "O": #Bot
        nombre = 2
        choix = random.randint(1,9)
        print(f"Le bot (joueur {nombre}) a choisi la case {choix}")
    if tableau[choix - 1] == " ":
        tableau[choix - 1] = icon
    else:
        print("Cette case est déja prise!")
        tour_joueur(icon)