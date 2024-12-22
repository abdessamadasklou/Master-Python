from abc import ABC,abstractclassmethod
import math
class Forme (ABC):
    @abstractclassmethod
    def calculer_surface(self) :
        pass
class Rectangle (Forme):
    def __init__(self,long,larg):
        self.long = long
        self.larg = larg
    def calculer_surface(self):
        return self.long * self.larg
    
class Cercle(Forme):
    def __init__(self,ray):
        self.ray = ray
    def calculer_surface(self):
        return math.pi*self.ray**2

if __name__ == "__main__":
    rectangle = Rectangle(2,3)
    cercle = Cercle(7)
    print(f"Surface du rectangle : {rectangle.calculer_surface():.2f}")
    print(f"Surface du cercle : {cercle.calculer_surface():.2f}")