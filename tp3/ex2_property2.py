class Personne ():
    def __init__(self,nom, prenom, age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom=nom
    
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom):
        self.__prenom=prenom

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age=age

P1 = Personne("Asklou","Abdessamad", 22)
print(P1.nom,"age :",P1.age)