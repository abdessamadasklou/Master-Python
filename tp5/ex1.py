with open ("example.txt","r") as fichier :
    lignes = fichier.readlines()
    i=1
    for ligne in lignes:
        print (f"ligne {i}: {ligne.replace("\n","")}")
        i+=1