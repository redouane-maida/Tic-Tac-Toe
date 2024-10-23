# Résultat de la partie

while True:
    print_tableau()
    tour_joueur("X")
    print_tableau()
    if est_victorieux("X"):
        print("X gagne! Félicitation!")
        break
    elif est_égal():
        print("C'est un match nul!")
        break
    player_move("O")
    if est_victorieux("O"):
        print_tableau()
        print("O gagne! Félicitation!")
        break
    elif est_égal():
        print("C'est un match nul!")
        break