def anagrame(ch1: str, ch2: str) -> bool | str:
    """
    Fonction qui permet de savoir si deux chaîne de caractère sont des anagrames
    Entrée : deux chaines de caractères
    Sortie : Boolean
    """
    ch1 = ch1.lower()
    ch2 = ch2.lower()
    ch1.replace(" ", "")
    ch2.replace(" ", "")
    ch1 = sorted(ch1)
    ch2 = sorted(ch2)

    if len(ch1) == len(ch2):
        return ch1 == ch2
    else:
        return "les deux chaîne de caractères ne sont pas comparable par leur longueur"


assert anagrame('CHien', 'Niche'), "analyse de chien et niche"
assert not anagrame('louve', 'poule'), "analyse de louve et poule"

if __name__ == "__main__":
    chaine1 = input("Entrez la première chaîne de caractères : ")
    chaine2 = input("Entrez la deuxième chaîne de caractères : ")
    resultat = anagrame(chaine1, chaine2)
    print(resultat)
