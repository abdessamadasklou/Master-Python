class Vehicule :
    def __init__(self,marque,modele,annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        return f"Marque : {self.marque}\nModele : {self.modele}\nAnnee : {self.annee}\n"

class Moteur:
    def __init__(self,puissance,type_moto):
        self.puissance = puissance
        self.type_moto = type_moto
    def afficher_moteur(self):
        return f"Puissance : {self.puissance}\nType de moteur : {self.type_moto}"

class Voiture(Vehicule, Moteur):
    def __init__(self,marque,modele,annee,puissance,type_moto,nombre_de_places):
        self.nombre_de_places = nombre_de_places
        Vehicule.__init__(self, marque,modele,annee)
        Moteur.__init__(self,puissance,type_moto)
    def afficher_info(self):
        info_vehicule = super().afficher_info()
        info_moteur = super().afficher_moteur()
        return f"{info_vehicule} {info_moteur}\nNombre de places: {self.nombre_de_places}\n"
    
class Moto(Vehicule,Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moto, type_de_moto):
        Vehicule.__init__(self,marque, modele, annee)
        Moteur.__init__(self,puissance,type_moto)
        self.type_de_moto=type_de_moto
    def afficher_info(self):
        info_vehicule = super().afficher_info()
        info_moteur = super().afficher_moteur()
        return f"{info_vehicule} {info_moteur}\nType de moto: {self.type_de_moto}"
    
voiture = Voiture("RAM", "TRX", 2024, 702, "Essence", 5)

moto = Moto("scania", "C50", 2017, 150, "Essence", "Sport")

print("Informations de voiture :")
print(voiture.afficher_info())

print("Informations de MOTO :")
print(moto.afficher_info())
    


        
        