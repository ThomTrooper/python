def saisirEntier() -> int:
    while True:
        try:
            entier = int(input("Veuillez saisir un entier : "))
            return entier
        except ValueError:
            print("Veuillez saisir un entier")


def saisirEntierSuivant(nbr1: int) -> int:
    while True:
        nbr2: int = saisirEntier()
        if nbr2 > nbr1:
            return nbr2
        else:
            print("Veuillez saisir un nombre supérieur")


def somme(premier: int, second: int) -> int:
    result = 0
    for i in range(premier, second + 1):
        result += i

    return result


premier_entier: int = saisirEntier()
second_entier: int = saisirEntierSuivant(premier_entier)

resultat: int = somme(premier_entier, second_entier)

if __name__ == "__main__":
    print(f"La somme des entiers dans l'intervalle [{premier_entier}, {second_entier}] inclus est : {resultat}")
