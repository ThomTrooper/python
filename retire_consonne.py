def retire_consonne(texte: str) -> str:
    """
    Fonction retirant les consonnes dans une chaînes de caractère
    Entrée : str
    Sortie : str
    """
    texte_consonne: str = ""
    consonne: list = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
    for i in texte:
        if i in consonne:
            texte_consonne += i

    print(texte_consonne)


if __name__ == "__main__":
    retire_consonne("il fait chaud")
