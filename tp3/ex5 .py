class Employe():
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_informations(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Salaire: {self.salaire:.2f}MAD"

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.emp_supervises = []

    def ajouter_emp(self,employe):
        if isinstance (employe, Employe):
            self.emp_supervises.append(employe)
        else :
            raise ValueError("L'objet doit être une instance de la classe Employe.")
    def afficher_emp_supervises(self):
        if self.emp_supervises :
             print(f"Employés supervisés par {self.prenom} {self.nom} :")
             for employe in self.emp_supervises:
                print(f"- {employe.prenom} {employe.nom}, Salaire: {employe.salaire:.2f}MAD")
        else :
            print(f"{self.prenom} {self.nom} ne supervise aucun employé.")

em1 = Employe("Asklou","Abdessamad",10000)
em2 = Employe("Chafik","Driss",3000)
em3 = Employe("Asnous","imad",15000)

M = Manager("Bennis","Achraf",5000)

M.ajouter_emp(em1)
M.ajouter_emp(em2)
M.ajouter_emp(em3)

print(M.afficher_informations())
M.afficher_emp_supervises()
        