def retirer_doublons(liste_trie: list):
    """
    Fonction retirant les doublons dans une liste d'entier, de float ou de chaîne de caractère
    Entrée : list
    Sortie : list
    """
    resultat = []
    for nombre in liste_trie:
        if nombre not in resultat:
            resultat.append(nombre)
    return resultat


if __name__ == "__main__":
    liste_initiale = [1, 2, 2, 3, 4, 4, 4, 5]
    liste_triee = sorted(liste_initiale)
    resultat_final = retirer_doublons(liste_triee)
    print(resultat_final)
