"""# Tic-Tac-Toe
Matthieu, Franck, Redouane"""

#Création du tableau et de ses lignes.
tableau = [" " for i in range(9)]

def affichez_tableau():
    Ligne1 = "| {} | {} | {} |".format(tableau[0], tableau[1], tableau[2])
    Ligne2 = "| {} | {} | {} |".format(tableau[3], tableau[4], tableau[5])
    Ligne3 = "| {} | {} | {} |".format(tableau[6], tableau[7], tableau[8])
    
    print(Ligne1)
    print(Ligne2)
    print(Ligne3)


    
    if victoire("X"):
        affichez_tableau()
        print("X gagne! Félicitation!")
        break
    elif egalite():
        affichez_tableau()
        print("C'est un match nul!")
        break

    
