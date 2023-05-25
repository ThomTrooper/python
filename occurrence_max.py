def occurence_max(chaine):
    '''
    la fonction prend en paramètre une chaine de caractere et renvoie le caractere le plus frequent
    Entree : <str> 
    Sortie : <str>
    '''
    chaine = chaine.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    occurence = []
    # On parcours l'alphabet et on compte le nombre d'occurence de chaque caractères dans la chaîne
    if len(chaine) == 0:
        return False
    for i in range(len(alphabet)):
        compteur = 0
        for j in range(len(chaine)):
            if chaine[j] == alphabet[i]:
                compteur += 1
        occurence.append(compteur)
    # On cherhe l'indice de la valeur max dans le tableau occurence
    max = occurence[0]
    indice_max = 0
    for k in range(len(occurence)):
        if occurence[k] > max:
            max = occurence[k]
            indice_max = k
    # On renvoie la lettre à la position indice_max
    return alphabet[indice_max]

print(occurence_max("mon mot ou ma phrase")) # Ici l'occurrence maximal seras la lettre "m"
