class Produit:
    def __init__(self,nom,prix):
        self.__nom=nom
        self.__prix=prix
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom=nom
    
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,prix):
        self.__prix=prix

class Commande:
    def __init__(self,produit, quantite):
        if not isinstance(produit,Produit):
            raise ValueError("Le produit doit être une instance de la classe Produit.")
        if quantite <= 0 :
            raise ValueError("La quantité doit être supérieure à zéro.")
        self.produit = produit
        self.quantite = quantite
    def calculer_total(self):
        return self.produit.prix*self.quantite
    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} (Prix unitaire: {self.produit.prix:.2f}MAD) - Total: {self.calculer_total():.2f}MAD"
        
class Panier:
    def __init__(self):
        self.commandes = []
    def ajouter_commande(self,commande):
        if not isinstance(commande,Commande):
            raise ValueError("La commande doit être une instance de la classe Commande.")
        self.commandes.append(commande)
    def calculer_total_panier(self):
        return sum(commande.calculer_total() for commande in self.commandes)
    def afficher_panier(self):
        print("contenu du panier :")
        if not self.commandes:
            print("le panier est vide")
        else :
            for commande in self.commandes:
                print(commande)
            print(f"total du panier :{self.calculer_total_panier():.2f}MAD")
p1=Produit("samsung",3000)
p2=Produit("sac", 900)
p3=Produit("camera",1000)

c1=Commande(p1,1)
c2=Commande(p2,3)
c3=Commande(p3,2)

panier = Panier()
panier.ajouter_commande(c1)
panier.ajouter_commande(c2)
panier.ajouter_commande(c3)

panier.afficher_panier()
        