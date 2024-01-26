"""
Ci-dessous sont présenter 3 fonctions qui renvoie le plus petit nombre entre deux saisie en paramètre.
Le but est de voir plusieurs façon de faire un même chose
"""

def minimum_min(nbr1, nbr2):
    """
    Fonction qui va renvoyer le plus petit nombre saisie en paramètre
    Entrée : Nombre
    Sortie : Phrase
    """

    print(min(nbr1, nbr2))


def minimum_condition_compact(nbr1, nbr2):
    """
    Fonction qui va renvoyer le plus petit nombre saisie en paramètre
    Entrée : Nombre
    Sortie : Phrase
    """

    print(nbr1 if nbr1 < nbr2 else nbr2)


def minimum_condition_pas_compact(nbr1, nbr2):
    """
    Fonction qui va renvoyer le plus petit nombre saisie en paramètre
    Entrée : Nombre
    Sortie : Phrase
    """

    if nbr1 < nbr2:
        print(nbr1)
    else:
        print(nbr2)
