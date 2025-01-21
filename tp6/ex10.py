from ex3 import read_file
from ex9 import get_positive_integer

def all():
    try:
    
        filename = input("Entrez le nom du fichier : ")
        content = read_file(filename)
        if content: 
            print(f"Contenu du fichier '{filename}' :")
            print(content)

        number = get_positive_integer()
        print(f"Vous avez saisi l'entier : {number}")

    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    all()