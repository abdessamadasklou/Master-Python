class voiture :
    def __init__(self,marque,modéle,année):
        self.marque=marque
        self.modéle=modéle
        self.année=année
    def afficher_info(self) :
       return f"MARQUE : {self.marque}, MODELE : {self.modéle}, ANNEE : {self.année}"
V1=voiture('volvo','xc90','2022')
V2=voiture('Dodge','Ram TRX','2024')   
print(V1.afficher_info())
print(V2.afficher_info()) 
