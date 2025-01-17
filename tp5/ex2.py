with open ("phrases.txt","w") as fichier :
    for i in range (1,4):
        ligne = input(f"entrez la phrase numero {i} :")
        fichier.write(ligne+"\n")
