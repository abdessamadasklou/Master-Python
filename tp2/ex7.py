class Livre :
    def __init__(self, titre, auteur, annee_pub):
        self.titre = titre
        self.auteur = auteur
        self.annee_pub = annee_pub
    def __str__(self):
        return f"'{self.titre}' par {self.auteur}, publié en {self.annee_pub}"  
class Bibliotheque :
    def __init__(self):
        self.livres = []
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        return f"Le livre {livre.titre} a été ajouté à la bibliothèque."
    def afficher_livres(self):
        if not self.livres:
            return "La bibliothèque est vide."
        return "\n".join(str(livre) for livre in self.livres)
livre1 = Livre("song of ice and fire", "George R.R martin", 1990)
livre2 = Livre("Lord of the rings ", "Tolkien", 1983)
livre3 = Livre("Harry Potter", "Rowling", 1997)
biblio = Bibliotheque()

print(biblio.ajouter_livre(livre1))
print(biblio.ajouter_livre(livre2))
print(biblio.ajouter_livre(livre3))

print("\nLivres dans la bibliothèque :")
print(biblio.afficher_livres())