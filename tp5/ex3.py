while True:
    reponse=input("souhaite veut ajouter des phrases ? :")
    if reponse.lower()== "oui":
        phrase=input("entrez votre phrase :")
        with open ("phrases.txt","a") as fichier :
            fichier.write(phrase)
    elif reponse.lower()=="non":
        break
    else :
        print("svp repondre par oui ou non")
        
    