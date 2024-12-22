class Personne ():
    def __init__(self,nom, prenom, age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    def getnom(self):
        return self.__nom
    def setnom(self, nom):
        self.__nom=nom
    def getprenom(self):
        return self.__prenom
    def setprenom(self, prenom):
        self.__prenom=prenom
    def getage(self):
        return self.__age
    def setage(self, age):
        self.__age=age
# if __name__ == "__main__":
P1 =Personne("ASKLOU","Abdessamad",22)
print(P1.getnom(), P1.getprenom(),"age:",P1.getage())
P1.setage(23)
P1.setprenom("Cristiano")
print(P1.getprenom(),"age:",P1.getage())