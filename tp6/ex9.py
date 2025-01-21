def get_positive_integer():
    while True:
        try :
            entier=int(input("Entrez un entier positif:"))
            if entier > 0:
                print(f"vous avez entré : {entier}")
                return entier
                break
            else :
                print("entier n'est pas positif")
        except ValueError:
            print("Erreur: entrer un nombre entier valide")
if __name__=="__main__":
    get_positive_integer()
