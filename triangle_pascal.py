from typing import List

def triangle_pascal(longueur: int):
    """
    Fonction affichant le triangle de pascal sur longueur
    Entrée : entier
    Sortie : entier
    """
    for i in range(longueur):
        nbr = 1
        for j in range(1, i + 2):
            print(nbr, end=" ")
            nbr = nbr * (i + 1 - j) // j
        print()

rang_triangle_pascal = int(input("Entrez le nombre de rang que vous souhaitez : "))
triangle_pascal(rang_triangle_pascal)
