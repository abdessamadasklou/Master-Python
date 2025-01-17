import json

donnees=[
     {"nom": "Messi", "âge": 20, "note": 15},
     {"nom": "Vini", "âge": 22, "note": 18},
]

with open('etudiants.json','w') as fichier:
    json.dump(donnees, fichier, indent=4)
with open('etudiants.json','r') as fichier:
    donnees=json.load(fichier)
    for donnee in donnees :
            nom = donnee["nom"]
            age = donnee["âge"]
            note = donnee["note"]
            print(f"Nom : {nom}, Âge : {age}, Note : {note}")