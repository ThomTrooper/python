def correspondance(mot_complet: str, mot_a_trous: str) -> bool:
    mot_complet.lower()
    mot_a_trous.lower()
  
    if len(mot_a_trous) != len(mot_complet):
        return False
      
    for indice in range(len(mot_complet)):
        if not mot_complet[indice].isalpha() and not mot_a_trous[indice].isalpha():
            return False
          
        if mot_complet[indice] != mot_a_trous[indice] and mot_a_trous[indice] != ".":
            return False
    return True


if __name__ == "__main__":
    mot1: str = input("Entrez le mot complet: ")
    mot2: str = input("Entrez le mot à trous: ")
    resultat = correspondance(mot1, mot2)
    print(resultat)
