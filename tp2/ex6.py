class Rectangle :
    def __init__(self, largeur, hauteur):
        self.largeur = largeur 
        self.hauteur = hauteur
    def calculer_surface(self) :
        return self.largeur * self.hauteur
    def calculer_perimetre(self):
        return (self.hauteur + self.largeur) * 2
rec = Rectangle(5, 2)   
surface = rec.calculer_surface()
print(f"La surface est : {surface}")

perimetre = rec.calculer_perimetre()
print(f"Le perimetre est : {perimetre}")
        