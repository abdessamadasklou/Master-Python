class Personne ():
    def __init__(self,nom, prenom, age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    def __getnom(self):
        return self.__nom
    def __setnom(self, nom):
        self.__nom=nom
    
    nom = property(__getnom,__setnom)

    def __getprenom(self):
        return self.__prenom
    def __setprenom(self, prenom):
        self.__prenom=prenom
        
    prenom = property(__getprenom,__setprenom)

    def __getage(self):
        return self.__age
    def __setage(self, age):
        self.__age=age

    age = property(__getage,__setage)

if __name__ == "__main__":
    P1 = Personne("Asklou","Abdessamad", 22)
    print(P1.nom,"age :",P1.age)