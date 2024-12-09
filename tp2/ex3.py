class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            return f"{montant} MAD ont été déposés sur le compte de {self.titulaire}."
        else:
            return "Le montant à déposer doit être positif."

    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                return f"{montant} MAD ont été retirés du compte de {self.titulaire}."
            else:
                return "Fonds insuffisants pour effectuer ce retrait."
        else:
            return "Le montant à retirer doit être positif."

    def afficher_solde(self):
        return f"Le solde actuel du compte de {self.titulaire} est de {self.solde} MAD."


compte = CompteBancaire("ASKLOU", 1000)
print(compte.deposer(200))
print(compte.retirer(300))
print(compte.afficher_solde())
print(compte.retirer(1500))
