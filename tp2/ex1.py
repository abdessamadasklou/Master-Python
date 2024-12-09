class Chien:
    def __init__(self,nom,race,age):
        self.nom=nom
        self.race=race
        self.age=age
    def aboyer(self) :
        print('woof!')
    
MAX=Chien('MAX','Root','4months')
MAX.aboyer()
        