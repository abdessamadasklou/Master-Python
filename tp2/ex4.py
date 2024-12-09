class Personne :
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.nom} {self.prenom}, j'ai {self.age} ans."
class Etudiant(Personne):
    def __init__(self, nom, prenom, age,matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
    def etudier (self):
        return f"L'etudiant {self.nom} {self.prenom} (Matricule : {self.matricule}) est en train d'etudier."
    
personne = Personne("ASKLOU","Abdessamad",22)
print(personne.se_presenter())

etudiant=Etudiant("ASKLOU","Abdessamad",22,"BA2222")
print(etudiant.se_presenter())
print(etudiant.etudier())
