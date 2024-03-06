def retire_voyelle(texte: str) -> str:
    """
    Fonction retirant les voyelles dans une chaînes de caractère
    Entrée : str
    Sortie : str
    """
    texte_voyelle: str = ""
    voyelle: list = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in texte:
        if i in voyelle:
            texte_voyelle += i

    print(texte_voyelle)


if __name__ == "__main__":
    retire_voyelle("il fait chaud")
