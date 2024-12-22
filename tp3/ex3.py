import math 
class Forme ():
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self,ray):
        self.ray = ray
    def calculer_surface(self):
        return math.pi * self.ray ** 2
    
class Rectangle(Forme):
    def __init__(self,lon,larg):
        self.lon = lon
        self.larg = larg
    def calculer_surface(self):
        return self.lon * self.larg
def afficher_surface(Formes):
    for forme in Formes :
        surface = forme.calculer_surface()
        print(f"La surface de la forme est : {surface:.2f}")

formes =[Rectangle(2,3),Cercle(3),Rectangle(4,6)]
afficher_surface(formes)