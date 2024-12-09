class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []  # Liste pour stocker les amis

    def se_presenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}, j'ai {self.age} ans."

    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
            return f"{ami} a été ajouté à la liste des amis de {self.prenom}."
        else:
            return f"{ami} est déjà dans la liste des amis de {self.prenom}."

    def afficher_amis(self):
        if not self.amis:
            return f"{self.prenom} n'a pas encore d'amis."
        return f"Liste des amis de {self.prenom} : {', '.join(self.amis)}."


# Exemple d'utilisation
personne = Personne("ASKLOU", "Abdessamad", 22)

# Ajouter des amis
print(personne.ajouter_ami("Yassine"))
print(personne.ajouter_ami("Abdhamid"))
print(personne.ajouter_ami("Abdhamid"))  # Test pour éviter les doublons

# Afficher la liste des amis
print(personne.afficher_amis())
