def u(nombre:int):
  '''
  Fonction d'une suite par récurrence
  Entrée : <int> (peut être changer par un float)
  Sortie : <int> (peut être changer par un float si l'entrée est un float aussi)
  '''
    retour = 0 # variable qui va stocker notre résultat final plus tard.
    if n == 0: 
        retour = 1
    else:
        retour = 2 * n (n - 1) + 3 # Notre calcul
    return retour

# Exemples :
print(u(2))
print(u(0))
