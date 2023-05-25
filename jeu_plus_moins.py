from random import randint
"""
#____________________________________#
|                                    |
|        Jeu du plus ou moins        |
|                                    |
#____________________________________#
"""
def plus_moins():
    # définition d'une variable qui contiendras un nombre aléatoire
    nbr_random = randint(1,100)
    chance = 5
    # Création d'une boucle qui va ce répéter 5 fois (correspond en somme au nombre de chance laisser au joueur).
    for i in range(5):
        # On va demander à chaque tour au joueur d'entré un nombre, ce dernier va être stocker dans une variable
        nbr_joueur=int(input("Selon vous quel est le nombre auquel je pense ?\n\n"))
        if nbr_joueur == nbr_random:
            return "Gagner !"
        elif nbr_joueur < nbr_random:
            print("Plus grand !")
            chance -= 1
        else:
            print("Plus petit !")
            chance -= 1
    #Condition qui permet de ne pas renvoyer "perdu" lorsque l'on sors de la boucle en ayant gagner 
    if chance == 0:
            print("Perdu ! Le nombre était :", nbr_random)  

print(plus_moins())
