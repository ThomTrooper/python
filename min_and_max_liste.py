def max_in_liste(liste:list):
    """
    Fonction permettant de trouver le nombre le plus grand dans une liste
    Entrée : <list>
    Sortie : <int> or <float>
    """
    if len(liste) == 0:
        return 'Veuillez remplir votre liste.'
    maxi = float('-inf')
    for i in liste:
        if maxi < i:
            maxi = i
    print(maxi)

def min_in_liste(liste:list):
    """
    Fonction permettant de trouver le nombre le plus petit dans une liste
    Entrée : <list>
    Sortie : <int> or <float>
    """
    if len(liste) == 0:
        return 'Veuillez remplir votre liste.'
    minim = float('+inf')
    for i in liste:
        if minim > i:
            minim = i
    print(minim)

    
liste_a_remplir = []
print(max_in_liste(liste_a_remplir))
print(min_in_liste(liste_a_remplir))
