class Produit():
    def __init__(self,nom, prix):
        self.__nom= nom
        self.__prix= prix
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom=nom

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, newprix):
        self.__prix= newprix

    def calculer_prix_avec_remise(self, remise, seuil_remise):
        if self.__prix > seuil_remise :
            return self.__prix * (1-remise/100)
        return self.__prix
    
p1 = Produit("tonik",1)
p2 = Produit("samsung", 3000)

print(f"Prix original de {p1.nom} : {p1.prix}MAD")
print(f"Prix après remise (10%) : {p1.calculer_prix_avec_remise(10, 100)}MAD")

print(f"Prix original de {p2.nom} : {p2.prix}MAD")
print(f"Prix après remise (10%) : {p2.calculer_prix_avec_remise(10, 100)}MAD")