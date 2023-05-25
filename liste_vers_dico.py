def convert_liste_en_dico(liste):
    '''
    Fonction qui transforme une liste en dico
    Entrée : <list>
    Sortie : <dict>
    '''
    dictionnaire = {}
    if len(liste)%2 == 0: #si nbr element pair dans liste
        for i in range(0,len(liste),2):
            dictionnaire[liste[i]] = liste[i+1]
    else:
        liste.append('None')
        for i in range(0,len(liste),2):
            dictionnaire[liste[i]] = liste[i+1]
    return dictionnaire
    
# Exemple :
print(convert_liste_en_dico(["Voiture","4 roues","Vélo","2 roues"]))
