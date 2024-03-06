def inserer_trier_liste(liste_trier: list, nbr: float):
    """
    Fonction permettant d'inséré dans une liste trier un élément "nbr" de sorte
    à ce que ce dernier sois lui aussi trier dans l'ordre croissant.
    Entrée : list & float
    Sortie : list
    """
    liste_trier.append(nbr)
    liste_trier.sort()
    print(liste_trier)


if __name__ == "__main__":
    liste_prefaite = [8, 32, 16, 128]
    liste_prefaite.sort()
    inserer_trier_liste(liste_prefaite, 64)
