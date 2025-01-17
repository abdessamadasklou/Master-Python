def calculer_lignes(file):
    try:
        with open(file, "r") as fichier:
            contenu = fichier.readlines()

            lignes=len(contenu)
            mots=0
            caracteres=0
            for ligne in contenu:
                mots+=len(ligne.split())
                caracteres+=len(ligne)

            print(f"Nombre total de lignes : {lignes}")
            print(f"Nombre total de mots : {mots}")
            print(f"Nombre total de caractères : {caracteres}")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file}' n'existe pas.")

calculer_lignes("example.txt")