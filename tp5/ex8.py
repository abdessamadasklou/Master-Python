try:
    with open("inexistant.txt", "r") as fichier:
        contenu = fichier.read()
        print(f"Contenu du fichier : {contenu}")

except FileNotFoundError:
    print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")
