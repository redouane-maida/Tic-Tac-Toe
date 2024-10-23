"""# Tic-Tac-Toe
Matthieu, Franck, Redouane"""

#Création de tableau et ses lignes.
tableau = [" " for i in range(9)]
def affichez_tableau():
     Ligne1 = "| {} | {} | {} |".format(tableau[0], tableau[1], tableau[2])
     Ligne2 = "| {} | {} | {} |".format(tableau[3], tableau[4], tableau[5])
     Ligne3 = "| {} | {} | {} |".format(tableau[6], tableau[7], tableau[8])
     print()
     print(Ligne1)
     print(Ligne2)
     print(Ligne3)
     print()

def egalite():
    if " " not in tableau:
        return True
    else:
        return False
    
