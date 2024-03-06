def fusionEtTrie_liste(liste_un: list, liste_deux: list):
    """
    Fonction permettant de fusionner deux listes et les triants
    Entrée : list
    Sortie : list
    """
  
    liste_fusionner_trier = liste_un + liste_deux
    liste_fusionner_trier.sort()
    print(liste_fusionner_trier)


if __name__ == "__main__":
    liste_un = [8, 16, 32, 128]
    liste_deux = [1, 2, 3, 9]
    fusionEtTrie_liste(liste_un, liste_deux)
