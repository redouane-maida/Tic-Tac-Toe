
# condition de victoire 

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